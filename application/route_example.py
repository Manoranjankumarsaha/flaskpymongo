from application import api
from flask_restx import Resource,fields

example_ns = api.namespace('example', description='Example endpoints')

example_model = example_ns.model('Example_model', {
    'id': fields.Integer(required=True, description='Example ID'),
    'name': fields.String(required=True, description='Example name')
})

EXAMPLES = [
    {'id': 1, 'name': 'Example 1'},
    {'id': 2, 'name': 'Example 2'}
]

@example_ns.route('/')
class ExampleList(Resource):
    @example_ns.marshal_list_with(example_model)
    def get(self):
        return EXAMPLES

    @example_ns.expect(example_model)
    @example_ns.marshal_with(example_model)
    def post(self):
        example = api.payload
        EXAMPLES.append(example)
        return example, 201

@example_ns.route('/<int:id>')
@example_ns.response(404, 'Example not found')
class ExampleItem(Resource):
    @example_ns.marshal_with(example_model)
    def get(self, id):
        for example in EXAMPLES:
            if example['id'] == id:
                return example
        example_ns.abort(404)

    @example_ns.expect(example_model)
    @example_ns.marshal_with(example_model)
    def put(self, id):
        for example in EXAMPLES:
            if example['id'] == id:
                example.update(api.payload)
                return example
        example_ns.abort(404)

    def delete(self, id):
        for i, example in enumerate(EXAMPLES):
            if example['id'] == id:
                del EXAMPLES[i]
                return '', 204
        example_ns.abort(404)

# api.add_resource(ExampleList, '/todos')
# api.add_resource(ExampleItem, '/todos/<int:id>')
# api.add_namespace(example_ns)