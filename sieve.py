#!/var/www/treeio/venv/bin/python

import sifter.parser
import email

#rule='require ["fileinto"];if header :contains ["From", "To"] ["2root"] {fileinto "root";}'
#rules=sifter.parser.grammar.parser().parse(rule, lexer=sifter.parser.lexer.lexer())


f=open("test.sieve", "U") 
rules = sifter.parser.parse_file(f)

msg = email.message_from_file(open("/dev/stdin"))

print rules.evaluate(msg)

