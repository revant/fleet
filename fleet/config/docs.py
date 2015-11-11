"""
Configuration for docs
"""

source_link = "https://github.com/revant/fleet"
docs_base_url = "https://revant.github.io/fleet"
headline = "Fleet Management App for ERPNext"
sub_heading = "Fill Up Records, Trip Records and Fleet Database integrated into ERPNext"
# long_description = """(long description in markdown)"""

def get_context(context):
	context.brand_html = "Fleet"
	# context.favicon = 'path to favicon'
    #
    # context.top_bar_items = [
    #   {"label": "About", "url": context.docs_base_url + "/about"},
    # ]
