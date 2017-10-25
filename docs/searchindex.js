Search.setIndex({docnames:["coordinate","cutting_strategies","gcode","gcode_formatters","index","machine","panel","profile","rib","surface"],envversion:52,filenames:["coordinate.rst","cutting_strategies.rst","gcode.rst","gcode_formatters.rst","index.rst","machine.rst","panel.rst","profile.rst","rib.rst","surface.rst"],objects:{"hotwing_core.Coordinate":{__add__:[0,1,1,""],__eq__:[0,1,1,""],__mul__:[0,1,1,""],__ne__:[0,1,1,""],__sub__:[0,1,1,""],calc_dist:[0,2,1,""],calc_slope:[0,2,1,""],rotate:[0,2,1,""]},"hotwing_core.Gcode":{code:[2,3,1,""],code_as_str:[2,3,1,""],dwell:[2,1,1,""],fast_move:[2,1,1,""],move:[2,1,1,""],normalize:[2,1,1,""],set_formatter:[2,1,1,""]},"hotwing_core.Panel":{__getitem__:[6,1,1,""],copy:[6,2,1,""],get_feedrate_multiplier:[6,1,1,""],reverse:[6,2,1,""],trim:[6,2,1,""]},"hotwing_core.Profile":{__add__:[7,1,1,""],__eq__:[7,1,1,""],__mul__:[7,1,1,""],__ne__:[7,1,1,""],__sub__:[7,1,1,""],copy:[7,2,1,""],interpolate_new_profile:[7,2,1,""],left_midpoint:[7,3,1,""],offset_around_profile:[7,2,1,""],right_midpoint:[7,3,1,""],rotate:[7,2,1,""],scale:[7,2,1,""],translate:[7,2,1,""],trim:[7,2,1,""],trim_overlap:[7,2,1,""],x_bounds:[7,3,1,""],y_bounds:[7,3,1,""]},"hotwing_core.Rib":{airfoil_profile:[8,3,1,""],interpolate_new_rib:[8,2,1,""],profile:[8,3,1,""]},"hotwing_core.Surface":{__add__:[9,1,1,""],__eq__:[9,1,1,""],__getitem__:[9,1,1,""],__mul__:[9,1,1,""],__ne__:[9,1,1,""],__sub__:[9,1,1,""],bounds:[9,3,1,""],interpolate:[9,1,1,""],interpolate_around_profile_dist:[9,1,1,""],interpolate_around_profile_dist_pct:[9,1,1,""],interpolate_new_surface:[9,2,1,""],left:[9,3,1,""],length:[9,3,1,""],offset_around_surface:[9,2,1,""],right:[9,3,1,""],rotate:[9,2,1,""],scale:[9,2,1,""],to_file:[9,1,1,""],translate:[9,2,1,""],trim:[9,2,1,""]},"hotwing_core.cutting_strategies":{CuttingStrategyBase:[1,0,1,""],CuttingStrategyFactory:[1,0,1,""]},"hotwing_core.cutting_strategies.CuttingStrategyBase":{cut:[1,1,1,""]},"hotwing_core.cutting_strategies.CuttingStrategyFactory":{"default":[1,3,1,""],get_cls:[1,2,1,""],strategies:[1,3,1,""]},"hotwing_core.gcode":{MachineCommand:[2,0,1,""]},"hotwing_core.gcode.MachineCommand":{has_option:[2,1,1,""]},"hotwing_core.gcode_formatters":{GcodeFormatterBase:[3,0,1,""],GcodeFormatterFactory:[3,0,1,""]},"hotwing_core.gcode_formatters.GcodeFormatterBase":{end_commands:[3,1,1,""],process_command:[3,1,1,""],start_commands:[3,1,1,""]},"hotwing_core.gcode_formatters.GcodeFormatterFactory":{"default":[3,3,1,""],debug:[3,3,1,""],formatters:[3,3,1,""],get_cls:[3,2,1,""]},"hotwing_core.machine":{Machine:[5,0,1,""]},"hotwing_core.machine.Machine":{calculate_move:[5,1,1,""],generate_gcode:[5,1,1,""],load_panel:[5,1,1,""]},hotwing_core:{Coordinate:[0,0,1,""],Gcode:[2,0,1,""],Panel:[6,0,1,""],Profile:[7,0,1,""],Rib:[8,0,1,""],Surface:[9,0,1,""],machine:[5,4,0,"-"]}},objnames:{"0":["py","class","Python class"],"1":["py","method","Python method"],"2":["py","classmethod","Python class method"],"3":["py","attribute","Python attribute"],"4":["py","module","Python module"]},objtypes:{"0":"py:class","1":"py:method","2":"py:classmethod","3":"py:attribute","4":"py:module"},terms:{"abstract":1,"boolean":[2,5],"class":[0,1,2,3,4,5,6,7,8,9],"default":[1,2,3,5,7,9],"final":8,"float":[0,5,6,7,8,9],"function":[6,9],"import":[7,9],"int":[5,7,8,9],"new":[0,6,7,8,9],"return":[0,1,2,3,5,6,7,9],"switch":6,"true":5,The:[0,2,3,5,6,7,8],__add__:[0,7,9],__eq__:[0,7,9],__getitem__:[6,9],__init__:7,__mul__:[0,7,9],__ne__:[0,7,9],__sub__:[0,7,9],_find_convergence_point:7,access:3,account:[8,9],accur:[8,9],actual:[7,8,9],add:[0,2,9],added:7,addit:[2,5],adjust:6,after:[7,8],airfoil:[7,8,9],airfoil_profil:8,alia:[1,3],all:[2,5,6],allow:[2,5,8,9],along:9,alwai:6,amount:[7,8,9],angl:[0,7,9],ani:[3,5],anyth:5,appli:[6,8,9],appropri:3,area:9,arg:7,around:[0,6,7,8,9],ascend:9,assum:9,attribut:8,axi:6,back:8,base:[1,7,8,9],becaus:6,becom:9,befor:8,being:3,between:[0,5,6,7,8,9],block:5,bottom:[5,7,8,9],bottom_offset:7,bottom_sheet:8,bottom_surfac:7,bound:9,box:9,calc_dist:0,calc_slop:0,calcul:[0,9],calculate_mov:5,call:1,can:[2,3,5,6,7,8],cannot:5,center:5,check:2,chord:[6,8],classmethod:[0,1,3,6,7,8,9],clockwis:8,closest:9,cnc:5,code:[2,5],code_as_str:2,command:[1,2,3,5],compar:[0,9],complet:5,connect:9,consist:7,contain:[2,3,6,7,8,9],contrac:7,contract:9,convert:3,coord:2,coordin:[4,5,7,8,9],copi:[6,7,8],correct:6,creat:[3,5,6,7,8,9],current:9,cut:[3,4,5,6,8,9],cutter:5,cutting_strategi:[1,5],cutting_strategy_1:1,cutting_strategy_2:1,cutting_strategy_nam:5,cuttingstrategy1:1,cuttingstrategy2:1,cuttingstrategybas:4,cuttingstrategyfactori:4,dat:7,data:[2,9],debug:3,debug_formatt:3,debuggcodeformatt:3,defin:[0,6,7,9],degre:[0,7,8,9],delag:7,deleg:[2,5],depend:7,descend:9,determin:2,dict:[2,5],differ:7,diistanc:8,dimension:0,direct:[5,6,7],dist_between:[7,8,9],dist_interp:[7,8,9],distanc:[0,6,7,8,9],doesn:8,doubl:7,down:[6,7,9],downward:[7,9],dwell:2,each:[5,7,8,9],easili:2,edg:[6,8],effect:7,either:9,end:[7,9],end_command:3,entir:8,evalu:9,except:8,exclud:8,exist:6,expand:[7,9],expect:3,express:9,extend:9,face:[6,8],far:5,fast_mov:2,feedrat:[2,5,6],field:9,file:[7,9],filepath:7,find:[7,9],first:[0,7,8,9],flip:6,foam:5,foam_height:5,foil:8,foil_data:8,foil_definit:8,format:[2,3],formatt:4,formatter_nam:2,found:7,freeli:5,from:[1,3,5,6,7,8,9],front:8,front_stock:8,gcode:[4,5],gcode_formatt:3,gcode_formatter_nam:5,gcodeformatt:[1,2,3],gcodeformatterbas:4,gcodeformatterfactori:4,gener:[1,3,5],generate_gcod:5,genericgcodeformatt:3,get:[1,3,5,7,9],get_cl:[1,3],get_feedrate_multipli:6,given:9,goe:5,greater:5,half:7,has_opt:2,have:[5,6,8],heat:5,height:5,hit:5,hold:[2,7],horizont:[8,9],hotwing_cor:[0,1,2,3,5,6,7,8,9],hotwir:5,how:5,idea:8,implement:[1,3],inch:[2,5],includ:[5,8],incorrect:6,index:4,inherit:[1,3],initi:[7,8],input:7,instanc:3,interpol:[5,6,7,8,9],interpolate_around_profile_dist:9,interpolate_around_profile_dist_pct:9,interpolate_new_profil:7,interpolate_new_rib:8,interpolate_new_surfac:9,intersect:5,inward:[7,8],item:6,its:9,itself:7,job:[3,7],just:6,kei:[6,9],kerf:5,lap:7,larger:[7,9],largest:5,lead:[6,8],left:[5,6,7,8,9],left_midpoint:7,left_offset:5,left_rib:6,leftmost:7,length:[5,8,9],lies:9,like:7,line:9,linear:9,list:[2,7,9],load:[5,7],load_panel:5,machin:[1,2,4],machinecommand:4,made:9,mai:[5,7,9],maintain:[2,3,6,7],make:[5,6,7,9],manipul:[7,8],materi:8,max:[7,9],max_i:7,max_x:7,measur:6,melt:5,method:[1,7,9],mid:7,millimet:[2,5],min:[2,7,9],min_i:7,min_x:7,minimum:3,modul:4,more:9,most:[7,9],move:[2,5,9],multipli:[0,9],must:[1,5],name:[1,3],narrow:9,necessari:[6,8],neg:[7,9],newlin:[5,9],none:[2,5,6,7,8,9],normal:[2,5],now:7,number:[5,7,8,9],object:[0,1,2,3,5,6,7,8,9],occur:7,offset:[2,7,8,9],offset_around_profil:7,offset_around_surfac:[7,9],onc:8,onli:8,oper:9,option:2,order:[5,8,9],origin:[0,7,9],other:[0,7,8,9],otherwis:5,output:[2,9],output_fil:9,outsid:9,outward:[7,9],over:7,overlap:7,overload:7,page:4,panel:[4,5,8],panel_obj:6,paramet:[0,2,5,6,7,8,9],parent:[1,3],part:6,path:[1,5,7,9],pct:9,per:2,percent:9,percentag:9,perform:8,place:5,plu:5,point:[0,5,7,8,9],pos:9,posit:[5,7,8,9],post:5,process_command:3,process_fast_mov:3,process_mov:3,produc:[6,7],profil:[4,5,8,9],profile_point:5,provid:[3,9],radiant:5,radiu:5,rais:8,read:2,reduc:7,rel:9,relat:[2,9],repres:[2,6,8],represent:[5,6,7],requir:5,result:7,revers:6,rib:[4,5,6],rib_1:6,rib_2:6,right:[6,7,9],right_midpoint:7,right_rib:6,root:6,rotat:[0,7,8,9],rotation_po:8,safe_height:5,same:6,scale:[7,8,9],search:4,second:[0,2,7,8,9],separ:[5,9],seri:5,set:[5,6],set_formatt:2,shape:[6,8,9],sheet:[8,9],should:[7,8,9],side:[5,6,8,9],similar:8,simpli:7,singl:2,size:[7,8],slice:[6,8,9],slope:0,smaller:[7,9],solv:9,sourc:[0,1,2,3,5,6,7,8,9],space:[0,8],specif:3,specifi:[7,9],start:[7,8,9],start_command:3,stock:8,str:2,strageti:4,strategi:[1,3],string:[5,7,9],subclass:3,subtract:[0,9],sure:5,surfac:[4,5,7,8],surface_obj:9,survac:9,tail:8,tail_stock:8,take:[5,6,7],term:8,than:[5,7,9],thei:7,them:3,thi:[1,2,3,5,6,7,8,9],thick:8,those:[7,9],thought:[6,7,8],through:[2,5],time:2,tip:[6,8],to_fil:9,togeth:9,top:[5,7,8,9],top_offset:7,top_sheet:8,top_surfac:7,total:9,trail:6,translat:[5,7,9],trim:[6,7,9],trim_overlap:7,tupl:[7,9],two:[0,5,7,8,9],type:[0,2,5,6,7,9],type_:2,unit:[2,5,9],upward:[7,9],url:7,use:[5,7,8,9],used:[5,9],user:7,uses:9,using:[6,7,9],util:2,valu:[0,2,5,6,7,8,9],variabl:[0,2,3,5,6,7,8,9],varieti:7,vertic:[7,8,9],view:8,wai:[7,9],want:[8,9],washin:8,washout:8,when:[2,5,6,9],where:[5,7,9],which:[2,7,8],width:[5,6,7,9],wing:[6,8],wire:5,without:5,wood:8,write:9,written:9,x_bound:7,x_max:[7,9],x_min:[7,9],xy_offset:8,xyuv:5,y_bound:7,you:[2,3,5,6,7,9],your:5},titles:["Coordinate","Cutting Strageties","Gcode","GCode Formatters","Welcome to HotWing-Core\u2019s documentation!","Machine","Panel","Profile","Rib","Surface"],titleterms:{coordin:0,core:4,cut:1,cuttingstrategybas:1,cuttingstrategyfactori:1,document:4,formatt:3,gcode:[2,3],gcodeformatterbas:3,gcodeformatterfactori:3,hotw:4,indic:4,machin:5,machinecommand:2,panel:6,profil:7,rib:8,strageti:1,surfac:9,tabl:4,welcom:4}})