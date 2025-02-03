import os
import json
import requests
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import CheckImeiSerializer, CheckWhiteListSerializer


User = get_user_model()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_imei(self, request):
    serializer = CheckImeiSerializer
    serializer.is_valid(raise_exception=True)
    url = 'https://api.imeicheck.net/v1/checks'
    token = os.getenv('TOKEN_IMEI')
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    body = json.dumps({
        "deviceId": serializer.validated_data['imei'],
        "serviceId": 1
    })
    response = requests.post(url, headers=headers, data=body)
    return Response({'imei': response.json()['properties']}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_wite_list(self, request):
    serializer = CheckWhiteListSerializer()
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(User, tg_id=serializer.validated_data['tg_id'])
    return user.whtite_list
