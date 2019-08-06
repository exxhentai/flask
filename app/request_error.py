class RequestError(object):
    def __init__(self, name=''):
        self.name = name

    def required_parameter_not_found(self):
        error_description = self.name + ' is a required parameter'
        return {'error_description': error_description}

    def record_not_found(self):
        return {'error_description': 'Unable to find the record you are looking for.'}
