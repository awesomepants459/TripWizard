from flask import Flask, request, render_template
import random
from flask import Blueprint
import sqlite3

'''Blueprint'''
bp = Blueprint("survey", __name__)

'''Site Class, Day Class, and Itinerary Class'''
class site():
  def __init__(self, siteName, siteDesc, siteTime, siteCost, siteAddress, siteCategory):
      self.__name = siteName
      self.__desc = siteDesc
      self.__time = siteTime
      self.__cost = siteCost
      self.__address = siteAddress
      self.__category = siteCategory

  def get_name(self):
      stri = str(self.__name)
      return stri

  def get_desc(self):
      stri = str(self.__desc)
      return stri

  def get_time(self):
      ti = int(self.__time)
      return ti

  def get_cost(self):
      stri = "Cost: $"
      stri += self.__cost
      return stri

  def get_address(self):
      return self.__address

  def get_category(self):
      return self.__category

class day():
    def __init__(self, site1, site2, site3, site4, site5, site6):
        self.__s1 = site1
        self.__s2 = site2
        self.__s3 = site3
        self.__s4 = site4
        self.__s5 = site5
        self.__s6 = site6

    def get_s1(self):
        return self.__s1

    def get_s2(self):
        return self.__s2

    def get_s3(self):
        return self.__s3

    def get_s4(self):
        return self.__s4

    def get_s5(self):
        return self.__s5

    def get_s6(self):
        return self.__s6

    '''This method deals with the way that we chose to handle time. It takes the time input and converts it into regular time.'''
    def time_converter(self, timeNum):
        time = timeNum
        toMinutes = (3/5)
        timeString = str(time)
        length = len(timeString)
        
        if length == 4:
            hour = int(timeString[0])
            hour *= 10
            hour2 = int(timeString[1])
            hour += hour2
            minute = timeString[2]
            if minute !="0":
                numMinute = int(minute)
                numMinute *= 10
                numMinute2 = int(timeString[3])
                numMinute += numMinute2
                minute = numMinute
                minute *= toMinutes
                minute = round(minute)
            else:
                numMinute2 = int(timeString[3])
                if numMinute2 == 0:
                    minute = "00"
                elif numMinute2 == 1:
                    minute = "01"
                elif numMinute2 == 2:
                    minute = "02"
                elif numMinute2 == 3:
                    minute = "03"
                elif numMinute2 == 4:
                    minute = "04"
                elif numMinute2 == 5:
                    minute = "05"
                elif numMinute2 == 6:
                    minute = "06"
                elif numMinute2 == 7:
                    minute = "07"
                elif numMinute2 == 8:
                    minute = "08"
                elif numMinute2 == 9:
                    minute = "09"
            print(str(hour) + ":" + str(minute))
        else:
            hour = int(timeString[0])
            minute = timeString[1]
            if minute !="0":
                numMinute = int(minute)
                numMinute *= 10
                numMinute2 = int(timeString[2])
                numMinute += numMinute2
                minute = numMinute
                minute *= toMinutes
                minute = round(minute)
            else:
                numMinute2 = int(timeString[2])
                if numMinute2 == 0:
                    minute = "00"
                elif numMinute2 == 1:
                    minute = "01"
                elif numMinute2 == 2:
                    minute = "02"
                elif numMinute2 == 3:
                    minute = "03"
                elif numMinute2 == 4:
                    minute = "04"
                elif numMinute2 == 5:
                    minute = "05"
                elif numMinute2 == 6:
                    minute = "06"
                elif numMinute2 == 7:
                    minute = "07"
                elif numMinute2 == 8:
                    minute = "08"
                elif numMinute2 == 9:
                    minute = "09"
        time = str(hour) + ":" + str(minute) + ":"
        return time
            

    def fullDayInformation(self):
        '''This method prints out all the information of the itinerary. It puts it all together. '''
        '''Leave hotel: Start of Day'''
        time = 850
        happening = str(self.time_converter(time))
        happening += "\t"
        happening += "Leave Hotel and go to " + self.__s1.get_name() + ". \n\n"
        time += 50

        '''Arrive at Site 1'''
        happening += str(self.time_converter(time))
        happening += "\tArrive at " + self.__s1.get_name() + ". \n\t\t"
        s1desc = self.__s1.get_desc()
        happening += s1desc + "\n\t\t"
        '''Display Address so user can get the route'''
        happening += "Address: "
        s1address = self.__s1.get_address()
        happening += s1address
        happening += "\n\n"
        '''Account for time spent at the site'''
        time += self.__s1.get_time()

        '''Leave Site 1, go to Site 2'''
        happening += str(self.time_converter(time))
        happening += "\tLeave " + self.__s1.get_name() + " and go to " + self.__s2.get_name() + ". \n\n"
        time += 50

        '''Arrive at Site 2'''
        happening += str(self.time_converter(time))
        happening += "\tArrive at " + self.__s2.get_name() + ". \n\t\t"
        s2desc = self.__s2.get_desc()
        happening += s2desc + "\n\t\t"
        happening += "Address: "
        s2address = self.__s2.get_address()
        happening += s2address
        happening += "\n\n"
        '''Account for time spent at the site'''
        time += self.__s2.get_time()

        if self.__s3 != 0:
            '''Leave Site 2, go to Site 3'''
            happening += str(self.time_converter(time))
            happening += "\tLeave " + self.__s2.get_name() + " and go to " + self.__s3.get_name() + ". \n\n"
            time += 50

            '''Arrive at Site 3'''
            happening += str(self.time_converter(time))
            happening += "\tArrive at " + self.__s3.get_name() + ". \n\t\t"
            s3desc = self.__s3.get_desc()
            happening += s3desc + "\n\t\t"
            happening += "Address: "
            s3address = self.__s3.get_address()
            happening += s3address
            happening += "\n\n"
            '''Account for time spent at the site'''
            time += self.__s3.get_time()

            if self.__s4 != 0:
                '''Leave Site 3, go to Site 4'''
                happening += str(self.time_converter(time))
                happening += "\tLeave " + self.__s3.get_name() + " and go to " + self.__s4.get_name() + ". \n\n"
                time += 50

                '''Arrive at Site 4'''
                happening += str(self.time_converter(time))
                happening += "\tArrive at " + self.__s4.get_name() + ". \n\t\t"
                s4desc = self.__s4.get_desc()
                happening += s4desc + "\n\t\t"
                happening += "Address: "
                s4address = self.__s4.get_address()
                happening += s4address
                happening += "\n\n"
                '''Account for time spent at the site'''
                time += self.__s4.get_time()

                if self.__s5 != 0:
                    '''Leave Site 4, go to Site 5'''
                    happening += str(self.time_converter(time))
                    happening += "\tLeave " + self.__s4.get_name() + " and go to " + self.__s5.get_name() + ". \n\n"
                    time += 50

                    '''Arrive at Site 5'''
                    happening += str(self.time_converter(time))
                    happening += "\tArrive at " + self.__s5.get_name() + ". \n\t\t"
                    s5desc = self.__s5.get_desc()
                    happening += s5desc + "\n\t\t"
                    happening += "Address: "
                    s5address = self.__s5.get_address()
                    happening += s5address
                    happening += "\n\n"
                    '''Account for time spent at the site'''
                    time += self.__s5.get_time()

                    if self.__s6 != 0:
                        '''Leave Site 5, go to Site 6'''
                        happening += str(self.time_converter(time))
                        happening += "\tLeave " + self.__s6.get_name() + " and go to " + self.__s6.get_name() + ". \n\n"
                        time += 50

                        '''Arrive at Site 6'''
                        happening += str(self.time_converter(time))
                        happening += "\tArrive at " + self.__s6.get_name() + ". \n\t\t"
                        s6desc = self.__s6.get_desc()
                        happening += s6desc + "\n\t\t"
                        happening += "Address: "
                        s6address = self.__s6.get_address()
                        happening += s6address
                        happening += "\n\n"
                        '''Account for time spent at the site'''
                        time += self.__s6.get_time()
                    else:
                        '''no site 6, no more time adjustments'''
                else:
                    '''no site 5, no more time adjustments'''
            else:
                '''no site 4, no more time adjustments'''
        else:
            '''no site 3, no more time adjustments'''
        return happening
    
class itinerary():
    def __init__(self, day1, day2, day3, day4):
        self.__d1 = day1
        self.__d2 = day2
        self.__d3 = day3
        self.__d4 = day4

    def printFullItinerary(self):
        str = "Day 1: \n\n"
        d1full = self.__d1.fullDayInformation()
        str += d1full
        if self.__d2 != 0:
            str += "\n\nDay 2: \n\n"
            d2full = self.__d2.fullDayInformation()
            str += d2full
            if self.__d3 != 0:
                str += "\n\nDay 3: \n\n"
                d3full = self.__d3.fullDayInformation()
                str += d3full
                if self.__d4 != 0:
                    str += "\n\nDay 4: \n\n"
                    d4full = self.__d4.fullDayInformation()
                    str += d4full
        else:
            '''Dont do anything, there's only one day'''
        return str


'''Berlin Sites Database'''
conn = sqlite3.connect('berlin.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS berlin (
    name,
    desc,
    time,
    cost,
    address,
    category
)
''')
conn.commit()

#insert name, desc, time, ccost, address, category
cursor.execute("INSERT INTO berlin VALUES ('Brandenburg Gate', 'A historic landmark symbolizing peace and unity', '25', '0', 'Pariser Platz', 'historical')")
cursor.execute("INSERT INTO berlin VALUES ('East Side Gallery', 'The longest remaining section of the Berlin Wall, adorned with colorful murals.', '75', '0', 'Mühlenstraße 79-81', 'historical')")
cursor.execute("INSERT INTO berlin VALUES ('Reichstag Building', 'The seat of the German Parliament, offering panoramic views of Berlin.', '200', '0', 'Platz der Republik 1', 'historical')")
cursor.execute("INSERT INTO berlin VALUES ('Berlin Wall Memorial', 'A poignant reminder of the Cold War division of Berlin.', '150', 'o', 'Bernauer Straße 111', 'historical')")
cursor.execute("INSERT INTO berlin VALUES ('Museum Island', 'A UNESCO World Heritage Site housing five world-class museums.', '400', '5', 'Museum Island', 'historical')")
cursor.execute("INSERT INTO berlin VALUES ('Berlin Cathedral', 'A magnificent Baroque cathedral with stunning interior and exterior.', '100', '5', 'Am Lustgarten 4', 'historical')")
cursor.execute("INSERT INTO berlin VALUES ('Checkpoint Charlie', 'A former border crossing point between East and West Berlin.', '25', '0', 'Friedrichstraße 43-45', 'historical')")
cursor.execute("INSERT INTO berlin VALUES ('Tiergarten Park', 'A vast urban park with diverse flora, fauna, and historical monuments.', '100', '0', 'Tiergarten', 'nature')")
cursor.execute("INSERT INTO berlin VALUES ('Berlin TV Tower', 'A striking television tower offering panoramic views of the city.', '200', '15', 'Potsdamer Platz 1', 'family')")
cursor.execute("INSERT INTO berlin VALUES ('Charlottenburg Palace', 'A magnificent Baroque palace and gardens, once the residence of Prussian royalty.', '300', '10', 'Spandauer Damm 10-22', 'historical')")
cursor.execute("INSERT INTO berlin VALUES ('Pergamon Museum', 'A world-renowned museum housing ancient artifacts from Greece, Rome, and the Middle East.', '200', '15', 'Bodestraße 1-2', 'family')")
cursor.execute("INSERT INTO berlin VALUES ('Humboldt Forum', 'A cultural complex dedicated to world cultures, history, and art.', '250', '10', 'Unter den Linden 2', 'historical')")
cursor.execute("INSERT INTO berlin VALUES ('Berlin Zoo', 'One of the oldest zoos in the world, home to a diverse range of animals.', '250', '15', 'Hahnstraße 13', 'family')")
cursor.execute("INSERT INTO berlin VALUES ('Viktoriapark', 'A picturesque hilltop park offering stunning views of the city.', '200', '0', 'Kreuzbergstraße 70', 'nature')")
cursor.execute("INSERT INTO berlin VALUES ('Hackescher Markt', 'A vibrant district with historic courtyards, shops, and restaurants.', '200', '10', 'Rosenthaler Straße 40-41', 'family')")
cursor.execute("INSERT INTO berlin VALUES ('Bebelplatz', 'A historic square associated with the Nazi book burning of 1933.', '25', '0', 'Bebelplatz', 'historical')")
cursor.execute("INSERT INTO berlin VALUES ('Gedenkstätte Berliner Mauer', 'A memorial site commemorating the victims of the Berlin Wall.', '100', '0', 'Bernauer Straße 111', 'historical')")
cursor.execute("INSERT INTO berlin VALUES ('Topographie des Terrors', 'A historical museum dedicated to the history of Nazi terror.', '150', '0', 'Niederkirchnerstraße 8', 'historical')")

cursor.execute("SELECT * FROM berlin")
ber_sites = cursor.fetchall()
berlin_sites = []
conn.close()



'''Krakow Sites Database'''
conn_kra = sqlite3.connect('krakow.db')
cursor_kra = conn_kra.cursor()

# Create a table
cursor_kra.execute('''
CREATE TABLE IF NOT EXISTS krakow (
    name,
    desc,
    time,
    cost,
    address,
    category
)
''')
conn_kra.commit()

#insert name, desc, time, ccost, address, category
cursor_kra.execute("INSERT INTO krakow VALUES ('Main Market Square', 'The heart of the Old Town, surrounded by colorful buildings and historic churches.', '300', '5', 'Rynek Główny 1', 'historical')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Wawel Castle', 'A majestic royal castle complex overlooking the Vistula River.', '300', '10', 'Wawel 5', 'family')")
cursor_kra.execute("INSERT INTO krakow VALUES ('St. Marys Basilica', 'A Gothic church famous for its distinctive trumpet call.', '200', '5', 'Rynek Główny 1', 'historical')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Kazimierz District', 'The former Jewish quarter, now a vibrant cultural hub.', '200', '0', 'ul. Miodowa 22', 'historical')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Planty Park', 'A green belt encircling the Old Town, perfect for leisurely walks.', '200', '0', 'ul. Planty', 'family')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Kraków Barbican', 'A fortified gateway to the Old Town.', '100', '0', 'ul. Basztowa 1', 'historical')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Wieliczka Salt Mine', 'A UNESCO World Heritage Site, a vast network of underground salt chambers.', '300', '0', 'ul. Daniłowicza 20', 'historical')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Rynek Główny Underground Museum', 'A fascinating museum showcasing the history of the Main Market Square.', '200', '0', 'Rynek Główny 1', 'historical')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Czartoryski Museum', 'A museum housing a diverse collection of art and historical artifacts.', '200', '0', 'ul. św. Jana 19', 'historical')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Collegium Maius', 'The oldest building of the Jagiellonian University.', '150', '0', 'ul. Gołębia 24', 'historical')")
cursor_kra.execute("INSERT INTO krakow VALUES ('National Museum in Krakow', 'A comprehensive museum with a vast collection of art and artifacts.', '250', '0', 'ul. św. Jana 22', 'family')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Kraków Zoological Garden', 'A zoo with a diverse range of animals, including many endangered species.', '200', '0', 'ul. Krasińskiego 9a', 'family')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Kopiec Kościuszki', 'A hilltop mound commemorating Tadeusz Kościuszko, a Polish military leader.', '50', '0', 'ul. Kościuszki 1', 'nature')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Błonia Park', 'A large park used for various events and festivals.', '150', '0', 'Błonia', 'nature')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Kraków Philharmonic Hall', 'A beautiful concert hall hosting classical music performances.', '150', '0', 'ul. Zwierzyniecka 1', 'family')")
cursor_kra.execute("INSERT INTO krakow VALUES ('St. Florians Gate', 'A historic gate leading to the Old Town.', '50', '0', 'ul. Floriańska 41', 'historical')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Kraków Main Railway Station', 'A beautiful Art Nouveau railway station.', '75', '0', 'pl. Jana Nowaka-Jeziorańskiego 1', 'family')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Smoczy Smok Wawelski', 'A mythical dragon sculpture near Wawel Castle.', '50', '0', 'ul. Wawel 5', 'family')")
cursor_kra.execute("INSERT INTO krakow VALUES ('Auschwitz-Birkenau Memorial', 'The Auschwitz-Birkenau Memorial and Museum serves as a poignant reminder of the Holocaust.', '300', '0', 'Auschwitz, 32-600 Oświęcim, Poland', 'historical')")

cursor_kra.execute("SELECT * FROM krakow")
kra_sites = cursor_kra.fetchall()
krakow_sites = []
conn_kra.close()





'''Amsterdam Sites Database'''
conn_ams = sqlite3.connect('amsterdam.db')
cursor_ams = conn_ams.cursor()

# Create a table
cursor_ams.execute('''
CREATE TABLE IF NOT EXISTS amsterdam (
    name,
    desc,
    time,
    cost,
    address,
    category
)
''')
conn_ams.commit()

#insert name, desc, time, ccost, address, category
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Rijksmuseum', 'A world-class museum showcasing Dutch art and history.', '200', '0', 'Museumstraat 1', 'historical')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Anne Frank House', 'A poignant museum dedicated to the life of Anne Frank.', '200', '0', 'Prinsengracht 263-267', 'historical')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Van Gogh Museum', 'A museum dedicated to the life and work of Vincent van Gogh.', '200', '0', 'Museumplein 6', 'historical')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Stedelijk Museum', 'A museum of modern and contemporary art.', '150', '0', 'Museumplein 10', 'family')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Vondelpark', 'A large urban park with beautiful gardens, ponds, and playgrounds.', '200', '0', 'Overtoom 185', 'family')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Dam Square', 'A historic square in the heart of Amsterdam.', '100', '0', 'Dam 1', 'historical')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Royal Palace', 'A 17th-century palace on Dam Square.', '150', '0', 'Dam 1', 'historical')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Nieuwe Kerk', 'A medieval church on Dam Square.', '75', '0', 'Dam 9', 'family')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Jordaan District', 'A charming neighborhood with canals, historic houses, and trendy shops.', '175', '0', 'Jordaan', 'historical')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Red Light District', 'A historic district known for its red-lit windows.', '75', '0', 'De Wallen', 'historical')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Hermitage Amsterdam', 'A branch of the State Hermitage Museum in St. Petersburg.', '150', '0', 'Amstel 51', 'historical')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('NEMO Science Museum', 'An interactive science museum for all ages.', '200', '0', 'Oosterdok 2', 'family')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('ADAM Lookout', 'A panoramic observation deck on top of a former ferry terminal.', '100', '0', 'Overhoeksplein 5', 'family')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Bloemenmarkt', 'A floating flower market on the Singel canal.', '100', '0', 'Singel', 'family')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Rembrandtplein', 'A lively square with theaters, cinemas, and restaurants.', '125', '0', 'Rembrandtplein', 'family')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Waterlooplein', 'A vibrant market square with flea markets and vintage shops.', '125', '0', 'Waterlooplein', 'family')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Begijnhof', 'A historic cloister with charming houses and a peaceful atmosphere.', '75', '0', 'Begijnhof', 'family')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Museumplein', 'A square home to several world-class museums.', '200', '0', 'Museumplein', 'historical')")
cursor_ams.execute("INSERT INTO amsterdam VALUES ('Westerkerk', 'A 17th-century church with a distinctive tower.', '75', '0', 'Prinsengracht 297', 'historical')")

cursor_ams.execute("SELECT * FROM amsterdam")
ams_sites = cursor_ams.fetchall()
amsterdam_sites = []
conn_ams.close()








'''Venice Sites Database'''
conn_ven = sqlite3.connect('venice.db')
cursor_ven = conn_ven.cursor()

# Create a table
cursor_ven.execute('''
CREATE TABLE IF NOT EXISTS venice (
    name,
    desc,
    time,
    cost,
    address,
    category
)
''')
conn_ven.commit()

#insert name, desc, time, ccost, address, category
cursor_ven.execute("INSERT INTO venice VALUES ('Campo Santa Maria Formosa', 'A charming square with a beautiful church and lively atmosphere.', '50', '0', 'Castello, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Campo San Stefano', 'A beautiful square with four churches, offering a glimpse of Venetian history.', '75', '0', 'Castello, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Fondamenta della Misericordia', 'A picturesque street with stunning views of the Grand Canal.', '50', '0', 'Dorsoduro, Venice', 'family')")
cursor_ven.execute("INSERT INTO venice VALUES ('Scuola Grande di San Marco', 'A former charitable institution with a beautiful facade and interior.', '100', '0', 'San Marco, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Jewish Ghetto', 'A historic neighborhood with synagogues and a museum.', '125', '0', 'Cannaregio, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Arsenale', 'A historic shipyard once used to build Venetian galleys.', '100', '0', 'Castello, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Punta della Dogana', 'A contemporary art museum with stunning views of the Grand Canal.', '150', '0', 'Dorsoduro, Venice', 'family')")
cursor_ven.execute("INSERT INTO venice VALUES ('Palazzo Grassi', 'A contemporary art museum showcasing international exhibitions.', '150', '0', 'San Marco, Venice', 'family')")
cursor_ven.execute("INSERT INTO venice VALUES ('Querini Stampalia Foundation', 'A cultural institution with a library, art gallery, and historical archives.', '150', '0', 'San Marco, Venice', 'historical');")
cursor_ven.execute("INSERT INTO venice VALUES ('Peggy Guggenheim Collection', 'A museum showcasing modern and contemporary art, including works by Picasso, Pollock, and Dalí.', '150', '0', 'Dorsoduro, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Libreria Acqua Alta', 'A unique bookstore with books displayed in gondolas and bathtubs.', '50', '0', 'Dorsoduro, Venice', 'family')")
cursor_ven.execute("INSERT INTO venice VALUES ('Campo San Polo', 'The second-largest square in Venice, often hosting markets and events.', '50', '0', 'San Polo, Venice', 'family')")
cursor_ven.execute("INSERT INTO venice VALUES ('Campo Santa Margherita', 'A lively square with numerous bars, restaurants, and shops.', '125', '0', 'Dorsoduro, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Teatro La Fenice', 'A historic opera house, often hosting world-class performances.', '100', '0', 'San Marco, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('San Giorgio Maggiore', 'A Benedictine monastery with a beautiful church and stunning views of Venice.', '100', '0', 'San Giorgio Maggiore, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Basilica di Santa Maria della Salute', 'A magnificent Baroque church offering stunning views of the Grand Canal.', '75', '0', 'Dorsoduro, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Ca Rezzonico', 'A Baroque palace showcasing 18th-century Venetian life and art.', '100', '0', 'Dorsoduro, Venice', 'family')")
cursor_ven.execute("INSERT INTO venice VALUES ('Ca dOro', 'A Gothic palace with a beautiful facade and a collection of Renaissance art.', '125', '0', 'Cannaregio, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Scuola Grande di San Rocco', 'A stunning Renaissance building with a magnificent collection of Tintoretto paintings.', '125', '0', 'Campo San Rocco, Venice', 'Art Gallery')")
cursor_ven.execute("INSERT INTO venice VALUES ('Rialto Market', 'A bustling market offering fresh produce, seafood, and souvenirs.', '75', '0', 'Rialto, Venice', 'Market')")
cursor_ven.execute("INSERT INTO venice VALUES ('Torcello Island', 'A peaceful island with ancient Byzantine mosaics and a serene atmosphere.', 'Half-day', '0', 'Torcello, Venice', 'Island')")
cursor_ven.execute("INSERT INTO venice VALUES ('Burano Island', 'A colorful island known for its lace-making and vibrant houses.', '400', '0', 'Burano, Venice', 'nature')")
cursor_ven.execute("INSERT INTO venice VALUES ('Murano Glass Factory', 'Witness the centuries-old tradition of glassblowing on the island of Murano.', '125', '0', 'Murano, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Gallerie dellAccademia', 'A world-class art museum showcasing Venetian paintings from the 14th to 18th centuries.', '150', '0', 'Campo della Carità, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Bridge of Sighs', 'A romantic bridge connecting the Doges Palace to the Prigioni, offering a unique perspective of Venice.', '25', '0', 'Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Grand Canal', 'The main waterway of Venice, lined with stunning palaces and churches.', '50', '0', 'Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Rialto Bridge', 'A historic bridge spanning the Grand Canal, offering beautiful views.', '50', '0', 'Rialto, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('St. Marks Basilica', 'A stunning Byzantine cathedral with golden mosaics and intricate details.', '125', '0', 'Piazza San Marco, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('Doges Palace', 'A magnificent palace overlooking St. Marks Square, once the seat of Venetian power.', '150', '0', 'Piazza San Marco, Venice', 'historical')")
cursor_ven.execute("INSERT INTO venice VALUES ('St. Marks Square', 'The heart of Venice, with St. Marks Basilica, Doges Palace, and Campanile.', '50', '0', 'Piazza San Marco, Venice', 'historical')")

cursor_ven.execute("SELECT * FROM venice")
ven_sites = cursor_ven.fetchall()
venice_sites = []
conn_ven.close()
















for i in ber_sites:
    sName = i[0]
    sDesc = i[1]
    sTime = i[2]
    sCost = i[3]
    sAdd = i[4]
    sCat = i[5]
    newsite = site(sName, sDesc, sTime, sCost, sAdd, sCat)
    berlin_sites.append(newsite)

for i in kra_sites:
    sName = i[0]
    sDesc = i[1]
    sTime = i[2]
    sCost = i[3]
    sAdd = i[4]
    sCat = i[5]
    newsite = site(sName, sDesc, sTime, sCost, sAdd, sCat)
    krakow_sites.append(newsite)

for i in ams_sites:
    sName = i[0]
    sDesc = i[1]
    sTime = i[2]
    sCost = i[3]
    sAdd = i[4]
    sCat = i[5]
    newsite = site(sName, sDesc, sTime, sCost, sAdd, sCat)
    amsterdam_sites.append(newsite)

for i in ven_sites:
    sName = i[0]
    sDesc = i[1]
    sTime = i[2]
    sCost = i[3]
    sAdd = i[4]
    sCat = i[5]
    newsite = site(sName, sDesc, sTime, sCost, sAdd, sCat)
    venice_sites.append(newsite)

def generate_itinerary(site_list, daynum, howBusy, checkboxes):
    '''This function generates a random itinerary for the user.'''
    '''The values here are just placeholder values for the variables. in reality, these will be obtained from the survey. '''

    days = daynum
    busyness = howBusy
    checked = checkboxes
    my_sites = []
    
    '''Takes the list of cities, and gets the ones with the categories the user wants.'''
    for i in site_list:
        cat = i.get_category()
        if cat in checked:
            my_sites.append(i)

    '''The following statements will randomly select from the list of sites the user would want to see, and puts them into a day, then makes an itinerary. '''
    if days == 1:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 7):
                '''Six sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
        elif busyness == "moderate":
            for i in range (1, 5):
                '''Four sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
        elif busyness == "light":
            for i in range (1, 3):
                '''Two sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
        myItinerary = itinerary(d1, 0, 0, 0)
    elif days == 2:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 13):
                '''Six sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
            d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
        elif busyness == "moderate":
            for i in range (1, 9):
                '''Four sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
            d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
        elif busyness == "light":
            for i in range (1, 5):
                '''Two sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
            d2 = day(myPickedSites[2], myPickedSites[3], 0, 0, 0, 0)
        myItinerary = itinerary(d1, d2, 0, 0)
    elif days == 3:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 19):
                '''Six sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
            d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
            d3 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], myPickedSites[16], myPickedSites[17])
        elif busyness == "moderate":
            for i in range (1, 13):
                '''Four sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
            d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
            d3 = day(myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11], 0, 0)
        elif busyness == "light":
            for i in range (1, 7):
                '''Two sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
            d2 = day(myPickedSites[2], myPickedSites[3], 0, 0, 0, 0)
            d3 = day(myPickedSites[4], myPickedSites[5], 0, 0, 0, 0)
        myItinerary = itinerary(d1, d2, d3, 0)
    elif days == 4:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 25):
                '''Six sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
            d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
            d3 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], myPickedSites[16], myPickedSites[17])
            d4 = day(myPickedSites[18], myPickedSites[19], myPickedSites[20], myPickedSites[21], myPickedSites[22], myPickedSites[23])
        elif busyness == "moderate":
            for i in range (1, 17):
                '''Four sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
            d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
            d3 = day(myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11], 0, 0)
            d4 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], 0, 0)
        elif busyness == "light":
            for i in range (1, 9):
                '''Two sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
            d2 = day(myPickedSites[2], myPickedSites[3], 0, 0, 0, 0)
            d3 = day(myPickedSites[4], myPickedSites[5], 0, 0, 0, 0)
            d4 = day(myPickedSites[6], myPickedSites[7], 0, 0, 0, 0)
        myItinerary = itinerary(d1, d2, d3, d4)
    return myItinerary


@bp.route('/makeNewItinerary', methods=['POST'])
def makeNewItinerary():
    if request.method == 'POST':
        '''Grab survey inputs'''
        city = request.form['city']
        checked = request.form.getlist('category')
        days = int(request.form['days'])
        busyness = request.form['busyness']

        if city == "berlin":
            createdItinerary = generate_itinerary(berlin_sites, days, busyness, checked)
            itin = createdItinerary.printFullItinerary()

        elif city == "krakow":
            createdItinerary = generate_itinerary(krakow_sites, days, busyness, checked)
            itin = createdItinerary.printFullItinerary()

        elif city == "amsterdam":
            createdItinerary = generate_itinerary(amsterdam_sites, days, busyness, checked)
            itin = createdItinerary.printFullItinerary()

        elif city == "venice":
            createdItinerary = generate_itinerary(venice_sites, days, busyness, checked)
            itin = createdItinerary.printFullItinerary()

        return render_template('itinerary.html', itin=itin)
    else:
        return render_template('survey.html')