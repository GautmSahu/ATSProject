from django.db.models import Case, When, IntegerField, Q, F, Value,  ExpressionWrapper
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Candidate
from .serializers import CandidateSerializer
from .constants import ERROR_MSG
from functools import reduce
import operator
import logging
import os
import sys

logger = logging.getLogger(__name__)

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        try:
            query = request.GET.get('q', '').strip()
            if not query:
                return Response([], status=status.HTTP_200_OK)

            search_terms = query.lower().split()

            # Annotate only matching rows
            candidates = Candidate.objects.filter(
                # Create OR condition for all search terms
                reduce(
                    operator.or_, (Q(name__icontains=word) for word in query.split()), Q())    
                ).annotate(
                    # Assign a high score (100) if there is an exact match with the query
                    exact_match=Case(
                        When(name__iexact=query, then=Value(100)),  # Exact match gets the highest weight
                        default=Value(0),
                        output_field=IntegerField()
                    ),
                    # Count the number of words from the search query that appear in the candidate's name
                    partial_match=ExpressionWrapper(
                        sum(
                            Case(
                                When(name__icontains=term, then=Value(1)),  # Add 1 for each word in the query that appears in the name
                                default=Value(0),
                                output_field=IntegerField()
                            )
                            for term in search_terms
                        ),
                        output_field=IntegerField()
                    ),
                    # Total score = exact match score + partial match score
                    total_score=F('exact_match') + F('partial_match')
                ).order_by('-total_score')  # Order candidates by highest relevance score

            serializer = self.get_serializer(candidates, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error("Error on 'FileName: {}', %s at %s ".format(str(fname)), str(e), str(exc_tb.tb_lineno), extra={'AppName': "ATSApp"})
        return Response(ERROR_MSG,status=status.HTTP_500_INTERNAL_SERVER_ERROR)