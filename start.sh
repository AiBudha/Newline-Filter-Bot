if [ -z $UPSTREAM_REPO ]
then
  echo "Repository not found, ensure UPSTREAM_REPO is set."
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /bot
fi
cd /bot
pip3 install -U -r requirements.txt
echo "Starting New Line Movies Bot...."
python3 bot.py
