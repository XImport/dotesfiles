
/* See LICENSE file for copyright and license details. */

/* appearance */
static const unsigned int borderpx  = 1;        /* border pixel of windows */
static const unsigned int gappx     = 5;        /* gaps between windows */
static const unsigned int snap      = 32;       /* snap pixel */
static const int showbar            = 1;        /* 0 means no bar */
static const int topbar             = 1;        /* 0 means bottom bar */
static const char *fonts[]          = { "monospace:size=10" , "Mononoki Nerd Font:size=12" };
static const char dmenufont[]       = "monospace:size=10";
static const char col_gray1[]       = "#282a36";
static const char col_gray2[]       = "#444444";
static const char col_gray3[]       = "#bbbbbb";
static const char col_gray4[]       = "#f8f8f2";
static const char col_cyan[]        = "#44475a";
static const char *colors[][3]      = {
	/*               fg         bg         border   */
	[SchemeNorm] = { col_gray3, col_gray1, col_gray2 },
	[SchemeSel]  = { col_gray4, col_cyan,  col_cyan  },
	[SchemeStatus]  = { col_gray3, col_gray1,  "#000000"  }, // Statusbar right {text,background,not used but cannot be empty}
	[SchemeTagsSel]  = { col_gray4, col_cyan,  "#000000"  }, // Tagbar left selected {text,background,not used but cannot be empty}
    	[SchemeTagsNorm]  = { col_gray3, col_gray1,  "#000000"  }, // Tagbar left unselected {text,background,not used but cannot be empty}
    	[SchemeInfoSel]  = { col_gray4, col_gray1,  "#000000"  }, // infobar middle  selected {text,background,not used but cannot be empty}
    	[SchemeInfoNorm]  = { col_gray3, col_gray1,  "#000000"  }, // infobar middle  unselected {text,background,not used but cannot be empty}
};

/* tagging */
static const char *tags[] = { " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 " };

static const Rule rules[] = {
	/* xprop(1):
	 *	WM_CLASS(STRING) = instance, class
	 *	WM_NAME(STRING) = title
	 */
	/* class      instance    title       tags mask     iscentered     isfloating   monitor */
	{ "LibreWolf",                  NULL,       NULL,       1 << 8,       0,           -1 },
	{ "Nitrogen",                   NULL,       NULL,       1 << 7,       1,           -1 },
	{ "weather",                    NULL,       NULL,       1 << 7,       1,           -1 },
	{ "Lxappearance",               NULL,       NULL,       1 << 7,       1,           -1 },
	{ "Nvidia-settings",            NULL,       NULL,       1 << 7,       1,           -1 },
	{ "SimpleScreenRecorder",       NULL,       NULL,      1 << 5,       1,           -1 },
	{ "qutebrowser",                NULL,       NULL,       1 << 8,       0,           -1 },
	{ "Brave-browser",              NULL,       NULL,       1 << 8,       0,           -1 },
	{ "LibreWolf",                  NULL,       NULL,       1 << 8,       0,           -1 },
	{ "whatsdesk",                  NULL,       NULL,       1 << 4,       0,           -1 },
	{ "DesktopEditors",             NULL,       NULL,       1 << 5,       0,           -1 },
	{ "Gpick",                      NULL,       NULL,       1 << 7,       1,           -1 },
};

/* layout(s) */
static const float mfact     = 0.55; /* factor of master area size [0.05..0.95] */
static const int nmaster     = 1;    /* number of clients in master area */
static const int resizehints = 1;    /* 1 means respect size hints in tiled resizals */

static const Layout layouts[] = {
	/* symbol     arrange function */
	{ "",      tile },    /* first entry is default */
	{ "",      NULL },    /* no layout function means floating behavior */
	{ "掠",      monocle },
};

/* key definitions */
#define MODKEY Mod4Mask
#define TAGKEYS(KEY,TAG) \
	{ MODKEY,                       KEY,      view,           {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask,           KEY,      toggleview,     {.ui = 1 << TAG} }, \
	{ MODKEY|ShiftMask,             KEY,      tag,            {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask|ShiftMask, KEY,      toggletag,      {.ui = 1 << TAG} },

/* helper for spawning shell commands in the pre dwm-5.0 fashion */
#define SHCMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }
#define CMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }

/* commands */
static char dmenumon[2] = "0"; /* component of dmenucmd, manipulated in spawn() */
static const char *dmenucmd[] = { "dmenu_run", "-m", dmenumon, "-fn", dmenufont, "-nb", col_gray1, "-nf", col_gray3, "-sb", col_cyan, "-sf", col_gray4, NULL };
static const char *termcmd[]  = { "st", NULL };

static Key keys[] = {
	/* modifier                     key        function        argument */
        { MODKEY,                       XK_p,      spawn,          {.v = dmenucmd } },
        { MODKEY,                       XK_Return, spawn,          {.v = termcmd } },
        { MODKEY,                       XK_j,      focusstack,     {.i = +1 } },
        { MODKEY,                       XK_k,      focusstack,     {.i = -1 } },
        { MODKEY,                       XK_i,      incnmaster,     {.i = +1 } },
        { MODKEY,                       XK_d,      incnmaster,     {.i = -1 } },
        { MODKEY,                       XK_h,      setmfact,       {.f = -0.05} },
        { MODKEY,                       XK_l,      setmfact,       {.f = +0.05} },
        { MODKEY,                       XK_Return, zoom,           {0} },
        { MODKEY,                       XK_b,      togglebar,      {0} },
        { MODKEY,                       XK_Tab,    view,           {0} },
        { MODKEY,                       XK_t,      setlayout,      {.v = &layouts[0]} },
        { MODKEY,                       XK_f,      setlayout,      {.v = &layouts[1]} },
        { MODKEY,                       XK_m,      setlayout,      {.v = &layouts[2]} },
        { MODKEY,                       XK_0,      view,           {.ui = ~0 } },
        { MODKEY,                       XK_space,  setlayout,      {0} },
        { MODKEY,                       XK_comma,  focusmon,       {.i = -1 } },
        { MODKEY,                       XK_period, focusmon,       {.i = +1 } },
        { MODKEY,                       XK_Down,  setgaps,        {.i = -1 } },
        { MODKEY,                       XK_Up,  setgaps,        {.i = +1 } },
        { MODKEY,                       XK_e,       spawn,          CMD("/home/import/dmenu-scripts/dmenu-edit.sh") },
        { MODKEY,                       XK_s,       spawn,          CMD("/home/import/dmenu-scripts/dmenuweb.sh") },

/* Mod + Shift Key */
        { MODKEY|ShiftMask,             XK_Return, zoom,           {0} },
        { MODKEY|ShiftMask,             XK_w,       spawn,          CMD("/home/import/dmenu-scripts/dmenu-wifi.sh") },
        { MODKEY|ShiftMask,             XK_q,       spawn,          CMD("python3 /home/import/dmenu-scripts/dmenu-logout.py") },
        { MODKEY|ShiftMask,             XK_s,       spawn,          CMD("python3 /home/import/dmenu-scripts/sys-monitor.py") },
        { MODKEY|ShiftMask,             XK_f,       spawn,          CMD("/home/import/dmenu-scripts/dmenu-flatpak.sh") },
        { MODKEY|ShiftMask,             XK_e,       spawn,          CMD("/home/import/dmenu-scripts/dmenuemoji.sh") },
        { MODKEY|ShiftMask,             XK_a,       spawn,          CMD("python3 /home/import/dmenu-scripts/dmenu_appimage.py") },
        { MODKEY|ShiftMask,             XK_j,      rotatestack,    {.i = +1 } },
        { MODKEY|ShiftMask,             XK_k,      rotatestack,    {.i = -1 } },
        { MODKEY|ShiftMask,             XK_c,      killclient,     {0} },
        { MODKEY|ShiftMask,             XK_space,  togglefloating, {0} },
        { MODKEY|ShiftMask,             XK_0,      tag,            {.ui = ~0 } },
        { MODKEY|ShiftMask,             XK_Down,  tagmon,         {.i = -1 } },
        { MODKEY|ShiftMask,             XK_Up,    tagmon,         {.i = +1 } },
        { MODKEY|ShiftMask,             XK_equal,  setgaps,        {.i = 0  } },
        { MODKEY|ShiftMask,             XK_r,      quit,           {0} },
/* Mod + Alt Key  */

        { MODKEY|Mod1Mask,              XK_f,       spawn,          CMD("alacritty -e ranger") },
        { MODKEY|Mod1Mask,              XK_t,       spawn,          CMD("pcmanfm") },
        { MODKEY|Mod1Mask,              XK_s,       spawn,          CMD("flameshot gui -d 2") },
        { MODKEY|Mod1Mask,              XK_m,       spawn,          CMD("/home/import/dmenu-scripts/menu.py") },
        { MODKEY|Mod1Mask,              XK_Up,      spawn,          CMD("pkill -RTMIN+10 dwmblocks ; pactl set-sink-volume @DEFAULT_SINK@ +1%") },
        { MODKEY|Mod1Mask,              XK_Down,    spawn,          CMD("pkill -RTMIN+10 dwmblocks ; pactl set-sink-volume @DEFAULT_SINK@ -1%") },
        { MODKEY|Mod1Mask,              XK_c,               spawn,      CMD("python3 /home/import/dmenu-scripts/dmenu-color.py") },
        { MODKEY|Mod1Mask,              XK_b,       spawn,          CMD("librewolf") },
        { MODKEY|Mod1Mask,              XK_q,       spawn,          CMD("calc") },
        { MODKEY|Mod1Mask,              XK_d,       spawn,          CMD("python /home/import/dmenu-scripts/dwm.py") },

/* ALT SWICTHER KEY */
        { Mod1Mask,              XK_Tab,       spawn,          CMD("/home/import/dmenu-scripts/dswitcher") },


        TAGKEYS(                        XK_1,                      0)
	        TAGKEYS(                        XK_2,                      1)
	        TAGKEYS(                        XK_3,                      2)
	        TAGKEYS(                        XK_4,                      3)
	        TAGKEYS(                        XK_5,                      4)
	        TAGKEYS(                        XK_6,                      5)
	        TAGKEYS(                        XK_7,                      6)
	        TAGKEYS(                        XK_8,                      7)
	        TAGKEYS(                        XK_9,                      8)	
};

/* button definitions */
/* click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin */
static Button buttons[] = {
	/* click                event mask      button          function        argument */
	{ ClkLtSymbol,          0,              Button1,        setlayout,      {0} },
	{ ClkLtSymbol,          0,              Button3,        setlayout,      {.v = &layouts[2]} },
	{ ClkWinTitle,          0,              Button2,        zoom,           {0} },
	{ ClkStatusText,        0,              Button2,        spawn,          {.v = termcmd } },
	{ ClkClientWin,         MODKEY,         Button1,        movemouse,      {0} },
	{ ClkClientWin,         MODKEY,         Button2,        togglefloating, {0} },
	{ ClkClientWin,         MODKEY,         Button3,        resizemouse,    {0} },
	{ ClkTagBar,            0,              Button1,        view,           {0} },
	{ ClkTagBar,            0,              Button3,        toggleview,     {0} },
	{ ClkTagBar,            MODKEY,         Button1,        tag,            {0} },
	{ ClkTagBar,            MODKEY,         Button3,        toggletag,      {0} },
};

