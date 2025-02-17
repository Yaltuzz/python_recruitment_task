from datetime import datetime

def convert_stars_to_points(stars):
    points = {
        1: -1,
        2: 1,
        3: 0,
        4: 2,
        5: 3
    }
    return points.get(stars, 0)

class Rating:
    def __init__(self, bill_value, taste, size, service):
        self.date = datetime.now()
        self.bill_value = bill_value
        self.taste = taste
        self.size = size
        self.service = service


    def get_points(self):
        taste_points = convert_stars_to_points(self.taste)
        size_points = convert_stars_to_points(self.size)
        service_points = convert_stars_to_points(self.service)
        
        return taste_points, size_points, service_points
    
    def __repr__(self):
        return f"Rating(date={self.date.strftime('%Y-%m-%d %H:%M:%S')}, bill_value={self.bill_value}, taste={self.taste}, size={self.size}, service={self.service})"


class Restaurant:
    def __init__(self, restaurant_id):
        self.restaurant_id = restaurant_id
        self.ratings = []
    
    def rate(self, bill_value, taste, size, service):
        rating = Rating(bill_value, taste, size, service)
        self.ratings.append(rating)
    
    def get_rating_history(self):
        history = []
        for rating in self.ratings:
            history.append(repr(rating))
        return history
    
    def get_rating(self):
        taste_sum_weighted = 0
        size_sum_weighted = 0
        service_sum_weighted = 0
        total_bills_value = 0
        
        for rating in self.ratings:
            bill_value = rating.bill_value
            taste, size, service = rating.get_points()
            
            taste_sum_weighted += taste * bill_value
            size_sum_weighted += size * bill_value
            service_sum_weighted += service * bill_value
            total_bills_value += bill_value
        
        average_taste_weighted = taste_sum_weighted / total_bills_value if total_bills_value else 0
        average_size_weighted = size_sum_weighted / total_bills_value if total_bills_value else 0
        average_service_weighted = service_sum_weighted / total_bills_value if total_bills_value else 0
        
        average_overall_rating = (average_taste_weighted+average_size_weighted+average_service_weighted)/3
        

        average_taste_weighted = round(average_taste_weighted, 2)
        average_size_weighted = round(average_taste_weighted, 2)
        average_service_weighted = round(average_taste_weighted, 2)
        average_overall_rating = round(average_taste_weighted, 2)


        def points_to_stars(points):
            rounded_points = round(points)
            if rounded_points < 0:
                return '*'
            elif rounded_points < 1:
                return '**'
            elif rounded_points < 2:
                return '***'
            elif rounded_points < 3:
                return '****'
            else:
                return '*****'
        
        return {
            'taste': (average_taste_weighted, points_to_stars(average_taste_weighted)),
            'size': (average_size_weighted, points_to_stars(average_size_weighted)),
            'service': (average_service_weighted, points_to_stars(average_service_weighted)),
            'overall': (
                average_overall_rating,
                points_to_stars(average_overall_rating)
            )
        }

class RestaurantRatingSystem:
    def __init__(self):
        self.restaurants = {}
    
    def rate_restaurant(self, restaurant_id, bill_value, taste, size, service):
        if restaurant_id not in self.restaurants:
            self.restaurants[restaurant_id] = Restaurant(restaurant_id)
        
        restaurant = self.restaurants[restaurant_id]
        restaurant.rate(bill_value, taste, size, service)
    
    def get_rating_history(self, restaurant_id):
        if restaurant_id not in self.restaurants:
            return []
        
        restaurant = self.restaurants[restaurant_id]
        return restaurant.get_rating_history()
    
    def get_rating(self, restaurant_id):
        if restaurant_id not in self.restaurants:
            return None, None
        
        restaurant = self.restaurants[restaurant_id]
        return restaurant.get_rating()



if __name__ == '__main__':
    system = RestaurantRatingSystem()

    system.rate_restaurant(1, 4, 1, 1, 1)
    system.rate_restaurant(1, 31, 5, 5, 5)
    system.rate_restaurant(1, 2, 2, 2, 2)
    system.rate_restaurant(1, 23, 3, 3, 3)


    print(system.get_rating_history(1))
    print()
    print(system.get_rating(1))
