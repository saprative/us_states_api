from flask import (
        Blueprint,
        url_for,
        request
)
import json

from flask_restplus import (
        Resource, 
        Api, 
        reqparse
)
import math,os
dir = os.path.dirname(__file__)
state_file = os.path.join(dir,'states.json')

states = Blueprint('states',__name__)
api = Api(states)

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, default=1)


with open(state_file) as data_file:
    data = json.load(data_file)

@api.route('/states')
class StatesList(Resource):

    @api.expect(pagination_arguments)
    def get(self):
        args = pagination_arguments.parse_args(request)
        page = args.get('page',1)
        total_page = math.ceil(len(data)/5)
        data_5 = data[5*(page-1):5*(page)]
        if page > 1:
            prev = url_for('states.states_list',page=page-1,_external=True)
        else:
            prev = None
        if page < total_page:
            next = url_for('states.states_list',page=page+1,_external=True)
        else: 
            next = None
        return {
                "data":data_5,
                "prev":prev, 
                "next":next,
                "page":page,
                "total_page": total_page
                }




