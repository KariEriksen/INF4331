from scraper import find_urls
from parser_text import verify 


"""
Used this file to check if the scraper.py would work, in 5.4, for urls.

Simply just run

$ python scraper_url_text.py

in terminal.
"""

sample_inputs = ["""
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>

        <a href='http://www.mn.uio.no/ifi/personer/vit/karleh.html'>
          
            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
            </div>

    This URL is not inside a hyperlink tag, so should be ignored: "http://www.google.com"
    """,
    
    """
    This is almost a hyperlink, but the quotes are mismatched, so it shouldn't be captured:

    <a href="http://www.google.com/super_secret/all_the_user_data/'>Please don't click</a>

    <a href="http://www.google.com/super_secret/user_data/'>Please don't click</a>
    """
]


expected_outputs = [
    [
        "http://www.mn.uio.no/ifi/personer/vit/karleh/index.html",
        'http://www.mn.uio.no/ifi/personer/vit/karleh.html'
    ],
    
    []
    
]

verify(find_urls, [sample_inputs], [expected_outputs])
