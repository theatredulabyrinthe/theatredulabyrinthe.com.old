from flask import render_template, Blueprint, request, url_for, redirect

spectacles = Blueprint("spectacles", __name__)


@spectacles.route("/creations_adultes/les-caprices-de-nina/")
@spectacles.route("/creations_adultes/les-caprices-de-nina")
def caprices_nina():
    return render_template("spectacles/adultes/nina.html", title="LABY | SPECTACLES")


@spectacles.route("/creations_adultes/un-pepin-dans-la-paille/")
@spectacles.route("/creations_adultes/un-pepin-dans-la-paille")
def pepin_paille():
    return render_template("spectacles/adultes/pepin.html", title="LABY | SPECTACLES")


@spectacles.route("/creations_adultes/echec-et-mat/")
@spectacles.route("/creations_adultes/echec-et-mat")
def echec_mat():
    return render_template("spectacles/adultes/echec.html", title="LABY | SPECTACLES")


@spectacles.route("/creations_adultes/green-paradise/")
@spectacles.route("/creations_adultes/green-paradise")
def green_paradise():
    return render_template("spectacles/adultes/green.html", title="LABY | SPECTACLES")


@spectacles.route("/creations_adultes/rouge-cerise/")
@spectacles.route("/creations_adultes/rouge-cerise")
def rouge_cerise():
    return render_template("spectacles/adultes/rouge.html", title="LABY | SPECTACLES")


@spectacles.route("/creations_adultes/bleue-nuit/")
@spectacles.route("/creations_adultes/bleue-nuit")
def bleue_nuit():
    return render_template("spectacles/adultes/bleue.html", title="LABY | SPECTACLES")


@spectacles.route("/creations_adultes/oui-je-le-veux/")
@spectacles.route("/creations_adultes/oui-je-le-veux")
def oui_je_le_veux():
    return render_template("spectacles/adultes/oui.html", title="LABY | SPECTACLES")
