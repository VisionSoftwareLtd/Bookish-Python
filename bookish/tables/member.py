class Member:
    def __init__(self, firstName, lastName, memberId=None):
        self.memberId = memberId
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self) -> str:
        return f'MemberId: {self.memberId}, FirstName: {self.firstName}, LastName: {self.lastName}'
