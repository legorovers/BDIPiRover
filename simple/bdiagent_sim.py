import time
import sim_robot as robohat

beliefbase = {}
goalbase = {}


def getpercepts(beliefbase):
	dist = robohat.getDistance()
	beliefbase['dist'] = dist
	return

def manage_goals(beliefbase, goalbase):
	for goal in goalbase.keys():
		if (goal in beliefbase):
			if (goalbase[goal](beliefbase) == 1):
				goalbase.pop(goal, None)
	return

def believe(condition):
	global beliefbase
	return condition(beliefbase)

def alwaystrue(beliefbase):
	return 1

def is_obstacle(beliefbase):
	if 'dist' in beliefbase:
		if (beliefbase['dist'] < 50):
			return 1
	return 0

rules = {}
num_rules = 0

def add_rule(rule):
	global rules
	global num_rules
	rules[num_rules] = (alwaystrue, rule)
	num_rules = num_rules + 1

def add_condition_rule(condition, rule):
	global rules
	global num_rules
	rules[num_rules] = (condition, rule)
	num_rules = num_rules + 1

def add_belief(key, value):
	global beliefbase
	beliefbase[key] = value

def change_belief(key, value):
	global beliefbase
	beliefbase[key] = value

def add_goal(key, value):
	global goalbase
	goalbase[key] = value

def selectRule(beliefbase): 
	for key in rules.keys(): 
		tuple = rules[key]
		guard = tuple[0]
		if (guard(beliefbase) == 1):
			selected_rule = tuple[1] 
			return selected_rule
	

def execute(beliefbase, rule):
	rule(beliefbase)  

def and_belief(belief1, belief2):
	return lambda x: and_belief_support(belief1, belief2, x)

def not_belief(belief):
	return lambda x: not_belief_support(belief, x)

def and_belief_support(belief1, belief2, beliefbase):
	if (belief1(beliefbase) == 1):	
		return belief2(beliefbase)
	else:
		return 0

def not_belief_support(belief, beliefbase):
	if (belief(beliefbase) == 1):
		return 0
	else:
		return 1
 
def run_agent():
	robohat.init()
	global running
	running = 1
	while (running):
		getpercepts(beliefbase)
		manage_goals(beliefbase, goalbase)
		selected_rule = selectRule(beliefbase)
		execute(beliefbase, selected_rule)

def done():
	global running
	running = 0;


