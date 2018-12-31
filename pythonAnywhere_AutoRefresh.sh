if (( $# < 2 )); then
     echo "Usage: ./<script> <username> <passw> [<seconds-interval>]"
     exit
fi
pip install requests
curl -o pyAny_autoRefresh.py https://pastebin.com/raw/Pxvs4uxW
python pyAny_autoRefresh.py "$@"
#rm pyAuto.py
