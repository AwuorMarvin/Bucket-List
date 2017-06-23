class Bucket(object):
    """Creates class Bucket that inherits from the object class"""
    bucketlist = []

    def __init__(self):
        """Initializing the class"""
        self.bucket_list = {}

    def create_bucket(self, title, description):
        """Method to create the bucketlist"""
        self.bucket_list.update({title:description})
        self.bucketlist.append(self.bucket_list)
        return self.bucketlist

    def delete_bucket(self, title):
        """Method to delete the bucketlist"""
        self.bucketlist.pop(self.bucket_list)

    def update_bucket(self, title, description):
        """Method to update the bucketlist"""
        self.bucket_list.update({title:description})
                