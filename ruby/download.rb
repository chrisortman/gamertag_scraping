require 'open-uri'
(1720..1800).each do |i|
  url = "https://www.xboxgamertag.com/leaderboards/#{i}"
  puts "Downloading #{url}"
  contents = open(url).read
  File.open("#{i}.html", "w") do |f|
    f.write contents
  end
end
