from flask import redirect, render_template, request, send_from_directory, abort, jsonify, url_for, session, flash,json
from flask_app import app
from flask_app.models.user import User
from flask_app.models.listing import Listing
from flask_app.models.booking import Booking
import os
from datetime import datetime

@app.route('/booking/<int:listing_id>')
def show_booking_page(listing_id):
    listing = Listing.get_listing_by_id(listing_id)
    user_id = session.get('user_id')
    booked_dates = Booking.get_booked_dates(listing_id)
    if user_id:
        return render_template("/bookings/create_booking.html", listing=listing, user_id=user_id, booked_dates=booked_dates)
    else:
        flash('You must create an account to book a rental.')
        return redirect('/login')

@app.route('/booking/create', methods=['POST'])
def create_booking():
    check_in = datetime.strptime(request.form["check_in"], "%m/%d/%Y").strftime("%Y-%m-%d")
    check_out = datetime.strptime(request.form["check_out"], "%m/%d/%Y").strftime("%Y-%m-%d")
    data = {
    "check_in" : check_in,
    "check_out" : check_out,
    "number_of_guests" :request.form["number_of_guests"],
    "listing_id": request.form["listing_id"],
    "user_id": session['user_id']
    }
    Booking.book_it(data)
    listing_id = data['listing_id']
    return redirect('/booking/success/' + str(listing_id))


@app.route('/booking/success/<int:listing_id>')
def booking_success(listing_id):
    listing = Listing.get_listing_by_id(listing_id)
    user_id = session.get('user_id')
    host = User.get_by_id(listing.user_id)
    if user_id:
        bookings = Booking.get_all_bookings_with_users(user_id)
        return render_template('/bookings/booking_success.html', listing=listing, bookings=bookings, host = host)
    else:
        flash('User ID not found in session. Please log in.')
        print(listing)
        print(bookings)
        return redirect('/login')

@app.route('/booking/my_booking')
def show_my_bookings():
    first_name = session.get('first_name')
    user_id = session.get('user_id')
    
    if user_id:
        bookings = Booking.get_all_bookings_with_users(user_id)
        user_listings = Listing.get_user(user_id)
        print("Bookings",bookings)
        return render_template('/bookings/my_bookings.html', bookings=bookings, listings=user_listings, first_name=first_name)
    else:
        flash('User ID not found in session. Please log in.')
        return redirect('/login')

@app.route('/booking/show_who_booked')
def show_who_booked():
    first_name = session.get('first_name')
    user_id = session.get('user_id')
    user_listings = Listing.get_user(user_id)
    if user_listings:
        listing_ids = [listing.id for listing in user_listings]
        bookings = Booking.get_all_bookings_for_listings(listing_ids)
        return render_template('/bookings/show_who_booked.html', bookings=bookings, first_name=first_name)
    else:
        flash('User ID not found in session or no listings found. Please log in or create listings.')
        return redirect('/login')


@app.route('/booking/delete/<int:booking_id>')
def remove_booking(booking_id):
    Booking.delete(booking_id)
    return redirect ('/booking/my_booking')