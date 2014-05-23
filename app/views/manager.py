# -*- coding: utf-8 -*-

# Flask Imports
from flask import render_template, redirect, request, flash

# Local Imports
from app import app
from app.scenario import ScenarObject
from decorators import login_required
from constants import ips, globalsettings, scenario
from app.forms import NmapForm, TypeIpForm

@app.route('/scenarios/type', methods=['GET', 'POST'])
@login_required
def type():
    formdict = dict()
    formdict['typeipform'] = TypeIpForm()
    formdict['nmap'] = NmapForm()
    if ips.includedip:
        return render_template('type.html', title='IntrePId', settings=globalsettings, ips=ips, forms=formdict)
    else:
        flash(u"No target specified", "error")
        return redirect('/scenarios')


@app.route('/scenarios/_addObject', methods=['GET', 'POST'])
@login_required
def add_object():
    presets = "caca"
    newobject = ScenarObject()
    newobject.target = ips.includedip[int(request.args.get('id'))]
    newobject.type = request.args.get('cmd')
    if request.args.get('cmd') in presets:
        newobject.command = presets[request.args.get('cmd')]
    scenario.append(newobject)
    flash(u"Saved in the manager", "info")
    return redirect('/scenarios/type')


# Scenario Manager
# Associated to manager.html
@app.route('/scenarios/manager', methods=['GET', 'POST'])
@login_required
def manager():
    """ Scenario Manager Page, Associated to manager.html """
    if ips.includedip and scenario:
        return render_template('manager.html', title='IntrePId', settings=globalsettings, ips=ips,
                               scenario=scenario)
    else:
        flash(u"No scenario object specified", 'error')
        return redirect('/scenarios/type')


@app.route('/scenarios/manager/_upObj')
@login_required
def up_obj():
    id = int(request.args.get('id'))
    try:
        scenario[id], scenario[id - 1] = scenario[id - 1], scenario[id]
    except:
        flash(u"Can't move that item", 'error')
    return redirect('/scenarios/manager')


@app.route('/scenarios/manager/_downObj')
@login_required
def down_obj():
    index = int(request.args.get('id'))
    try:
        scenario[index], scenario[index + 1] = scenario[index + 1], scenario[index]
    except:
        flash(u"Can't move that item", 'error')
    return redirect('/scenarios/manager')


@app.route('/scenarios/manager/_delObj')
@login_required
def del_obj():
    id = int(request.args.get('id'))
    try:
        scenario.pop(id)
    except:
        flash(u"That element doesn't exist anymore", 'error')
    return redirect('/scenarios/manager')
