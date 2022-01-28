import pdb
from models.sight import Sight
from models.country import Country

import repositories.sight_repository as sight_repository
import repositories.country_repository as country_repository

# sight_repository.delete_all()
# country_repository.delete_all()

country1 = Country("Scotland", "Europe", True)
country_repository.save(country1)
country2 = Country("India", "Asia", False)
country_repository.save(country2)
country3 = Country("Australia", "Oceania", True)
country_repository.save(country3)
country4 = Country("Italy", "Europe", False)
country_repository.save(country4)
country5 = Country("USA", "North America", True)
country_repository.save(country5)
country6 = Country("Peru", "South America", False)
country_repository.save(country6)
country7 = Country("Eygpt", "Africa", False)
country_repository.save(country7)


# sight1 = Sight("Edinburgh Castle", country1, "Old historic castle at the heart of Edinburgh", True)
# sight_repository.save(sight1)
# sight2 = Sight("Taj Mahal", country2, "Beautiful white temple made of marble. Built hundreds of years ago.", False)
# sight_repository.save(sight2)
# sight3 = Sight("Kelvingrove Art Gallery and Museum", country1, "Free Entry. Kelvingrove Art Gallery and Mu​seum is Scotland's most visited free attraction.​ With 22 themed, state-of-the-art galleries displaying an astonishing 8000 objects, the collections are extensive, wide-ranging and internationally-significant.", False)
# sight_repository.save(sight3)
# sight4 = Sight("Swaminarayan Akshardham", country2, "Fantastic site to visit - unimaginable architechture, great theme show, diaorama and I max presentation. If any tourist, irresepctive of his religion or creed, has half a day to spare, this is a must see. It is one man's creation in five years totally with voluntary support. A monument which makes every indian proud!", False)
# sight_repository.save(sight4)
# sight5 = Sight("Royal Botanic Gardens Victoria", country3, "Over 10,000 plant species from around the world are presented in a kaleidoscope of colour and texture. Sweeping lawns, tranquil lakes and majestic trees are home to an amazing range of wildlife.", True)
# sight_repository.save(sight5)
# sight6 = Sight("Sydney Opera House", country3, "One of the most iconic buildings in the world – the Sydney Opera House is an architectural masterpiece and vibrant performance space.", True)
# sight_repository.save(sight6)
# sight7 = Sight("Pantheon", country4, "Dedicated to the seven planetary divinities and featuring an interior of gorgeous marble, the Pantheon is one of the most impressive monuments of Augustan Rome.", False)
# sight_repository.save(sight7)
# sight8 = Sight("Piazza Maggiore", country4, "The Centre of Bologna to meet or stroll or sit with drink or visit many of the historic sites surrounding The Piazza. Should be first stop when you arrive for first time.", False)
# sight_repository.save(sight8)
# sight9 = Sight("Disney Land", country5, "Covering nearly 47 square-miles, the Walt Disney World Resort features four theme parks: Epcot, Magic Kingdom Park, Disney’s Animal Kingdom Park and Disney's Hollywood Studios, two water parks: Disney's Blizzard Beach and Disney's Typhoon Lagoon and over 20 resort hotels.", True)
# sight_repository.save(sight9)
# sight10 = Sight("The Strip", country5, "Main city strip. Lots to see.", False)
# sight_repository.save(sight10)
# sight11 = Sight("Museo Larco", country6, "The Museo Larco is housed in an exquisite 18th century vice-royal mansion, built over a 7th century pre-Columbian pyramid and surrounded by beautiful gardens.", False)
# sight_repository.save(sight11)
# sight12 = Sight("Sacsayhuaman", country6, "Fascinating rock walls built by Inca people just outside of Cusco. Tour guides are available at the entrance, but you can do a self-guided tour as well. There is a breathtaking view of Cusco as well from this high vantage point.", False)
# sight_repository.save(sight12)
# sight13 = Sight("The Museum of Egyptian Antiquities", country7, "This famous museum houses the world’s largest collection of ancient Egyption artifacts (more than 120,000 items on display) featuring the famous Tutankhamun collection with its beautiful gold death mask and sarcophagus and the royal Mummy room, which houses an additional eleven Pharaonic dignitaries.", False)
# sight_repository.save(sight13)
# sight14 = Sight("Pyramids of Giza", country7, "Perhaps the most recognizable among the Seven Wonders of the World, the exact origin of these majestic pyramids continues to spark debate.", False)
# sight_repository.save(sight14)

pdb.set_trace