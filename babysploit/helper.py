def run():
    from terminaltables import SingleTable
    from pyfiglet import Figlet
    banner = """    BabySploit is a framework aimed at helping aspiring
 penetration testers learn how to use the most common and
  useful tools in the field. Below is a table displaying 
      what commands are available and what they do.    
    """
    table_data = [
        ['Command', 'Description'],
        ['help or ?', 'Display this menu'],
        ['info', 'Display current configuration options'],
        ['search', 'Search exploitdb for exploits and get link'],
        ['tools', 'Display available tools'],
        ['set <key name>', 'Set configuration key'],
        ['reset', 'Reset configuration to default'],
        ['tutorial', 'Run the tutorial wizard'],
        ['exit', 'Exit framework']
    ]
    table = SingleTable(table_data)
    f = Figlet(font='slant')
    print(f.renderText("       Help"))
    print(banner)
    print(table.table)