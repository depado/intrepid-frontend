# -*- coding: utf-8 -*-

# System Imports
import os

# Flask Imports
from flask import flash, render_template, redirect, request, url_for
from werkzeug import secure_filename

# Local Imports
from app import app
from decorators import login_required
from app.functions import check_ip_string, extension_ok
from app.forms import IpForm
from constants import DOSSIER_UPS, ips, globalsettings

@app.route('/scenarios', methods=['GET', 'POST'])
@login_required
def scenarios():
    """ Scenario Page, Associated to scenarios.html """
    xmlist = [xml for xml in os.listdir(DOSSIER_UPS) if extension_ok(xml)]
    form = IpForm()
    if form.validate_on_submit():
        if form.ipincluded.data:
            if check_ip_string(form.ipincluded.data):
                if form.ipincluded.data in ips.excludedip:
                    flash(u"IP is in the exclusion list", 'error')
                else:
                    if form.ipincluded.data in ips.includedip:
                        flash(u"IP already added", 'error')
                    else:
                        ips.includedip.append(form.ipincluded.data)
                        flash(u"Saved", 'info')
            else:
                flash(u"Not an IP", 'error')
        if form.ipexcluded.data:
            if check_ip_string(form.ipexcluded.data):
                if form.ipexcluded.data in ips.includedip:
                    flash(u"IP is in the inclusion list", 'error')
                else:
                    if form.ipexcluded.data in ips.excludedip:
                        flash(u"IP already added", 'error')
                    else:
                        ips.excludedip.append(form.ipexcluded.data)
                        flash(u"Saved", 'info')
            else:
                flash(u"Not an IP", 'error')
    else:
        if request.method == 'POST':
            f = request.files['fic']
            if f:
                if extension_ok(f.filename):
                    nom = secure_filename(f.filename)
                    f.save(DOSSIER_UPS + nom)
                    flash(u'File uploaded', 'info')
                    return redirect("/scenarios#select")
                else:
                    flash(u'Wrong extension (only *.xml)', 'error')
            else:
                flash(u'No file to upload', 'error')
    return render_template('scenarios.html', title='IntrePid', settings=globalsettings, form=form, ips=ips,
                           xmlist=xmlist)


@app.route('/scenarios/remove_include', methods=['GET', 'POST'])
@login_required
def remove_include():
    """ Removes an Included IP """
    try:
        ips.includedip.pop(int(request.args.get('id')))
        flash(u'Removed', 'info')
    except Exception:
        flash(u"Can't remove this item", 'error')

    return redirect(url_for('scenarios'))


@app.route('/scenarios/remove_exclude', methods=['GET', 'POST'])
@login_required
def remove_exclude():
    """ Removes an Excluded IP """
    try:
        ips.excludedip.pop(int(request.args.get('id')))
        flash(u"Removed" 'info')
    except Exception:
        flash(u"Can't remove this item", 'error')
    return redirect(url_for('scenarios'))
