#!/bash/sh
##safe
#provide title URL for the playlist content URL scraping
python scrape_via_login.py $1 > title.html

#local scraping of title.html to get all the content page urls
python scrape_content_urls.py title.html > contents.url

rm title.html

#for each content url in contents.url
    #print name of the video to videolinks.txt
    echo {name line} >> videolinks.txt

    #login scrape 
    python scrape_via_login.py {content.url.line} > content.html

    #local scrape download link
    python scrape_download_link.py content.html >> videolinks.txt

    #cleaning
    rm content.html


#videolinks is passed into the curl script