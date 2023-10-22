#!/usr/bin/env bash
PATH=$PATH:/sbin
set -e

if [ $# -ne 1 ]; then
  echo "Usage: $0 AWS-icon-zip-file"
  exit 1
fi

rm -rf target build
mkdir target build

# GROUPICONS FROM AWSLABS
tempdir0=awslabs-repo

mkdir build/Groups

if [ ! -d "${tempdir0}/.git" ]; then
  maindir=$(pwd)
  git clone https://github.com/awslabs/aws-icons-for-plantuml.git $tempdir0
  cd $tempdir0
  git checkout 3d42fc82ac898614c9b6dcebbc895ba4043208da
  cd $maindir
fi

rsync -av $tempdir0/source/unofficial/Groups_04282023/ build/Groups/Light/ --exclude *.touch --exclude DARK --exclude *.png
rsync -av $tempdir0/source/unofficial/Groups_04282023/Dark/ build/Groups/Dark/ --exclude *.png

# OTHER ICONS FROM ASSETS ZIP
zipfile=$1
tempdir=`mktemp -d`

unzip -q $zipfile "*.svg" -d $tempdir
rsync -av $tempdir/ build --exclude GRAYSCALE/* --exclude __MACOSX

rm -rf $tempdir

servicedir=$(ls -d build/Architecture-Service*)
if [ -d "$servicedir/Arch_Developer- Tools" ]; then
  mv "$servicedir/Arch_Developer- Tools" "$servicedir/Arch_Developer-Tools"
fi

for dir in build/Resource*/*; do
  componentname=$(basename $dir | sed 's/^Res_//' | tr 'A-Z_' 'a-z-')

  lightfiles=$dir/*.svg
  #darkfiles=$dir/*.svg
  if [ $componentname == "general-icons" ]; then
    lightfiles=$dir/Res_48_Light/*.svg
    #darkfiles=$dir/Res_48_Dark/*.svg
  fi

  python3 files_to_svg.py "Resource $componentname" target/AWS-Resource-$componentname-light.svg $lightfiles
  #python files_to_svg.py "Resource $componentname-dark" target/aws-$componentname-resource-dark.svg $darkfiles
done

for dir in build/Architecture-Service*/*; do
  componentname=$(basename $dir | sed 's/^Arch_//' | tr 'A-Z_' 'a-z-')
  echo $dir
  files=$dir/*48/*.svg
  python3 files_to_svg.py "Service $componentname" target/AWS-Service-$componentname.svg $files
done

for dir in build/Category*/Arch-Category_48; do
  echo $dir
  componentname=$(basename $dir | sed 's/^Arch_//' | tr 'A-Z_' 'a-z-')
  files=$dir/*.svg
  python3 files_to_svg.py "Category $componentname" target/AWS-Category-$componentname.svg $files
done

for dir in build/Groups/*; do
  echo $dir
  componentname=$(basename $dir | sed 's/^Arch_//' | tr 'A-Z_' 'a-z-')
  files=$dir/*.svg
  python3 files_to_svg.py "Group $componentname" target/AWS-Group-$componentname.svg $files
done

