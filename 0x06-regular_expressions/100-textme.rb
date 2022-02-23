#!/usr/bin/env ruby
from = ARGV[0].scan(/\[[from](\w+(:\-?\+?\w+))\]/).join.split(':')[-1]
to = ARGV[0].scan(/\[[to](\w+(:\+?\d+))\]/).join.split(':')[-1]
flags = ARGV[0].scan(/\[[flags](\w+(:\-?\+?\d+){1,5})\]/).join.split(':')[1..-2]
puts (from + "," + to + "," + flags.join(':'))
