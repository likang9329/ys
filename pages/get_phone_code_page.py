from base.bases import Base


class Get_phone_code:
    def get_phone_code(self):
        i=Base().getUrl()
        url = i+'minorApp/common/sendPhoneCode'
        print(url)
        params = {
            'phone': '13296592650',
            'sType': '1'
        }
        return Base().send_request('g',url,params)