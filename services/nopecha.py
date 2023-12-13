import nopecha

class NopeCha:
    def __init__(self,key=None) -> None:
        self._key = key
    
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key
        nopecha.api_key = self.key



    def balance(self):
        return nopecha.Balance.get()

    def recaptcha2(self, sitekey, url):
        token = nopecha.Token.solve(
            type='recaptcha2',
            sitekey=sitekey,
            url=url
        )
        return token

    def recaptcha3(self, sitekey, url):

        token = nopecha.Token.solve(
            type='recaptcha3',
            sitekey=sitekey,
            url=url,
            data={
                    'action': 'check'
                }
        )
        return token

    
    def hcaptcha(self, sitekey, url):
        token = nopecha.Token.solve(
            type='hcaptcha',
            sitekey=sitekey,
            url=url
        )
        return token

api = NopeCha()
