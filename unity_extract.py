# -*- coding: utf-8 -*-
# 3.8.3
import struct, re
import IPython

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
    return list(map(lambda v: int(v,16), re.findall("[a-f0-9]{2}", inp)))

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

# a thisobject passed to most of the custom zuc shit
zuc_instance = {
    "b": zuc_block, # b.ytes of the key
    "idx": 0 # number of uint32_ts into the key
}

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
    return True

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

IPython.embed()