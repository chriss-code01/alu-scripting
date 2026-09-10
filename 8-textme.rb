#!/usr/bin/env ruby

message = ARGV[0]

from = message.match(/\[from:(.*?)\]/)
to = message.match(/\[to:(.*?)\]/)
flags = message.match(/\[flags:(.*?)\]/)

if from && to && flags
  puts "#{from[1]},#{to[1]},#{flags[1]}"
end
