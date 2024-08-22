# ECHO OFF
# ECHO Execuite UI Build Batch File

cd ./raw_ui_files/
pyuic5 -x ginaa_gui.ui -o ginaa_gui.py
mv ginaa_gui.py ./../built_ui_files/
cd ..

# ECHO Built the Raw UI Files!
