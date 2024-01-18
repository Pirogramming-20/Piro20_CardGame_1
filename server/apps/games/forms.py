from django import forms
from .models import Game
from apps.users.models import User
import random

##### utils #####
def make_random():
    random_numbers = sorted(random.sample(range(1, 11), 5))
    return random_numbers


### forms ###
# 1. Attacker의 form
class GameFormAttacker(forms.ModelForm):
    a_choice = forms.IntegerField(
        label='내가 고른 카드: ', widget=forms.Select(choices=[]))

    class Meta:
        model = Game
        fields = ['a_choice', 'player_b']

    def __init__(self, *args, **kwargs):
        self.user =kwargs.pop('user', None)
        super(GameFormAttacker, self).__init__(*args, **kwargs)
        choices = make_random()
        self.fields['a_choice'].widget.choices = [('----', '----')] + [
            (choice, choice) for choice in choices]
        # admin과 본인을 제외한 player로 선택항목 설정
        self.fields['player_b'].queryset = User.objects.exclude(is_superuser=1).exclude(
            nickname=self.user.nickname)
        self.fields['player_b'].label = "공격할 상대는?"

# 2. Defender의 form
class GameFormDefender(forms.ModelForm):
    b_choice = forms.IntegerField(
        label='내가 고른 카드: ', widget=forms.Select(choices=[]))
    
    class Meta:
        model = Game
        fields = ['b_choice']

    def __init__(self, *args, **kwargs):
        super(GameFormDefender, self).__init__(*args, **kwargs)
        choices = make_random()
        self.fields['b_choice'].widget.choices = [('----', '----')] + [
            (choice, choice) for choice in choices]
        
