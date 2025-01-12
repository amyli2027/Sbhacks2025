import scrapy
from datetime import datetime, timedelta

class MenuSpider(scrapy.Spider):
    name = "menu"
    
    def __init__(self, *args, **kwargs):
        super(MenuSpider, self).__init__(*args, **kwargs)
        self.start_date = datetime.today()
        self.end_date = self.start_date + timedelta(days=6)  # 7 days from today

    def start_requests(self):
        # Start from the current date
        current_url = self.generate_url(self.start_date)
        yield scrapy.Request(url=current_url, callback=self.parse)

    def parse(self, response):
        # Get the current date we're scraping for
        current_scraped_date = self.start_date.strftime('%Y-%m-%d')
        
        # Check if the page is available
        if response.status != 200:
            self.logger.info(f"Page not available for {current_scraped_date}")
            return  # Stop the spider if the page isn't available

        # If the page is available, scrape the data
        self.logger.info(f"Scraping data for {current_scraped_date}")
        
        # Process the data (e.g., extract dining hall and meal info)
        dining_halls = response.css('div.col-sm-6.col-md-6.col-lg-3')
        
        for dining_hall in dining_halls:
            hall_name = dining_hall.css('h4[data-toggle="collapse"]::text').get().strip()
            meal_sections = dining_hall.css('div.panel.panel-default')
            meals = []

            for meal_section in meal_sections:
                meal_name = meal_section.css('div.panel-heading h5::text').get().strip()
                if meal_name not in ["Breakfast", "Brunch", "Lunch", "Dinner"]:
                    continue

                food_items = []
                categories = meal_section.css('dl') 

                for category in categories:
                    category_name = category.css('dt::text').get().strip()
                    items = category.css('dd::text').getall()
                    food_items.append({
                        'category': category_name,
                        'items': [item.strip() for item in items]
                    })

                meals.append({
                    'meal_type': meal_name,
                    'food_items': food_items
                })

            # Yield data only if there are meals
            if meals:
                yield {
                    'date': current_scraped_date,
                    'dining_hall': hall_name,
                    'meals': meals,
                }

        # Move to the next day if we're within the 7-day range
        if self.start_date < self.end_date:
            self.start_date += timedelta(days=1)
            next_url = self.generate_url(self.start_date)
            yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            self.logger.info("Scraping finished for the 7-day period.")

    def generate_url(self, date):
        """Generate the URL for a given date"""
        return f'https://apps.dining.ucsb.edu/menu/day?dc=carrillo&dc=de-la-guerra&dc=ortega&dc=portola&d={date.strftime("%Y-%m-%d")}&m=breakfast&m=brunch&m=lunch&m=dinner&m=late-night&food='
