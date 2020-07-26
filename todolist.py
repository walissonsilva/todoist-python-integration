from todoist.api import TodoistAPI
from datetime import date

api = TodoistAPI(open('api-token.txt').read())

api.sync()

# TAREFAS DO DIA
print('{:^40}|{:^20}'.format('Task', 'Category'))
print('·' * 61)

for task in api['items']:
	data = task['due']['date'].split('-')
	data = [int(data[i]) for i in range(len(data))]

	data = date(data[0], data[1], data[2])

	if data <= date.today() and not task['checked']:
		for project in api.state['projects']:
			if (task['project_id'] == project['id']):
				print('{:^40}|{:^20}'.format(task['content'], project['name']))


"""print(api.state.keys())
print(api.state['day_orders'])

for order in api.state['day_orders']:
	print(order)
	item = api.items.get_by_id(order)
	if item != None:
		item = item['item']

		print(item['content'])
		print(item['due'])
	#if (not order['item']['checked']):
#		print(api.items.get_by_id(order))
"""