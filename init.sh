mkdir master
mkdir slave
cp -r src ./master
cp -r src ./slave
sed -i 's+127\.0\.0\.1+master+g' master/src/project/settings.py
sed -i 's+127\.0\.0\.1+slave+g' slave/src/project/settings.py
