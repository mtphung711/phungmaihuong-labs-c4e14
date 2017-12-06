from gmail import GMail, Message

content = '''<p>Em ch&agrave;o c&ocirc;,</p>
<p>H&ocirc;m nay m&egrave;o nh&agrave; em đi lạc n&ecirc;n em phải nghỉ học để t&igrave;m m&egrave;o ạ. Em xin hứa sẽ ch&eacute;p b&agrave;i v&agrave; l&agrave;m b&agrave;i đầy đủ.</p>
<p>Học tr&ograve; y&ecirc;u thương của c&ocirc;.</p>'''


gmail = GMail('nit.c4e@gmail.com','vinamilk711')

msg = Message('Xin nghi om',to='nit.c4e@gmail.com',html=content)

from datetime import datetime

hour = datetime.now().hour

if hour == 7:
    gmail.send(msg)
