from django import forms
from point.models import Carbonpoint, Greenpoint

class CarbonForm(forms.ModelForm):
    class Meta:
        model = Carbonpoint
        fields = ['pointtype', 'cpoint']

        labels = {
            'pointtype':'포인트 종류',
            'cpoint':'포인트량',
        }


class GreenForm(forms.ModelForm):
    class Meta:
        model = Greenpoint
        fields = ['pointtype', 'gpoint']

        labels = {
            'pointtype': '포인트 종류',
            'gpoint': '포인트량',
        }