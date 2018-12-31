if (( $# < 2 )); then
     echo "Usage: ./<script> <username> <passw> [<seconds-interval>]"
     exit
fi
pip install requests
curl -o pyAny_autoRefresh.py https://raw.githubusercontent.com/smartm13/AutoExtend_pythonanywhere/master/pythonAnywhere_AutoRefresh.py
python pyAny_autoRefresh.py "$@"
#rm pyAuto.py
