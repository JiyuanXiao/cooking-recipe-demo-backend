from rest_framework.response import Response
from rest_framework import status

def AddDataList(data_list, Serializer) -> Response:
    serializer_list = []
    saved_objects = []
    for data in data_list:
        serializer = Serializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer_list.append(serializer)
    
    for serializer in serializer_list:
        serializer.save()
        saved_objects.append(serializer.data)
    return Response(saved_objects, status=status.HTTP_201_CREATED)

def AddData(data, Serializer) -> Response:
    serializer = Serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)