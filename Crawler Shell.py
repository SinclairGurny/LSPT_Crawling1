###########################Crawler Shell##############################
# ===============
# Crawler Process
# =============== 



# Permission Process Function
# ===========================
# Function to check the root directory for crawling Permissions
# -------------------------------------------------------------

# =============== =============     ========== =========
# Requirements    Inputs            Outputs    Throws 
# =============== =============     ========== =========
# None            List of links     None       None

# This function prematurly precosses each robots.txt file and stores them in 
# a hashtable with the key being the doc ID for the website and the value bing
# the rules of crawling for that website. 
def Permissions(): 

# Crawling Process Function
# ===========================
# Function to crawl each website by each permission
# -------------------------------------------------------------

# =============== =============     ========== ==============================
# Requirements    Inputs            Outputs    Throws 
# =============== =============     ========== ==============================
# None            List of links     None       Error if link no longer exists
  

# This function crawls each page by the robots.txt permissions from the root
# directory. It grabs the raw text data from the website. It then grabs the 
# outlinks from the websites and calls the Document Data Sore's API with the 
# crawl time, raw text, and website link
def Crawler():

######################################################################