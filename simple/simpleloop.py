import bdiagent, robohat, time


def reverse_rule(beliefbase):
	print "Obstacle!"
	robohat.reverse(80)
	time.sleep(1)
	robohat.stop()
	return

def print_dist_rule(beliefbase):
	print "Distance: ", beliefbase['dist']
	return

def print_obstacle_rule(beliefbase):
	print "Obstacle no move"
	return

def stop_rule(beliefbase):
	print "Stopping Agent"
	bdiagent.done()
	return

def start_rule(beliefbase):
	print "Starting Operation"
	bdiagent.change_belief('waiting_to_start', 0)
	return

def really_close(beliefbase):
	if (beliefbase['dist'] < 10):
		return 1
	return 0

def test_passes(beliefbase):
	if 'test' in beliefbase:
		if (beliefbase['test'] == 1):
			return 1
	return 0

def waiting_to_start(beliefbase):
	if 'waiting_to_start' in beliefbase:
		if (beliefbase['waiting_to_start'] == 1):
			return 1  
	return 0

def started(beliefbase):
	if 'waiting_to_start' in beliefbase:
		if (beliefbase['waiting_to_start'] == 0):
			return 1
	return 0


bdiagent.add_belief('waiting_to_start', 1)
bdiagent.add_condition_rule(bdiagent.and_belief(waiting_to_start, bdiagent.is_obstacle), start_rule)
bdiagent.add_condition_rule(bdiagent.and_belief(bdiagent.not_belief(waiting_to_start), really_close), stop_rule)
bdiagent.add_condition_rule(bdiagent.and_belief(started, bdiagent.is_obstacle), reverse_rule)
bdiagent.add_rule(print_dist_rule)

bdiagent.run_agent()