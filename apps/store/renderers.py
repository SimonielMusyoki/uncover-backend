import json
from rest_framework.renderers import JSONRenderer

class ProductJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        errors = data.get("errors", None)
        if errors is not None:
            return super(ProductJSONRenderer, self).render(data)
        return json.dumps({
            "status": status_code,
            "product": data
        })

class ProductsJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        errors = data.get("errors", None)
        if errors is not None:
            return super(ProductsJSONRenderer, self).render(data)
        return json.dump({
            "status": status_code,
            "products": data
        })


class CategoryJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        errors = data.get("errors", None)
        if errors is not None:
            return super(CategoryJSONRenderer, self).render(data)
        return json.dumps({
            "status": status_code,
            "data": data
        })