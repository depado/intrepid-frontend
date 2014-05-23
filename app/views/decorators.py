from functools import wraps
from flask import redirect, url_for, session


def login_required(f):
    """
    Decorator to use if a view needs to be protected by a login.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'username' in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
