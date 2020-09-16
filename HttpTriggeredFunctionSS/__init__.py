import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

#    name = req.params.get('name')
    productId = req.params.get('productId')
    if not productId:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            productId = req_body.get('productId')

    if productId:
#        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
        return func.HttpResponse(f"The product name for your product id {productId} is Starfruit Explosion")

    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a productId in the query string or in the request body for getting the name of the product.",
             status_code=200
        )
