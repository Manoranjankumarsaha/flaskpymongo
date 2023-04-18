from application import api
from flask import jsonify,json
from application.models.emp import Employee as Emp 
from flask_restx import Resource,fields

es = api.namespace('Emp', description='Emp Info...')

emp_model = api.model('Employe', {
    'emp_id': fields.Integer(required=True, description='EmpID'),
    'name': fields.String(required=True, description='name'),
    'age': fields.Integer(required=True, description='age'),
    'email': fields.String(description='Email')
})

@es.route('/')
class EmployeList(Resource):
    # @es.marshal_with(emp_model)
    def get(self):
        # return jsonify(Emp.objects.exclude('_id'))
        return jsonify(Emp.objects.all())

    @es.expect(emp_model)
    def post(self):
        emp = Emp(**api.payload)
        emp.save()
        return {'id': str(emp.emp_id)}, 201

@es.route('/<int:idx>')
class EmployeDetail(Resource):
    def get(self, idx):
        # Get user object by emp_id and exclude some fields
        #emp = Emp.objects.exclude('_id').get(emp_id=idx)
        emp = Emp.objects.get(emp_id=idx)
        # Serialize user object to JSON
        emp_json = json.loads(emp.to_json())
        return jsonify(emp_json)
        # return jsonify(Emp.objects.get_or_404(emp_id=idx))
        
    @es.expect(emp_model)
    def put(self, idx):
        data = api.payload
        # Emp.objects(id=idx).update(title=data['title'], description=data.get('description'))
        # return {'message': 'Todo updated successfully'}
        emp = Emp.objects(emp_id=idx).first()
        # Exclude some fields from update if required
        # data.pop('password', None)
        # Update user object with new values
        Emp.objects(emp_id=idx).update(**data)
        emp = Emp.objects.get(emp_id=idx)
        return jsonify({'message': f'Emp {idx} updated successfully','emp':json.loads(emp.to_json())})

    def delete(self, idx):
        emp = Emp.objects.get(emp_id=idx)
        emp.delete()
        return {'message': f'Emp {idx} deleted successfully'}    