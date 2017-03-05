cd build
cp index.html ../../app/templates/
rm -rf ../../app/static
cp -r static ../../app/
echo 'Installed to Flask app'