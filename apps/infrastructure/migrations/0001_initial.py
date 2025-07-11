# Generated by Django 5.2.3 on 2025-06-22 05:33

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BridgeInfo",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="पुलको नाम")),
                ("ward_number", models.CharField(max_length=30, verbose_name="वडा नं")),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="ठेगाना"
                    ),
                ),
            ],
            options={
                "verbose_name": "झोलुंगे पुल तथा पुलपुलेसा",
                "verbose_name_plural": "झोलुंगे पुल तथा पुलपुलेसाहरू",
            },
        ),
        migrations.CreateModel(
            name="WardWiseCookingFuel",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ward_number",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9),
                        ],
                        verbose_name="वडा नं.",
                    ),
                ),
                (
                    "cooking_fuel",
                    models.CharField(
                        choices=[
                            ("WOOD", "काठ/दाउरा/कोइला"),
                            ("LP_GAS", "एल.पी. ग्याँस"),
                            ("KEROSENE", "मट्टितेल"),
                            ("ELECTRICITY", "विद्युत"),
                            ("BIOGAS", "गोबर ग्याँस/बायोग्याँस"),
                            ("DUNGCAKE", "गोबर/गुँइठा"),
                            ("OTHER", "अन्य"),
                        ],
                        max_length=15,
                        verbose_name="खाना पकाउने इन्धन",
                    ),
                ),
                (
                    "households",
                    models.PositiveIntegerField(default=0, verbose_name="घरपरिवार"),
                ),
            ],
            options={
                "verbose_name": "वडागत खाना पकाउने इन्धन",
                "verbose_name_plural": "वडागत खाना पकाउने इन्धन",
                "unique_together": {("ward_number", "cooking_fuel")},
            },
        ),
        migrations.CreateModel(
            name="WardWiseElectricitySource",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ward_number",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9),
                        ],
                        verbose_name="वडा नं.",
                    ),
                ),
                (
                    "electricity_source",
                    models.CharField(
                        choices=[
                            ("ELECTRICITY", "विद्युत"),
                            ("SOLAR", "सोलार"),
                            ("KEROSENE", "मट्टितेल"),
                            ("BIOGAS", "बायोग्याँस"),
                            ("OTHER", "अन्य"),
                        ],
                        max_length=15,
                        verbose_name="बत्ति बाल्ने इन्धन",
                    ),
                ),
                (
                    "households",
                    models.PositiveIntegerField(default=0, verbose_name="घरपरिवार"),
                ),
            ],
            options={
                "verbose_name": "वडागत बत्ति बाल्ने इन्धन",
                "verbose_name_plural": "वडागत बत्ति बाल्ने इन्धन",
                "unique_together": {("ward_number", "electricity_source")},
            },
        ),
        migrations.CreateModel(
            name="WardWiseFacilities",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ward_number",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9),
                        ],
                        verbose_name="वडा नं.",
                    ),
                ),
                (
                    "facility",
                    models.CharField(
                        choices=[
                            ("RADIO", "रेडियो सुविधा"),
                            ("TELEVISION", "टेलिभिजन"),
                            ("COMPUTER", "कम्प्युटर/ल्यापटप"),
                            ("TELEPHONE", "टेलिफोन"),
                            ("MOBILE_PHONE", "मोबाइल फोन"),
                            ("INTERNET", "इन्टरनेट"),
                            ("BICYCLE", "साइकल"),
                            ("MOTORCYCLE", "मोटरसाइकल"),
                            ("CAR_JEEP_VAN", "कार/जीप/भ्यान"),
                            ("TRACTOR", "ट्याक्टर"),
                            ("OTHER", "अन्य"),
                        ],
                        max_length=20,
                        verbose_name="सुविधा",
                    ),
                ),
                (
                    "households",
                    models.PositiveIntegerField(default=0, verbose_name="घरपरिवार"),
                ),
            ],
            options={
                "verbose_name": "वडागत सुविधा",
                "verbose_name_plural": "वडागत सुविधाहरू",
                "unique_together": {("ward_number", "facility")},
            },
        ),
        migrations.CreateModel(
            name="WardWiseHouseholdFloor",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ward_number",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9),
                        ],
                        verbose_name="वडा नं.",
                    ),
                ),
                (
                    "floor_type",
                    models.CharField(
                        choices=[
                            ("CONCRETE", "सिमेन्ट ढलान"),
                            ("MUD", "माटो"),
                            ("WOOD", "काठको फल्याक/बाँस"),
                            ("BRICK", "इँटा/ढुङ्गा"),
                            ("TILE", "सेरामिक टायल"),
                            ("OTHER", "अन्य"),
                        ],
                        max_length=15,
                        verbose_name="भुइँको प्रकार",
                    ),
                ),
                (
                    "households",
                    models.PositiveIntegerField(default=0, verbose_name="घरपरिवार"),
                ),
            ],
            options={
                "verbose_name": "वडागत घरको भुइँको प्रकार",
                "verbose_name_plural": "वडागत घरको भुइँको प्रकार",
                "unique_together": {("ward_number", "floor_type")},
            },
        ),
        migrations.CreateModel(
            name="WardWiseHouseholdRoof",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ward_number",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9),
                        ],
                        verbose_name="वडा नं.",
                    ),
                ),
                (
                    "roof_type",
                    models.CharField(
                        choices=[
                            ("CEMENT", "सिमेन्ट ढलान"),
                            ("TIN", "जस्ता/टिन"),
                            ("TILE", "टायल/खपडा/झिँगटी"),
                            ("STRAW", "खर/पराल/छ्वाली"),
                            ("WOOD", "काठ/फल्याक"),
                            ("STONE", "ढुङ्गा/स्लेट"),
                            ("OTHER", "अन्य"),
                        ],
                        max_length=15,
                        verbose_name="छानोको प्रकार",
                    ),
                ),
                (
                    "households",
                    models.PositiveIntegerField(default=0, verbose_name="घरपरिवार"),
                ),
            ],
            options={
                "verbose_name": "वडागत छानोको प्रकार",
                "verbose_name_plural": "वडागत छानोको प्रकार",
                "unique_together": {("ward_number", "roof_type")},
            },
        ),
        migrations.CreateModel(
            name="WardWiseHouseMapPassed",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ward_number",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9),
                        ],
                        verbose_name="वडा नं.",
                    ),
                ),
                (
                    "house_map_status",
                    models.CharField(
                        choices=[
                            ("PASSED", "पास भएको"),
                            ("NOT_PASSED", "पास नभएको"),
                            ("IN_PROCESS", "प्रक्रियामा"),
                            ("NOT_APPLICABLE", "लागू नहुने"),
                        ],
                        max_length=20,
                        verbose_name="घरको नक्शा पास स्थिति",
                    ),
                ),
                (
                    "households",
                    models.PositiveIntegerField(default=0, verbose_name="घरपरिवार"),
                ),
            ],
            options={
                "verbose_name": "वडागत घरको नक्शा पास स्थिति",
                "verbose_name_plural": "वडागत घरको नक्शा पास स्थिति",
                "unique_together": {("ward_number", "house_map_status")},
            },
        ),
        migrations.CreateModel(
            name="WardWiseRoadStatus",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ward_number",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9),
                        ],
                        verbose_name="वडा नं.",
                    ),
                ),
                (
                    "road_status",
                    models.CharField(
                        choices=[
                            ("BLACKTOPPED", "कालोपत्रे"),
                            ("GRAVELED", "ढुंगामाटो"),
                            ("EARTHEN", "कच्ची"),
                            ("NO_ROAD", "सडक छैन"),
                        ],
                        max_length=15,
                        verbose_name="सडकको अवस्था",
                    ),
                ),
                (
                    "households",
                    models.PositiveIntegerField(default=0, verbose_name="घरपरिवार"),
                ),
            ],
            options={
                "verbose_name": "वडागत सडकको अवस्था",
                "verbose_name_plural": "वडागत सडकको अवस्था",
                "unique_together": {("ward_number", "road_status")},
            },
        ),
        migrations.CreateModel(
            name="WardWiseTimeToActiveRoad",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ward_number",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9),
                        ],
                        verbose_name="वडा नं.",
                    ),
                ),
                (
                    "time_duration",
                    models.CharField(
                        choices=[
                            ("UNDER_15_MIN", "१५ मिनेट भन्दा कम"),
                            ("UNDER_30_MIN", "१५-३० मिनेट"),
                            ("UNDER_1_HOUR", "३०-६० मिनेट"),
                            ("1_HOUR_OR_MORE", "१ घण्टा वा बढी"),
                        ],
                        max_length=25,
                        verbose_name="सक्रिय सडकमा पुग्न लाग्ने समय",
                    ),
                ),
                (
                    "households",
                    models.PositiveIntegerField(default=0, verbose_name="घरपरिवार"),
                ),
            ],
            options={
                "verbose_name": "वडागत सक्रिय सडकमा पुग्न लाग्ने समय",
                "verbose_name_plural": "वडागत सक्रिय सडकमा पुग्न लाग्ने समय",
                "unique_together": {("ward_number", "time_duration")},
            },
        ),
        migrations.CreateModel(
            name="WardWiseTimeToMarketCenter",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ward_number",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9),
                        ],
                        verbose_name="वडा नं.",
                    ),
                ),
                (
                    "time_duration",
                    models.CharField(
                        choices=[
                            ("UNDER_15_MIN", "१५ मिनेट भन्दा कम"),
                            ("UNDER_30_MIN", "१५-३० मिनेट"),
                            ("UNDER_1_HOUR", "३०-६० मिनेट"),
                            ("1_HOUR_OR_MORE", "१ घण्टा वा बढी"),
                        ],
                        max_length=25,
                        verbose_name="बजार केन्द्रमा पुग्न लाग्ने समय",
                    ),
                ),
                (
                    "households",
                    models.PositiveIntegerField(default=0, verbose_name="घरपरिवार"),
                ),
            ],
            options={
                "verbose_name": "वडागत बजार केन्द्रमा पुग्न लाग्ने समय",
                "verbose_name_plural": "वडागत बजार केन्द्रमा पुग्न लाग्ने समय",
                "unique_together": {("ward_number", "time_duration")},
            },
        ),
        migrations.CreateModel(
            name="WardWiseTimeToPublicTransport",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ward_number",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9),
                        ],
                        verbose_name="वडा नं.",
                    ),
                ),
                (
                    "time_duration",
                    models.CharField(
                        choices=[
                            ("UNDER_15_MIN", "१५ मिनेट भन्दा कम"),
                            ("UNDER_30_MIN", "१५-३० मिनेट"),
                            ("UNDER_1_HOUR", "३०-६० मिनेट"),
                            ("1_HOUR_OR_MORE", "१ घण्टा वा बढी"),
                        ],
                        max_length=25,
                        verbose_name="सार्वजनिक यातायातमा पुग्न लाग्ने समय",
                    ),
                ),
                (
                    "households",
                    models.PositiveIntegerField(default=0, verbose_name="घरपरिवार"),
                ),
            ],
            options={
                "verbose_name": "वडागत सार्वजनिक यातायातमा पुग्न लाग्ने समय",
                "verbose_name_plural": "वडागत सार्वजनिक यातायातमा पुग्न लाग्ने समय",
                "unique_together": {("ward_number", "time_duration")},
            },
        ),
    ]
