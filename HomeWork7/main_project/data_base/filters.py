from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Post, Category

class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name = 'postcategory__category',
        queryset=Category.objects.all(),
        label = 'Категории'
    )

    class Meta:
        model = Post
        fields = {
            'heading': ['icontains'],
        }