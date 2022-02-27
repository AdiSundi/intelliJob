# intelliJob

## Intelligent job listing screener (made during iNTUition v8 2022)

> A curated list of jobs keeping in mind your cognitive, sensory and mobile impairments, powered by data and delivered to your fingertips. Unleash your true potential, don't let the world hold you back.

### We designed this solution to solve the following problems:
- Lack of clarity for job compatibility for employees with impairments
- Difficulty in finding job listings for the less tech savvy

### Our solution to this:   
_An NLP powered algorithm that uses past employement data to scout and provide you with the most suitable job listings for you based on your impairments, delivered to you through the Indeed job portal or via email_

### The following impairments are considered for this algorithm:
1. LV - Low Vision
2. HI - Hearing Impaired
3. MPD - Mild Physical Disability
4. PD - Physical Disability
5. CP - Cerebral Palsy

### Code Base:
1. ` indeedscraper.py  ` - initial web scraper to populate job database
2. ` job_smartFilter.py ` - prepares our NLP pipeline, and standardizes the job posting input to an analysable format
3. ` ruleset.py ` - generates a rule binding between jobs and the disability classes based on past employment data found through web url scraping
4.  ` world_cluster_predictor.py ` - creates the NLP model, saves it, and reads through the job posting database, preparing it for impairment tag addition
5.  `model_ODE.py ` - loads our NLP model, runs it on the test data, adds the tag for the impairment suitability and exports it to a spreadsheet form.
6.  `StochasticPredictor.ipynb` - Predicts job suitability likelihood using a Stochastic Gradient Descent Regression algorithm over a Bag of Words model of hand picked data set
7.  Along with these scripts, some additional scripts were written to help clean and regulate our databases, but they have not been added here as they are standard     pandas dataframe cleaning functions.
8.  The .txt files contain standardised data generated from past employment data to help us find key words for jobs secured by people with different impairments

### Spread Sheets:
1. `300_job_listings.xls` - 300 job postings from Indeed, cleaned up
2. `Rated_650JobPostings_cleaned.xlsx` - 650 job postings from Indeed, cleaned up
3. `indeed_ODE.csv` - output from our Gensin/FastText NLP algorithm, with job suitability rating for each impairment tag
4. `indeed_ODE_average.csv` - output that combines the results of both our Stochastic Gradient Descent Regression algorithm along with the Gensin/FastText NLP algorithm, with job suitability rating for each impairment tag

## Algorithm Flow Chart:
![Alt text](./workflow1.png?raw=true "Workflow")


## DISCLAIMER : This project does not condone web scraping/web crawling in any way. Please follow rules set by the robots.txt file for each job portal. This web scraper was used purely for the hackathon, the end goal is to provide this to Indeed to integrate into their portal as a feature.
 
