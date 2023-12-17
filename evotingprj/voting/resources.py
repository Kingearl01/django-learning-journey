from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Voter
from accounts.models import CustomUser

class VoterResource(resources.ModelResource):
    voter = fields.Field(
        column_name='admin',
        attribute='admin',
        widget=ForeignKeyWidget(CustomUser, field='username')

    )
    
    class Meta:
        model = Voter
        fields = ['id', 'phone', 'otp', 'verified', 'voted', 'otp_sent']
        # export_order = ['id','admin', 'phone', 'otp', 'verified', 'voted', 'otp_sent']