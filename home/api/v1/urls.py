from django.urls import path, include
from rest_framework import routers
from home.api.v1.views import FormAListView, FormBListView, FormFieldsViewSet, UnHideFieldsView, HideFieldsView, \
    DeleteDataListView, UpdateDataListView, AddDataListView, GetDataListView

router = routers.DefaultRouter()
router.register(r'api/form_fields', FormFieldsViewSet)
router.register(r'api/updateDataList', UpdateDataListView, basename="updateDataList")

urlpatterns = [
    path('api/form_alist/', FormAListView.as_view(), name='form_alist'),
    path('api/form_blist/', FormBListView.as_view(), name='form_blist'),
    path('api/addDataList/', AddDataListView.as_view(), name='add_data_list'),
    path('api/unhideFields', UnHideFieldsView.as_view(), name='unhide_fields'),
    path('api/hideFields', HideFieldsView.as_view(), name='hide_fields'),
    path('api/deleteDataList', DeleteDataListView.as_view(), name='delete_data_list'),
    path('api/getDataList', GetDataListView.as_view(), name='get_data_list'),
    path('', include(router.urls)),
]