from django.forms import ModelForm
from projects.models import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "featured_image", "description",
                  'demo_link', 'source_link', 'tags', ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    # customizing form fields such as classes, attributes, ids, etc
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#         self.fields['title'].widget.attrs.update(
#             {'class': "input", "placeholder": "Add Title..."})
#
#         self.fields['description'].widget.attrs.update({
#             'class': "input",
#             "placeholder": "Enter some description",
#             "type": "text"
#         })

        for name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "input",
                "placeholder": f"Add {' '.join(name.split('_'))}",
            })

