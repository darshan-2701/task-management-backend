from flask_cors import cross_origin
from flask import Blueprint, request, jsonify

from services import task_service

task_bp = Blueprint('task_bp', __name__)


@task_bp.route('/create', methods=['POST'])
@cross_origin()
def create_task():
    result = task_service.TaskCls().create_task(request.json)
    return jsonify(result)


@task_bp.route('/get', methods=['GET'])
@cross_origin()
def get_task():
    result = task_service.TaskCls().get_task()
    return jsonify(result)


@task_bp.route('/delete', methods=['DELETE'])
@cross_origin()
def delete_task():
    result = task_service.TaskCls().delete_task(request.json)
    return jsonify(result)


@task_bp.route('/update', methods=['POST'])
@cross_origin()
def update_task():
    result = task_service.TaskCls().update_task(request.json)
    return jsonify(result)
