# modular-battery-symbol (for waybar)

## how to use: 
calling run.py creates image called bat.png. (keep in mind ull have to change paths and stuff)
> dont ask about why the popin stuff
basicly make waybar module like:
``` json
"image/bat":{
 "path":"/home/trollroy/.config/custom_run_scripts/battery-symbol/bat.png",
	"size": 32,
	 "interval": 5,
	"on-click": "mpc toggle"
},
```
> - i dont even know if the interval is required, i just put it there 
- run run.py every so often to change the battey icon on ur bar. 
- I used a battery-symbol.timer system timer unit to call a system service that ran run.py. theres gutta be a batter way to do that but im too eepy. 

## the circle stuff
- like the android battery circle. just gutta cut out a section :skull: to make that arr usable as a battery icon. (didnt figure out how)
