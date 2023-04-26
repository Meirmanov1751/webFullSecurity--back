# from djoser.serializers import TokenSerializer
# from rest_framework import serializers
# from django.contrib.auth import get_user_model
#
# class CustomTokenSerializer(TokenSerializer):
#     email = serializers.EmailField(source='user.email')
#     role = serializers.SerializerMethodField()
#
#     def get_role(self, obj):
#         User = get_user_model()
#         return User.ROLES_CHOICES[obj.user.role][1]
#
#     class Meta(TokenSerializer.Meta):
#         fields = ('auth_token', 'email', 'role')
#

