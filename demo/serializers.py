from rest_framework import serializers

from demo.models import Weapon


# class WeaponSerializers(serializers.Serializer):
#     power = serializers.IntegerField()
#     rarity = serializers.CharField()

class WeaponSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['power', 'rarity', 'value']