
from flask_app.config.mysqlconnection import connectToMySQL
from flask import session
from flask_app.models.user import User
from flask_app.models.listing import Listing
import datetime

class Booking:
    DB = "rv_rentals_schema"
    def __init__(self, booking_dict):
        self.id = booking_dict["id"]
        self.check_in = booking_dict["check_in"]
        self.check_out = booking_dict["check_out"]
        self.number_of_guests = booking_dict["number_of_guests"]
        self.created_at = booking_dict["created_at"]
        self.updated_at = booking_dict["updated_at"]
        self.listing_id = booking_dict["listing_id"]
        self.user_id = booking_dict["user_id"]
        self.user = booking_dict["user"]
        self.listing = booking_dict['listing']
        self.bookings = []


    @classmethod
    def book_it(cls, data):
        query = "INSERT INTO bookings (check_in, check_out, number_of_guests, listing_id, user_id) VALUES (%(check_in)s, %(check_out)s, %(number_of_guests)s, %(listing_id)s, %(user_id)s)"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result


    @classmethod
    def get_all_bookings_with_users(cls, user_id):
        query = """
            SELECT bookings.*, listings.id AS listing_id, listings.title, listings.description, listings.rate, 
            listings.location, listings.availability, listings.add_photos, listings.created_at AS listing_created_at,
            listings.updated_at AS listing_updated_at, users.id AS user_id, users.first_name, users.last_name, 
            users.email, users.password, users.created_at AS user_created_at, users.updated_at AS user_updated_at
            FROM bookings
            JOIN listings ON bookings.listing_id = listings.id
            JOIN users ON bookings.user_id = users.id 
            WHERE bookings.user_id = %(user_id)s"""
        data = {"user_id": user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        all_bookings = []
        for row in results:
            booking_dict = {
                "id": row["id"],
                "check_in": row["check_in"],
                "check_out": row["check_out"],
                "number_of_guests": row["number_of_guests"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "listing_id": row["listing_id"],
                "user_id": row["user_id"],
            }
            listing = Listing({
                "id": row["listing_id"],
                "title": row["title"],
                "description": row["description"],
                "rate": row["rate"],
                "location": row["location"],
                "availability": row["availability"],
                "add_photos": row["add_photos"],
                "created_at": row["listing_created_at"],
                "updated_at": row["listing_updated_at"],
                "user_id": row["user_id"]
            })

            user = User({
                "id": row["user_id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["user_created_at"],
                "updated_at": row["user_updated_at"]
            })

            booking_dict["listing"] = listing
            booking_dict["user"] = user
            booking = Booking(booking_dict)
            all_bookings.append(booking)

        print("All-Bookings", all_bookings)
        return all_bookings


    
    @classmethod
    def get_user_with_bookings(cls, user_id):
        query = "SELECT * FROM users JOIN bookings ON users.id = bookings.user_id WHERE bookings.user_id = %(user_id)s"
        data = {"user_id":user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        user = User(results[0])
        for row in results:
            booking_data = {
                "id":row['id'],
                "check_in":row['check_in'],
                "check_out":row['check_out'],
                "number_of_guests":row['number_of_guests'],
                "created_at":row['created_at'],
                "updated_at":row['updated_at'],
                "listing_id":row['listing_id']
            }
            booking_object = Booking(booking_data)
            user.bookings.append(booking_object)
        return user


    @classmethod
    def get_all_bookings_for_listings(cls, listing_ids):
        query = """
            SELECT bookings.*, listings.*, users.*
            FROM bookings
            JOIN listings ON bookings.listing_id = listings.id
            JOIN users ON bookings.user_id = users.id
            WHERE bookings.listing_id IN %(listing_ids)s
            """
        data = {"listing_ids": tuple(listing_ids)}
        results = connectToMySQL(cls.DB).query_db(query, data)
        all_bookings = []
        for row in results:
            booking_dict = {
                "id": row["id"],
                "check_in": row["check_in"],
                "check_out": row["check_out"],
                "number_of_guests": row["number_of_guests"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "listing_id": row["listing_id"],
                "user_id": row["user_id"],
            }
            listing = Listing({
                "id": row["id"],
                "title": row["title"],
                "description": row["description"],
                "rate": row["rate"],
                "location": row["location"],
                "availability": row["availability"],
                "add_photos": row["add_photos"],
                "created_at": row["listings.created_at"],
                "updated_at": row["listings.updated_at"],
                "user_id": row["listings.user_id"]
            })

            user = User({
                "id": row["id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            })

            booking_dict["listing"] = listing
            booking_dict["user"] = user
            booking = Booking(booking_dict)
            all_bookings.append(booking)
        print("bookings",all_bookings)
        return all_bookings
    
    @classmethod
    def get_booked_dates(cls, listing_id):
        query = """
                    SELECT bookings.check_in, bookings.check_out
                    FROM bookings
                    WHERE bookings.listing_id = %(listing_id)s
                """
        data = {"listing_id": listing_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        booked_dates = []
        for row in results:
            start_date = row["check_in"]
            end_date = row["check_out"]
            date_range = {
                'start_date': start_date,
                'end_date': end_date
            }
            booked_dates.append(date_range)
        return booked_dates

    @classmethod
    def delete(cls, booking_id):
        query = "DELETE from bookings WHERE id = %(id)s"
        result = connectToMySQL(cls.DB).query_db(query, {"id":booking_id})
        return result
    