import hashlib, datetime

class Helper(object):

    md5 = "md5"
    sha256 = "sha256"

    def generate_md5_hash(self, string):
        try:
            hash_obj = hashlib.new(self.md5, bytes(string.encode()))
            hash_string = hash_obj.hexdigest()
            return hash_string
        except Exception as error:
            print(error)

    def generate_sha256_hash(self, string):
        try:
            hash_obj = hashlib.new(self.sha256, bytes(string.encode()))
            hash_string = hash_obj.hexdigest()
            return hash_string
        except Exception as error:
            print(error)
