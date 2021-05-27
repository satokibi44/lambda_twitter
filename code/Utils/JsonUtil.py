class JsonUtil():
    def __init__(self) -> None:
        pass
    def sort_reply_with_id(self, json):
        return sorted(json, key=lambda x: x['id'])
