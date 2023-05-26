from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash
from flask_app.models import user


import json

class Listing:
    DB = "rv_rentals_schema"
    def __init__(self, listing_dict):
        self.id = listing_dict["id"]
        self.title = listing_dict["title"]
        self.description = listing_dict["description"]
        self.rate = listing_dict["rate"]
        self.location = listing_dict['location']
        self.availability = listing_dict["availability"]
        self.add_photos = listing_dict["add_photos"]
        self.created_at = listing_dict["created_at"]
        self.updated_at = listing_dict["updated_at"]
        self.user_id = listing_dict["user_id"]
        self.photo_paths = []

    

    @classmethod
    def create_listing(cls, data):
        user_id = session['user_id']
        data["user_id"] = user_id
        query = "INSERT INTO listings (title, description, rate, location, availability, add_photos, user_id) VALUES (%(title)s, %(description)s, %(rate)s, %(location)s, %(availability)s, %(add_photos)s, %(user_id)s)"
        results = connectToMySQL(cls.DB).query_db(query, data)

        return results

    @classmethod
    def show_all_listings(cls):
        query = "SELECT * FROM listings"
        result = connectToMySQL(cls.DB).query_db(query)
        return result
    

    @classmethod
    def get_all_listings_with_users(cls):
        query = "SELECT * FROM listings JOIN users on listings.user_id = users.id"
        results = connectToMySQL(cls.DB).query_db(query)
        all_listings = []
        for row in results:
            users = user.User({
                "id" : row["id"],
                "first_name" : row["first_name"],
                "last_name": row["last_name"],
                "email":row["email"],
                "password":row["password"],
                "created_at":row["created_at"],
                "updated_at":row["updated_at"],
            })
            new_listing = Listing({
                "id":row['id'],
                "title" :row["title"],
                "description" :row["description"],
                "rate" :row["rate"],
                "location" :row["location"],
                "availability" :row["availability"],
                "add_photos" :json.loads(row["add_photos"]),
                "created_at":row["created_at"],
                "updated_at":row["updated_at"],
                "user_id" : users
            })
            new_listing.photo_paths = cls.get_photos_for_listing(new_listing.id)
            all_listings.append(new_listing)
        return all_listings
    
    @classmethod
    def get_listing_by_id(cls, listing_id):
        query = "SELECT * FROM listings WHERE id = %(listing_id)s"
        data = {'listing_id': listing_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) == 0:
            return None
        return cls(results[0])

    @classmethod
    def get_user(cls, user_id):
        query = "SELECT * FROM listings WHERE user_id = %(user_id)s"
        data = {'user_id': user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        all_listings = []
        for row in results:
            listing = Listing({
                "id": row["id"],
                "title": row["title"],
                "description": row["description"],
                "rate": row["rate"],
                "location": row["location"],
                "availability": row["availability"],
                "add_photos": row["add_photos"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "user_id": row["user_id"]
            })
            all_listings.append(listing)
        return all_listings

    @classmethod
    def get_photos_for_listing(cls, listing_id):
        query = "SELECT add_photos FROM listings WHERE id = %s"
        result = connectToMySQL(cls.DB).query_db(query, (listing_id,))
        
        if result and result[0]["add_photos"]:
            photo_paths = json.loads(result[0]["add_photos"])
            return photo_paths
        
        return []

    @classmethod
    def has_bookings(cls, listing_id):
        query = """
            SELECT COUNT(*) AS count
            FROM bookings
            WHERE listing_id = %(listing_id)s
        """
        data = {"listing_id": listing_id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result[0]['count'] > 0
    
    @classmethod
    def edit_listing(cls, listing_data):
        query = """UPDATE listings SET title=%(title)s, description = %(description)s, rate=%(rate)s, location = %(location)s, availability = %(availability)s WHERE id = %(listing_id)s"""
        return connectToMySQL(cls.DB).query_db(query, listing_data)
    

        

    @classmethod
    def delete(cls, listing_id):
        query = "DELETE from listings WHERE id = %(id)s"
        result = connectToMySQL(cls.DB).query_db(query, {"id":listing_id})
        return result
    
    

    @classmethod
    def update_listing_photos(cls, data):
        query = "UPDATE listings SET add_photos = %(add_photos)s WHERE id = %(listing_id)s"
        return connectToMySQL(cls.DB).query_db(query, data)
    