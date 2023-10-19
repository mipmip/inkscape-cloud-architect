#!/usr/bin/env bash
PATH=$PATH:/sbin
set -e

if [ $# -ne 1 ]; then
  echo "Usage: $0 AWS-icon-zip-file"
  exit 1
fi

zipfile=$1

rm -rf target build
mkdir target build

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

  python files_to_svg.py "Resource $componentname" target/aws-$componentname-resource-light.svg $lightfiles
  #python files_to_svg.py $componentname-dark target/aws-$componentname-resource-dark.svg $darkfiles
done

for dir in build/Architecture-Service*/*; do
  componentname=$(basename $dir | sed 's/^Arch_//' | tr 'A-Z_' 'a-z-')
  echo $dir
  files=$dir/*48/*.svg
  python files_to_svg.py "Service $componentname" target/aws-$componentname-service.svg $files
done

for dir in build/Category*/Arch-Category_48; do
  echo $dir
  componentname=$(basename $dir | sed 's/^Arch_//' | tr 'A-Z_' 'a-z-')
  files=$dir/*.svg
  python files_to_svg.py "Category $componentname" target/aws-$componentname-service.svg $files
done

