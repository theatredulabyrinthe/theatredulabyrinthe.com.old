from flask import render_template, Blueprint, request, url_for, redirect

galerie = Blueprint("galerie", __name__)


@galerie.route("/galerie/green-paradise/")
@galerie.route("/galerie/green-paradise")
def green_paradise():
    return render_template("galerie/adultes/green.html", title="LABY | SPECTACLES")


@galerie.route("/galerie/bleue-nuit/")
@galerie.route("/galerie/bleue-nuit")
def bleue_nuit():
    return render_template("galerie/adultes/bleue.html", title="LABY | SPECTACLES")


@galerie.route("/galerie/oui-je-le-veux/")
@galerie.route("/galerie/oui-je-le-veux")
def oui_je_le_veux():
    return render_template("galerie/adultes/oui.html", title="LABY | SPECTACLES")


@galerie.route("/galerie/rouge-cerise/")
@galerie.route("/galerie/rouge-cerise")
def rouge_cerise():
    return render_template("galerie/adultes/rouge.html", title="LABY | SPECTACLES")

@galerie.route("/galerie/rouge-cerise-2022/")
@galerie.route("/galerie/rouge-cerise-2022")
def rouge_cerise():
    return render_template("galerie/adultes/rouge-cerise-2022.html", title="LABY | SPECTACLES")


@galerie.route("/galerie/un-pepin-dans-la-paille/")
@galerie.route("/galerie/un-pepin-dans-la-paille")
def pepin():
    return render_template("galerie/adultes/pepin.html", title="LABY | SPECTACLES")

