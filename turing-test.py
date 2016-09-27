  """Fully execute a set of given rules that match a given belief, until
    no more new rules are triggered. That is, this function should:
    (i) Scan through the rules until it finds rule(s) which are applicable,
    (ii) trigger such rules and update beliefs,
    (iii) repeat (i) and (ii) until no further rules can be triggered.
   
    Returns a new set of beliefs (without changing the original set of beliefs)
    based on which rules were triggered.

    Note: this function should employ a `while` loop and should call the `match`
    function you implemented in the first part of this problem.

    Hint: you should be able to do this in 8 lines of code, including the
    return statement.
   
    Parameters
    ----------
    belief : set
        A set of true propositions.
    rules : list of tuples
        A list of tuples, such that for each tuple, the first element implies
        the second (but not vice versa).
       
    Returns
    -------
    tuple of (new_belief, triggered_rules):
        new_belief is an updated set of true propositions, and triggered_rules
        is the list of rules that were triggered, in order.
"""



def match(belief, rule):
	
	for tuple in rule:
		for i in range(len(tuple) -1):
			if tuple[i] in belief:
				if tuple[i+1] not in belief:
					return tuple
		
			

#print_rules is GSI defined procedure
def print_rules(rules):

    for i in range((len(rules)-1)):
    	print(str(rules[i]) + " --> " + str(rules[i+1]))


def forward_chain(belief, rules):
	new_belief = belief.copy()
 	triggered_rules = list(new_belief)
	
	while match(new_belief, rules):
		
		returned_tuple = match(new_belief, rules)

		for i in range(len(returned_tuple)):
			if returned_tuple[i] not in new_belief:
				continue
			
			if returned_tuple[i] not in triggered_rules:
				triggered_rules.append(returned_tuple[1])
			
			new_belief.add(returned_tuple[1])

		forward_chain(new_belief, rules)
	
	
	return new_belief, triggered_rules
	

# test case
b,r = forward_chain({'a'}, [('a', 'b'), ('b', 'c'),  ('e', 'f')])

print_rules(r) # should print both 'a --> b' and 'b --> c'
