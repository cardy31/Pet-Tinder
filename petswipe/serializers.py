from rest_framework import serializers
from django.contrib.auth.models import User
from petswipe.models import Member, SwipedAnimal


class MemberSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Member
        fields = ('id', 'firstname', 'lastname', 'email', 'username', 'hash', 'age', 'address', 'prov', 'postal',
                  'animalToAdopt', 'adoptWithMedical', 'previousOwnership', 'owner')


class SwipedAnimalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SwipedAnimal
        fields = ('id', 'animalCode', 'memberUsername', 'owner')


# Implements a special user class that has built-in login/out abilities
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Will be a list of all the foods a member has eaten
    member = serializers.HyperlinkedRelatedField(many=True, view_name='memberinfo-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'member')


