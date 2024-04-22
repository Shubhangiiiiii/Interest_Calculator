from django.db import models

class InterestCalculation(models.Model):
    principal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    time_period = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_interest(self):
        return (self.principal_amount * self.interest_rate * self.time_period) / 100