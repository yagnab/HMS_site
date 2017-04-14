from django.db import models

class Customer(models.Model):
    #fields
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username

class Hotel(models.Model):
    name = models.CharField(max_length = 150)
    street_num = models.CharField(max_length = 10)
    street_name = models.CharField(max_length = 100)
    town_name = models.CharField(max_length = 100)
    postcode = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

class Room(models.Model):
    #relations
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    #fields
    room_number = models.IntegerField(unique=True)
    cost_per_night = models.DecimalField(max_digits = 8, decimal_places=2)
    
    def __str__(self):
        return "Room: " + str(self.room_number)

    #remove later
    def test_function(self):
        return "This should be removed"

##class Bed(models.Model):
##    #relations
##    room = models.ManyToManyField(Room)
##
##    #fields
##    bed_type = models.CharField(max_length=30)
##
##    #methods
##    def __str__(self):
##        return self.bed_type
##    
###TODO: Fin bookings db model
##class Booking(models.Model):
##    #relations
##    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
##    room = models.ForeignKey(Room, on_delete=models.CASCADE)
##
##    #fields
##    start_day = models.DateField()
##    end_day = models.DateField()
##    is_active = models.BooleanField(default=False)
##
##    #properties
##    @property
##    def nights_active(self):
##        dt = self.end_day - self.start_day
##        return dt.days
##
##    #methods
##    def detail_are_valid(self):
##        if self.nights_active > 0:
##            return True
##        else:
##            return False
##        
##    def save(self):
##        if self.detail_are_valid():
##            super().save() # Call the "real" save() method.
##        else:
##            raise AttributeError('Those attributes are invalid.')
##
##    def __str__(self):
##        return self.customer + ": " + self.room
##    
##class ActiveBooking(models.Model):
##    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
##
##    def __str__(self):
##        return self.booking
