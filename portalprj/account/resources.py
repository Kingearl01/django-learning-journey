from import_export import resources

from .models import User

class CustomUserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = [
            'id','password','last_login',
            'is_superuser','groups','user_permissions',	
            'username',	'first_name','last_name',
            'email','is_staff',	'date_joined',	
            'profile_pic']
        export_order = [
            'id', 'username','password','first_name','last_name','email','profile_pic','last_login',
            'is_superuser','groups','user_permissions',	
            'is_staff',	'date_joined',	
            ]
