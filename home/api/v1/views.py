from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializer import FormAListSerializer, FormFieldsSerializer, FormBListSerializer, UnhideFieldsSerializer, \
    DeleteDataListSerializer, UpdateDataListSerializer, GetDataListSerializer
from ...models import FormFields, FormAList, FormBList


class FormAListView(APIView):
    def post(self, request):
        serializer = FormAListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FormBListView(APIView):
    def post(self, request):
        serializer = FormBListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FormFieldsViewSet(ModelViewSet):
    serializer_class = FormFieldsSerializer
    queryset = FormFields.objects.all()
    permission_classes = [AllowAny,]


class UnHideFieldsView(APIView):
    def post(self, request):
        serializer = UnhideFieldsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fields = serializer.validated_data['fields']
        FormFields.objects.filter(name__in=fields).update(hide="")
        # Perform the necessary operations with the fields
        # For example, you could save the fields to a database or perform any other required logic
        return Response({'message': 'OK'}, status=200)


class HideFieldsView(APIView):
    def post(self, request):
        serializer = UnhideFieldsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fields = serializer.validated_data['fields']
        FormFields.objects.filter(name__in=fields).update(hide="true")
        return Response({'message': 'OK'}, status=200)


class DeleteDataListView(APIView):
    def post(self, request):
        serializer = DeleteDataListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data_type = serializer.validated_data['type']
        ids = serializer.validated_data['ids']
        if data_type == 'A':
            FormAList.objects.filter(id__in=ids).delete()
        else:
            FormBList.objects.filter(id__in=ids).delete()

        return Response({'message': f"delete {len(ids)} rows"}, status=204)


class UpdateDataListView(ModelViewSet):


    def create(self, request, *args, **kwargs):
        serializer = UpdateDataListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data_type = serializer.validated_data['type']
        data_list = serializer.validated_data['list']

        for item in data_list:
            item_id = item.get('id')

            if data_type == 'A':
                try:
                    instance = FormAList.objects.get(id=item_id)
                    serializer = FormAListSerializer(instance, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    self.perform_update(serializer)
                except FormAList.DoesNotExist:
                    pass
            else:
                try:
                    instance = FormBList.objects.get(id=item_id)
                    serializer = FormBListSerializer(instance, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    self.perform_update(serializer)
                except FormBList.DoesNotExist:
                    pass

        return Response({'message': f'Updated {data_list.length()} rows.'})


class AddDataListView(APIView):
    def post(self, request):
        type  = request.data.get('type', '')
        list_items = request.data.get('list', [])
        if type == 'A':
            serializer = FormAListSerializer(data=list_items, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message":f"add {len(list_items)} rows"}, status=201)
        if type == 'B':
            serializer = FormBListSerializer(data=list_items, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": f"add {len(list_items)} rows"}, status=201)
        return Response({"error": "something went wrong"}, status=400)


class GetDataListView(APIView):
    def post(self, request):
        serializer = GetDataListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data_type = serializer.validated_data['type']
        fields = serializer.validated_data['fields']

        data_list = []
        res_list = []
        if data_type == 'A':
            for field in fields:
                for key, values in field.items():
                    res_list.append(values)
                    for value in values:
                        data_list.append(({key : value}))
                    serializer = FormAListSerializer(data=data_list, many=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
        if data_type == 'B':
            for field in fields:
                for key, values in field.items():
                    res_list.append(values)
                    for value in values:
                        data_list.append(({key : value}))
                    serializer = FormBListSerializer(data=data_list, many=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()

        return Response(res_list)