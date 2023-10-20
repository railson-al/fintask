from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import HTTP_HEADER_ENCODING

class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        try:
            auth = header.decode(HTTP_HEADER_ENCODING)
        except UnicodeError:
            raise AuthenticationFailed('Invalid token header. Token string should not contain invalid characters.')

        prefix, token = auth.split()
        
        if prefix.lower() != self.keyword.lower():
            return None

        return self.authenticate_credentials(token)

    def get_header(self, request):
        header = request.headers.get('Authorization')
        if header is None:
            return None
        
        return header.split()