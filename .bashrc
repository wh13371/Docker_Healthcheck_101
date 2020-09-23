# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

PS1='\[\e[1;32m\]\n\u\[\e[1;36m\] @ \[\e[1;31m\]\h\[\e[1;33m\] (\[\e[1;36m\]\w\[\e[1;33m\])\[\e[1;32m\]\[\e[1;32m\] @ \[\e[1;36m\]\D{%F %T}\[\e[1;37m\]\n#\e[m'

export GREP_OPTIONS='--color=auto'

alias c="clear"
alias ll="ls -lh"
alias mx='chmod a+x'
alias h='history'
alias x='exit'
alias cdh='cd ~'
alias now='date "+%Y_%m_%d_%H_%M_%S"'
