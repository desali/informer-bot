from django.db import migrations

from core.models import Hour, Minute, Timing


def create_model(model):
    model.save()
    return model


def init_data(apps, schema_editor):
    # Hour
    hour_0 = create_model(Hour(title="00", hour=0))
    hour_1 = create_model(Hour(title="01", hour=1))
    hour_2 = create_model(Hour(title="02", hour=1))
    hour_3 = create_model(Hour(title="03", hour=1))
    hour_4 = create_model(Hour(title="04", hour=1))
    hour_5 = create_model(Hour(title="05", hour=1))
    hour_6 = create_model(Hour(title="06", hour=1))
    hour_7 = create_model(Hour(title="07", hour=1))
    hour_8 = create_model(Hour(title="08", hour=1))
    hour_9 = create_model(Hour(title="09", hour=1))
    hour_10 = create_model(Hour(title="10", hour=1))
    hour_11 = create_model(Hour(title="11", hour=1))
    hour_12 = create_model(Hour(title="12", hour=1))
    hour_13 = create_model(Hour(title="13", hour=1))
    hour_14 = create_model(Hour(title="14", hour=1))
    hour_15 = create_model(Hour(title="15", hour=1))
    hour_16 = create_model(Hour(title="16", hour=1))
    hour_17 = create_model(Hour(title="17", hour=1))
    hour_18 = create_model(Hour(title="18", hour=1))
    hour_19 = create_model(Hour(title="19", hour=1))
    hour_20 = create_model(Hour(title="20", hour=1))
    hour_21 = create_model(Hour(title="21", hour=1))
    hour_22 = create_model(Hour(title="22", hour=1))
    hour_23 = create_model(Hour(title="23", hour=1))

    # Minute
    minute_0 = create_model(Minute(title="00", minute=0))
    minute_1 = create_model(Minute(title="01", minute=1))
    minute_2 = create_model(Minute(title="02", minute=2))
    minute_3 = create_model(Minute(title="03", minute=3))
    minute_4 = create_model(Minute(title="04", minute=4))
    minute_5 = create_model(Minute(title="05", minute=5))
    minute_6 = create_model(Minute(title="06", minute=6))
    minute_7 = create_model(Minute(title="07", minute=7))
    minute_8 = create_model(Minute(title="08", minute=8))
    minute_9 = create_model(Minute(title="09", minute=9))
    minute_10 = create_model(Minute(title="10", minute=10))
    minute_11 = create_model(Minute(title="11", minute=11))
    minute_12 = create_model(Minute(title="12", minute=12))
    minute_13 = create_model(Minute(title="13", minute=13))
    minute_14 = create_model(Minute(title="14", minute=14))
    minute_15 = create_model(Minute(title="15", minute=15))
    minute_16 = create_model(Minute(title="16", minute=16))
    minute_17 = create_model(Minute(title="17", minute=17))
    minute_18 = create_model(Minute(title="18", minute=18))
    minute_19 = create_model(Minute(title="19", minute=19))
    minute_20 = create_model(Minute(title="20", minute=20))
    minute_21 = create_model(Minute(title="21", minute=21))
    minute_22 = create_model(Minute(title="22", minute=22))
    minute_23 = create_model(Minute(title="23", minute=23))
    minute_24 = create_model(Minute(title="24", minute=24))
    minute_25 = create_model(Minute(title="25", minute=25))
    minute_26 = create_model(Minute(title="26", minute=26))
    minute_27 = create_model(Minute(title="27", minute=27))
    minute_28 = create_model(Minute(title="28", minute=28))
    minute_29 = create_model(Minute(title="29", minute=29))
    minute_30 = create_model(Minute(title="30", minute=30))
    minute_31 = create_model(Minute(title="31", minute=31))
    minute_32 = create_model(Minute(title="32", minute=32))
    minute_33 = create_model(Minute(title="33", minute=33))
    minute_34 = create_model(Minute(title="34", minute=34))
    minute_35 = create_model(Minute(title="35", minute=35))
    minute_36 = create_model(Minute(title="36", minute=36))
    minute_37 = create_model(Minute(title="37", minute=37))
    minute_38 = create_model(Minute(title="38", minute=38))
    minute_39 = create_model(Minute(title="39", minute=39))
    minute_40 = create_model(Minute(title="40", minute=40))
    minute_41 = create_model(Minute(title="41", minute=41))
    minute_42 = create_model(Minute(title="42", minute=42))
    minute_43 = create_model(Minute(title="43", minute=43))
    minute_44 = create_model(Minute(title="44", minute=44))
    minute_45 = create_model(Minute(title="45", minute=45))
    minute_46 = create_model(Minute(title="46", minute=46))
    minute_47 = create_model(Minute(title="47", minute=47))
    minute_48 = create_model(Minute(title="48", minute=48))
    minute_49 = create_model(Minute(title="49", minute=49))
    minute_50 = create_model(Minute(title="50", minute=50))
    minute_51 = create_model(Minute(title="51", minute=51))
    minute_52 = create_model(Minute(title="52", minute=52))
    minute_53 = create_model(Minute(title="53", minute=53))
    minute_54 = create_model(Minute(title="54", minute=54))
    minute_55 = create_model(Minute(title="55", minute=55))
    minute_56 = create_model(Minute(title="56", minute=56))
    minute_57 = create_model(Minute(title="57", minute=57))
    minute_58 = create_model(Minute(title="58", minute=58))
    minute_59 = create_model(Minute(title="59", minute=59))

    # Timing
    timing_5 = create_model(Timing(title='5 минут', minutes=5))
    timing_10 = create_model(Timing(title='10 минут', minutes=10))
    timing_15 = create_model(Timing(title='15 минут', minutes=15))
    timing_30 = create_model(Timing(title='30 минут', minutes=30))
    timing_45 = create_model(Timing(title='45 минут', minutes=45))
    timing_60 = create_model(Timing(title='1 час', minutes=60))
    timing_120 = create_model(Timing(title='2 часа', minutes=120))
    timing_180 = create_model(Timing(title='3 часа', minutes=180))
    timing_360 = create_model(Timing(title='6 часов', minutes=360))
    timing_720 = create_model(Timing(title='12 часов', minutes=720))
    timing_1440 = create_model(Timing(title='1 день', minutes=1440))


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_minute')
    ]

    operations = [
        migrations.RunPython(init_data),
    ]
