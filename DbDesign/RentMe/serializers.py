# coding:utf-8
from rest_framework import serializers
from RentMe.models import *

#关联Model_info
class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = model_info
        fields = ('model_id','car_model_id','car_type','car_brand','car_series','car_issue_date','car_config_model','car_seats_num','car_doors','car_fuel_type','car_gearbox_type','car_displacement','car_fuel_num','car_drive_way','car_engine_intake','car_skylight','car_tank_capa','car_voicebox','car_seats_type','car_reverse_radar','car_airbag','car_dvd','car_gps','car_deposit','car_day_price','car_time_out_price','car_over_kilo_price','car_record_create_time','record_delete_status')
#关联user_info
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_info
        fields = ('user_id','user_name','user_sex','user_age','user_ident','user_tel','user_office','user_addr','user_post','user_email','user_record_create_time','record_delete_status')

#关联driving_license
class DrivingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = driving_license
        fields = ('drive_id','user_drive','drive_type','drive_age','drive_start_date','drive_end_date')
#关联admin_info
class AdminSerializer(serializers.HyperlinkedModelSerializer):
    #store_manage = serializers.HyperlinkedRelatedField(many=True,view_name='adminn-detail',read_only=True)
    class Meta:
        model = admin_info
        fields = ('admin_id','admin_tel','admin_pas','admin_name','store_manage','admin_sex','admin_age','admin_record_create_time','admin_type','admin_email','admin_ident',)
#关联store_info
class StoreSerializer(serializers.HyperlinkedModelSerializer):
    #store_admin = serializers.ReadOnlyField(source='store_admin.admin_name')
    class Meta:
        model = store_info
        fields = ('store_id','store_addr','store_tel','store_start_time','store_admin','store_record_create_time','record_delete_status')
#关联car_info
class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =car_info
        field = ('car_id','car_num','car_model_id','car_color','car_engine_num','car_engine_num','car_fame_num','car_buy_date','car_retailer','car_status','car_ins_num','car_record_create_time','record_delete_status')


#class DrivingSerializer(serializers.Serializer):
    #pk = serializers.IntegerField(read_only=True)
   # user_drive = serializers.CharField(required=False,allow_blank=True,max_length=12)
    #drive_type = serializers.CharField(required=False,default='C级驾照',max_length=12)
    #drive_age = serializers.IntegerField()
    #drive_start_date = serializers.DateField()
    #drive_end_date = serializers.DateField()

    #def create(self, validated_data):
        #数据合法，返回并创建driving_license实例
       # return driving_license.objects.create(**validated_data)

    #def update(self, instance, validated_data):
        #instance.user_drive = validated_data.get('user_drive',instance.user_drive)
        #instance.drive_type = validated_data.get('user_drive',instance.user_drive)
        #instance.drive_age = validated_data.get('user_drive',instance.user_drive)
        #instance.drive_start_date = validated_data.get('drive_start_date',instance.drive_start_date)
        #instance.drive_end_date = validated_data.get('drive_end_date',instance.drive_end_date)
        #instance.save()
       # return instance
