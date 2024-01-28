from flask import Blueprint

from ..service.hardware import Hardware

bp = Blueprint('cpu', __name__, url_prefix='/cpu')


@bp.route('/temp', methods=['GET'])
def cpu_temp():
    hw = Hardware()

    return str(hw.get_cpu_temp())