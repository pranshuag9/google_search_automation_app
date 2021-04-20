import time
from selenium.webdriver import Firefox, Chrome

class Search():
    googleSearchEngineUrl = "http://www.google.com"
    duckduckgoSearchEngineUrl = "http://www.duckduckgo.com"
    def __init__(self, searchQuery, browser="firefox", searchEngine="google", timeToRemain=100):
        self.searchQuery = searchQuery
        self.searchEngineUrl = self.duckduckgoSearchEngineUrl if searchEngine == "ddg" else self.googleSearchEngineUrl
        self.browser = Chrome() if browser == "chrome" else Firefox()
        self.timeToRemain = timeToRemain
        self.search()
        time.sleep(timeToRemain)
        self.browser.quit()

    def search(self):
        self.browser.set_page_load_timeout("100")
        self.browser.get(self.searchEngineUrl)
        searchField = self.browser.find_element_by_name("q")
        searchField.send_keys(self.searchQuery)
        searchField.submit()

if __name__ == "__main__":
    searchQuery = input("Enter your search query: ").strip()
    browser = input("Enter the preferred browser for this search (Default is 'Firefox', enter 'chrome' for 'Chrome'): ").strip()
    searchEngine = input("Enter your preferred search engine for this search (Default is 'Google', enter 'ddg' for 'duckduckgo'): ").strip()
    timeToRemainActive = input("Enter number of seconds to remain on this browser(Default time is 100secs): ").strip()

    if browser is "" and searchEngine is "" and timeToRemainActive is "": Search(searchQuery)
    elif browser is not "" and searchEngine is "" and timeToRemainActive is "": Search(searchQuery, browser)
    elif browser is "" and searchEngine is not "" and timeToRemainActive is "": Search(searchQuery, searchEngine=searchEngine)
    elif browser is "" and searchEngine is "" and timeToRemainActive is not "": Search(searchQuery, timeToRemain=int(timeToRemainActive))
    elif browser is not "" and searchEngine is not "" and timeToRemainActive is "": Search(searchQuery, browser, searchEngine)
    else: Search(searchQuery, browser, searchEngine, int(timeToRemainActive))