git pull &&
python merge_data.py &&
git add _data/hot-or-not/*.csv &&
git add _data/hot-or-not/*.js &&
git rm _data/hot-or-not/raw/dat* -f &&
git commit -m "crunch!" &&
git push https://5670f2140a11dc8e83598ff1259eb74385739237@github.com/zschutzman/districts-lol-data.git &&
cp _data/hot-or-not/*.csv ../hot-or-not/data &&
cp _data/hot-or-not/vote-data.js ../hot-or-not/data/vote-data.js &&
cd ../hot-or-not &&
git pull https://5670f2140a11dc8e83598ff1259eb74385739237@github.com/zschutzman/hot-or-not.git &&
git add data/*
git commit -m "updating data" &&
pwd &&
git push https://5670f2140a11dc8e83598ff1259eb74385739237@github.com/zschutzman/districts-lol.git &&
echo "done"
