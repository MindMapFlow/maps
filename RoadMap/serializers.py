from rest_framework import serializers
from .models import Map

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['id', 'major', 'course', 'weeks']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        map_id = str(data['id'])
        major_name = instance.major.name
        year = instance.course.semester
        course_name = instance.course.name
        weeks = data['weeks']

        formatted_data = {
            f"mapid{map_id}": {
                major_name: {
                    year: {
                        course_name: weeks
                    }
                }
            }
        }
        
        return formatted_data