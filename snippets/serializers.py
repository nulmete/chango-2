from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


"""
Prevent code duplication with the model.
Default implementation of create() and update() methods.
"""
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    # Notice that we've also added a new 'highlight' field.
    # This field is of the same type as the url field,
    # except that it points to the 'snippet-highlight' url pattern,
    # instead of the 'snippet-detail' url pattern.
    # Because we've included format suffixed URLs such as '.json',
    # we also need to indicate on the highlight field that any format suffixed hyperlinks it
    # returns should use the '.html' suffix.
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
