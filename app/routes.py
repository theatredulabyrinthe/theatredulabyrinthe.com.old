from flask import render_template, Blueprint, request, url_for, redirect

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home/")
@main.route("/home")
def home():
    page = "salon"
    if page == "olympe":
        return render_template("home-olympe.html", title="LABY | HOME")
    if page == "info":
        return render_template("home-info.html", title="LABY | HOME")
    elif page == "rentree":
        return render_template("home-rentree.html", title="LABY | HOME")
    elif page == "salon":
        return render_template("home-salon.html", title="LABY | HOME")
    else:
        return render_template("home.html", title="LABY | HOME")

@main.route("/presse/")
@main.route("/presse")
def presse():
    return render_template("presse.html", title="LABY | PRESSE")


@main.route("/association/")
@main.route("/association")
@main.route("/l-association")
def association():
    return render_template("association.html", title="LABY | L'ASSOCIATION")


@main.route("/ateliers/")
@main.route("/ateliers")
@main.route("/les-ateliers")
def ateliers():
    return render_template("ateliers.html", title="LABY | ATELIERS")


@main.route("/coaching/")
@main.route("/coaching")
def coaching():
    return render_template("coaching.html", title="LABY | COACHING")


@main.route("/galerie/")
@main.route("/galerie")
def galerie():
    return render_template("galerie.html", title="LABY | GALERIE")


@main.route("/rentree/")
@main.route("/rentree")
def rentree():
    return render_template("rentree.html", title="LABY | RENTRÉE")


@main.route("/tarifs/")
@main.route("/tarifs")
def tarifs():
    return render_template("tarifs.html", title="LABY | TARIFS")


@main.route("/contact/")
@main.route("/contact")
def contact():
    return render_template("contact.html", title="LABY | CONTACT")


@main.route("/creations_enfants/")
@main.route("/creations_enfants")
def creations_enfants():
    return render_template("creations_enfants.html", title="LABY | SPECTACLES")


@main.route("/creations_adultes/")
@main.route("/creations_adultes")
def creations_adultes():
    return render_template("creations_adultes.html", title="LABY | SPECTACLES")

