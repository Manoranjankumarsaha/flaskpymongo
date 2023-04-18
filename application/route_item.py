from application import api
from flask_restx import Resource,fields

item_ns = api.namespace('Item', description='Item endpoints')

# define data models
model = item_ns.model('Item_model', {
    'id': fields.Integer(readOnly=True, description='The identifier'),
    'name': fields.String(required=True, description='Name'),
    'description': fields.String(required=True, description='Description')
})

# define storage
storage = []

# define resources
@item_ns.route('/items')
class ItemList(Resource):
    @item_ns.doc('list_items')
    @item_ns.marshal_list_with(model)
    def get(self):
        '''List all items'''
        return storage

    @item_ns.doc('create_item')
    @item_ns.expect(model)
    @item_ns.marshal_with(model, code=201)
    def post(self):
        '''Create a new item'''
        item = api.payload
        item['id'] = len(storage) + 1
        storage.append(item)
        return item, 201

@item_ns.route('/items/<int:item_id>')
@item_ns.response(404, 'Item not found')
class Item(Resource):
    @item_ns.doc('get_item')
    @item_ns.marshal_with(model)
    def get(self, item_id):
        '''Get an item'''
        for item in storage:
            if item['id'] == item_id:
                return item
        api.abort(404, message=f'Item {item_id} not found')

    @item_ns.doc('update_item')
    @item_ns.expect(model)
    @item_ns.marshal_with(model)
    def put(self, item_id):
        '''Update an item'''
        for item in storage:
            if item['id'] == item_id:
                item.update(api.payload)
                return item
        api.abort(404, message=f'Item {item_id} not found')

    @item_ns.doc('delete_item')
    @item_ns.response(204, 'Item deleted')
    def delete(self, item_id):
        '''Delete an item'''
        for i, item in enumerate(storage):
            if item['id'] == item_id:
                storage.pop(i)
                return '', 204
        api.abort(404, message=f'Item {item_id} not found')
