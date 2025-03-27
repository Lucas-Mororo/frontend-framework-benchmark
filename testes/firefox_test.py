from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def configure_firefox():
    # Configure Firefox options
    options = Options()
    options.headless = False  # Set to True if you don't need GUI
    
    # Set network preferences
    profile = webdriver.FirefoxProfile()
    
    # Limit network speed (values in KB/s)
    # This simulates a slower connection (e.g., 256 KB/s)
    profile.set_preference("network.throttle.download", 256)
    profile.set_preference("network.throttle.upload", 256)
    
    # Basic browser configurations
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("network.http.pipelining", True)
    
    # Initialize Firefox with the profile
    driver = webdriver.Firefox(
        options=options,
        firefox_profile=profile
    )
    
    return driver

def run_test():
    try:
        # Configure and launch Firefox
        driver = configure_firefox()
        
        # Open localhost project
        driver.get("http://localhost:8000")  # Adjust port if needed
        
        # Keep browser open for 30 seconds
        print("Browser opened to localhost. Running for 30 seconds...")
        time.sleep(30)
        
        # Basic test example
        print("Page title:", driver.title)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Cleanup
        driver.quit()

if __name__ == "__main__":
    run_test()