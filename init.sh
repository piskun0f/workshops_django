rm -rf master
rm -rf slave
mkdir master
mkdir slave
cp -r src ./master
cp -r src ./slave
sed -i 's+127\.0\.0\.1+postgresql-master+g' master/src/project/settings.py
sed -i 's+127\.0\.0\.1+postgresql-slave+g' slave/src/project/settings.py
