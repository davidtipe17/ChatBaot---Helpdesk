from flask import Flask, render_template, request, jsonify
from app.controller.chat import get_response
from flask_restx import Resource
from app import api

users_ns = api.namespace(
    name='chats',
    description='Rutas de Usuarios',
    path='/chats'
)


@users_ns.route('/')
class ChatsHelp(Resource):
    def get(self):
        return {
            'message': 'hello world'
        }


@users_ns.route('/predict')
class ChatPredict(Resource):
    def post(self):   
        text = request.get_json().get("message")
        response = get_response(text)
        message = {"answer": response}
        return jsonify(message)


