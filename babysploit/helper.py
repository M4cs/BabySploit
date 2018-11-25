def run():
    from terminaltables import SingleTable
    table_data = [
        ['Command', 'Description'],
        ['help or ?', 'Display this menu'],
        ['info', 'Display current configuration options'],
        ['search', 'Search exploitdb for exploits and get link'],
        ['tools', 'Display available tools'],
        ['set <key name>', 'Set configuration key'],
        ['reset', 'Reset configuration to default'],
        ['update', 'Check for updates and update thes framework'],
        ['tutorial', 'Run the tutorial wizard'],
        ['exit', 'Exit framework']
    ]
    table = SingleTable(table_data)
    print(table.table)