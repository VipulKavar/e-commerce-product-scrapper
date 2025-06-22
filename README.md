# 🛒 E-Commerce Product Scraper

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/Playwright-Latest-green.svg)](https://playwright.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/product-scraper?style=social)](https://github.com/VipulKavar/e-commerce-product-scrapper)

> **Effortlessly extract product details from Amazon and Flipkart with lightning-fast web scraping powered by Playwright.**

## 🌟 Features

-   🎯 **Multi-Platform Support** - Works seamlessly with Amazon and Flipkart
-   ⚡ **Lightning Fast** - Powered by Playwright for maximum performance
-   💰 **Complete Price Analysis** - Current price, original price, and discount percentage
-   🔧 **Easy Configuration** - Simply update the URL and run
-   📊 **Clean JSON Output** - Structured data ready for your applications
-   🛡️ **Robust & Reliable** - Built-in error handling and retry mechanisms

## 🚀 Quick Start

Get up and running in less than 2 minutes!

### Prerequisites

-   Python 3.11 or higher
-   pip package manager

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/VipulKavar/e-commerce-product-scrapper.git
    cd e-commerce-product-scrapper
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Install Playwright browsers**
    ```bash
    playwright install
    ```

### Usage

1. **Configure your target product**

    Open `main.py` and update the `url` variable with your desired product URL:

    ```python
    url = "https://www.amazon.in/your-product-url"
    # or
    url = "https://www.flipkart.com/your-product-url"
    ```

2. **Run the scraper**

    ```bash
    python main.py
    ```

3. **Get your results**
    ```json
    {
        "product_name": "Sparx Men Buckle Sandal",
        "current_price": "₹768",
        "original_price": "₹1,025",
        "discount_percentage": "-25%"
    }
    ```

## 📋 Example Usage

Here's a complete example of scraping a product from Amazon:

```python
# Example URL for Amazon India
url = "https://www.amazon.in/Sparx-Mens-Dark-Sandal-SS0561G/dp/B08ZNKCQN2"

# The scraper will automatically detect the platform and extract:
# ✅ Product Name
# ✅ Current Price
# ✅ Original Price
# ✅ Discount Percentage
```

## 🏗️ Project Structure

```
product-scraper/
│
├── main.py              # Main scraping script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🛠️ Supported Platforms

| Platform      | Status             | Features               |
| ------------- | ------------------ | ---------------------- |
| Amazon India  | ✅ Fully Supported | Price, Name, Discounts |
| Flipkart      | ✅ Fully Supported | Price, Name, Discounts |
| Amazon Global | 🔄 Coming Soon     | -                      |
| Myntra        | 💡 Planned         | -                      |

## 📊 Output Format

The scraper returns a clean JSON object with the following structure:

```json
{
    "product_name": "string",
    "current_price": "string (with currency symbol)",
    "original_price": "string (with currency symbol)",
    "discount_percentage": "string (with percentage sign)"
}
```

## 🚨 Rate Limiting & Best Practices

-   **Respect robots.txt** - Always check the website's robots.txt file
-   **Add delays** - Implement reasonable delays between requests
-   **Use proxies** - For large-scale scraping, consider using proxy rotation
-   **Monitor performance** - Keep track of success rates and adjust accordingly

## 🤝 Contributing

We love contributions! Here's how you can help:

1. 🍴 **Fork the repository**
2. 🌿 **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. 💾 **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. 📤 **Push to the branch** (`git push origin feature/amazing-feature`)
5. 🔄 **Open a Pull Request**

### What we're looking for:

-   🆕 New e-commerce platform support
-   🐛 Bug fixes and improvements
-   📚 Documentation enhancements
-   ⚡ Performance optimizations

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Always ensure you comply with the terms of service of the websites you're scraping. Be respectful and don't overload servers with requests.

## 🌟 Show Your Support

If this project helped you, please consider:

-   ⭐ **Starring the repository**
-   🐛 **Reporting bugs**
-   💡 **Suggesting new features**
-   📢 **Sharing with friends**

## 📞 Contact & Support

-   📧 **Email**: vipulkavar@gmail.com
-   💼 **LinkedIn**: [@vipul-kavar](https://www.linkedin.com/in/vipul-kavar-45a695124/)
-   💬 **Issues**: [GitHub Issues](https://github.com/VipulKavar/e-commerce-product-scrapper/issues)

---

<div align="center">

**Made with ❤️ by [Vipul Kavar](https://github.com/VipulKavar) in INDIA**

_Don't forget to ⭐ this repo if you found it useful!_

</div>
