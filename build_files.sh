echo " BUILD START"
python3.12 -m ensurepip --upgrade
python3.12 -m pip install --upgrade pip
pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput
echo " BUILD END"