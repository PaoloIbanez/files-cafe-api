from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random", methods=["GET"])
def get_random_cafe():
    random_cafe = db.session.execute(db.select(Cafe).order_by(db.func.random())).scalar()
    return jsonify(
        id=random_cafe.id,
        name=random_cafe.name,
        map_url=random_cafe.map_url,
        img_url=random_cafe.img_url,
        location=random_cafe.location,
        seats=random_cafe.seats,
        has_toilet=random_cafe.has_toilet,
        has_wifi=random_cafe.has_wifi,
        has_sockets=random_cafe.has_sockets,
        can_take_calls=random_cafe.can_take_calls,
        coffee_price=random_cafe.coffee_price,
    )

@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[{
        "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "has_toilet": cafe.has_toilet,
        "has_wifi": cafe.has_wifi,
        "has_sockets": cafe.has_sockets,
        "can_take_calls": cafe.can_take_calls,
        "coffee_price": cafe.coffee_price,
    } for cafe in cafes])

@app.route("/search", methods=["GET"])
def search_cafe():
    loc = request.args.get("loc")
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if cafes:
        return jsonify(cafes=[{
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        } for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, no cafes found at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    # Check if all required fields are present in the request
    if not request.form.get("name"):
        return jsonify(error={"message": "Cafe name is required."}), 400

    # Create a new Cafe object with the data from the request
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=int(request.form.get("seats")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})



# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    if not new_price:
        return jsonify(error={"Bad Request": "new_price parameter is required."}), 400

    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    cafe_to_update.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."}), 200


# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
