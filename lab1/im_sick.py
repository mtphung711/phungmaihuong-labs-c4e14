from gmail import GMail, Message


content = '''<p>Em ch&agrave;o chị,</p>
<p>Em đang bị {{sickness}}&nbsp;n&ecirc;n nghỉ l&agrave;m nh&eacute; chị đừng gọi em lại đau th&ecirc;m.</p>
<p>Thank you chị miss you loads!</p>'''


gmail = GMail('nit.c4e@gmail.com','vinamilk711')

msg = Message('Xin nghi om',to='nit.c4e@gmail.com',html=content)

gmail.send(msg)
