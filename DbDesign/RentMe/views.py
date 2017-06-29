# coding:utf-8
from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from RentMe.models import *
from RentMe.serializers import *
import json
import datetime

#展示或者创建driving_license
#request.data 返回 字典包含前端传来的jason数据
#XXXX.objects.all.values()返回字典类型
#如果查询到多个记录时会以[dict(),dict(),……]的格式返回
#用 属性__in = []的方式来访问一个属性多个值匹配的情况
#filter(user_drive__in=['123456789','12345'])

#license_info查询&添加
@api_view(['GET','POST'])
def license_list(request=[],format=None):
    if request.method == 'GET':
        if len(request.data)==0:
            licenses = driving_license.objects.all()
            serializer = DrivingSerializer(licenses,many=True)
            return Response(serializer.data)
        else:
            request_dict = request.data
            licenses = driving_license.objects.all()
            if 'drive_id' in request_dict:
                licenses = licenses.filter(drive_id__in=request_dict['drive_id'])
            elif 'user_drive' in request_dict:
                licenses = licenses.filter(user_drive__in=request_dict['user_drive'])
            elif 'drive_type' in request_dict:
                licenses = licenses.filter(drive_type__in=request_dict['drive_type'])
            elif 'drive_age' in request_dict:
                licenses = licenses.filter(drive_age__in=request_dict['drive_age'])
            elif 'drive_name' in request_dict:
                licenses = licenses.filter(drive_name__in=request_dict['drive_name'])
            elif 'drive_start_date' in request_dict:
                licenses = licenses.filter(drive_start_date__in=request_dict['drive_start_date'])
            elif 'drive_end_date' in request_dict:
                licenses = licenses.filter(drive_end_date__in=request_dict['drive_end_date'])
            elif 'record_delete_status' in request_dict:
                licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
            #print(licenses.values())
            licenses_list=list()
            for item in licenses.values():
                licenses_list.append(item)

            serializer = DrivingSerializer(data=licenses_list,many=True)
            if serializer.is_valid():
                return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DrivingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print('post')
            #print(Response(serializer.data))
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#illegal_record查询&添加
@api_view(['GET','POST'])
def illegal_list(request=[],format=None):
    if request.method == 'GET':
        licenses = illegal_record.objects.all()
        if len(request.data)==0:
            serializer = illegalSerializer(licenses,many=True)
            return Response(serializer.data)
        else:
            request_dict = request.data
            #licenses = illegal_record.objects.all()
            if 'illegal_id' in request_dict:
                licenses = licenses.objects.filter(illegal_id__in=request_dict['illegal_id'])
            elif 'illegal_car_num' in request_dict:
                licenses = licenses.filter(illegal_car_num__in=request_dict['illegal_car_num'])
            elif 'illegal_date' in request_dict:
                licenses = licenses.filter(illegal_date__in=request_dict['illegal_date'])
            elif 'illegal_bill' in request_dict:
                licenses = licenses.filter(illegal_bill__in=request_dict['illegal_bill'])
            elif 'illegal_info' in request_dict:
                licenses = licenses.filter(illegal_info__in=request_dict['illegal_info'])
            elif 'illegal_record_create_time' in request_dict:
                licenses = licenses.filter(illegal_record_create_time__in=request_dict['illegal_record_create_time'])
            elif 'record_create_admin' in request_dict:
                licenses = licenses.filter(record_create_admin__in=request_dict['record_create_admin'])
            elif 'record_delete_status' in request_dict:
                licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
            #print(licenses.values())
            licenses_list=list()
            for item in licenses.values():
                licenses_list.append(item)
            serializer = illegalSerializer(data=licenses_list,many=True)
            if serializer.is_valid():
                return Response(serializer.data)

    elif request.method == 'POST':
        serializer = illegalSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#car_info查询&添加
@api_view(['GET','POST'])
def car_list(request=[],format=None):
    if request.method == 'GET':
        licenses = car_info.objects.all()
        if len(request.data)==0:
            serializer = CarSerializer(licenses,many=True)
            return Response(serializer.data)
        else:
            request_dict = request.data
            #licenses = car_info.objects.all()
            if 'car_id' in request_dict:
                licenses = licenses.objects.filter(car_id__in=request_dict['car_id'])
            elif 'car_num' in request_dict:
                licenses = licenses.filter(car_num__in=request_dict['car_num'])
            elif 'car_model_id' in request_dict:
                licenses = licenses.filter(car_model_id__in=request_dict['car_model_id'])
            elif 'car_color' in request_dict:
                licenses = licenses.filter(car_color__in=request_dict['ar_color'])
            elif 'car_engine_num' in request_dict:
                licenses = licenses.filter(car_engine_num__in=request_dict['car_engine_num'])
            elif 'car_frame_num' in request_dict:
                licenses = licenses.filter(car_frame_num__in=request_dict['car_frame_num'])
            elif 'car_buy_date' in request_dict:
                licenses = licenses.filter(car_buy_date__in=request_dict['car_buy_date'])
            elif 'car_retailer' in request_dict:
                licenses = licenses.filter(car_retailer__in=request_dict['car_retailer'])
            elif 'car_status' in request_dict:
                licenses = licenses.filter(car_status__in=request_dict['car_status'])
            elif 'car_ins_num' in request_dict:
                licenses = licenses.filter(car_ins_num__in=request_dict['car_ins_num'])
            elif 'car_record_create_time' in request_dict:
                licenses = licenses.filter(car_record_create_time__in=request_dict['car_record_create_time'])
            elif 'record_create_admin' in request_dict:
                licenses = licenses.filter(record_create_admin__in=request_dict['record_create_admin'])
            elif 'record_delete_status' in request_dict:
                licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
            #print(licenses.values())
            licenses_list=list()
            for item in licenses.values():
                licenses_list.append(item)
            serializer = CarSerializer(data=licenses_list,many=True)
            if serializer.is_valid():
                return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#admin_info查询&添加
@api_view(['GET','POST'])
def admin_list(request=[],format=None):
    if request.method == 'GET':
        if len(request.data)==0:
            licenses = admin_info.objects.all()
            serializer = AdminSerializer(licenses,many=True)
            return Response(serializer.data)
        else:
            request_dict = request.data
            licenses = admin_info.objects.all()
            if 'admin_id' in request_dict:
                licenses = licenses.filter(admin_id__in=request_dict['admin_id'])
            elif 'admin_pas' in request_dict:
                licenses = licenses.filter(admin_pas__in=request_dict['admin_pas'])
            elif 'admin_name' in request_dict:
                licenses = licenses.filter(admin_name__in=request_dict['admin_name'])
            elif 'admin_sex' in request_dict:
                licenses = licenses.filter(admin_sex__in=request_dict['admin_sex'])
            elif 'admin_age' in request_dict:
                licenses = licenses.filter(admin_age__in=request_dict['admin_age'])
            elif 'admin_ident' in request_dict:
                licenses = licenses.filter(admin_ident__in=request_dict['admin_ident'])
            elif 'admin_tel' in request_dict:
                licenses = licenses.filter(admin_tel__in=request_dict['admin_tel'])
            elif 'admin_email' in request_dict:
                licenses = licenses.filter(admin_email__in=request_dict['admin_email'])
            elif 'admin_type' in request_dict:
                licenses = licenses.filter(admin_type__in=request_dict['admin_type'])
            elif 'admin_record_create_time' in request_dict:
                licenses = licenses.filter(admin_record_create_time__in=request_dict['admin_record_create_time'])
            elif 'record_delete_status' in request_dict:
                licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
            #print(licenses.values())
            admin_list=list()
            for item in licenses.values():
                licenses_list.append(item)

            serializer = AdminSerializer(data=licenses_list,many=True)
            if serializer.is_valid():
                return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print('post')
            #print(Response(serializer.data))
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#store_info查询&添加
@api_view(['GET','POST'])
def store_list(request=[],format=None):
    if request.method == 'GET':
        licenses = store_info.objects.all()
        if len(request.data)==0:
            serializer = StoreSerializer(licenses,many=True)
            return Response(serializer.data)
        else:
            request_dict = request.data
            #licenses = store_info.objects.all()
            if 'store_id' in request_dict:
                licenses = licenses.objects.filter(store_id__in=request_dict['store_id'])
            elif 'store_addr' in request_dict:
                licenses = licenses.filter(store_addr__in=request_dict['store_addr'])
            elif 'store_tel' in request_dict:
                licenses = licenses.filter(store_tel__in=request_dict['store_tel'])
            elif 'store_start_time' in request_dict:
                licenses = licenses.filter(store_start_time__in=request_dict['store_start_time'])
            elif 'store_admin' in request_dict:
                licenses = licenses.filter(store_admin__in=request_dict['store_admin'])
            elif 'store_record_create_time' in request_dict:
                licenses = licenses.filter(store_record_create_time__in=request_dict['store_record_create_time'])
            elif 'record_create_admin' in request_dict:
                licenses = licenses.filter(record_create_admin__in=request_dict['record_create_admin'])
            elif 'record_delete_status' in request_dict:
                licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
            #print(licenses.values())
            licenses_list=list()
            for item in licenses.values():
                licenses_list.append(item)
            serializer = StoreSerializer(data=licenses_list,many=True)
            if serializer.is_valid():
                return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StoreSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#rent_order查询&添加
@api_view(['GET','POST'])
def rent_list(request=[],format=None):
    if request.method == 'GET':
        licenses = rent_order.objects.all()
        if len(request.data)==0:
            serializer = OrderSerializer(licenses,many=True)
            return Response(serializer.data)
        else:
            request_dict = request.data
            #licenses = rent_info.objects.all()
            if 'order_id' in request_dict:
                licenses = licenses.objects.filter(order_id__in=request_dict['order_id'])
            elif 'user_num' in request_dict:
                licenses = licenses.filter(user_num__in=request_dict['user_num'])
            elif 'car_num' in request_dict:
                licenses = licenses.filter(car_num__in=request_dict['car_num'])
            elif 'user_drive' in request_dict:
                licenses = licenses.filter(user_drive__in=request_dict['user_drive'])
            elif 'pick_addr' in request_dict:
                licenses = licenses.filter(pick_addr__in=request_dict['pick_addr'])
            elif 'pick_time' in request_dict:
                licenses = licenses.filter(pick_time__in=request_dict['pick_time'])
            elif 'drop_time' in request_dict:
                licenses = licenses.filter(drop_time__in=request_dict['drop_time'])
            elif 'actual_deposit' in request_dict:
                licenses = licenses.filter(actual_deposit__in=request_dict['actual_deposit'])
            elif 'breaken_bill' in request_dict:
                licenses = licenses.filter(breaken_bill__in=request_dict['breaken_bill'])
            elif 'illegal_info' in request_dict:
                licenses = licenses.filter(illegal_info__in=request_dict['illegal_info'])
            elif 'illegal_bill' in request_dict:
                licenses = licenses.filter(illegal_bill__in=request_dict['illegal_bill'])
            elif 'actual_money' in request_dict:
                licenses = licenses.filter(actual_money__in=request_dict['actual_money'])
            elif 'record_create_admin' in request_dict:
                licenses = licenses.filter(record_create_admin__in=request_dict['record_create_admin'])
            elif 'order_record_create_time' in request_dict:
                licenses = licenses.filter(order_record_create_time__in=request_dict['order_record_create_time'])
            elif 'record_delete_status' in request_dict:
                licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
            #print(licenses.values())
            licenses_list=list()
            for item in licenses.values():
                licenses_list.append(item)
            serializer = OrderSerializer(data=licenses_list,many=True)
            if serializer.is_valid():
                return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#relet_record查询&添加
@api_view(['GET','POST'])
def relet_list(request=[],format=None):
    if request.method == 'GET':
        licenses = relet_record.objects.all()
        if len(request.data)==0:
            serializer = ReletSerializer(licenses,many=True)
            return Response(serializer.data)
        else:
            request_dict = request.data
            #licenses = relet_info.objects.all()
            if 'relet_id' in request_dict:
                licenses = licenses.objects.filter(relet_id__in=request_dict['relet_id'])
            elif 'order_num' in request_dict:
                licenses = licenses.filter(order_num__in=request_dict['order_num'])
            elif 'relet_start_time' in request_dict:
                licenses = licenses.filter(relet_start_time__in=request_dict['relet_start_time'])
            elif 'relet_end_time' in request_dict:
                licenses = licenses.filter(relet_end_time__in=request_dict['relet_end_time'])
            elif 'record_create_admin' in request_dict:
                licenses = licenses.filter(record_create_admin__in=request_dict['record_create_admin'])
            elif 'relet_record_create_time' in request_dict:
                licenses = licenses.filter(relet_record_create_time__in=request_dict['relet_record_create_time'])
            elif 'record_delete_status' in request_dict:
                licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
            #print(licenses.values())
            licenses_list=list()
            for item in licenses.values():
                licenses_list.append(item)
            serializer = ReletSerializer(data=licenses_list,many=True)
            if serializer.is_valid():
                return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReletSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#user_info查询&添加
@api_view(['GET','POST'])
def user_list(request=[],format=None):
    if request.method == 'GET':
        licenses = user_info.objects.all()
        if len(request.data)==0:
            serializer = UserSerializer(licenses,many=True)
            return Response(serializer.data)
        else:
            request_dict = request.data
            #licenses = user_info.objects.all()
            if 'user_id' in request_dict:
                licenses = licenses.objects.filter(user_id__in=request_dict['user_id'])
            elif 'user_name' in request_dict:
                licenses = licenses.filter(user_name__in=request_dict['user_name'])
            elif 'user_sex' in request_dict:
                licenses = licenses.filter(user_sex__in=request_dict['user_sex'])
            elif 'user_age' in request_dict:
                licenses = licenses.filter(user_age__in=request_dict['user_age'])
            elif 'user_ident' in request_dict:
                licenses = licenses.filter(user_ident__in=request_dict['user_ident'])
            elif 'user_tel' in request_dict:
                licenses = licenses.filter(user_tel__in=request_dict['user_tel'])
            elif 'user_office' in request_dict:
                licenses = licenses.filter(user_office__in=request_dict['user_office'])
            elif 'user_addr' in request_dict:
                licenses = licenses.filter(user_addr__in=request_dict['user_addr'])
            elif 'user_post' in request_dict:
                licenses = licenses.filter(user_post__in=request_dict['user_post'])
            elif 'user_email' in request_dict:
                licenses = licenses.filter(user_email__in=request_dict['user_email'])
            elif 'record_create_admin' in request_dict:
                licenses = licenses.filter(record_create_admin__in=request_dict['record_create_admin'])
            elif 'user_record_create_time' in request_dict:
                licenses = licenses.filter(user_record_create_time__in=request_dict['user_record_create_time'])
            elif 'record_delete_status' in request_dict:
                licenses = licenses.filter(record_delete_status__in=request_dict['record_delete_status'])
            #print(licenses.values())
            licenses_list=list()
            for item in licenses.values():
                licenses_list.append(item)
            serializer = UserSerializer(data=licenses_list,many=True)
            if serializer.is_valid():
                return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#登陆
@api_view(['GET','POST'])
def login(request):
    if request.method == 'POST':
        tel = request.data['admin_tel']
        pas = request.data['admin_pas']
        admin = admin_info.objects.filter(admin_tel__exact=tel,admin_pas__exact=pas)
        #filter返回QuerySet集合对象，遍历获得唯一元素
        if admin:
            for admin_item in admin:
                #print(admin_item)
                admin_serializer = AdminSerializer(admin_item)
            return Response(admin_serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'GET':
        admins = admin_info.objects.all()
        serializer = AdminSerializer(admins,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    return  Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','PUT','DELETE'])
def license_detail(request,pk,format=None):
    try:
        license = driving_license.objects.get(pk=pk)
    except driving_license.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DrivingSerializer(license)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrivingSerializer(license,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        license.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','PUT','DELETE'])
def license_detail(request,pk,format=None):
    try:
        license = driving_license.objects.get(pk=pk)
    except driving_license.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DrivingSerializer(license)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrivingSerializer(license,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        license.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','PUT','DELETE'])
def model_info_detail(request,pk,format=None):
    try:
        models_ = model_info.objects.get(pk=pk)
    except model_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ModelSerializer(models_)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ModelSerializer(models_,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        models_.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#user_info查询
@api_view(['GET','POST'])
def user_info_list(request,format=None):
    #展示或者创建driving_license
    if request.method == 'GET':
        users = user_info.objects.all()
        serializer = UserSerializer(users,many=True)
        #print('get')
        #print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print('post')
            #print(Response(serializer.data))
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def user_info_detail(request,pk,format=None):
    try:
        users = user_info.objects.get(pk=pk)
    except user_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(users)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(users,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST'])
def get_car_info_by_type(request):
    dict_type = dict()
    json_dict = dict()
    dict_type['商务车'] = 0
    dict_type['SUV'] = 0
    dict_list = list()
    for order in rent_order.objects.all():
        car = order.car_num
        model = car.car_model_id
        if(model.car_type == 0):
            dict_type['商务车'] +=1
        elif (model.car_type == 1):
            dict_type['SUV'] +=1
    for key,values in dict_type.items():
        #json_dict['car_type'] = key
        #json_dict['car_count'] = values
        dict_list.append({'car_type':key,'car_count':values})
        print(dict_list)
    return Response(dict_list,status=status.HTTP_200_OK)
@api_view(['GET','POST'])
def get_car_info_by_date(request):
    query_dict = dict()
    dict_list = list()
    for order in rent_order.objects.filter(pick_time__month=datetime.datetime.now().month):
        query_dict[order.pick_time.date().isoformat()] = 0
    for order in rent_order.objects.filter(pick_time__month=datetime.datetime.now().month):
        query_dict[order.pick_time.date().isoformat()] = query_dict[order.pick_time.date().isoformat()] + 1
    for key,values in query_dict.items():
        dict_list.append({'pick_time':key,'car_count':values})
        print(dict_list)
    return Response(dict_list,status=status.HTTP_200_OK)
@api_view(['GET','POST'])
def get_car_info_by_dateAndStore(request):
    query_dict = dict()
    dict_list = list()
    result_dict = dict()
    for order in rent_order.objects.filter(pick_time__month=datetime.datetime.now().month):
            query_dict[order.pick_time.date().isoformat()] = dict()
    for store in store_info.objects.all():
        for order in store.pick_store.filter(pick_time__month=datetime.datetime.now().month):
            query_dict[order.pick_time.date().isoformat()]['store_count'+str(store.store_id)] = 0
    for store in store_info.objects.all():
        for order in store.pick_store.filter(pick_time__month=datetime.datetime.now().month):
            print(order.pick_addr)
            query_dict[order.pick_time.date().isoformat()]['store_count'+str(store.store_id)] += 1
    for key,values in query_dict.items():
        dict_list.append({"pick_time":key,"store_count":values})
    print(dict_list)
    return Response(dict_list,status=status.HTTP_200_OK)
@api_view(['GET','POST'])
def order_pay(request):
    json_query = dict()
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        #print(request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            order = rent_order.objects.get(pk=serializer.data['order_id'])
            json_query['form'] = dict()
            json_query['form']['pick_add'] = order.pick_addr.store_addr
            json_query['form']['pick_time'] = order.pick_time
            json_query['form']['drop_time'] = order.drop_time
            json_query['user_deposit'] = order.actual_deposit
            json_query['car_deposit'] = order.car_num.car_model_id.car_deposit
            json_query['user_name'] = order.user_num.user_name
            json_query['drive_name'] = order.user_drive.drive_name
            json_query['car_num'] = order.car_num.car_num
            json_query['car_brand'] = order.car_num.car_model_id.car_brand
            json_query['car_series'] = order.car_num.car_model_id.car_series
            json_query['car_config_model'] = order.car_num.car_model_id.car_config_model

            return Response(json_query,status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_404_NOT_FOUND)

class ModelList(generics.ListCreateAPIView):
    queryset = model_info.objects.all()
    serializer_class = ModelSerializer

#管理员列表
class AdminList(generics.ListCreateAPIView):
    queryset = admin_info.objects.all()
    serializer_class = AdminSerializer

#管理详情
class AdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = admin_info.objects.all()
    serializer_class = AdminSerializer

#门店列表
class StoreList(generics.ListCreateAPIView):
    queryset = store_info.objects.all()
    serializer_class = StoreSerializer

    #def perform_create(self, serializer):
       # serializer.save(store_admin=self.request.)

#门店详情
class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = store_info.objects.all()
    serializer_class = StoreSerializer
#车辆列表
class CarList(generics.ListCreateAPIView):
    queryset = car_info.objects.all()
    serializer_class=CarSerializer
   # def perform_create(self, serializer):
       # print(self.request.POST)
       ## model_at = model_info.objects.get(pk=self.request.POST.car_model_id)
       # serializer.save(model_at)
#车辆详情
class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = car_info.objects.all()

    serializer_class=CarSerializer
#租车订单列表
class OrderList(generics.ListCreateAPIView):
    queryset = rent_order.objects.all()
    serializer_class = OrderSerializer
#租车订单详情
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = rent_order.objects.all()
    serializer_class = OrderSerializer
#续租记录列表
class ReletList(generics.ListCreateAPIView):
    queryset = relet_record.objects.all()
    serializer_class = ReletSerializer
#续租记录详情
class ReletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = relet_record.objects.all()
    serializer_class = ReletSerializer
#违章列表
class IllegalList(generics.ListCreateAPIView):
    queryset = illegal_record.objects.all()
    serializer_class = illegalSerializer
#违章详情
class IllegalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = illegal_record.objects.all()
    serializer_class = illegalSerializer
