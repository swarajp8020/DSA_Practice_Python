from datetime import timedelta
from django.utils import timezone

last_30_days = timezone.now() - timedelta(days = 30)
records = MyModel.objects.filter(created_at__gte = last_30_days)