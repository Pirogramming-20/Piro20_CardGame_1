from django import forms
from .models import Game
import random

##### utils #####


def make_random():
    random_numbers = sorted(random.sample(range(1, 11), 5))
    return random_numbers

### forms ###
# 1. Attacker의 form
class GameFormAttacker(forms.ModelForm):
    a_choice = forms.IntegerField(
        label='플레이어 A 선택 숫자', widget=forms.Select(choices=[]))

    class Meta:
        model = Game
        fields = ['a_choice', 'player_b']

    def __init__(self, *args, **kwargs):
        super(GameFormAttacker, self).__init__(*args, **kwargs)
        choices = make_random()
        self.fields['a_choice'].widget.choices = [('----', '----')] + [
            (choice, choice) for choice in choices]
        self.fields['a_choice'].label = "내가 고른 카드: "
        self.fields['player_b'].label = "공격할 상대는? "
