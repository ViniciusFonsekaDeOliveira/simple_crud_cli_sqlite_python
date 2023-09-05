class Person:
    def __init__(self, uuid: str, firstname: str, lastname: str, nickname: str, email: str ):
        self._uuid = uuid
        self._firstname = firstname
        self._lastname = lastname
        self._nickname = nickname
        self._email = email
    
    @property
    def uuid(self):
        return self._uuid
    
    @property
    def firstname(self):
        return self._firstname
    
    @property
    def lastname(self):
        return self._lastname
    
    @property
    def nickname(self):
        return self._nickname
    
    @property
    def email(self):
        return self._email
    

    @uuid.setter
    def uuid(self, uuid: str):
        self._uuid = uuid
    
    @firstname.setter
    def firstname(self, firstname: str):
        self._firstname = firstname
    
    @lastname.setter
    def lastname(self, lastname: str):
        self._lastname = lastname
    
    @nickname.setter
    def nickname(self, nickname: str):
        self._nickname = nickname
    
    @email.setter
    def email(self, email):
        self._email = email


    def to_dict(self):
        return {
            "uuid": self.uuid,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "nickname": self.nickname,
            "email": self.email
        }
    
    def __str__(self):
        return str({
            "uuid": self.uuid,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "nickname": self.nickname,
            "email": self.email
        })

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Person):
            return (self.email == other.email and 
                    self.firstname == other.firstname and 
                    self.lastname == other.lastname and
                    self.uuid == other.uuid and
                    self.nickname == other.nickname)
        return False
    
    def __hash__(self) -> int:
        return hash(self.uuid) ^ hash(self.firstname) ^ hash(self.lastname) ^ hash(self.nickname) ^ hash(self.email)