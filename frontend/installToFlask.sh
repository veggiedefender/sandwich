cd build
cp index.html ../../app/templates/
rm -rf ../../app/static
cp -r static ../../app/
cp -r ../src/css/* ../../app/static/css
echo 'Installed to Flask app'