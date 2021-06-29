inp = open('test-results.xml', 'r')
out = open('test-results2.xml', 'w')
prev = inp.readline()
for line in inp:
   if line.startswith('<?xml'):
      out.write(line)
      
out.write(prev)
out.close()
inp.close()
