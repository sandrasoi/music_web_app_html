from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

def test_get_albums_html(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Title: Doolittle",
        "Released: 1989", 
        "Title: Surfer Rosa",
        "Released: 1988"])
        
        
    
    

def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Doolittle")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text(["Released: 1989", 
                                "Artist: Pixies"])

def test_visit_album_page(page,test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Surfer Rosa")

def test_return_single_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    p_tags = page.locator("p")
    expect(p_tags).to_have_text(["Artist: Pixies", "Genre: Rock"])

def test_list_all_artists(page,test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    p_tags = page.locator("p")
    expect(p_tags).to_have_text(['Pixies', 'ABBA', 'Taylor Swift', 'Nina Simone'])

def test_click_to_artist_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    p_tags = page.locator("p")
    expect(p_tags).to_have_text(["Artist: Pixies", "Genre: Rock"])

