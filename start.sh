if [ -z "$UPSTREAM_REPO" ]
then
  echo "No UPSTREAM_REPO found, using local files..."
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone "$UPSTREAM_REPO" /bot_upstream
  cp -r /bot_upstream/* .
fi

echo "Starting New Line Movies Bot...."
python3 bot.py
