import math

print('┌──────────────────────── Input ──────────────────────────┐')

def get_input() -> float:
    total_match = input("├ Total Match:          ").replace('%', '')
    current_winrate = input("├ Current winrate:      ").replace('%', '')
    wanted_winrate = input("├ Wanted Winrate:       ").replace('%', '')

    total_match = float(total_match)
    current_winrate = float(current_winrate)
    wanted_winrate = float(wanted_winrate)

    if not total_match < 0.0 or current_winrate < 0.0 or wanted_winrate < 0.0:
        return total_match, current_winrate, wanted_winrate

    print("Value can't be lower than 0, canceling")

def calculate(total_match, wanted_winrate, current_winrate) -> float:
    current_win = (total_match*current_winrate)/100
    needed_match = ((100*current_win) - (wanted_winrate*total_match))/(wanted_winrate-100)
    estimate_win = needed_match+(needed_match*(current_winrate/100))

def print_value()
print('├────────────────────── Summerize ────────────────────────┤')
print(f'├ Total Match:          {int(total_match):,}')
print(f'├ Current Winrate:      {current_winrate}%')
print(f'├ Wanted Winrate:       {wanted_winrate}%')
print('├───────────────────── Calculation ───────────────────────┤')
print(f'├ Needed Win:           {int(math.ceil(needed_match))}')
print(f'├ Estimate Match:       {int(math.ceil(estimate_win))}')
print(f'├ Estimate Time (min):  {int(needed_match*15)}/{int(estimate_win*15)}')
print('└─────────────────────────────────────────────────────────┘')




