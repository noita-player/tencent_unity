# -*- coding: utf-8 -*-
# 3.8.3 - pip instlal ipython lz4
import struct, re, argparse
from pathlib import *
import IPython
import lz4.block


banner = """
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWMWWWWWWWWWWWWWNXKOkdcldddool:::cc:,,;::::lllooc:cc:;;;;:c:,',;'..';;',;;:c:;;;,,,'';;;:ccllllx0XNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNXK0dll:;cloodocc::clllc::::;::cclc:;,;:ccclolcc:,,:;,,',,.',',,',,,'';;,,;;;:::;;;;:dOOKNNNWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMWWWWWNNNNX0kdool:;:llccloolooolccc:::,',:cc:;;;:::lolll:;,;cc::::;'........';;,,,:c;;;;,,;::::;,;:ldkOKXNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWWWWWNXKOxkxdooolc::cllccclcloolc::clc;,,:cll:;;;;:cllc:;,,:clc:cc:,,,',;'...,:cccc::c:;,;:;,;:::;;;,,;::lxO0XNNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMMMMMMMMWWWWWWWKxcccloooolcccllc:::ccc:::cccccc:ccccc::::::c::,'',;clllccol::::;;c:;;;;;:lc:cc;,,';c::;,::,,:::cc::clldkKXXXNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWWWWWWWWWWWWNNXOdccccodolcc::c:;;,;:ccc:;:ccc:ccc:;;::cc:;;;'''',:;;clolc:::::;;:::lc;,::::,',:;'',,:lc:;;cc,,coooolooc:cldkOKNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWMWWMMMWWWWWWWWNKkdlc:;;coollc::c:,,'',;cc:;,;::::c:;,,,;;::;,,,,',,::;,:c:::;,,,,;:;::;;,,;,,;c:',,,;:c:;lool::::;,:odddolcc:cclokXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWMMWWWWXOdl:;;:;,;cc:::;;:;''''',,,,,'',;;;;;,,,,,,,,,,;;::;;;;;,;:;,,'',,,,;;,;:;;,;;,'':l:::;,;:lc;cdoooccc;,cddl:::c::clloxk0XNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKd:;,,::;,,;;;,;;,'.................''''',,,'',,;;;::;;;,,,,,,,,,,,,,,,,;;::;;;;,,';c:::;,,;:::clddodllolcldo;:oolc;;lddolox0XNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNXkl,''';;;'''''.............   .   .............',,,,,,''...''''''''',;;;,;;;,'',,,,,;;;;;,,,,,',:cloloolollloo:;ldxl,';clllllxOKNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNWX0d:,',',,...............  ..............   ............. ..........',,,,,,,,'.....',,,,,''',,,,,,,',:l:colllcclllccloollc;;;:coodx0XNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXkl,',,,''.. ..  ....'','.......'',,,.........'''''''.....'...,;;;;::cc::;;;;;;,,,;;:llc::;;;;,;;;,'..,;;:clllcccloo:;clloddlc:;;cccdk0NWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWN0d:,..,,...      ...';:ccc:;::::cllodoc:cccllodxxxxkkOOOOOOkxdxkkkxxxxkkkkkkkxxxxdxxxO0Okxxddollll:,..';::cllllllooolc;:cclodddo:,;:coooONWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWMMMWWMWWWNWN0dc;,'.',..      .',,:ldkkkkkkOOOO00KKKKKKXXXXNNNNNWWWWWWMMMMWWWWWNNNNNNNWWWWWNNNNXXNNNNNNNXXKK0000Oxolldxxkkkkkkxxxxoll:;,,:llodoooc::cl::kXNWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWNXd;,'...'..     .':ldxO0KKKKKXXKXXXXNNNNNNWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMWWWWNNNNNNNNNNNNNNX00Oxoc;'',;;cclodo:;;;;:lkKNNWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWMWWWWWNKkc'......     .,ldxO00KKXXXXXXXXXXNNNNWWNWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNX0xl;;;'',,;ccccc:;:codOXNNWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWN0xc,......    .'lxOO0KKKKKKXXXXXXXXXXNNNNNNWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkoc,''..',;cc:cldxdx0XWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWNNXOdc;.....    .,lxkOO000KKKKKKXXXKXXXXXXXNNNNWWNNWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0xc;,....,,'coldlcxKXNWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWNNNKxc;'...     ,okkOOOOO000KKKKKKKKKKXKKKXXXNNNNNNNNNNWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkd:......:l::ccokOKNWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWKxc,'..     .lkOOOOOOOOO000000KKKKKKKKKKKKXXXXXXNNNNNNNNNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWX0d;.. ..,;;c:coxKXNNWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWXd:,'..     'dkOOOOOOOkkO0000000KKKKKKKKKKKKKKKKXXNNNNNNNNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKd:'...,;:cclx0XNWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWNOc,...    .:xkOOOOOkkkkkO000000000000KKKK0000KKKKKXXXXXXNNNWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0l,''',;lxdodOXNWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWKd;...   .'cxkOkkkkkkkkkkOO0000000000000000000KKKKKKXXKKXXXNNNWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo;'',;lxxookKNWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWNO:.  .  .,cdkOOkkkkkxxxkkkOOO000OOO000000000KKKKK00KKKKKXXXXXNNNNNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXx:,;:coxxxxkKNWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWNOl'     .':dkkkkkxxxxxxxxkkOOOO00OOOOO000000000000000000KKXXXXXXXXXNNNWWWMWWWMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMXxc:cldxkOkxOXNWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWNKl'.    .';lxkkkkxxxxxxxxxkkkOOOOOOOOOOOOO000000000000000KKKKKXXXXXXXNNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd:coxxkOOOO0XWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWXx'..   ..,cdxxxxxxxxxxddxxxkkkOOOOOOOOOOOOOOOOOOO00OOO0000KKKKKKXXKKXXXNNNNNWWWWWWWWWWWWNNNNNNNNNNNWNWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0ocldxdxkkkkOXWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWN0:..   ...;lddxxxddddxxddxxxkkkOOkkkkkkkkOkkOOOOOOOOOOOOOOO0KK00KKKKKXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNWNWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkc:colodxkxx0XNWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWXo..    ...,ldddddddddxxdddxxxxkkkkkkkkkkkkkkOOkkkkOOOOOOOO0000000KKKKKKKXXXXXXNNNNNNNNNXXNNNNNNNNNNNNNNNNNNNNNWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMWWWKd;:::loodxkOXNNWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWN0:.     ...;loddddddddddddddxxxxkkkkkkkkkkkOkkkkkkkkOOOOO00000000KKKKKKKKKXXXXXXXXXXXXXXXXXXXXXNNNNNNNNNNXNNNNNNNNNWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMWWWWWWNOc;;;:ccldxx0NWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWNO,       .';lodddddddddddddddxxxxkkkkOkkkkOOkOOOOOOOOOOO000000000KKKXXKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNNNXXNXXXNNNNWWWWWWWWWWWMMMMWWWWWWWWWWWWWWWNNWW0oc::;,;:lxxkKWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWXx,.      .';cloddddddddddddddddxxkkkkkkkkkOOO000OOOOO0000000000KKKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXXNNXNNNNNNWNNWWWWWWWWWWWWWWWWWWWWWWWWWNNNNWXxlcc;.';ldxdONWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWKo'.      ..;cloodddddodddddodddxxxxkkkkOOOOOO0000OO0000000KKK00KKK00KKXXXXXXXXXXXXXXXXXXXXXXXXXXNNNNXXXXXNNNXNNNNNNNNNNNNNWWWWWWWWWWWWWNNWWWWNNNNNNNNNNNXkcclc..,codd0NWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWN0c..      .';:clooooooooddoooodddxxkkkkkOOOOOO000000000O00KKKK00KKKKKKXXXXNXXXXXXXXXXXXXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNWWWWWWWWWNNNNNNNNNNNNNNNNNXXXXXOocll,..;lolxNWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWNXOc.       ..,:cllooooooooooooooddxxkkkkkkOOOOO00000K0000KKKKKK0KKKKKKXXXXNNNNNNNXXXXXXXNNXXNNXXNNNNNNNNNNNNNNNNNNNNNNNWNWWNWWWWWNNNNNNXXXXXXNNNNNXNNNXXXXXOolll:'..cocoKWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWXk;.       ..';:clooolloooooooodddxxkkkkkOOOOO0000KKKKKKXXXXXXXXXXXXNXNNNNNNNNNNNNXNNNNNNNNNNNNNWWWWWWWWWWWWWWWWWWWWWWWWNWWNWWWWWWNNNNNXXXXXXXXXXXXXXXXXXXKkllc:::..:llo0NWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWNXO;.        ..,:cllllllooooooooodddxxxkkOOOOO0000KKKXKXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWWWWWWWWWMMMMWWWWWWWMWWWWWWWWWWWWWWNNNNNXXXXXXXXXXXXXXXXXXXXK0kl:;,,:,';cldONWWWWWWWWWWWWWWW
WWWWWWWWWWWWNNWNx'         ..';:cclllllllooooooddddxxkkkOOO00000KKXXXXXNNNNNNNNNNNWWWWWWWWWWWWWWNNNNNNNNNNWWWWWWWWMMMMMMMMMMMMMMMMMWWWWMMWWWWWWNNNNNXXXXXXXXXXXXKKKKKKKK0Okl,,'',',clldOXNWWWWWWWWWWWWWW
WWWWWWWWWWWWWNNKc          ...,::ccllllllloooooddxxxkkOO00000KKKKKXXKXXNNNNNNNNNNNNWWWWWWWWWWWWWWWWNNNNNNWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWNNNXNNXXXXXXXXKKKKK000KKK0Okl;'...';ccllkXNNWWWWWWWWWWWWW
WWWWWWWWWWWWWWWK;           ..',::ccclllllllooddxxkkkOO0000KKKKKKXXKKXXXXXXXXNNNNNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWNNNNNXXXXKKXKKKKK0000000Okdl;'..'';;:clxXWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWK;            ..';:cccclllllloodxkkOOOO00KKK00KKKKXKKKXXXXXXXXXXXXXXXNNNNNNWWWWWWWWNNNNWNNWWWWWWWWWWMMMMWWMMMMMMMMMMMMMMMMMMMMMWWWNNXXXXXXKKKKKKKK000OO00Oxl:,....',,;coONWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWK;            ..',:cccccclllloddxkOO0000KKKK0KKKKKKKKKKXXXXXKKKXXXXXXXXXXNNNNNWWNNNNNXXNNNNNNNNNNNNNWWWWWWMMMMMMMMMMMMMMWWMMMMMMMMWNNNNXXXKKKKK000000OOOOxo:,....'''.':o0NWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWK:            ...,:ccclcccclodxxkkO000000000KKKKXXKKKKKKKKKKKKKKKKKKKK0O0KXXXXNXXXXXXXXXXXXXXNNNXXXNNNNNWWWWWWWWWWWWWMMWWMMMMMMMMMMWWNNNNXXKK000000OOOOOkdc,'...',,'..'oKNWWWWWWWWWWWWNWW
WWWWWWWWWWWWWWWXd.            ..,:ccccccclodxxxxxxkkkOOOOkkOOkkOOOOkkkkkkkkkOOOOOO000OO00KKKKKXKKKKKKKKKKKKKKKKKKXXXXKXXXNNNNNNWWWNNNWMMMMMMMMMMMMMMWWWNNNXKK00000OOOOkxl:''...,;'...,dXNNWWWWWWWWWNNNNW
WWWWWWWWWWWWWWWNO,             .,cccccllloooolllloooodxxdoooolllllcccllloooodxxxxkkkOOOOOO000000000000000000000000OOOO000000000000KKKXNNNNNWWWWWWWMMMMWWWWNXKK0000OOOOkdc;.....,,'...,dKNNNWWWWWNNNNNNNW
WWWWWWWWWWWWWWWNKd.            .,ccccclllollcccccclllllllcccccc:::;;;;;:::cclooodddxxxkkkkkkOOOOOkkOOOOOOOkkkkkxxxdddddddooooooooddxxkkkkkOO0KKKKKXNWWWWWWWNXKK00000Okxl:'...'..'....'dXNNNNNNNNNWWWWWWW
WWWWWWWWWWWNNNNNNK:            .,ccllllllllccccccccllllccllllcccc::;;;;;;;;::::cllloodddxxxxxxxxxxxxxxdddxxdddooollcccc::::::;;;;:::cccllllodxkkkkOO0KXNWWWNXKKK00000Odc;...;:....  .,kNNNNNNNNNNNNNNNNN
WWWWWWWWWX0OOOOOO0o.           .;cllllllllcccclllllloollllooooollcc:::::;;;;;;;;:::cllloodddxxxxxxxxxdooodoolllccc::;;;;;;;;;;;;:::cclllllloooodddxxxkO0KXNNNXKKK0000Odc;'.,c:'...  .;ONNNNNNNNWWWWWWWWW
WWWWWWWWNkddxxkxdoc.           .;llccclllccccclccllllllloooddddooolccc::::;;;;;,;;;;:::clloddxxxxxxxdddoollccc:;;;;;;;;;;;;;;;;:ccclollooooooodddddxxxkO00KXXXKKKKK00Od:;,':c:'.....':ONNNNNWWWWWWWWWWWW
WWWWWWWWXo;;cdxdxxd:.          .:lllllllccccccccclloolllllloolcllcccccccc::;;;;;;,,,;;;:cloddxkkxxxdddoolcc:;;;,,,,;;;;;;;;;:;;::ccclllooddddddxddddxxxkkkO0KXXXKKKKKOo::;;c:,'.....,dKNNNWWWWWWWWWWWWWW
WWWWWWWWO:''',cddddo;.        .'cllllllc::::::cccc:cc:;,''',,;;;;;,'....',;;;:;;;;,,,,;;:cldxkkOOOkxxddolc:;;;,,,,,,;;;;;;,,'....''',,;,;:cloodddddddxxxxkO0KXXXXXKKK0o::;;:,.......:OKXNWWNXXNWWWWWWWWW
WWWWWWWNx;....':lddoc,.       .'cllllolccc:::cc::;,'.....',;:;;;,'.....  ....',,,,,,,,,;;cldxkOOOOOkkkxdlc:;;,,,,,,,;;,'.......'',;:ccccc:;,',;coooddxxxxxkO0XXXXXXXX0d:;;,:,......,lOKNWN0xdkXWWWWWWWWW
WWWWNWWXd,...''',:ool:,..    ..,loooollcccc::c::;'.....'''...                 ..''',,,,,;coxk00KKK00OOxolc::;;,,''''..................';:cll:,..':lodxxxxxxk0KXXNNXXXKxc;,,;,....':dOKXNNkc:co0WWWWWWWWW
WWWWWWWXd,.......';ccc:,..   ..:loooollccccc:::;'...''.......  (   x  )   .    ..'',,;;;;cdkO0XXXXK00Oxdlllcc:;,''............           ..,::;,..';codxddxkO0XXNNNXXKkl:;;;;'.. ;kKK0KKkc;;:ckXWWWWWWWW
WWWWWWWNd,.......',;;:::;.   .'cooooollcccc::;,..........',,.             ..   ..';;;;:::ldk0KXNNNXK00kxxxdooolc:;'........';'  (   x  )   ..';:;...;lodxxxkO0KXNNNNNXOo:;,;:;,..o00O0Oxl:::::o0WWWWWWWW
WWWWWNWNk;....''.',,,;:::'.  .'coooollllccc:;;'..........',,'.  .        .'...  .':lccccloxO0XNNNNXXK0Okkkkxxkxoc,.......',;:'...         .....,;;'.':oddxxkO0KXNNNNNX0d:;;;;;;;lxkkkxxolccccclONWWWWWWW
WWWWWNWW0c,.....',;,,,,;:,.  .;looooooolllc;,,'''.''''''',;;;,.........',;;;;;;:cllllcllodk0KNWWWNNXXK0OOOkkkkkxdoc::::;;::cc;....       .';'..';;;,,:lodxxkO00KNNNWNNKdc;;::ccoxkxxxxxxocldxolxXWWWWWWW
WWWWWNNWXx:'...';;;;;;,;;;....cooooooooooooc::;;;;;:::ccccccccclllllloollccclooooolclooodxO0XNWWWWNXXXK0OOOOOkxxdddddoolloollollc:;,,,;;:cllloollc::::cldxkO000KXNNNNNKxc:;;:codxxkxdk0Oocldo::dKWWWWWWW
WWWWWNNWW0o:'..,::::::;'..'..,cllllooodddddolllllccccccccllllllcccclllcc:clloodooolloddddkO0XNWMWWNXXXKK00000OkkxollllccllloddddddxxxxxkxxxxxxkOkxxxddddxkOO00KXXNNNNWXxl:;;:ldxxkOOkO0Oo:cl:,;xKNWWNWWN
WWWWWNNNNN0l;'':ccc:;,... ...,clllloddxxxxddoooooooollllcllccccccc:::cclooddddooooodxxddxkO0XNWWWNXXXXKKKKKKK0Okxdoooolc:::clodddddxxxxxxkkkkOOOOOOO000000KKKXXXNNNNNNNkc,;:codxOKXK0000dllc:;cx0NWNNWNN
WWWWWWNNNWNOl::cc::;,.......,:clclllodxxxxxxdddddddoooollllccccccllloddddddoooodddxxxxxdxkO0XNWWWNNXXKKKKKKKKK00Okxxddoollc:;;;:cclooddxxxxxxxxkO00KXXXXXXXXXXXXXXNNXNNOc,:loddok0XXK000koc;;;cd0NWWWNNN
WWWWWWWNNNWNOlc::;,,.......';cllllllodxxxxxxdddddddddddoodddoooooddddddoolllodxxkkxdddddxkOKXWWWWWNXXKKKKKKKKKKK00OOkkxdddddolc:;;,,;;;:::cldxkO0KKKXXNNNNNNNNNXXXXXXXN0dcoddd:';ldkOOO00o;;,;cdKWWWWWNW
WWWWWWWWWWNWNkc::;,'...'''',:ccllllloddddxxxxxxxkxxddxxxxxkkdddddddooooollodxkxxxxxdddodxkOKNWWWWWWNXXKKXXKKKKKKKKKKK0OkxxxxxxxxxddoolllodkkO00KXXNXXXNNWNNNNNNNXXXXXXKKOkxoo:...':codxk0Ol;:co0WWWWWNWW
WWWWWWWWWWWWWKdcc:,''',,,,;clccccllloddddxxkkkkkkOOkkkkxdddxdddxxxxxxxxxxxkkOkkxxxdxddodxkOKNWWNNNNNNXXKKKKKKKKKKKKXXXK00OkkkkkkkkkkOOOOO0000KKXXXXXNNNNWNNNNNNNXXXXKKK0KKOoc'...',;cldk0Kdcod0NWWWWWNWW
WWWWWWWWWWWWWXxloc:;;;:c::cllccllllloodxxkkkkOkkOOOOOO00OOOOkkkOOOOOOOOOOOOOOkxxxddddooddxk0NWWNNNNNNNXKKKKKKKKKKKXXXXXXXXKK0000000000000000KKKKKKKKXXXXNNNXXXXXXXKKKKK0KX0o:,,,''',;cldk0kdk0NWWWWWWWWW
WWWWWWWWWWWWWNkodoc:;:lolclol::clllllodxxxxkkkOO0000KKKKKKKKKKKKK00KK00OOOOOkxxdddddoododxk0XWWNNWWWNNXXXXXXKKKKKXXXXXXXXXNXXXXKKKXXXXXKKKKKXKKKKXXKKKKKXXNNXXXXXKKK000O0NXxcc::;,,,,;coxOOO0NWWWWWWWWWW
WWWWWWWWWWWWWWKxxxoc:cloolodo::ccccllodxxxxxkkkOO00KKKKKKKKKKKXXKKKKKK00OOkkxxxxdooooooooxk0XNWWNWWNNNXXXXXXXXKKKXXXXXXXXXXNNNNNNNNNNNNNNNNNNNXXXXXXXXXXXXXNXKXKKKKK000O0XN0dddolc:;;:coxkO0XWWWWWWWWWWW
WWWWWWWWWWWWWWNkddddllloooodoc:cccllloodxkkkkOOOO0000KKKKXXXXXXXXKK0KK00OOkxxxxddooooooloxk0KNWWWWWNNNXXXXXXXXXKKXXXXXXXXXXXNNNNNNNNNWWNNWWWWWWNNNXXXXXXXXXXXKKKKKKK00OOKXNKkkkkdlc::coxOOkKWWWWWWWWWWWW
WWWWWWWWWWWWWWWOlodddoddooodoc:cccllloodxkkkOOOO0000KKKXXXXXXXXXKKKKKK00OOkxxxddddoooollodxO0XNNNNWNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNWWWNNWWWWWWWWWWWNNNNXXXXKKKKK00K0OkOKXNX0OOOkdlcloxOK00NWWWWWWWWWWWW
WWWWWWWWWWWWWWMKoc:codxkdooolcccclllooddxkkkOOOOO0000KKKKXXXXXXXKKKKK000OOkkxdoooooloolloddk0XNNNWWWWWNNNXXXXKKKXXXXXXXXXXXXXXXXXXNNNNNNNNWWWWWWWWMMWWWNNXXXKKKK0O000OOOKNNXK000kdlloxOXKOKWWWWWWWWWWWWW
WWWWWWWWWWWWWWWNOoc;;oxxxxdol:cclllloodxxxkkkOOO000000KKKKKKXXKKKKKK0000Okkxdoollllloooddxxk0XWWWWWWWWWNNXK00000KKKXXKKKKKXXXXXXXXXNNNNNNNWWWWWWWWWWWWWWNNXXK00000K00OO0KNXXKK00kdooxOKX00XWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWKxdoclddddolc:cclllloddxxxxkkkOO000000000KKKKKKKKKK0000OkkxxollcccllodxxkkkkOKNNNWWWWWWWNNXK0OOOkO0000KKKKKXXXXXXXNNNNNNNNNNNWWWWNWWWWWWWNNXKKK000KK0OO0KXXK0000Okkk000kkKWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWNOxxdddddolcccccclllodddxxxxkkkOOOO000000000000000000OOOkkxdollllloddkkkkOOOOKXXNNWWWWWWWWNXKK00OOOOOO0000KKKXXXXXXXNNXXNNNNNNNNNNNNWNNNNNXXKKK000000OO00K0O0KXNNX0kxddk0XWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWXOxxxddddollcccccloooodddxxkkkkkkOOOO000OO00O000OOOOOkkkxddooddxxxxxkkOOOOO0KXNNNNWWWWWWWNNXXXXK0OkkOOOO0000KKKKKKXXXXXXXXXXXXNNNNNNNNNNNXXKKK00000000OOKXXXXNWNKkoldO0KNWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWNKkdkkxxxddoccccllloooodddxxkkkkkkOOOOOOOOOOOOOOOOkkkkxxdddddxkkxxxkkkOOO0KXNNNXXNNNNNNNNXXXNNNXK0OkkkkkOOOOOO0000KKKKKXXXKKXXXXXXXXXXXXXXKKKK00000000OO0XXXKKNXOddk0KKNWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWW0xdxxxxxdol:cclllllooooddxxxkkkkkkkkkkOkkxkkkkkkkkkxxddddxxkkxxddxxkOO00KXXXXXXXXNXXXXXKXXNNWNXK0kxxxxxxxkkkkkOOO00KKKKKKKKKKXKKKKKKXKKKKKKK0000O00OOOOO00KKXX00KXXXNWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWN0ddddddolccccccllllolooooodxxxxxxxkkkkkxxxxxkkxxxxdddoodddddddooodxkkOO000000KKKKK0000KKXXNNNNX0kdddddddddxxxkkkkkOO0000000KKKKKKKKKK0000K0O000000OOOO00KKXXNNNNXXNWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWN0dllllc::ccccccclllclllllodddxdddxxxxxxxxdddddoooooooollccllllllooddddddxxxkkkkkkkkkOOO00000K0OkxdddddddddddxxxxxdxOO0000000000000000OO000000000OO0KXXXXXXNNWNXXNWWWWWWWWWWWWNNWWWW
WWWWWWWWWWWWWWWWWWNNWWXOdlc;,;:ccccc:cccccllooooooooddooddddddollllllloodool:,,'',;;::::ccccccloooodddddddddddddddxxxxxxxddoooooddxxxxxxkkkOOOOOOOOOOOO0OOOO00000000OkOKXNNNNXNNNNXXNWWWWWWWWWWWNNNNWWWW
WWWWWWWWWWWWWWWWWWWNNWWWNX0kkxc:cccc:::ccccllolllooooooollllllcccccclloodddl:'.......'''',,,,,;::::ccc::;;,'...';coxkkxxxdollllllooodddxxxxkkkkkkkkkOOOOOkkkOO000K00xdk0KXXXXXKKKKXNWWNWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWNNWWWWWWWWWWKl:ccc:::::::cclllllllllllllccc::::::ccloooooolc,.............'''',;;;;;,'.......';codkkkkkxdolccccccclloodddxxxxxxxxxxkxxkkkkkkO00000OocdkOOO00OkOKXNWWNNNNNNNNNWNWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWKl:cc:::::;::cccccllllllllc:;;;;;;;;:cclooooollc;,'................'''''..',;;;:cloddxkkOkkkxdolc::;;;:clloodddooddddxxxddxxxxkkkO0000KxlclodddxkOXNNNNNNNNNNNNNNNNWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWNWKo::::::::;::ccccllllllcc::;,,,,;;::cclllllllcc:;,''...................'',;;::ccllooddxkkkkkxdoolc:;;;;;:clloolllodoodxxdddddxkkkO0000XWXOxxxkOKNNNNNNNNNNNNNNNNNWWWWWWWWWW
NNWWWWWWWWWWWWWWWWWWWWWWWWWNWXo:::::::::::cclllllllc:;;,',,;;:ccccclccccccc::;,,'''.................'';;;:ccllllooddxkkkkxdoolc:;;,,,;::ccloooddoodddxxddddxkkO00OKNWWWWWWWWNNNNNNNNNNNNNNNNNNWWWWWWWWWW
NNNNNWWWWWWWWWWWWWWWWWWWWWWWWXd:;::::;;:::clllllllcc:;,,;;;::ccccccllcccc:::::;;;,,,,,'''''....''.''',;:;;cclllllodddxxxxddooolc:;,',,;;:ccloodddddxxxxddddxxkOOO0XWWWWWWWNNNNNNNNNNNNNNNNNNNNWWWWWWWWWW
NNNNNNWWNWWWWWWWWWWWWWWWWNWWNNk:;:::::;;::cllcllllccc;;::;;;;::ccclllllllccccc:c::;;;;;,,,,,'',,,,,;;;:ccclcclllooodddxxxxdddoolc:;,'',;;:cllooddddxxxxddddxxkO00KNWWWWWWWNNNNNNNNNNNNNNNNNNNNWWWWWWWWWW
NNNNNWWWWWWWWWWWWWWWWWWWNNWWWWOc;::::::;;::cclllllllc::;'',,;;:ccllllllcllccccccccc::::;;;:;;;;:::::::cclolcccloooooodddddddoolllcc:;'';:cllooddddxkxxxddddxkkkO0KNWWWWWNNNNNNNNNNNNNNNNWWWWWWWWWWWWWWWW
NNWWWWWWWWWWWWWWWWWWWWWNWWNWWWKl;:::::;:::::cllooooollc:,',;;;;;;;;:::::;:::::::;;;;;,,,;;:;;;::::cccccclllllloooooooodddoooollc::;:;,,;:clooodddxkkkxxddddkOkkk0XWWWWWWNNNNNNNNNWNNNNNNWWWWWWWWWWWWWWWW
NNWWWWWWWWWWWWWWWWWWWWWWWWWWNWXd;;::::;;;:::ccloooddddoc::ccc::;'...............''''''''''''',,;::;;;;;;;;::::cccccccc::;,,,,,;;;::::::cllodoodddxxxxxddddxkkkkOKNWWWWWWWWWNWWWNNNNNNNNNNNNNWWWWWWWWWWWW
NNWWWWWWWWWWWWWWWWWWWWWWWNWWNWWk;,;:::;;;::::cclooddxxddooolllllllc;'.... ...........'''....',,,,,''',,;;;:::;;,,,'... ....'',::clllooooddddddddddxxxdddddxxkkO0XWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNWWWWWW
NNWWWWWWWWWWWWWWWWWWWWWWWWWWWNWKc,;:::::;:::::ccloddxxxxxddoooddxxddolc:;,,,'............  ................'''....'''';:coddooddddddxxxxxxxdddddddxxxddddxxkkkk0NWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWNWNd,,;:::::::::::ccloddxkkxxddoodxxxkxxddolc::;;;,,;;::::;;,''....''',,,;;;;:cllllllllodxxkkOkkxkxxxxxkkkkxxxddddddxxxxxddxxkkkkOXWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNNWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNW0c,;;::::::::::cclodxxxxddxxooodxxxkkkxxddollc:;,;;;::ccllloooloooooooooooooooddxxxkkOOOO000OOkxxxkkkkkkxxxddddddxxxxddxxxxkkkKNWWWWWWWWWWWWWWNNNNNWNNNNNNNNNNNNNNNNWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNWNx;,;;;;:::::;:cccloddxxxxxxdoooddxkkkkxxxxddoocc::::::::cclllllllollooddddxxkkkkOOO00000000OOkxxkkkkkkkkxddddddddxdddddxxxxk0NWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNNWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWO;',;;::::::;::cccloodxxxkkxdoooddddddxxxxxxxdddoooolllccclllloooodddxkkOOOOO00O0000000000OOOkkkkkkkkkxxxddddodddddddddxxxdkXWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNNWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW0:,,,;;::cc::::::cccloddxxxkkxddooddddddddddddddddddddooloooooodddxxxkkkOOOOO000000000000OOOkkkOkkkxxxxdddddddddddddddddxxx0NWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNNNWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW0c,,,,,;::::::;:::ccllodddxkkkxxddoddddoooooooooooooooooooolllooooooddddxxxkkOOOO000000OOOOOOOOOkkxddddddooddddddoddddddxxOXWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNNWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKl;;,,,;;:::::;::::cclooddxxkkkkxdoooooooolllllllllccccclllllllllcllllooooddxkkkOOOOO0OOO00000OOkkxddddooooodddddoddddddxx0NWWWWWWWWWWWWWWWWWNNNNWWWWWWWNWWWWWWWWWWWWWW
WWNNNWWWWWWWWWWWWWWWWWWWNWWWWNNWWKo;;,',;;:::::::::::cllooddxxxkkkxdddoolllllllccccc:::::::::ccccccccccclloddxxkkkOOOOO000000000OkkxxdoolcloodddooodddddxxkKWWWWWWWWWWWWWWWWWWWNWWWWWWWWWWWWWWWWWWWWWWWW
WWNNNNWWWWWWWWWWWWWWWWWWWWWWWWNWWXo;:;,,,;;;;;::::;;::cloodddxxxxxxxxddoolllllccccc::;;;::;;;::::ccccccccloodxxxkkkOOOO00000000OOkkxddoollodddddoooodddxxk0XWWWWWWWWWWWWWWWWWWWNWWWWWWWWWWWWWWWWWWWWWWWW
WWNNNNWWWWWWWNNWWWWWWWWWWWWWWWWWWXd::;,,',,;;;;:::::::cllooddddxxxxxxxddooollllccc::;;;;;;,,,;;;:::cccccclooddxxkkkOOO00000000OOOOkxxddddddddddooooodddxkkKNWWWWWWWWWWWWWWWWWWWNWWWWWWWWWWWWWWWWWWWWWWWW
WWNNNNWWWWWWWNNNNNNNNNWWWWWWWWWWNKo::;;,'',,;;;;::::::ccllolooddxxxxxxxxdddoollllcc::::;;;;;;;;;::cccccllodddxxkkkOOO000000OOOOOOkkkxxxxxxdddddddooodxkkkOXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWNNNNNNNWWWWWWNNNNNNWWWWWWWWWWWNOl::;;;'''''',;;;;;;:::cclcloodddxxxxxxxxxddddoolcccc:::::::::::cllllloddxxxxkkOOO000000OOOOOOkkkkkxxxxxdddddddoooddxOOOKNWWWWWWWWWWWWWWWWWWWWWWNNWWWWWWWWWWWWWWWWWWWWW
NNNNNNNNNWWWWNNNNNNNWWWWWWWWWWWWWKo:::;;,''.'',,,,;;;;;;:ccclooooooddxxxxxxxxxxdodddooooolllllloooddddddxxxxxkkkO00000OOOOOOOOkkkkkkxxdxddooddooooodkkOkOXWWWWWWWWWWWWWWWWWWWNNNNNNNWWWWWNNWWWWWWWWWWWWW
NNNNNNNNNWWWWWNNWNNNNWWWWWWWWNNWMNkc::;;;,'..'''',,,;;;;;::ccloooodddxxxkkkkkkxxxxxxxdddddddddddxxxxxkkkkkkkOOOO00OOOOOOOOOOkkkxxxxxxxddddoooooooodkkOOk0NWWWWWWWWWWWWWWWWWWWWWWNNNWWWWWWWWWWWWWWWWWWWWW
NNNNNNNNNNNWWWWWWWWWWWWWWWNWWNNWMMXxc;;;,,''....''',,,,,,,;;::clloddddxxxkkkkkkkkkkxxxxxxxxxxxxkkkkOOOOOOOO0000000000OOOOkkkkxxxxxxddddoooolooooodkOOOkOKWWWWWWWWWWWWWWWWWWWWWWWNNNWWWWWWWWWWWWWWWWWWWWW
NNNNNNNNNNWWWWWWWWWWWWWWWWWWWNNNWMMXd:;;;,,,'....''''',,,,,,;;:clodddddxxkkkkkkkkkkkkkkkkkkkOOOOOOOO0OO00000K0000000OOOOOkkxxxxxddddddoooolloodddxkOOOk0NWWWWWWWWWWWWWWWWWWWWWWWWNWWWWWWWWWWWWWWWWWWWWWW
NNNNNNNNNNWWWWWWWWWWWWWWWWWWWWWWWMMWXd:;;;,,,'......'''''',,,;;:cloooooddxkkkkkkkkkkkOOkkkkkkOOOOO0000000000000000OOOkkkkkxdddddddoooolllolloddxkkkOOkOXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
NNNNNNNNNWWWWWWWWWWWWWWWWWWMMMMWWWWMMXx:;;;,,,'........''''''',;;:ccllloodxkkkkkkkkOOOOOOkkkkkOO00000000000000OkOOkkkkkkxxxddoooooooolllloooddxxkOOOkk0NWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
NNNNNNNNWWWWWWWWWWWWWWWWNWWMMMMMMWWWMMXx:,,,,,''.........''''''',;;:cclloodxxxxkkkkkkkkOOkkkkkOOOOOOOOOOO00OOOkkkkkxxxxddddoooolooloollloooddxxkOOOOOOXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
NNNNNNNWWWWWWWWWX0kddolkXWWMMMMMMMMWWWMNOc,,,,,''.............''',,;::clllloodxxkkxkxxkkkkxxxxxkkkxxxxkOOOkkkxxxxxxxdddooollllllllloooooooddxxkkOOOkk0NWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
NNNNWWWWWWWNWNOl'.    ,OWWWWMMMMMMMMWWMMWKo;;,,,''......  .......''',;:::::cccodxxxxxxxxxxddddddddddddxxxxdddoooooooooooollllcllclloooooodxxxkkkkkOkOXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
NWWNNWWWWWWNKl.      ,OWMMMMMMMMMMMMWWWWWWNkl;,,'''.......  ....''.''',,;;;;;::cllooooodddooooooooooolllllllllcccccllclllcccccllllllllloodxxxkOOOOOO0NWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWXd'       'OWMMMMMMMMMMMMMMMMWWWWNKd:,''''........   ........''',,,,,,;:::cccccccccccccccccc:::::::::::::::cccccccclllllllooooodxxxkkOOOO0XNWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWN0c.        ;KWWMMMMMMMMMMMMMMMMWWWWNXOo;''''.........   ...'......''''',,,,;;;;::::::;;;::::::;;;;;;;;;;;;;;::::cclcccllcllloooddxxxkkOOOOKNNNWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWNXd.          .oNMMMMMMMMMMMMMMMMMMWWWNNXKkc,''''........     ...''....''''''',,,,,;;;;;,,,,;;;;;;;;,,,;;,,;;;;;;::ccclccccclllooddxxkkOOkOO0XWNNWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWN0:.            .dNMMMMMMMMMMMMMMMMMMWWWNNNX0xc,''''.......      ...''''''''''''''''',,,,,',,,,,,,,,,,'''',,,,;;;;;::::c:::ccllloodxkkkOOOOOOKWWWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWXd.               .xNMMMMMMMMMMMMMMMMMMWWWNNNXXKkl;''''.......       ...''''','''''''''''''''''''''''''''',,,,;;;;;;;;:::::ccllooddxkOOOkOOOO0XWWWNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWW0:                  .dNMMMMMMMMMMMMMMMMMMMWWWNNNXX0kl;,''........        ....'',,'''',,''''''''''''''''''',,,,,,,,,,;;;;:::ccclodxxkOOOOOOOOOOKNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WKo.                    .oXMMMMMMMMMMMMMMMMMMMWWWNNNXXXKko:,'..........        .......''',,,,,,,,,,,,'''''',,,'',,,,,,,,,;;;::cclodxkOOOOOOOOOOO0XWNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
x'                       .cXMMMMMMMMMMMMMMMMMMMWWWNNNNXXK0ko:,''........         .................''''''''''''...'''',,,,,,;;:clodxkkO000OOOOOO0KNWNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                           :0WMMMMMMMMMMMMMMMMMMWWWWNNXXXKK0kdc,...........        .................................'',,,,;:cclodxkkOO00OOOO0000XWWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                            :XMMMMMMMMMMMMMMMMMMMWWWWNNXXXXKK0kl,..'........          ............................'',,;;;:cclodddxkO0000OOOO000KNWNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
动态网自由门 天安門 天安门 法輪功 李洪志 Free Tibet 六四天安門事件 The Tiananmen Square protests of 1989 天安門大屠殺 The Tiananmen Square Massacre 反右派鬥爭 The Anti-Rightist Struggle 大躍進政策 The Great Leap Forward 文化大革命 The Great Proletarian Cultural Revolution 人權 Human Rights 民運 Democratization 自由 Freedom 獨立 Independence 多黨制 Multi-party system 台灣 臺灣 Taiwan Formosa 中華民國 Republic of China 西藏 土伯特 唐古特 Tibet 達賴喇嘛 Dalai Lama 法輪功 Falun Dafa 新疆維吾爾自治區 The Xinjiang Uyghur Autonomous Region 諾貝爾和平獎 Nobel Peace Prize 劉暁波 Liu Xiaobo 民主 言論 思想 反共 反革命 抗議 運動 騷亂 暴亂 騷擾 擾亂 抗暴 平反 維權 示威游行 李洪志 法輪大法 大法弟子 強制斷種 強制堕胎 民族淨化 人體實驗 肅清 胡耀邦 趙紫陽 魏京生 王丹 還政於民 和平演變 激流中國 北京之春 大紀元時報 九評論共産黨 獨裁 專制 壓制 統一 監視 鎮壓 迫害 侵略 掠奪 破壞 拷問 屠殺 活摘器官 誘拐 買賣人口 遊進 走私 毒品 賣淫 春畫 賭博 六合彩 天安門 天安门 法輪功 李洪志 Winnie the Pooh 劉曉波动态网自由门
动态网自由门 天安門 天安门 法輪功 李洪志 Free Tibet 六四天安門事件 The Tiananmen Square protests of 1989 天安門大屠殺 The Tiananmen Square Massacre 反右派鬥爭 The Anti-Rightist Struggle 大躍進政策 The Great Leap Forward 文化大革命 The Great Proletarian Cultural Revolution 人權 Human Rights 民運 Democratization 自由 Freedom 獨立 Independence 多黨制 Multi-party system 台灣 臺灣 Taiwan Formosa 中華民國 Republic of China 西藏 土伯特 唐古特 Tibet 達賴喇嘛 Dalai Lama 法輪功 Falun Dafa 新疆維吾爾自治區 The Xinjiang Uyghur Autonomous Region 諾貝爾和平獎 Nobel Peace Prize 劉暁波 Liu Xiaobo 民主 言論 思想 反共 反革命 抗議 運動 騷亂 暴亂 騷擾 擾亂 抗暴 平反 維權 示威游行 李洪志 法輪大法 大法弟子 強制斷種 強制堕胎 民族淨化 人體實驗 肅清 胡耀邦 趙紫陽 魏京生 王丹 還政於民 和平演變 激流中國 北京之春 大紀元時報 九評論共産黨 獨裁 專制 壓制 統一 監視 鎮壓 迫害 侵略 掠奪 破壞 拷問 屠殺 活摘器官 誘拐 買賣人口 遊進 走私 毒品 賣淫 春畫 賭博 六合彩 天安門 天安门 法輪功 李洪志 Winnie the Pooh 劉曉波动态网自由门
动态网自由门 天安門 天安门 法輪功 李洪志 Free Tibet 六四天安門事件 The Tiananmen Square protests of 1989 天安門大屠殺 The Tiananmen Square Massacre 反右派鬥爭 The Anti-Rightist Struggle 大躍進政策 The Great Leap Forward 文化大革命 The Great Proletarian Cultural Revolution 人權 Human Rights 民運 Democratization 自由 Freedom 獨立 Independence 多黨制 Multi-party system 台灣 臺灣 Taiwan Formosa 中華民國 Republic of China 西藏 土伯特 唐古特 Tibet 達賴喇嘛 Dalai Lama 法輪功 Falun Dafa 新疆維吾爾自治區 The Xinjiang Uyghur Autonomous Region 諾貝爾和平獎 Nobel Peace Prize 劉暁波 Liu Xiaobo 民主 言論 思想 反共 反革命 抗議 運動 騷亂 暴亂 騷擾 擾亂 抗暴 平反 維權 示威游行 李洪志 法輪大法 大法弟子 強制斷種 強制堕胎 民族淨化 人體實驗 肅清 胡耀邦 趙紫陽 魏京生 王丹 還政於民 和平演變 激流中國 北京之春 大紀元時報 九評論共産黨 獨裁 專制 壓制 統一 監視 鎮壓 迫害 侵略 掠奪 破壞 拷問 屠殺 活摘器官 誘拐 買賣人口 遊進 走私 毒品 賣淫 春畫 賭博 六合彩 天安門 天安门 法輪功 李洪志 Winnie the Pooh 劉曉波动态网自由门             
"""

# hexdump to number list
def hex2b(inp):
    return list(map(lambda v: int(v,16), re.findall("[a-fA-F0-9]{2}", inp)))

# zuc: https://github.com/Arkq/SM2349/blob/master/src/ZUC.h
# one of ~6 xorkey derived by ZUC decrypting a static 16 byte constant with a static 16byte key
# the use of this as an xorkey is entirely tencent fucking with unity and not part of original ZUC
zuc_block_txt = """
52 a1 3e 4d a2 1b dd d1 1a dc 6c 04 df e3 c6 f4
ae 29 be 34 e9 e0 72 63 e2 d6 56 5a 78 76 8c 5c
e6 8f ad 74 5e 15 80 58 c2 7e f3 44 d5 9b e9 b5
80 12 b6 26 9b 77 16 1e b6 e2 7a da 7c aa 91 8c
"""
zuc_block = hex2b(zuc_block_txt)

zuc_key0 = zuc_block
zuc_key1 = hex2b("""
db c7 67 26 ed 04 33 50 37 14 b7 12 e4 3f 1c 19
38 e1 ed 7c b1 95 c3 0e 8a 48 58 b4 85 ff fd 40
15 22 39 28 0e 47 a7 4c db 84 3a 51 d5 7a e5 6b
96 46 98 f8 13 85 f4 f0 09 f6 34 90 a1 78 fe e2
""")
zuc_key2 = hex2b("""
bb 8f 0d db 0e 06 2c da c4 c4 78 00 e2 e5 20 c2
5a 1d 71 07 a1 63 03 9c b1 18 b0 20 e4 9e 8b 0e
5d 2f a4 52 64 0c 6a 9f b8 13 a4 1a b4 b3 85 52
96 d5 48 2a 24 1e 4e 2d e6 e9 d8 80 ee 65 35 22
""")


# a thisobject passed to most of the custom zuc shit
zuc_instance = {
    "b": zuc_block, # b.ytes of the key
    "idx": 0 # rolling index for decryption, incremented per op
}

# zuc_instance gets reset like 3 times per file
def new_zuc(key):
    return {"b": key, "idx": 0}


def bytes_int(b):
    i = 0
    result = 0
    for c in b:
        result = result | (c << i*8)
        i += 1
    return result

# decrypt a single 32bit immediate value
def zuc_xor(zuc_ins, num):
    """
  __int64 blob_first_qword; // x8
  unsigned __int32 v3; // w9

  blob_first_qword = *(_QWORD *)ZUC_blob;
  if ( *(_QWORD *)ZUC_blob )
  {
    v3 = ZUC_blob[2];
    if ( v3 >= 0x10 )
    {
      v3 = ZUC_blob[2] & 0xF;
      ZUC_blob[2] = v3;
    }
    ZUC_blob[2] = v3 + 1;
    a2 ^= *(_DWORD *)(blob_first_qword + 4LL * v3);
  }
  return a2;
    """
    if type(num) is bytearray:
        num = struct.unpack(">I",num)[0]

    dw = zuc_ins["idx"]
    if dw >= 0x10:
        dw = dw & 0xF
        zuc_ins["idx"] = dw
    zuc_ins["idx"] = dw+1
    lower = 4*dw
    num = num ^ bytes_int(zuc_ins["b"][lower:lower+4])
    return num

# decrypt an arbitrary block
def zuc_blockxor(zuc_ins, inp, size):
    """
zuckey *__fastcall sub_8EE67C(zuckey *result, char *a2, unsigned int a3, _BYTE *a4, unsigned int a5)
{
  char *data; // x9
  unsigned int v6; // w8
  __int64 v7; // x10
  char v8; // t1
  unsigned int v9; // w8
  int v10; // w8

  if ( a5 >= a3 ) { if ( a2 ) { if ( a3 ) { if ( a4 ) { if ( a5 ) {
    data = result->data;
    if ( result->data )
    {
        v6 = 4 * result->idxlol;
        if ( a3 )
        {
        v7 = a3;
        do
        {
            v8 = *a2++;
            --v7;
            *a4++ = data[v6] ^ v8;
            if ( v6 + 1 <= 0x3F )
            ++v6;
            else
            v6 = (v6 + 1) & 0x3F;
        }
        while ( v7 );
        }
        if ( v6 & 3 )
            v9 = (v6 >> 2) + 1;
        else
        v9 = v6 >> 2;
        if ( v9 <= 0xE )
            v10 = v9 + 1;
        else
            v10 = (v9 + 1) & 0xF;
        result->idxlol = v10;
}}}}}}
  return result;
}
"""
    key_off = 4*zuc_ins["idx"]
    key_off_orig = key_off
    inp_off = 0
    result = size
    if size > 0:
        while result > 0:
            key_byte = zuc_ins["b"][key_off]
            key_off = (key_off + 1) & 0x3F # really just modulo but this is a transliteration not translation
            inp[inp_off] = inp[inp_off] ^ key_byte
            inp_off = inp_off + 1
            result -= 1
    idx_update = 0
    if key_off & 3:
        idx_update = (key_off >> 2) + 1
    else:
        idx_update = key_off >> 2
    if idx_update <= 0xE:
        zuc_ins["idx"] = idx_update+1
    else:
        zuc_ins["idx"] = (idx_update+1) & 0xF
    return inp[0:0+size]

# only used for one part of header
def zuc_xoruint64(zuc_ins, num):
    """
  v2 = zuc_ins->data;
  if ( zuc_ins->data )
  {
    v3 = zuc_ins->idxlol;
    if ( v3 >= 0x10 )
    {
      v3 = zuc_ins->idxlol & 0xF;
      zuc_ins->idxlol = v3;
    }
    v4 = v3 + 1;
    zuc_ins->idxlol = v3 + 1;
    v5 = (unsigned __int64)*(unsigned int *)&v2[4 * v3] << 32;
    if ( v4 >= 0x10 )
    {
      v4 &= 0xFu;
      zuc_ins->idxlol = v4;
    }
    zuc_ins->idxlol = v4 + 1;
    num ^= v5 | *(unsigned int *)&v2[4 * v4];
  }
  return num;
}
    """
    if type(num) is bytearray:
        num = struct.unpack(">Q",num)[0]

    idx = zuc_ins["idx"]
    if idx >= 0x10:
        idx = idx & 0xF
        zuc_ins["idx"] = idx
    lower = idx*4
    top_32bits = bytes_int(zuc_ins["b"][lower:lower+4]) << 32
    idx = idx + 1
    if idx >= 0x10:
        idx = idx & 0xF
        zuc_ins["idx"] = idx
    zuc_ins["idx"] = idx + 1
    lower = idx*4
    num = num ^ (top_32bits | bytes_int(zuc_ins["b"][lower:lower+4]))
    return num

def zuc_xorshort(zuc_ins, num):
    """
__int64 __fastcall xor_short(zuckey *a1, unsigned int a2)
{
  char *v2; // x8
  unsigned int v3; // w9

  v2 = a1->data;
  if ( a1->data )
  {
    v3 = a1->idxlol;
    if ( v3 >= 0x10 )
    {
      v3 = a1->idxlol & 0xF;
      a1->idxlol = v3;
    }
    a1->idxlol = v3 + 1;
    a2 = *(_DWORD *)&v2[4 * v3] ^ (unsigned __int16)a2;
  }
  return a2;
    """
    if type(num) is bytearray:
        num = struct.unpack(">H",num)[0]

    idx = zuc_ins["idx"]
    if idx >= 0x10:
        idx = idx & 0xF
        zuc_ins["idx"] = idx
    zuc_ins["idx"] = idx + 1
    lower = idx*4
    num = bytes_int(zuc_ins["b"][lower:lower+4]) ^ num
    return num


#### tests
# empirically collected
tmp_ins = {
    "b": zuc_block,
    "idx": 2
}
test0 = (
    zuc_xor(tmp_ins, 0x46cdc1c) == 6
    and tmp_ins["idx"] == 3
)
if not test0:
    print("!!! hey idiot broke zuc_xor")
    print(tmp_ins)
    IPython.embed()

tmp_ins = {
    "b": zuc_block,
    "idx": 8
}
tmp_inp = hex2b("""
d4 bf 9c 4c 70 21 ae 69 f4 18 c2 3c ad e3 91 cd
""")
test1 = (
    zuc_blockxor(tmp_ins, tmp_inp, 16) 
    and bytes(tmp_inp) == b'2018.4.16f1xxxxx'
    and tmp_ins["idx"] == 0xD
)
if not test1:
    print("!!! hey idiot broke zuc_blockxor, note tmp_inp modified in-place by call")
    print(tmp_ins)
    IPython.embed()

tmp_ins = {
    "b": zuc_block,
    "idx": 0
}
test2 = (
    zuc_xoruint64(tmp_ins, 0x4d3ea152d1df4903) == 0x252a1
    and tmp_ins["idx"] == 2
)
if not test2:
    print("!!! hey idiot broke zuc_xoruint64")
    print(tmp_ins)
    IPython.embed()

# 76b51938555a8a6a0c1694f902cdaf75.bytes
# [5byte magic] - not read!
# [8 byte uint64 size? - 0x252a1] (full file size)
# [4 byte xor - 6]
# [8 byte blockxor - b'1.0.1000']
# [4 byte xor - 0x86]                                                               / 0x5e
# [4 byte xor - 0x40]
# [16 byte blockxor b'2018.4.16f1xxxxx'] - offset 0x21
# [4 byte xor - 0x86] -                 0x31                                        / 0x5e / 0xEF
# ZUC_DEC new key - db c7
# [4 byte xor - 0x5] -                  0x35                                        / 0x01 <--- number of entries
# [16 byte blockxor - null] -           0x39 - creepy, this matches new_key[4:]     
# [2 byte NO XOR - 48 89]
# [4 byte xor - 0x9be3]                                                             / 0x2d79
# [4 byte xor - 0x20000]                                                            / 0x886f
# [2 byte NONE - 47 0d]                                                             / skipped from here
# [4 byte xor - 0x8245]
# [4 byte xor - 0x20000]
# [2 byte NONE - 46 95]
# [4 byte xor - 0x874b]
# [4 byte xor - 0x20000]
# [2 byte none - 78 a2]
# [4 byte xor - 0xa356]
# [4 byte xor - 0x20000]
# [2 byte none - 14 34]
# [4 byte xor - 0x91d]
# [4 byte xor - 0x1c90]
# ZUC_DEC new key - bb 8f 0d...
# [4 byte xor - 0x1]                                                                / 0x01
# [8 byte uint64 - 0x81c90]                                                         / 0x886f
# [4 byte xor - 0x4]                                                                / 0x04
# [4 byte xor - 0x24]                                                               / 0x24
# [0x24 byte blockxor - the filename! - CAB-7942a9318242933bce22a3191daefa76]
# [8 byte uint64 - 0]
# done!

def parse_file(parseme):
    print(f"parsing {parseme}")
    zuc_ins = new_zuc(zuc_key0)
    idx = 0
    with open(parseme, "rb") as f:
        data = bytearray(f.read())
    
    magic = data[idx:idx+5]
    idx += 5
    filesz = zuc_xoruint64(zuc_ins, data[idx:idx+8])
    idx += 8
    usually_six = zuc_xor(zuc_ins, data[idx:idx+4])
    idx += 4
    tencent_ver = zuc_blockxor(zuc_ins, data[idx:idx+8], 8)
    idx += 8
    unk0 = zuc_xor(zuc_ins, data[idx:idx+4]) # seen 0x86, 0x5e - compressed/raw datatable size
    idx += 4
    flags = zuc_xor(zuc_ins, data[idx:idx+4]) # seen 0x40 formerly unk1
    idx += 4
    unity_ver = zuc_blockxor(zuc_ins, data[idx:idx+16], 16)
    idx += 16
    unk0_copy = zuc_xor(zuc_ins, data[idx:idx+4]) # uncompressed datatable size
    idx += 4

    print(f"{magic=}\n{filesz=:08X}\n{usually_six=:X}\n{tencent_ver=}\n{unk0=:X}\n{flags=:X}\n{unity_ver=}\n{unk0_copy=:X}")
    if not (b"FBAU" in magic):
        print("[!!!] magic bytes != FBAU, skipping...")
        return

    ####### large file handling
    # example 059caf18c820a78f87205e66126904e9.bytes
    # compression_mode != 0, then libunity normally reads an extra chunk of size (unk0) (sometimes unk0^0x20) - decompresses
    datatable = None
    datatable_idx = idx
    
    compression_mode = (flags & 0x3F) 
    has_dir_info = (flags & 0x40)
    block_dir_at_end = (flags & 0x80)

    if block_dir_at_end:
        print("[!!!] block_dir at end, skipping...")
        return

    # (Flags & 0x3F) is compression mode. 0 means no compression, 1 means LZMA and 2/3 means LZ4/LZ4HC.
    # (Flags & 0x40) says whether the bundle has directory info.
    # (Flags & 0x80) says whether the block and directory list is at the end of this bundle file.
    newidx = idx+unk0
    print(f"{compression_mode=}, {has_dir_info=}, {block_dir_at_end=} bumping idx from {idx=:04X} to {newidx=:04X}")
    if compression_mode:
        # read chunk 0xCF
        # num_files @ 0x35+2 (so add 2 to idx)

        if compression_mode > 2:
            datatable = bytearray(lz4.block.decompress(bytearray(data[idx:idx+unk0]), uncompressed_size=unk0_copy))
        
        datatable_idx = 0
        pass
        # unk0 > 0x7CF - do some shit
    else:
        datatable = data
    idx = newidx
    #######################

    ########################
    # unityfs datatable reading

    # reading file headers, swap to dbc7 key
    zuc_ins = new_zuc(zuc_key1)

    # determines how many file header entries we need to read
    num_blocks = zuc_xor(zuc_ins, datatable[datatable_idx:datatable_idx+4])
    datatable_idx += 4
    # if this is ever not null.. uhhh...
    big_null = zuc_blockxor(zuc_ins, datatable[datatable_idx:datatable_idx+16], 16)
    datatable_idx += 16
    nulled = big_null == bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    print(f"big_null look good? '{nulled}'")
    block_headers = []

    # we'll read blocks starting after datatable.
    data_raw = []


    print(f"{num_blocks=}\n{big_null=}\nblock table:")
    for header_idx in range(num_blocks):
        block_flag = zuc_xorshort(zuc_ins, datatable[datatable_idx:datatable_idx+2])
        datatable_idx += 2
        block_compressedsz = zuc_xor(zuc_ins, datatable[datatable_idx:datatable_idx+4])
        datatable_idx += 4
        block_decompressedsz = zuc_xor(zuc_ins, datatable[datatable_idx:datatable_idx+4])
        datatable_idx += 4
        block_headers.append( (block_flag, block_compressedsz, block_decompressedsz) )
        block_compression = block_flag & 0x3F
        print(f"({block_flag=:X}, {block_compressedsz=:X}, {block_decompressedsz=:X}) {block_compression=} ")
        
        if block_compression == 1:
            # lzma - not in this game
            print("lzma!!!!!!!??????\n"*5)
            IPython.embed()
            expand = bytearray([0x41]*block_decompressedsz)
            data_raw.append(expand)
            idx += block_compressedsz
            pass
        elif block_compression in [2,3]:
            #lz4/lzhc
            expand = bytearray(lz4.block.decompress(bytearray(data[idx:idx+block_compressedsz]), uncompressed_size=block_decompressedsz))
            data_raw.append(expand)
            idx += block_compressedsz
            pass
        else:
            data_raw.append(bytearray(data[idx:idx+block_compressedsz]))
            idx += block_compressedsz
            pass
            # none
    data_stream = bytearray(b"".join(data_raw))

    # file name "CAB-...." n other bits use key bb8f
    zuc_ins = new_zuc(zuc_key2)

    names_number = zuc_xor(zuc_ins, datatable[datatable_idx:datatable_idx+4])
    datatable_idx += 4
    name_entries = []
    for name_idx in range(names_number):
        file_size = zuc_xoruint64(zuc_ins, datatable[datatable_idx:datatable_idx+8])
        datatable_idx += 8
        file_flags = zuc_xor(zuc_ins, datatable[datatable_idx:datatable_idx+4])
        datatable_idx += 4
        name_len = zuc_xor(zuc_ins, datatable[datatable_idx:datatable_idx+4])
        datatable_idx += 4
        name = zuc_blockxor(zuc_ins, datatable[datatable_idx:datatable_idx+name_len], name_len)
        datatable_idx += name_len
        file_offset = zuc_xoruint64(zuc_ins, datatable[datatable_idx:datatable_idx+8])
        datatable_idx += 8
        print(f"{name_idx=}\n{file_size=:X}\n{file_flags=:X}\n{name_len=:X}\n{name=}\n{file_offset=:X}")
        name_entries.append(
            (file_size, file_flags, name_len, name, file_offset)
        )

        _ = """ yeah so they're pulling this ancient chinese secret here, xorpad SerializedFile header w/ blowfish constants...
  v5 = v21 ^ 0x2FFD72DB;
  v6 = v23 ^ 0x98DFB5AC;
  v21 ^= 0x2FFD72DBu;
  v7 = v24 ^ 0xD1310BA6;
  v23 ^= 0x98DFB5AC;                            // BLOWFISH????????????
  v24 ^= 0xD1310BA6;
  v8 = v20 ^ 0x43;
  LOBYTE(v20) = v20 ^ 0x43;
  BYTE1(v20) ^= 0x4Cu;
  BYTE2(v20) ^= 0x51u;
  HIBYTE(v20) ^= 0x54u;
        """
        cabkey = hex2b("""
        43 4c 51 54 db 72 fd 2f 00 00 00 00 ac b5 df 98 a6 0b 31 d1
        """)
        for i, (a,b) in enumerate(zip(cabkey, data_stream[0:20])):
            data_stream[i] = a^b

        # write a file for this
        outpath = (parseme.parent) / name.decode("utf-8")
        with open(outpath, "wb") as outf:
            outf.write(data_stream[file_offset:file_offset+file_size])
        print(f"Wrote {outpath}")
        # parse it as a SerializedFile

        # uint32_t file[]
        # v5: file[1] ^ 0x2FFD72DB
        # v6: file[3] ^ 0x98DFB5AC
        # v7: file[4] ^ 0xD1310bA6
        # char v8: file[0] ^ 0x43 # first byte onl
        # 0x43, 0x4c, 0x51, 0x54


    #IPython.embed()



if False:
    infolist = ["76b51938555a8a6a0c1694f902cdaf75.bytes","76b51938555a8a6a0c1694f902cdaf75.bytes","89270e59f0e63eb0cf41accb0e6fd84a.bytes","89270e59f0e63eb0cf41accb0e6fd84a.bytes","8512ae7d57b1396273f76fe6ed341a23.bytes","8512ae7d57b1396273f76fe6ed341a23.bytes","02cf5c3198d9714d1f6efdfd2076f70a.bytes","02cf5c3198d9714d1f6efdfd2076f70a.bytes","1aa355706e1767666124331a716c7890.bytes","1aa355706e1767666124331a716c7890.bytes","0b7043fbd23ca788dd796a0498c46e3c.bytes","0b7043fbd23ca788dd796a0498c46e3c.bytes","39a691fd5033f3f9cd98443e17e46b94.bytes","39a691fd5033f3f9cd98443e17e46b94.bytes","8a95a2a3b1b7ecfde12843e20249b016.bytes","8a95a2a3b1b7ecfde12843e20249b016.bytes","d41d8cd98f00b204e9800998ecf8427e.bytes","d41d8cd98f00b204e9800998ecf8427e.bytes","d4e21555f3cc01bc647179fae96b0eb6.bytes","d4e21555f3cc01bc647179fae96b0eb6.bytes","9e843dca12befffe123cb39e14837c5f.bytes","9e843dca12befffe123cb39e14837c5f.bytes","7115ef01f4707fcaaef738f001ab1666.bytes","7115ef01f4707fcaaef738f001ab1666.bytes","88ace7e55bfe1659f48da9aed1e92017.bytes","88ace7e55bfe1659f48da9aed1e92017.bytes","1b63d36f670b7fb1b8ddeece3887c9ac.bytes","1b63d36f670b7fb1b8ddeece3887c9ac.bytes","5836965dab54e3db1c8276e79fc5a4fb.bytes","5836965dab54e3db1c8276e79fc5a4fb.bytes","b5d6176220503c0664f6a0a4624c5ba1.bytes","b5d6176220503c0664f6a0a4624c5ba1.bytes","3e9506996476cf52014a2413f763d5a3.bytes","3e9506996476cf52014a2413f763d5a3.bytes","0589082cd8a9668981d909094215f69a.bytes","0589082cd8a9668981d909094215f69a.bytes","0647e98f5e1c8e9e345fc43a3ffa0383.bytes","0647e98f5e1c8e9e345fc43a3ffa0383.bytes","2719c83c72876c399b7a4cb472f71ac3.bytes","2719c83c72876c399b7a4cb472f71ac3.bytes","27ff5d8f32dd0ddb82eaac1d091bd0f6.bytes","27ff5d8f32dd0ddb82eaac1d091bd0f6.bytes","289bfa6b1322fd82ac0e86b70d55a47a.bytes","289bfa6b1322fd82ac0e86b70d55a47a.bytes","2c6a17dcb948df2147b2f011e9272434.bytes","2c6a17dcb948df2147b2f011e9272434.bytes","39f778cde807067d7ea3b5882e0e0783.bytes","39f778cde807067d7ea3b5882e0e0783.bytes","3a559b926e489ac961294ddee80aa7bf.bytes","3a559b926e489ac961294ddee80aa7bf.bytes","3d002b4e39ce145ea4bfa04c444cc975.bytes","3d002b4e39ce145ea4bfa04c444cc975.bytes","3e7a7dbec3097c0d8570ee1b9e0e13e1.bytes","3e7a7dbec3097c0d8570ee1b9e0e13e1.bytes","3fccb71678b8b4b1a8c3e8cb39187a7e.bytes","3fccb71678b8b4b1a8c3e8cb39187a7e.bytes","496e73155a00619d34c252971845642d.bytes","496e73155a00619d34c252971845642d.bytes","4ec192a76bdbb43f0f8078e68a0f2567.bytes","4ec192a76bdbb43f0f8078e68a0f2567.bytes","4fc71c22a21fead74a5d88762d005460.bytes","4fc71c22a21fead74a5d88762d005460.bytes","5e366439c90a0b0ca76afaadcf6a88d7.bytes","5e366439c90a0b0ca76afaadcf6a88d7.bytes","60a3c1f4375bfff6c81576273d5c8443.bytes","60a3c1f4375bfff6c81576273d5c8443.bytes","62901e9cb8f9d68c36040dffa8e1f9be.bytes","62901e9cb8f9d68c36040dffa8e1f9be.bytes","752ec3fc83c0fe18c87dee4006807966.bytes","752ec3fc83c0fe18c87dee4006807966.bytes","7accc03d6bc9a6730cf1104814c76b0c.bytes","7accc03d6bc9a6730cf1104814c76b0c.bytes","7e9905ddb079bd2347fd03f7cd6a392c.bytes","7e9905ddb079bd2347fd03f7cd6a392c.bytes","84f458ee272ac698d9adcfba65b5434a.bytes","84f458ee272ac698d9adcfba65b5434a.bytes","85b2f162b12f0febd71a9edc4a4b3bcd.bytes","85b2f162b12f0febd71a9edc4a4b3bcd.bytes","8ba9a6248032788506ffb6d490b9b58b.bytes","8ba9a6248032788506ffb6d490b9b58b.bytes","94eeaeda15c7c8dddc0084d9ddb30959.bytes","94eeaeda15c7c8dddc0084d9ddb30959.bytes","970cec8d0dbc31e9fb9c2f3ef70f4944.bytes","970cec8d0dbc31e9fb9c2f3ef70f4944.bytes","9fb6be5dcdf3fb7be9e9b2996e6fbe48.bytes","9fb6be5dcdf3fb7be9e9b2996e6fbe48.bytes","a79a2e427fbe1e813cc64a5a9b24a0f4.bytes","a79a2e427fbe1e813cc64a5a9b24a0f4.bytes","ad9e8b01b66b6adbfc3bebbf0519aeb9.bytes","ad9e8b01b66b6adbfc3bebbf0519aeb9.bytes","b3cce719df1142ce46d8143f0fc049c6.bytes","b3cce719df1142ce46d8143f0fc049c6.bytes","ba624cf9ba39fe17fa542b4a43340ac3.bytes","ba624cf9ba39fe17fa542b4a43340ac3.bytes","cab9745a6c1b54233a63d3db4b42f060.bytes","cab9745a6c1b54233a63d3db4b42f060.bytes","cf1ffb07b374237ece354ee59c5a53fc.bytes","cf1ffb07b374237ece354ee59c5a53fc.bytes","cf79a50784709580a1b32efe20a4c5a3.bytes","cf79a50784709580a1b32efe20a4c5a3.bytes","dc854566d52769fd2362d835f166fb6d.bytes","dc854566d52769fd2362d835f166fb6d.bytes","e9309edbd85fc153f70c7b45d9b94791.bytes","e9309edbd85fc153f70c7b45d9b94791.bytes","ebca1c6ae69177ce4b28928f361dbc62.bytes","ebca1c6ae69177ce4b28928f361dbc62.bytes","f2169dff808c114fe1f60c6815087e39.bytes","f2169dff808c114fe1f60c6815087e39.bytes","f7558d75e79543a5e659bfe38ee92eb8.bytes","f7558d75e79543a5e659bfe38ee92eb8.bytes","fa47a70be63afa4f0269215abb82c13d.bytes","fa47a70be63afa4f0269215abb82c13d.bytes","78966d07421dd144bbe338cf34a55ea1.bytes","78966d07421dd144bbe338cf34a55ea1.bytes","752ec3fc83c0fe18c87dee4006807966.bytes","60a3c1f4375bfff6c81576273d5c8443.bytes","059caf18c820a78f87205e66126904e9.bytes","087afb3f6d2b6b5052433e09f2aaa4bf.bytes","0a51e174f5dea5fffd2c764a69a764f6.bytes","18b17480f0e65cb454a96e6d0dbccb60.bytes","2a95b57671af294c2aa2adaff71def8d.bytes","5c875598fa1cb5a60e8e4eadc4441f99.bytes","61771a27d47278355fd74934d42c6e2c.bytes","6817d624b170d9a5e7783a6793c087a8.bytes","788b8977048ddf4bbc4ae88e6af02531.bytes","78ff3b90b43905df2830b0a848521b93.bytes","91dce9c4d34bd07939364805eff4abec.bytes","97156296ecd6fc9bb038746130b98c2b.bytes","a1ad08924c005ad7e0d39b31024a9b6f.bytes","ce5913fbd5f20d03f8a4516b36d084c2.bytes","db446422f460a832744cdcf974fb90fd.bytes","dd3d097c9d1f5f4744516536ab93bc87.bytes","5c875598fa1cb5a60e8e4eadc4441f99.bytes","5c875598fa1cb5a60e8e4eadc4441f99.bytes","76b51938555a8a6a0c1694f902cdaf75.bytes","76b51938555a8a6a0c1694f902cdaf75.bytes","89270e59f0e63eb0cf41accb0e6fd84a.bytes","89270e59f0e63eb0cf41accb0e6fd84a.bytes","059caf18c820a78f87205e66126904e9.bytes","059caf18c820a78f87205e66126904e9.bytes","8512ae7d57b1396273f76fe6ed341a23.bytes","8512ae7d57b1396273f76fe6ed341a23.bytes","1aa355706e1767666124331a716c7890.bytes","1aa355706e1767666124331a716c7890.bytes","0589082cd8a9668981d909094215f69a.bytes","0589082cd8a9668981d909094215f69a.bytes","0647e98f5e1c8e9e345fc43a3ffa0383.bytes","0647e98f5e1c8e9e345fc43a3ffa0383.bytes","0b7043fbd23ca788dd796a0498c46e3c.bytes","0b7043fbd23ca788dd796a0498c46e3c.bytes","2719c83c72876c399b7a4cb472f71ac3.bytes","2719c83c72876c399b7a4cb472f71ac3.bytes","27ff5d8f32dd0ddb82eaac1d091bd0f6.bytes","27ff5d8f32dd0ddb82eaac1d091bd0f6.bytes","289bfa6b1322fd82ac0e86b70d55a47a.bytes","289bfa6b1322fd82ac0e86b70d55a47a.bytes","2c6a17dcb948df2147b2f011e9272434.bytes","2c6a17dcb948df2147b2f011e9272434.bytes","39a691fd5033f3f9cd98443e17e46b94.bytes","39a691fd5033f3f9cd98443e17e46b94.bytes","39f778cde807067d7ea3b5882e0e0783.bytes","39f778cde807067d7ea3b5882e0e0783.bytes","3a559b926e489ac961294ddee80aa7bf.bytes","3a559b926e489ac961294ddee80aa7bf.bytes","3d002b4e39ce145ea4bfa04c444cc975.bytes","3d002b4e39ce145ea4bfa04c444cc975.bytes","3e7a7dbec3097c0d8570ee1b9e0e13e1.bytes","3e7a7dbec3097c0d8570ee1b9e0e13e1.bytes","3fccb71678b8b4b1a8c3e8cb39187a7e.bytes","3fccb71678b8b4b1a8c3e8cb39187a7e.bytes","496e73155a00619d34c252971845642d.bytes","496e73155a00619d34c252971845642d.bytes","4ec192a76bdbb43f0f8078e68a0f2567.bytes","4ec192a76bdbb43f0f8078e68a0f2567.bytes","4fc71c22a21fead74a5d88762d005460.bytes","4fc71c22a21fead74a5d88762d005460.bytes","5e366439c90a0b0ca76afaadcf6a88d7.bytes","5e366439c90a0b0ca76afaadcf6a88d7.bytes","60a3c1f4375bfff6c81576273d5c8443.bytes","60a3c1f4375bfff6c81576273d5c8443.bytes","62901e9cb8f9d68c36040dffa8e1f9be.bytes","62901e9cb8f9d68c36040dffa8e1f9be.bytes","752ec3fc83c0fe18c87dee4006807966.bytes","752ec3fc83c0fe18c87dee4006807966.bytes","7accc03d6bc9a6730cf1104814c76b0c.bytes"]
    skip = [
        "001cfb1bd3f1f54b92f55c8beabcf24a.bytes", # bad big_null, unk0_copy != unk0
        "00d29cbf787b4e9c6a32b5c5e18dbd06.bytes",
        "0109de29d2b84b4702130a997aee7be1.bytes",
        "011007bb53f23220315e728dbc8762a5.bytes",
        "01239eedfe7eae875c06d7ef3effac4a.bytes"
    ]
    root = Path(r"../../../wildriftcom.riotgames.league.wildrift/main.3050.com.riotgames.league.wildrift/Res")
    for item in root.iterdir():
        if ".bytes" in item.name and item.name in infolist:
            print(item.name)
            parseme = Path(item)#r"./76b51938555a8a6a0c1694f902cdaf75.bytes")
            parse_file(parseme)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="folder of .bytes to extract",
                        type=str)
    args = parser.parse_args()

    root = Path(args.path)
    for item in root.iterdir():
        if ".bytes" in item.name:
            print(item.name)
            parseme = Path(item)
            parse_file(parseme)