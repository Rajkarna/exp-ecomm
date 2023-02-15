from rest_framework import serializers

from Users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['userFirstName', 'email', 'phoneNumber', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('userFirstName', '')
        phonenumber = attrs.get('phoneNumber', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric'
            )
        return attrs

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    userFirstName = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.CharField(max_length=68, min_length=8, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'userFirstName', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        return attrs