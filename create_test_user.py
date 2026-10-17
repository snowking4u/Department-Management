
from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():

    email = "piyush@1234"

    # Check if test user already exists
    user = User.query.filter_by(email=email).first()

    if user:
        print("Test user already exists.")
    else:
        user = User(
            name="Test HOD",
            email=email,
            password=generate_password_hash("12345"),
            role="HOD"
        )

        db.session.add(user)
        db.session.commit()

        print("Test user created successfully!")

    print("Email:", email)
    print("Role: HOD")
