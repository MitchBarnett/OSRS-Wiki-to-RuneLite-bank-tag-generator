"""
By Mitch Barnett
OSRS IGN: Firelance
Github: MitchBarnett
Discord: Frogman#5072
Reddit: Wizard_Mitch
"""

from mwclient import Site       # pip install mwclient

# Wiki category to collect id's from
wiki_category = input("Enter wiki category to get ID's from: ")

user_agent = 'Wiki category to RuneLite bank tag generator (User:Fire Discord: Frogman#5072 Reddit:Wizard_Mitch)'

# Wiki URL and path to api.php
site = Site("oldschool.runescape.wiki", path="/", clients_useragent=user_agent)


def get_item_ids_from_category(category):
    """ Returns item id's from items listed in the given wiki category.
     Does not get items from subcategories as smw category depth is set to 0 on the wiki
     """
    category_item_ids = []

    # This is the query that is sent to the api. It gets the id's of items in a category including sub objects
    query = "[[Is variant of::<q>[[Category:" + wiki_category + "]]</q>]]OR[[Category:" + wiki_category + "]]|?Item ID"

    # Extract item id's from the json query response
    for answer in site.ask(query):
        item_ids = answer['printouts']['Item ID']
        for item_id in item_ids:
            category_item_ids.append(item_id)

    return category_item_ids


def make_runelite_import_string(item_ids):
    encoded_category = wiki_category.replace(" ", "-")
    import_string = encoded_category + ',' + str(item_ids[0]) + ','
    for item_id in item_ids:
        import_string += str(item_id) + ','

    import_string = import_string[:-1]  # Remove trailing comma
    return import_string


print(make_runelite_import_string(get_item_ids_from_category(wiki_category)))
