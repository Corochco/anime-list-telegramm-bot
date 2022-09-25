class User:
    def __init__(self, user_id, nickname, title_list, rate_list, note_list):
        self.user_id = user_id
        self.nickname = nickname
        self.title_list = title_list
        self.rate_list = rate_list
        self.note_list = note_list
    def get_user_id(self):
        return self.user_id
    def get_nickname(self):
        return self.nickname
    def get_title_list(self):
        return self.title_list
    def get_rate_list(self):
        return self.rate_list
    def get_note_list(self):
        return self.note_list


