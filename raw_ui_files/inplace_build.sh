# ECHO OFF
# ECHO Execuite UI Build Batch File

pyuic5 -x ginaa_gui.ui -o ginaa_gui.py
mv ginaa_gui.py ./../built_ui_files/

# ECHO Built the Raw UI Files!
