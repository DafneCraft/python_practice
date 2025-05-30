
EXPECTED_BAKE_TIME = 40

def bake_time_remainig(time):
     """ Calculate the bake time remainig 
          :param time: int - time in minutes of bake in the oven.
          return: int - time remaining"""
     time_remainig = EXPECTED_BAKE_TIME - time
     return time_remainig

def preparation_time_in_minutes(number_of_layers):
     """Calculate preparation time in minutes.
          :param number_of_layers: int - numbers of layers to prepare lasagna.
          :return: int - preparation total time"""
     time_per_layer = 2 * number_of_layers
     return time_per_layer

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
     """ Calculate the elapsed cooking time.
          :param number_of_layers: int - the number of layers in the lasagna.
          :param elapsed_bake_time: int - elapsed cooking time.
          :return: int - total time elapsed (in minutes) preparing and cooking.
          
          This function take two integers representing the number of lasagna layers
          and the time already spent baking and calculates the total elapsed minutes
          spent cooking the lasagna."""

     time_layers = 2 * number_of_layers
     total_time = time_layers + elapsed_bake_time
     return total_time

print(bake_time_remainig(30))
print(preparation_time_in_minutes(2))
print(elapsed_time_in_minutes(3,20))