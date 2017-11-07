File.open("extracted.csv") do |file|
  file.each_line do |check|
    puts check if check =~ /^n.+007,76\d\d\d$/
  end
end
