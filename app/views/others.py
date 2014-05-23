# -*- coding: utf-8 -*-

# System Imports
from xml.dom.minidom import parseString

# Flask Imports
from flask import render_template, redirect, request, send_from_directory
from werkzeug import secure_filename

# Local Imports
from app import app
from app.forms import *
from app.functions import *

# Package Imports
from decorators import login_required
from constants import *

@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    """ Index Page, Associated to index.html """
    info.update(globalsettings.interface)
    return render_template('index.html', title='IntrePid', settings=globalsettings, info=info, ips=ips)


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    """ Settings Page, Associated to settings.html """
    form = SettingForm()
    if form.validate_on_submit():
        if form.updatetime.data and form.updatetime.data != globalsettings.updatetime:
            globalsettings.updatetime = form.updatetime.data
            flash(u"Updatetime Changed", 'info')
        if form.interface.data and form.interface.data != globalsettings.interface:
            globalsettings.interface = form.interface.data
            flash(u"Interface Changed", 'info')
    return render_template('settings.html', title='IntrePid', settings=globalsettings, form=form, ips=ips)


@app.route('/updates', methods=['GET', 'POST'])
@login_required
def updates():
    """ Updates Page, Associated to updates.html """
    return render_template('updates.html', title='IntrePid', settings=globalsettings, ips=ips)


@app.route('/term', methods=['GET', 'POST'])
@login_required
def term():
    """ Terminal Page, Associated to terminal.html """
    form = TermForm()
    if form.validate_on_submit():
        if form.command.data:
            string = form.command.data.encode('utf-8').split()
            output = subprocess.check_output(string)
            output = output.replace("\n", "<br />")
            flash(u"Command sent", 'info')
            return render_template('terminal.html', title='IntrePid', settings=globalsettings, form=form,
                                   res=output, ips=ips)
    return render_template('terminal.html', title='IntrePid', settings=globalsettings, form=form, ips=ips)

#######################
#                     #
#  TODO MOTHERFUCKER  #
#                     #
#######################
# Update scenario in XML

@app.route('/liste/open/')
def cat_f():
    nom = request.args.get('file', '')
    f_open = open(DOSSIER_UPS + nom, "r")
    file = f_open.read()
    dom = parseString(file)

    xmlTag = dom.getElementsByTagName('runstats')[0].toxml()
    return render_template('up_liste.html', nom=xmlTag, settings=globalsettings, ips=ips, dom=dom)


@app.route('/liste/download')
def download():
    nom = request.args.get('file')
    return send_from_directory(DOSSIER_UPS, nom)


@app.route('/liste/delete/')
def deletefile():
    nom = request.args.get('id', '')
    os.remove(DOSSIER_UPS + nom)
    return redirect('/scenarios#select')
