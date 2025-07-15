from apy.cli import Cli
from apy.net import Net

# Initialize CLI and Net helper objects
cli = Cli()
net = Net()

# Add an item to the CLI menu
cli.item("Stations by TAG")

# Make a GET request to the radio-browser API for station stats
reply = net.get("http://all.api.radio-browser.info/json/stats")

# Verify the response status and display content or warning
if cli.verify("Getting stations...", reply['status'], 200):
    cli.content(reply['body'])
else:
    cli.warning(reply['log'])

"""
# Example usages of the CLI helper methods:

cli.info("Press 'Ctrl + C' anytime to cancel.")
cli.ask("Customer account ID")
cli.secret("User admin secret")
cli.section("Section")
cli.item("Item")
cli.content({"Content": "Dictonary"})
cli.verify("Verify OK", 1, 1)
cli.verify("Verify ERROR", 1, 2)
cli.wait(2)
cli.warning("Warning.")
cli.critical("Critical.")
"""