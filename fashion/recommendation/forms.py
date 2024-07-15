from django import forms

# Define choices based on your dataset
OCCASION_CHOICES = [
    ('Workout', 'Workout'),
    ('Party', 'Party'),
    ('Casual', 'Casual'),
    ('Formal', 'Formal'),
]

MATERIAL_CHOICES = [
    ('Denim', 'Denim'),
    ('Cotton', 'Cotton'),
    ('Polyester', 'Polyester'),
    ('Linen', 'Linen'),
    ('Wool', 'Wool'),
]

PATTERN_CHOICES = [
    ('Solid', 'Solid'),
    ('Striped', 'Striped'),
    ('Checked', 'Checked'),
    ('Printed', 'Printed'),
]

NECKLINE_CHOICES = [
    ('Boat Neck', 'Boat Neck'),
    ('Round Neck', 'Round Neck'),
    ('Collared', 'Collared'),
    ('V Neck', 'V Neck'),
]

FIT_CHOICES = [
    ('Slim', 'Slim'),
    ('Regular', 'Regular'),
    ('Loose', 'Loose'),
]

ACCESSORY_CHOICES = [
    ('None', 'None'),
    ('Bracelet', 'Bracelet'),
    ('Watch', 'Watch'),
    ('Necklace', 'Necklace'),
]

BRAND_CHOICES = [
    ('Adidas', 'Adidas'),
    ('Nike', 'Nike'),
    ('Puma', 'Puma'),
    ('Levi\'s', 'Levi\'s'),
    ('Zara', 'Zara'),
]

class OutfitForm(forms.Form):
    Occasion = forms.ChoiceField(choices=OCCASION_CHOICES, label="Occasion")
    Material = forms.ChoiceField(choices=MATERIAL_CHOICES, label="Material")
    Pattern = forms.ChoiceField(choices=PATTERN_CHOICES, label="Pattern")
    Neckline = forms.ChoiceField(choices=NECKLINE_CHOICES, label="Neckline")
    Fit = forms.ChoiceField(choices=FIT_CHOICES, label="Fit")
    Accessory = forms.ChoiceField(choices=ACCESSORY_CHOICES, label="Accessory")
    Brand = forms.ChoiceField(choices=BRAND_CHOICES, label="Brand")
