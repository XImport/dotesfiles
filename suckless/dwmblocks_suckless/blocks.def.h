//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
	{"WIFI : ","~/Documents/dwmblocks/scripts/wifi",					5,		0},
	{"Cpu: ", "~/Documents/dwmblocks/scripts/cpu",					1,		0},
	{"Mem:", "~/Documents/dwmblocks/scripts/memory",	1,		0},
	{"Volume: ", "~/Documents/dwmblocks/scripts/volume",					1,		0},

	{"", "date '+%b %d (%a) %I:%M%p'",					5,		0},
};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = " | ";
static unsigned int delimLen = 5;
