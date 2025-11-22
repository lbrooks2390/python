class Television:
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    MIN_VOLUME = 0
    MAX_VOLUME = 2

    def __init__(mod_var):
        mod_var.__status = False
        mod_var.__muted = False
        mod_var.__volume = Television.MIN_VOLUME
        mod_var.__channel = Television.MIN_CHANNEL
        mod_var.__saved_volume = mod_var.__volume

    def power(mod_var):
        mod_var.__status = not mod_var.__status

    def mute(mod_var):
        if mod_var.__status:
            if not mod_var.__muted:
                mod_var.__saved_volume = mod_var.__volume
                mod_var.__volume = Television.MIN_VOLUME
                mod_var.__muted = True
            else:
                mod_var.__volume = mod_var.__saved_volume
                mod_var.__muted = False

    def channel_up(mod_var):
        if mod_var.__status:
            if mod_var.__channel == Television.MAX_CHANNEL:
                mod_var.__channel = Television.MIN_CHANNEL
            else:
                mod_var.__channel += 1

    def channel_down(mod_var):
        if mod_var.__status:
            if mod_var.__channel == Television.MIN_CHANNEL:
                mod_var.__channel = Television.MAX_CHANNEL
            else:
                mod_var.__channel -= 1

    def volume_up(mod_var):
        if mod_var.__status:
            if mod_var.__muted:
                mod_var.__muted = False
                mod_var.__volume = mod_var.__saved_volume
            if mod_var.__volume < Television.MAX_VOLUME:
                mod_var.__saved_volume = mod_var.__volume + 1
                mod_var.__volume += 1

    def volume_down(mod_var):
        if mod_var.__status:
            if mod_var.__muted:
                mod_var.__muted = False
                mod_var.__volume = mod_var.__saved_volume
            if mod_var.__volume > Television.MIN_VOLUME:
                mod_var.__saved_volume = mod_var.__volume - 1
                mod_var.__volume -= 1

    def __str__(mod_var):
        return f"Power = {mod_var.__status}, Channel = {mod_var.__channel}, Volume = {mod_var.__volume}"