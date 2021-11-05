from rest_framework import serializers
from .models import CustomUser 

class UserSerializer(serializers.ModelSerializer):
	# add other extra fields or overwrite existing fields
	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
	
	class Meta:
		model = CustomUser 
		fields = ('username', 'email', 'password', 'password2')
		# write only will exclude field from GET request
		extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

	# override save method 
	def save(self):
		user = CustomUser(
			email = self.validated_data['email'],
			username = self.validated_data['username']
		)

		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Password must match'})
		
		user.set_password(password)
		user.save()
		return user