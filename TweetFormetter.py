import re
import emoji

class TweetFormetter():

    def screening(text):
        s = text

        # RTを外す
        if s[0:3] == "RT ":
            s = s.replace(s[0:3], "")
        # @screen_nameを外す
        while s.find("@") != -1:
            index_at = s.find("@")
            if s.find(" ") != -1:
                index_sp = s.find(" ", index_at)
                if index_sp != -1:
                    s = s.replace(s[index_at:index_sp + 1], "")
                else:
                    s = s.replace(s[index_at:], "")
            else:
                s = s.replace(s[index_at:], "")
                
        # 改行を外す
        while s.find("\n") != -1:
            index_ret = s.find("\n")
            s = s.replace(s[index_ret], "")
            
        # URLを外す
        s = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", s)
        
        # 絵文字を「。」に置き換え その１
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), '。')
        s = s.translate(non_bmp_map)
        
        # 絵文字を「。」に置き換え　その２
        s = ''.join(c if c not in emoji.UNICODE_EMOJI else '。' for c in s)
        
        # 置き換えた「。」が連続していたら１つにまとめる
        while s.find('。。') != -1:
            index_period = s.find('。。')
            s = s.replace(s[index_period:index_period + 2], '。')
            
        # ハッシュタグを外す
        while s.find('#') != -1:
            index_hash = s.find('#')
            s = s[0:index_hash]
            
        return s
