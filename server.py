from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# museum data
cur_id = 34

museums = [
	{
		"id": 0,
		"name": "The Africa Center",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/africacenterbuilding2.jpg",
		"description": "The Africa Center, formerly known as Museum for African Art, is a museum located at Fifth Avenue and 110th Street in East Harlem, Manhattan, New York City, near the northern end of Fifth Avenue's Museum Mile. Founded in 1984, the museum is dedicated to increasing public understanding and appreciation of African art and culture. The Museum is also well known for its public education programs that help raise awareness of African culture, and also operates a unique store selling authentic handmade African crafts. The Museum has organized nearly 60 critically acclaimed exhibitions and traveled these to almost 140 venues nationally and internationally, including 15 other countries. Forty of these exhibitions are accompanied by scholarly catalogues.",
		"rating": "4.6",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 1,
		"name": "The American Numismatic Society",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/ANS_1.jpg",
		"description": "The American Numismatic Society is an organization dedicated to the study of coins, currency, medals, tokens, and related objects from all cultures, past and present. The Society's headquarters in New York City has the foremost research collection and library specialized in numismatics in the United States. These resources are used to support research and education in numismatics, for the benefit of academic specialists, serious collectors, professional numismatists, and the interested public.",
		"rating": "4.5",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 2,
		"name": "The Bronx Museum of the Arts",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/Michael_Palma_BXMSM_077_01-copy.jpg",
		"description": "The Bronx Museum of the Arts is an internationally recognized cultural destination that presents innovative contemporary art exhibitions and education programs and is committed to promoting cross-cultural dialogues for diverse audiences.",
		"rating": "4.4",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 3,
		"name": "Brooklyn Historical Society DUMBO",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/BHS_Dumbo_photo_0.jpg",
		"description": "Founded in 1863, Brooklyn Historical Society is a nationally recognized urban history center dedicated to preserving and encouraging the study of Brooklyn’s extraordinary 400-year history. Located in Brooklyn Heights with a second location in DUMBO, BHS is a cultural hub for civic dialogue, thoughtful engagement, and community outreach. Our mission statement says it all: Brooklyn Historical Society connects the past to the present and makes the vibrant history of Brooklyn tangible, relevant, and meaningful for today’s diverse communities, and for generations to come.",
		"rating": "4.7",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 4,
		"name": "The Cloisters",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/theCloisters.jpg",
		"description": "The Cloisters is a museum in Fort Tryon Park in Washington Heights, Manhattan, New York City, specializing in European medieval architecture, sculpture, and decorative arts, with a focus on the Romanesque and Gothic periods. Governed by the Metropolitan Museum of Art, it contains a large collection of medieval artworks shown in the architectural settings of French monasteries and abbeys.",
		"rating": "4.7",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 5,
		"name": "El Museo del Barrio",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/elmuseofacade2.jpg",
		"description": "El Museo del Barrio, often known simply as El Museo, is a museum at 1230 Fifth Avenue in East Harlem, Manhattan, New York City. It is located near the northern end of Fifth Avenue's Museum Mile, immediately north of the Museum of the City of New York and south of the future Museum for African Art.",
		"rating": "4.3",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 6,
		"name": "International Center of Photography",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/ICP.jpg",
		"description": "The International Center of Photography is the world’s leading institution dedicated to photography and visual culture. Cornell Capa founded ICP in 1974 to champion “concerned photography”—socially and politically minded images that can educate and change the world. Through our exhibitions, education programs, community outreach, and public programs, ICP offers an open forum for dialogue about the power of the image.",
		"rating": "4.5",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 7,
		"name": "Japan Society",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/japansociety2.jpg",
		"description": "Japan Society is an American nonprofit organization supported by individuals, foundations and corporations that brings the people of Japan and the United States closer together through mutual understanding, appreciation and cooperation. More than a hundred years after the Society's founding, its goal remains the same—the cultivation of a constructive, resonant and dynamic relationship between the people of the U.S. and Japan.",
		"rating": "4.6",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 8,
		"name": "The Met Breuer",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/2_%20The%20Met%20Breuer-%20front_photograph%20by%20Ed%20Lederman%20copy.jpg",
		"description": "The Met Breuer is a museum of modern and contemporary art at 945 Madison Avenue and East 75th Street in the Upper East Side of Manhattan, New York City. It is part of the Metropolitan Museum of Art, also called the Met. The Met Breuer opened in March 2016 in the building formerly occupied by the Whitney Museum of American Art, designed by Marcel Breuer and completed in 1966. Its works come from the Met's collection and are both monographic and thematic exhibitions.",
		"rating": "4.5",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 9,
		"name": "MoMA PS1",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/ps1_building.jpg",
		"description": "MoMA PS1 is one of the largest art institutions in the United States dedicated solely to contemporary art. It is located in the Long Island City neighborhood in the borough of Queens, New York City. In addition to its exhibitions, the institution organizes the Sunday Sessions performance series, the Warm Up summer music series, and the Young Architects Program with the Museum of Modern Art. MoMA PS1 has been affiliated with the Museum of Modern Art since January 2000 and, as of 2013, attracts about 200,000 visitors a year.",
		"rating": "4.4",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 10,
		"name": "Museum of Jewish Heritage",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/jewish.jpg",
		"description": "The Museum of Jewish Heritage, right next to Battery Park at the southernmost tip of Manhattan, resembles any other office building from the outside. Yet once inside, the museum transports you into the past as you follow the chronological exhibit through the long and complex history of Judaism. With its three floors dedicated to the heritage, struggle, and hope of the Jewish community throughout the world, the museum is filled with a mixture of artifacts, photographs, and video testimonials. Be sure to stop by their peaceful Garden of Stones for a quiet moment to yourself, and mark your calendars for their Jewish Film Series and other monthly events.",
		"rating": "4.6",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 11,
		"name": "Museum of the City of New York",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/mcny.jpg",
		"description": "Museum of the City of New York serves as the unofficial starting point for Museum Mile in a four-story mansion that looks out onto the east edge of Central Park. The Museum pays homage to the greatest city in the world, blending historical displays with contemporary collections of art. The exhibits at MCNY cover a wide range of topics, from politics to architecture, in media ranging from photographs to multimedia presentations. Check out their programs like concerts, lectures, dance shows, and film screenings. MCNY is small enough for a brief overview of New York, but dense and varied enough to make for a full afternoon of browsing.",
		"rating": "4.4",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 12,
		"name": "New York City Police Museum",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/policeMuseum.jpg",
		"description": "The Police Museum's building, once the home of the First Precinct, sits in the center of the street at 100 Old Slip, right along the East River. At the museum, you'll find mostly historical information, old-fashioned police relics, and an arsenal of police weaponry, along with several opportunities for picture-taking at their mug shot backdrop and true-to-life jail cell. Their most popular exhibit, the Hall of Heroes, is situated on the third floor and pays tribute to the NYPD's role in the September 11th attacks. The museum also houses rotating exhibits, and sponsors monthly workshops on safety and crime prevention. Also, if you are seeking some NYPD gear, be sure to stop by the museum's store before you leave.",
		"rating": "3.7",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 13,
		"name": "Nicholas Roerich Museum",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/roerich.jpg",
		"description": "The Nicholas Roerich Museum is just a ten-minute stroll from campus via classy Riverside Drive, making it an easy place to stop after classes, or when you simply have an hour of free time. Though the museum exhibits the work of only one artist, it is by no means a limited collection. Over 200 of Roerich's paintings are on display in the permanent collection, as well as many drawings and sketches from throughout his career. The museum also regularly hosts poetry readings and concerts, so be sure to check out the events calendar before planning your visit.",
		"rating": "4.7",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 14,
		"name": "The Paley Center for Media",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/mtr.jpg",
		"description": "The Paley Center for Media is a museum dedicated to television, radio, film, and all other platforms used by the professional community and media-interested public. In short, the Paley Center examines the intersections between media and society. In the library, you can watch any program from the museum's vast collection on a console. You can also drop into one of the Paley's theaters to check out a screening selected from its wide variety of programming - from David Bowie in performance to a look at the work of Jim Henson to the short films of Saturday Night Live. Be on the lookout for some incredible subscription series that bring together writers, directors, producers, actors, critics, journalists, and artists from many disciplines to discuss everything from the creative process behind television and radio to the current trends in media and popular culture.",
		"rating": "4.5",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 15,
		"name": "Schomburg Center for Research in Black Culture",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/Schomburg-center.jpg",
		"description": "The Schomburg Center is one of four research libraries of the New York Public Library. It has expanded to include the Langston Hughes Auditorium, which is home to many concerts, forums, and exhibitions. The library pays tribute to figures like founder Arturo Alfonso Schomburg and scientist Lewis Howard Latimer. There is also a gallery tribute to the African Burial Ground, a site rediscovered in 1991, home to nearly 20,000 African men, women, and children who lived during the 17th & 18th centuries. The extensive book collection is on the bottom floor. Don't be afraid to ask the security guards or volunteers any questions you may have - they are more than eager to show you around!",
		"rating": "4.6",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 17,
		"name": "Studio Museum in Harlem",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/studioMuseum.jpg",
		"description": "Located across the street from the Apollo, The Studio Museum in Harlem waves an ironic green, black and red American Flag outside of its glass-windowed entrance. With mostly contemporary exhibits encompassing all genres from photography to paintings to text/image installations, the Studio Museum celebrates the diversity and constantly changing spirit of Harlem. At any given time, there might be three or four exhibits to browse.",
		"rating": "4.1",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 18,
		"name": "American Folk Art Museum",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/AFAM_Exterior_GavinAshworth.jpg",
		"description": "The American Folk Art Museum is the premier institution devoted to the appreciation of traditional folk art and creative expressions of contemporary self-taught artists from the United States and abroad. The museum preserves, conserves, and interprets a comprehensive collection of the highest quality, with objects dating from the eighteenth century to the present. Visit for its changing exhibitions, its engaging public programs, and for its award-winning museum shop. Be sure to stop by on a Friday evening for the museum's 'Free Music Fridays.' Each week, from 5:30 to 7:30 pm, you can enjoy live folk music in the atrium surrounded by the artworks on view.",
		"rating": "4.3",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 19,
		"name": "Asia Society",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/asiaSociety_1.jpg",
		"description": "Asia Society is the perfect place to spend a hour or two. Its collection includes art from all over Asia, from the Middle East to the Far East. The Museum presents exhibits of both traditional Asian works as well as cutting-edge contemporary art of videos and new media art by Asian and Asian American artists from India, Cambodia, China, and many other nations. Be sure to take advantage of the 'Cell Phone Audio Tour,' which offers useful commentary directly through your own phone! The Museum Shop offers a great collection of books, arts & crafts, and jewelry.",
		"rating": "4.4",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 20,
		"name": "Brooklyn Historical Society",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/brooklynhistorical-building.jpg",
		"description": "The Brooklyn Historical Society connects the past to the present and makes the vibrant history of Brooklyn tangible, relevant, and meaningful for today's diverse communities. Founded in 1863, the Brooklyn Historical Society is a nationally recognized urban history center dedicated to preserving and encouraging the study of Brooklyn's extraordinary 400-year history. Located in Brooklyn Heights and housed in a magnificent landmark building designed by George Post and opened in 1881, today's BHS is a cultural hub for civic dialogue, thoughtful engagement, and community outreach.",
		"rating": "4.6",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 21,
		"name": "Caribbean Cultural Center African Diaspora Institute",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/Screen-Shot-2017-06-06-at-5.11.26-PM.jpg",
		"description": "CCCADI presents music, dance, and art of Caribbean influence with programs and events featuring emerging locals from the community, along with renowned artists. Their art gallery features contemporary, themed, or historical exhibits that explore the effects of the African Diaspora. Check their website for events taking place while they are moving to a new location.",
		"rating": "4.7",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 23,
		"name": "Dahesh Museum",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/daheshMuseum.jpg",
		"description": "The Dahesh Museum of Art is the only museum in the United States devoted to the collection and exhibition of European academic art of the 19th and 20th century. The collection, located in Manhattan, New York City, originated with Lebanese writer, humanist, and philosopher Salim Moussa Achi (1909–1984), whose pen name was Dr. Dahesh. The core of the museum's holdings consists of Dahesh's collection of more than 2,000 academic paintings, which includes many notable Orientalist paintings.",
		"rating": "4.8",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 24,
		"name": "Goethe-Institut",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/GoetheInstitute2.jpg",
		"description": "A cultural center for all things German, the Goethe-Institut (30 Irving Place) offers everything from language lessons to jazz concerts to readings of contemporary literature. Although it does house a film archive and library of art, literature, and film, many of the Goethe-Institut's arts offerings take place off site. Be sure to check their website for the most recent information on German film series, art exhibitions, and music and theater performances. Ludlow 38 is the Goethe-Institut New York’s contemporary art space, made possible with the generous support of MINI, located at 38 Ludlow Street on the Lower East Side. Its mission is to introduce new international perspectives to the downtown art community and to foster dialogue within the aesthetic and sociopolitical context of New York and the United States.",
		"rating": "4.3",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 25,
		"name": "Intrepid Sea Air & Space Museum",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/IntrepidReturns081002_Tauber_084.jpg",
		"description": "The Intrepid Sea, Air & Space Museum is a nonprofit, educational institution featuring the legendary aircraft carrier Intrepid, the space shuttle Enterprise, the world’s fastest jets and a guided missile submarine. Through exhibitions, educational programming and the foremost collection of technologically groundbreaking aircraft and vessels, visitors of all ages and abilities are taken on an interactive journey through history to learn about American innovation and bravery. The mission of the Intrepid Sea, Air & Space Museum is to promote the awareness and understanding of history, science and service through its collections, exhibitions and programming in order to honor our heroes, educate the public and inspire our youth.",
		"rating": "4.6",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 26,
		"name": "The Jewish Museum",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/Jewish_museum_building.jpg",
		"description": "The Jewish Museum is the preeminent museum in the United States devoted exclusively to over 4,000 years of art and Jewish culture. Whether you visit the elegant Warburg mansion on New York City's Museum Mile, or enjoy the collections and exhibitions online, you will find yourself on a journey through time and across continents. The Museum's collection has over 26,000 objects including paintings, sculpture, archaeological artifacts, Jewish ceremonial art, and many other pieces important to the preservation of Jewish history and culture. Artists included in the collection include Marc Chagall, George Segal, Eleanor Antin, and Deborah Kass. Explore collections, exhibitions and more online at http://www.thejewishmuseum.org.",
		"rating": "4.4",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 27,
		"name": "The Metropolitan Museum of Art",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/met.JPG",
		"description": "A favorite of the Core department, The Metropolitan Museum of Art is practically a required stop for any student, professor or human being living in or visiting New York. Located at the edge of Central Park on 5th Ave, the largest museum in New York stretches across 4 blocks from 84th to 80th Street and is an easy 30-minute ride down from 116th and Broadway on the M4 (even if it takes you several trips to get through the whole museum). The Met is arguably the centerpiece of Museum Mile, with an immense permanent collection of modern and classical painting, sculpture, and photography. The Met also houses artifacts from a variety of ancient cultures, in addition to its rotating special exhibits, including rooftop displays. In 2007 the Met opened several new galleries, featuring Hellenistic, Etruscan, and Roman art, to name a few. Also, be sure to check out the Met's calendar of special events, including toga parties and mixers thrown by the College Group. Finally, if you are looking for a great way to spend a weekend evening, don't forget the Met is open until nine both nights!",
		"rating": "4.8",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 28,
		"name": "The Morgan Library & Museum",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/madison-view3.jpg",
		"description": "The Morgan Library & Museum began as the private library of financier Pierpont Morgan, one of the preeminent collectors and cultural benefactors in the United States. Today, more than a century after its founding in 1906, the Morgan serves as a museum, independent research library, musical venue, architectural landmark, and historic site. In October 2010, the Morgan completed the first-ever restoration of its original McKim building, Pierpont Morgan's private library, and the core of the institution. In tandem with the 2006 expansion project by architect Renzo Piano, the Morgan now provides visitors unprecedented access to its world-renowned collections of drawings, literary and historical manuscripts, musical scores, medieval and Renaissance manuscripts, printed books, and ancient Near Eastern seals and tablets.",
		"rating": "4.7",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 29,
		"name": "Museum of Modern Art (MoMA)",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/moma.JPG",
		"description": "MoMA can be daunting at first glance because of its sheer size and reputation. It is definitely not a museum you can expect to exhaust in one visit. You might want to browse the website for current exhibits, or focus solely upon one or two floors of its massive permanent collection. If you have apprehension about modern art, MoMA is the best place to learn, and a beautiful space to explore. Be sure to check out its film screenings throughout the year, and the summer concert series that takes place in MoMA's sculpture garden. If you are hungry after your visit, grab a bite to eat at the MoMA café for some excellent food in a lovely setting. And don't forget to check out the unbeatable gift shop!",
		"rating": "4.5",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 30,
		"name": "National Academy Museum",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/nationalAcademy.jpg",
		"description": "The National Academy Museum has closed its home on 5th Avenue and is currently looking to move its collection of over 7,700 pieces to a new location. The Academy houses one of the largest public collections of Nineteenth- and Twentieth-century American art in the country, with a vast array of styles and media, generously donated by Academy members elected every year. Members are artists and architects ranging from Andrew Wyeth and Frank Lloyd Wright to Cindy Sherman and Frank Gehry. We eagerly await the re-opening of this exciting and ever expanding collection in its new location!",
		"rating": "4.3",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 31,
		"name": "New York Transit Museum",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/ny_transit_building.jpg",
		"description": "Housed underground in a retired 1930s subway station, the New York Transit Museum is custodian of the most extensive collection of urban transportation materials in the United States. Objects on view span more than 100 years of transit history. The jewels of the collection, nearly 20 one-of-a-kind vintage subways and elevated cars, fill the station's platform level. Visitors can board these cars, step through a time tunnel of turnstiles, discover a working signal tower and view exhibits that look at city mass transit from unusual angles. The Museum also offers free guided tours and lectures, and runs a Gallery Annex and Store at Grand Central Terminal, which rotates four to six temporary exhibits annually. The New York Transit Museum holds equal appeal for families, urban historians, architects, transit buffs, and anyone interested in New York's unique past.",
		"rating": "4.6",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 32,
		"name": "The Noguchi Museum",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/noguchi_building_0.jpg",
		"description": "See what Isamu Noguchi meant when he said, “The essence of sculpture is for me the perception of space, the continuum of our existence,” by checking out this indoor/outdoor garden museum that was designed, built, and installed by the man himself. The space is a converted photo-engraving plant, which surrounds a garden of granite and basalt sculptures. It features Noguchi's works in stone, metal, wood, and clay, as well as models for public projects and gardens, dance sets, and Akari Light sculptures. Take advantage of the benches scattered throughout the garden and galleries for reflection. If you want a little background on the exhibits, you'll want to show up for the guided tour at 2pm (Noguchi liked his pieces displayed unaccompanied by titles or text). Afterwards, you can stroll down to Socrates Sculpture Park, which provides a great view of Manhattan and the East River.",
		"rating": "4.7",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 33,
		"name": "Queens Museum",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/Queens_Museum_building.jpg",
		"description": "The Queens Museum is more than just a museum; it's a historic site, a community center, and an educational classroom for children, adults, and seniors alike. Through programs like ArtAccess, the museum also accomodates visitors with special needs. Check out its homepage for current exhibitions that are designed to serve the borough's uniquely diverse ethnic, cultural, and international community. “The Panorama of the City of New York” is compulsory viewing for anyone living in the city: a 9,335 square foot model of the city's 320 square miles and 895,000 buildings. It was conceived by Robert Moses, whose first contract with the developer called for less than one percent margin of error between the model and reality! The museum is situated in the famous New York City Building that housed the U.N.'s General Assembly from 1946 to 1952 and its historic decisions, including the division of Palestine and the founding of UNICEF.",
		"rating": "4.4",
		"reviews": ["okay", "good", "amazing!"]
	},
	{
		"id": 34,
		"name": "Socrates Sculpture Park",
		"image": "https://artsinitiative.columbia.edu/sites/default/files/museums/ornamental-images/socrates_park.jpg",
		"description": "Socrates Sculpture Park was an abandoned riverside landfill and illegal dumpsite until 1986 when a coalition of artists and community members, under the leadership of artist Mark di Suvero, transformed it into an open studio and exhibition space for artists and a neighborhood park for local residents. Today it is an internationally renowned outdoor museum and artist residency program that also serves as a vital New York City park offering a wide variety of public services. Socrates Sculpture Park is the only site in the New York Metropolitan area specifically dedicated to providing artists with opportunities to create and exhibit large-scale work in a unique environment that encourages strong interaction between artists, artworks, and the public. The Park's existence is based on the belief that reclamation, revitalization, and creative expression are essential to the survival, humanity, and improvement of our urban environment.",
		"rating": "4.3",
		"reviews": ["okay", "good", "amazing!"]
	}

]


# routes
@app.route('/')
def index():
	return render_template('index.html', museums = museums)    

@app.route('/get_search', methods=['GET', 'POST'])
def get_search():
	global museums 

	json_data = request.get_json()   
	searchterm = json_data["searchterm"] 

	museums_match = []

	for museum in museums:
		if searchterm in museum["name"]:
			museums_match.append(museum)

	return jsonify(museums = museums_match)

@app.route('/delete_item', methods=['GET', 'POST'])
def delete_item():
	global museums  

	json_data = request.get_json()   
	del_id = json_data["id"]
	searchterm =  json_data["searchterm"]

	for museum in museums:
		if (str(museum["id"]) == str(del_id)):
			museums.remove(museum)

	museums_match = []

	for museum in museums:
		if searchterm in museum["name"]:
			museums_match.append(museum)

	return jsonify(museums = museums_match)



@app.route('/view/<id>')
def view(id):
	id = int(id)

	for museum in museums:
		if id == museum["id"]:
			id = museums.index(museum)

	name = museums[id]["name"]
	image = museums[id]["image"]
	description = museums[id]["description"]
	rating = museums[id]["rating"]
	reviews = museums[id]["reviews"]
	id = museums[id]["id"]
	return render_template('view.html', name = name, image = image, description = description, rating = rating, reviews = reviews, id = id)



@app.route('/create')
def create():
	return render_template('create.html') 

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
	global cur_id
	global museums 

	json_data = request.get_json()   
	name = json_data["name"]
	image = json_data["image"]
	description = json_data["description"]
	rating = json_data["rating"]
	review = json_data["review"] 

	cur_id += 1

	new_item = {
		"id":  cur_id,
		"name": name,
		"image": image,
		"description": description,
		"rating": rating,
		"reviews": [review]
	}

	museums.append(new_item)

	return jsonify(id = cur_id)



@app.route('/edit/<id>')
def edit(id):
	return render_template('edit.html', id=id) 

@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
	global museums 

	json_data = request.get_json()   
	id = json_data["id"]
	review = json_data["review"] 

	for museum in museums:
		if id == museum["id"]:
			museum["reviews"].append(review)

	return jsonify(id = id)


if __name__ == '__main__':
   app.run(debug = True)




