from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password', 'password2']

    def validate(self, attrs):
        p1 = attrs['password']
        p2 = attrs.get('password2')
        first_name = attrs['first_name']
        if not first_name.istitle():
            raise serializers.ValidationError('Имя должно начинаться с большой буквы')
        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        # user = User.objects.create_user(**validated_data)
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
