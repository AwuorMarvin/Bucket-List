class Bucket(object):
    bucketlist = []

    def __init__(self):
        self.bucket_list = {}
                
    def create_bucket(self, title, description):
        self.bucket_list.update({title:description})
        self.bucketlist.append(self.bucket_list)
        return self.bucketlist

    def delete_bucket(self, title):
        self.bucketlist.pop(self.bucket_list)

    def update_bucket(self, title, description):
        self.bucket_list.update({title:description})
                