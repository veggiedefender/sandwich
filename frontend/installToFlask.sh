rm -rf ../../../app/static
for folder in */ ; do
    folder="${folder::-1}"
    cd "$folder/build"
    cp index.html "../../../app/templates/$folder.html"
    cp -r static ../../../app/
    cp -r ../src/css/* ../../../app/static/css
    echo "Installed $folder to Flask app"
    cd ../../
done