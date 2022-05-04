from django import forms

class inputdialog(forms.Form):
    checkin = forms.CharField(max_length=50,label='チェックイン')
    time1 = forms.CharField(max_length=50,label='開始')
    checkout = forms.CharField(max_length=50,label='チェックアウト')
    time2 = forms.CharField(max_length=50,label='終了')