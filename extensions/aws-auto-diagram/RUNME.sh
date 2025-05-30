#!/usr/bin/env bash
#(C)2019-2022 Pim Snel - https://github.com/mipmip/RUNME.sh
CMDS=();DESC=();NARGS=$#;ARG1=$1;make_command(){ CMDS+=($1);DESC+=("$2");};usage(){ printf "\nUsage: %s [command]\n\nCommands:\n" $0;line="              ";for((i=0;i<=$(( ${#CMDS[*]} -1));i++));do printf "  %s %s ${DESC[$i]}\n" ${CMDS[$i]} "${line:${#CMDS[$i]}}";done;echo;};runme(){ if test $NARGS -eq 1;then eval "$ARG1"||usage;else usage;fi;}

##### PLACE YOUR COMMANDS BELOW #####

make_command "install" "Install in local extenions."
install(){
  cp -av ../aws-auto-diagram ~/.config/inkscape/extensions/
}

##### PLACE YOUR COMMANDS ABOVE #####
make_command "auto_install" "auto install while developing"
auto_install(){
  echo "Auto installing. Press CTRL-C to quit."
  find | entr cp -av ../aws-auto-diagram ~/.config/inkscape/extensions/
}
runme
