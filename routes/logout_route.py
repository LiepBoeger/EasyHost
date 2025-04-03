from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, logout_user

logout_route_bp = Blueprint('logout_route', __name__)

@logout_route_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado com sucesso.', 'success')
    return redirect(url_for('login_route.login'))