def names(*players):
    # *args used to get n number of input as arguments from user as tuple
    print(f"ALL PLAYER NAMES {players}")

names("virat","root","kane","smith","amla","sangakara")


def teams(*teamnames):
    for i in teamnames:
        print(f"{i}")
teams("INDIA","ENGLAND","AUSTRALIA","SOUTH AFRICA","SRILANKA")


def detail(**fulldetail):
    # **kwrgs is used to get n number of input as an arugument from user as an dictionary.
    for key , value in fulldetail.items():
        print(f"{key}:{value}")

detail(name="Virat",Age=37,Team="RCB",Status="King Kohli")


employees=[{"id":1,"first_name":"Beverlie","last_name":"Beekmann","email":"bbeekmann0@salon.com","gender":"Female"},
{"id":2,"first_name":"Dinah","last_name":"Isac","email":"disac1@xing.com","gender":"Genderfluid"},
{"id":3,"first_name":"Neel","last_name":"Linde","email":"nlinde2@prnewswire.com","gender":"Male"},
{"id":4,"first_name":"Lisle","last_name":"Blackden","email":"lblackden3@icq.com","gender":"Male"},
{"id":5,"first_name":"Nydia","last_name":"Rockey","email":"nrockey4@chicagotribune.com","gender":"Female"},
{"id":6,"first_name":"Hansiain","last_name":"Reap","email":"hreap5@wikipedia.org","gender":"Male"},
{"id":7,"first_name":"Lise","last_name":"Santino","email":"lsantino6@delicious.com","gender":"Female"},
{"id":8,"first_name":"Hallsy","last_name":"Buddock","email":"hbuddock7@yahoo.co.jp","gender":"Non-binary"},
{"id":9,"first_name":"Adolf","last_name":"Lamprey","email":"alamprey8@imgur.com","gender":"Male"},
{"id":10,"first_name":"Raul","last_name":"D'Alessio","email":"rdalessio9@purevolume.com","gender":"Male"},
{"id":11,"first_name":"Esteban","last_name":"Hupe","email":"ehupea@example.com","gender":"Male"},
{"id":12,"first_name":"Selig","last_name":"Prestney","email":"sprestneyb@toplist.cz","gender":"Male"},
{"id":13,"first_name":"Fields","last_name":"De Banke","email":"fdebankec@instagram.com","gender":"Male"},
{"id":14,"first_name":"Isis","last_name":"Bleasdale","email":"ibleasdaled@oracle.com","gender":"Female"},
{"id":15,"first_name":"Alastair","last_name":"Beckhurst","email":"abeckhurste@opera.com","gender":"Male"},
{"id":16,"first_name":"Daphene","last_name":"McAllaster","email":"dmcallasterf@comcast.net","gender":"Female"},
{"id":17,"first_name":"Devin","last_name":"Congram","email":"dcongramg@reuters.com","gender":"Male"},
{"id":18,"first_name":"Trumann","last_name":"Glader","email":"tgladerh@umich.edu","gender":"Male"},
{"id":19,"first_name":"Amalee","last_name":"Knowlson","email":"aknowlsoni@elpais.com","gender":"Female"},
{"id":20,"first_name":"Nadya","last_name":"Spriddle","email":"nspriddlej@flickr.com","gender":"Female"},
{"id":21,"first_name":"Rancell","last_name":"Lowell","email":"rlowellk@aboutads.info","gender":"Male"},
{"id":22,"first_name":"Melinde","last_name":"Tweddle","email":"mtweddlel@drupal.org","gender":"Female"},
{"id":23,"first_name":"Hugues","last_name":"Clawsley","email":"hclawsleym@mapquest.com","gender":"Male"},
{"id":24,"first_name":"Hubert","last_name":"Cowherd","email":"hcowherdn@wikimedia.org","gender":"Male"},
{"id":25,"first_name":"Yoko","last_name":"Bruckshaw","email":"ybruckshawo@stanford.edu","gender":"Female"},
{"id":26,"first_name":"Sharon","last_name":"Arnke","email":"sarnkep@quantcast.com","gender":"Female"},
{"id":27,"first_name":"Daisy","last_name":"Acom","email":"dacomq@google.com.hk","gender":"Female"},
{"id":28,"first_name":"Raychel","last_name":"Bellam","email":"rbellamr@illinois.edu","gender":"Female"},
{"id":29,"first_name":"Wain","last_name":"Brougham","email":"wbroughams@zdnet.com","gender":"Male"},
{"id":30,"first_name":"Karel","last_name":"Dowles","email":"kdowlest@printfriendly.com","gender":"Male"},
{"id":31,"first_name":"Benjamin","last_name":"Nacey","email":"bnaceyu@booking.com","gender":"Agender"},
{"id":32,"first_name":"Kimble","last_name":"Berger","email":"kbergerv@nsw.gov.au","gender":"Male"},
{"id":33,"first_name":"Stirling","last_name":"Greggs","email":"sgreggsw@over-blog.com","gender":"Male"},
{"id":34,"first_name":"Mitch","last_name":"Morkham","email":"mmorkhamx@networkadvertising.org","gender":"Male"},
{"id":35,"first_name":"Tyler","last_name":"Matschuk","email":"tmatschuky@bloglovin.com","gender":"Male"},
{"id":36,"first_name":"Raven","last_name":"Edwicke","email":"redwickez@sina.com.cn","gender":"Female"},
{"id":37,"first_name":"Darline","last_name":"Siege","email":"dsiege10@baidu.com","gender":"Female"},
{"id":38,"first_name":"Hanna","last_name":"Allbrook","email":"hallbrook11@woothemes.com","gender":"Female"},
{"id":39,"first_name":"Ker","last_name":"Methingam","email":"kmethingam12@eepurl.com","gender":"Male"},
{"id":40,"first_name":"Novelia","last_name":"Wolfarth","email":"nwolfarth13@webeden.co.uk","gender":"Female"},
{"id":41,"first_name":"Almeria","last_name":"Pristnor","email":"apristnor14@gov.uk","gender":"Female"},
{"id":42,"first_name":"Husain","last_name":"Duran","email":"hduran15@feedburner.com","gender":"Male"},
{"id":43,"first_name":"Madison","last_name":"Dymond","email":"mdymond16@reddit.com","gender":"Male"},
{"id":44,"first_name":"Cleo","last_name":"Ballintime","email":"cballintime17@about.me","gender":"Female"},
{"id":45,"first_name":"Kaila","last_name":"Thacker","email":"kthacker18@wsj.com","gender":"Female"},
{"id":46,"first_name":"Kayne","last_name":"Gilstin","email":"kgilstin19@cargocollective.com","gender":"Male"},
{"id":47,"first_name":"Stanton","last_name":"Renyard","email":"srenyard1a@pbs.org","gender":"Male"},
{"id":48,"first_name":"Patric","last_name":"Fookes","email":"pfookes1b@weibo.com","gender":"Male"},
{"id":49,"first_name":"Arlina","last_name":"O'Kennavain","email":"aokennavain1c@rediff.com","gender":"Female"},
{"id":50,"first_name":"Ichabod","last_name":"Morgan","email":"imorgan1d@people.com.cn","gender":"Male"},
{"id":51,"first_name":"Skyler","last_name":"Garwill","email":"sgarwill1e@over-blog.com","gender":"Male"},
{"id":52,"first_name":"Steffane","last_name":"Warbeys","email":"swarbeys1f@amazonaws.com","gender":"Female"},
{"id":53,"first_name":"Alika","last_name":"Anslow","email":"aanslow1g@bbc.co.uk","gender":"Female"},
{"id":54,"first_name":"Farlay","last_name":"Tolotti","email":"ftolotti1h@hostgator.com","gender":"Male"},
{"id":55,"first_name":"Claudius","last_name":"Tegler","email":"ctegler1i@cocolog-nifty.com","gender":"Male"},
{"id":56,"first_name":"Lloyd","last_name":"Earp","email":"learp1j@wp.com","gender":"Male"},
{"id":57,"first_name":"Aubrie","last_name":"Iskov","email":"aiskov1k@wp.com","gender":"Female"},
{"id":58,"first_name":"Cassius","last_name":"Bamlett","email":"cbamlett1l@photobucket.com","gender":"Male"},
{"id":59,"first_name":"Thatch","last_name":"Dimmick","email":"tdimmick1m@hugedomains.com","gender":"Male"},
{"id":60,"first_name":"Elie","last_name":"Llewellyn","email":"ellewellyn1n@fc2.com","gender":"Female"},
{"id":61,"first_name":"Foss","last_name":"Roakes","email":"froakes1o@nps.gov","gender":"Male"},
{"id":62,"first_name":"Alisander","last_name":"Galvin","email":"agalvin1p@g.co","gender":"Male"},
{"id":63,"first_name":"Briano","last_name":"Pecey","email":"bpecey1q@t.co","gender":"Male"},
{"id":64,"first_name":"Findlay","last_name":"Wickey","email":"fwickey1r@a8.net","gender":"Male"},
{"id":65,"first_name":"Lina","last_name":"Nussgen","email":"lnussgen1s@webmd.com","gender":"Female"},
{"id":66,"first_name":"Christian","last_name":"Giacobillo","email":"cgiacobillo1t@yahoo.com","gender":"Female"},
{"id":67,"first_name":"Rainer","last_name":"Trowbridge","email":"rtrowbridge1u@yandex.ru","gender":"Male"},
{"id":68,"first_name":"Dorise","last_name":"Aprahamian","email":"daprahamian1v@youtube.com","gender":"Female"},
{"id":69,"first_name":"Dirk","last_name":"Burrage","email":"dburrage1w@pen.io","gender":"Male"},
{"id":70,"first_name":"Jayme","last_name":"Odegaard","email":"jodegaard1x@goo.ne.jp","gender":"Male"},
{"id":71,"first_name":"Laney","last_name":"Stilgoe","email":"lstilgoe1y@stanford.edu","gender":"Female"},
{"id":72,"first_name":"Karalynn","last_name":"Strettle","email":"kstrettle1z@epa.gov","gender":"Female"},
{"id":73,"first_name":"Tremayne","last_name":"Eleshenar","email":"teleshenar20@sciencedirect.com","gender":"Genderqueer"},
{"id":74,"first_name":"Shaylah","last_name":"Kinge","email":"skinge21@mtv.com","gender":"Female"},
{"id":75,"first_name":"Javier","last_name":"Blackwell","email":"jblackwell22@wikimedia.org","gender":"Male"},
{"id":76,"first_name":"Hersh","last_name":"Caldecutt","email":"hcaldecutt23@slideshare.net","gender":"Male"},
{"id":77,"first_name":"Jonah","last_name":"Troy","email":"jtroy24@trellian.com","gender":"Male"},
{"id":78,"first_name":"Ellwood","last_name":"Halms","email":"ehalms25@joomla.org","gender":"Male"},
{"id":79,"first_name":"Keely","last_name":"Baptiste","email":"kbaptiste26@hp.com","gender":"Female"},
{"id":80,"first_name":"Emmey","last_name":"Speedy","email":"espeedy27@desdev.cn","gender":"Female"},
{"id":81,"first_name":"Nichole","last_name":"Hould","email":"nhould28@shareasale.com","gender":"Male"},
{"id":82,"first_name":"Michaela","last_name":"Pymer","email":"mpymer29@soup.io","gender":"Female"},
{"id":83,"first_name":"Marcos","last_name":"Renvoise","email":"mrenvoise2a@washingtonpost.com","gender":"Male"},
{"id":84,"first_name":"Sharyl","last_name":"Meriguet","email":"smeriguet2b@blogtalkradio.com","gender":"Female"},
{"id":85,"first_name":"Bjorn","last_name":"Birds","email":"bbirds2c@chron.com","gender":"Male"},
{"id":86,"first_name":"Heinrik","last_name":"Batterham","email":"hbatterham2d@blogger.com","gender":"Male"},
{"id":87,"first_name":"Ardith","last_name":"Carwithim","email":"acarwithim2e@shareasale.com","gender":"Non-binary"},
{"id":88,"first_name":"Alameda","last_name":"Colton","email":"acolton2f@stanford.edu","gender":"Polygender"},
{"id":89,"first_name":"Christy","last_name":"Jebb","email":"cjebb2g@over-blog.com","gender":"Male"},
{"id":90,"first_name":"Buddy","last_name":"Gabala","email":"bgabala2h@123-reg.co.uk","gender":"Male"},
{"id":91,"first_name":"Chris","last_name":"Snellman","email":"csnellman2i@rakuten.co.jp","gender":"Female"},
{"id":92,"first_name":"Fernandina","last_name":"Putt","email":"fputt2j@unesco.org","gender":"Female"},
{"id":93,"first_name":"Ryon","last_name":"Kayzer","email":"rkayzer2k@epa.gov","gender":"Male"},
{"id":94,"first_name":"Victor","last_name":"Hinchon","email":"vhinchon2l@eventbrite.com","gender":"Male"},
{"id":95,"first_name":"Lindon","last_name":"Colquite","email":"lcolquite2m@ebay.com","gender":"Male"},
{"id":96,"first_name":"Gaynor","last_name":"Errol","email":"gerrol2n@rambler.ru","gender":"Female"},
{"id":97,"first_name":"Aigneis","last_name":"Tzuker","email":"atzuker2o@sitemeter.com","gender":"Female"},
{"id":98,"first_name":"Buddy","last_name":"Dunston","email":"bdunston2p@chicagotribune.com","gender":"Male"},
{"id":99,"first_name":"Allegra","last_name":"Ramirez","email":"aramirez2q@freewebs.com","gender":"Female"},
{"id":100,"first_name":"Tana","last_name":"Lambrechts","email":"tlambrechts2r@who.int","gender":"Female"}]


print({"id":11,"first_name":"Esteban","last_name":"Hupe","email":"ehupea@example.com","gender":"Male"} in employees)
print({"id":11,"first_name":"Esteban","last_name":"Hupe","email":"ehupea@example.com","gender":"Male"} not in employees)

# used to verify the python sequence
