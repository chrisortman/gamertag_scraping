require 'nokogiri'

File.open("extracted.csv","w") do |output|
  Dir["*.html"].each do |html_file|
    doc = File.open(html_file) { |f| Nokogiri::HTML(f) }
    doc.css('table tr.row').each do |row|

      name = row.at('./td[3]').text
      points = row.at('./td[4]').text.gsub(",","")

      output.write"#{name},#{points}\n"
    end
  end
end
