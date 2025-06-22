from playwright.sync_api import sync_playwright

def extract_amazon_prices(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        
        # Wait for elements to load
        page.wait_for_selector("#productTitle", timeout=10000)
        page.wait_for_selector(".priceToPay", timeout=10000)
        
        # Extract product name
        product_name = page.text_content("#productTitle").strip()
        
        # Extract current price
        current_price = page.locator(".priceToPay .a-price-whole").first.text_content()
        currency_symbol = page.locator(".priceToPay .a-price-symbol").first.text_content()
        formatted_current_price = f"{currency_symbol}{current_price}"
        
        # Extract original price (MRP)
        original_price = page.locator(".a-price.a-text-price .a-offscreen").first.text_content()
        
        # Extract discount percentage if available
        discount_element = page.locator(".savingsPercentage").first
        discount_percentage = discount_element.text_content() if discount_element.count() > 0 else "0%"
        
        browser.close()
        
        return {
            "product_name": product_name,
            "current_price": formatted_current_price,
            "original_price": original_price,
            "discount_percentage": discount_percentage
        }

def extract_flipkart_prices(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        
        # Wait for price element to load
        page.wait_for_selector('div.Nx9bqj', state='visible')
        
        # Extract product name
        product_name = page.query_selector('h1._6EBuvT').text_content()
        
        # Extract current price
        current_price = page.query_selector('div.Nx9bqj').text_content()
        
        # Extract original price
        original_price = page.query_selector('div.yRaY8j').text_content()
        
        # Extract discount percentage
        discount = page.query_selector('div.UkUFwK').text_content()
        
        browser.close()
        
        return {
            'product_name': product_name.strip(),
            'current_price': current_price.strip(),
            'original_price': original_price.strip(),
            'discount_percentage': discount.strip()
        }

def main():
    url = "" # Place your url here
    
    if url:
        amazon_url = url if "https://www.amazon." in url else ""
        flipkart_url = url if "https://www.flipkart." in url else ""
    else:
        print("url is not provided.")

    if amazon_url:  
        amazon_price = extract_amazon_prices(amazon_url)
        print("Amazon Product Info : ", amazon_price)

    if flipkart_url:
        flipkart_price = extract_flipkart_prices(flipkart_url)
        print("Flipkart Product Info : ", flipkart_price)

if __name__ == "__main__":
    main()
