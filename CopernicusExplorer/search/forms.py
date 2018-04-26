from django import forms
import datetime


class SearchForm(forms.Form):
    min_ingestion_date = forms.DateField(label='Od',
                                         required=True,
                                         initial='2017-01-01')

    max_ingestion_date = forms.DateField(label='Do',
                                         required=True,
                                         initial=datetime.date.today)

    satellite = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=(('S1', 'S1'), ('S2', 'S2')),
                                  label='Satelita',
                                  required=True)

    orbit_direction = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                label='Kierunek orbity',
                                                choices=(('ASCENDING', 'ASCENDING'),
                                                         ('DESCENDING', 'DESCENDING')),
                                                required=False,)

    polarisation_mode = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                  label='Polaryzacja',
                                                  choices=(('HH', 'HH'),
                                                           ('HV', 'HV'),
                                                           ('VH', 'VH'),
                                                           ('VV', 'VV')),
                                                  required=False)

    product_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             label='Typ produktu',
                                             choices=(('GRD', 'GRD'),
                                                      ('SLC', 'SLC'),
                                                      ('RAW', 'RAW')),
                                             required=False)

    sensor_mode = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            label='Tryb sensora',
                                            choices=(('IW', 'IW'),
                                                     ('SM', 'SM'),
                                                     ('EW', 'EW')),
                                            required=False)

    cloud_cover = forms.DecimalField(label='Maksymalny % pokrywy chmur',
                                     required=False)

    relative_orbit_number = forms.IntegerField(label='Względny numer orbity',
                                               required=False)

    search_extent_min_x = forms.DecimalField(label='Minimalna długość geograficzna',
                                             required=False)

    search_extent_max_x = forms.DecimalField(label='Maksymalna długość geograficzna',
                                             required=False)

    search_extent_min_y = forms.DecimalField(label='Minimalna szerokość geograficzna',
                                             required=False)

    search_extent_max_y = forms.DecimalField(label='Maksymalna szerokość geograficzna',
                                             required=False)