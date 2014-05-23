# -*- coding: utf-8 -*-

# Flask Imports
from flask import redirect, session, flash, render_template, url_for

# Local Imports
from app import app
from app.forms import LoginForm
from constants import globalsettings
from decorators import login_required

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Login Page, Associated to login.html """
    if 'username' in session:
        flash(u"Already logged in", 'error')
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == globalsettings.password:
            session['username'] = 'admin'
            flash(u"You're now logged in", 'info')
            return redirect(url_for('index'))
        return redirect(url_for('login'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
@login_required
def logout():
    """ Logout Routine """
    session.pop('username', None)
    return redirect(url_for('login'))