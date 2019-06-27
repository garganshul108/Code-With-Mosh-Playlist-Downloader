
#provide title URL from title-page.urls for the playlist content URL scraping
echo "scraping title page from $1"
python scrape_via_login.py $1 > title.html
echo "scraped into title.html"

#local scraping of title.html to get all the content page urls
echo "local scraping of contents"
python scrape_content_urls.py title.html > contents.url
echo "END" >> contents.url
echo "contents scraped" 

echo "removing unneccesary title.html"
rm title.html
output=$2
output=$(echo -e "$output" | tr -d '[:space:]')
output="$output.txt"
echo $output
python scrape_via_login_list.py > $output

rm contents.url

