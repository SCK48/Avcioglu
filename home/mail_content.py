def get_mail_content():
    return """
<p>Sayın {name}</p>
<p>{quantity} Adet {product} Fidan Siparişiniz Alınmıştır, </p>
<p>En Kısa Sürede 05373815390 Telefon Numarası ile Geri Dönüş Yapılacaktır. </p>
<p>Saygılar </p>
<p>Avcıoğlu Tarım</p>
<p>Gölcük, 48640 Ula/Muğla</p>
<p>info@avcioglutarim.com</p>
"""

def get_mail_content2():
    return """
<p>Sipariş No         :  </p>
<p>Ürün               : {product} </p>
<p>Adet               : {quantity}  </p>
<p>Müşteri Ad & Soyad : {name}  </p>
<p>Telefon            : {phone}  </p>
<p>E-Posta Adresi     : {mail}  </p>
<p>Açıklama           : {note} </p>
"""