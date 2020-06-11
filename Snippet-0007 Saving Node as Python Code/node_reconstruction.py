# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/obj")

# Code for /obj/geo1
hou_node = hou_parent.createNode("geo", "geo1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.0503613, 1.98358))
hou_node.setSelectableInViewport(True)
hou_node.showOrigin(False)
hou_node.useXray(False)
hou_node.hide(False)
hou_node.setSelected(False)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4", "Transform", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("xOrd", "Transform Order", menu_items=(["srt","str","rst","rts","tsr","trs"]), menu_labels=(["Scale Rot Trans","Scale Trans Rot","Rot Scale Trans","Rot Trans Scale","Trans Scale Rot","Trans Rot Scale"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setJoinWithNext(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("rOrd", "Rotate Order", menu_items=(["xyz","xzy","yxz","yzx","zxy","zyx"]), menu_labels=(["Rx Ry Rz","Rx Rz Ry","Ry Rx Rz","Ry Rz Rx","Rz Rx Ry","Rz Ry Rx"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("t", "Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 0)", "script_action_help": "Select an object to match the translation with.", "script_action_icon": "BUTTONS_match_transform"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("r", "Rotate", 3, default_value=([0, 0, 0]), min=0, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 1)", "script_action_help": "Select an object to match the rotation with.", "script_action_icon": "BUTTONS_match_rotation"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("s", "Scale", 3, default_value=([1, 1, 1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 2)", "script_action_help": "Select an object to match the scale with.", "script_action_icon": "BUTTONS_match_scale"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("p", "Pivot Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 3)", "script_action_help": "Select an object to match the pivot with.", "script_action_icon": "BUTTONS_match_pivot"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("pr", "Pivot Rotate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 4)", "script_action_help": "Select an object to match the pivot rotation with.", "script_action_icon": "BUTTONS_match_pivot_rotation"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("scale", "Uniform Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("pre_xform", "Modify Pre-Transform", menu_items=(["clean","cleantrans","cleanrot","cleanscales","extract","reset"]), menu_labels=(["Clean Transform","Clean Translates","Clean Rotates","Clean Scales","Extract Pre-transform","Reset Pre-transform"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("keeppos", "Keep Position When Parenting", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("childcomp", "Child Compensation", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("constraints_on", "Enable Constraints", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("constraints_path", "Constraints", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional( hou.parmCondType.HideWhen, "{ constraints_on == 0 }")
hou_parm_template2.setTags({"opfilter": "!!CHOP", "oprelative": ".", "script_action": "import objecttoolutils\nobjecttoolutils.constraintsMenu(kwargs)", "script_action_help": "", "script_action_icon": "BUTTONS_add_constraints"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookatpath", "Look At", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookupobjpath", "Look Up Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookup", "Look At Up Vector", 1, default_value=(["on"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["off","on","quat","pos","obj"]), menu_labels=(["Don't Use Up Vector","Use Up Vector","Use Quaternions","Use Global Position","Use Up Object"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("pathobjpath", "Path Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!SOP!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("roll", "Roll", 1, default_value=([0]), min=-360, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Angle, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("pos", "Position", 1, default_value=([0]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("uparmtype", "Parameterization", menu_items=(["uniform","arc"]), menu_labels=(["Uniform","Arc Length"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("pathorient", "Orient Along Path", 1, default_value=([1]), min=0, max=1, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("up", "Orient Up Vector", 3, default_value=([0, 1, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Vector, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("bank", "Auto-Bank factor", 1, default_value=([0]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4_1", "Render", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("shop_materialpath", "Material", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"opfilter": "!!CUSTOM/MATERIAL!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("shop_materialopts", "Options", menu_items=([]), menu_labels=([]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Mini)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("tdisplay", "Display", default_value=False)
hou_parm_template2.setJoinWithNext(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("display", "Display", 1, default_value=([1]), min=0, max=1, min_is_strict=True, max_is_strict=True, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("viewportlod", "Display As", menu_items=(["full","points","box","centroid","hidden","subd"]), menu_labels=(["Full Geometry","Point Cloud","Bounding Box","Centroid","Hidden","Subdivision Surface / Curves"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setHelp("Choose how the object's geometry should be rendered in the viewport")
hou_parm_template2.setTags({"spare_category": "Render"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_rendervisibility", "Render Visibility", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["*","primary","primary|shadow","-primary","-diffuse","-diffuse&-reflect&-refract",""]), menu_labels=(["Visible to all","Visible only to primary rays","Visible only to primary and shadow rays","Invisible to primary rays (Phantom)","Invisible to diffuse rays","Invisible to secondary rays","Invisible (Unrenderable)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "rendervisibility", "spare_category": "Render"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vm_rendersubd", "Render Polygons As Subdivision (Mantra)", default_value=False)
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "rendersubd", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_subdstyle", "Subdivision Style", 1, default_value=(["mantra_catclark"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["mantra_catclark","osd_catclark"]), menu_labels=(["Mantra Catmull-Clark","OpenSubdiv Catmull-Clark"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional( hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "subdstyle", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_subdgroup", "Subdivision Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional( hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "subdgroup", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("vm_osd_quality", "Open Subdiv Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.setConditional( hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_quality", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vm_osd_vtxinterp", "OSD Vtx Interp", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No vertex interpolation","Edges only","Edges and Corners"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional( hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_vtxinterp", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vm_osd_fvarinterp", "OSD FVar Interp", 1, default_value=([4]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2","3","4","5"]), menu_labels=(["Smooth everywhere","Sharpen corners only","Sharpen edges and corners","Sharpen edges and propagated corners","Sharpen all boundaries","Bilinear interpolation"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional( hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_fvarinterp", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0", "Shading", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("categories", "Categories", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("A list of tags which can be used to select the object")
hou_parm_template3.setTags({"spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("reflectmask", "Reflection Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Objects that will be reflected on this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("refractmask", "Refraction Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Objects that will be refracted on this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("lightmask", "Light Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Lights that illuminate this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/LIGHT!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("lightcategories", "Light Selection", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_volumefilter", "Volume Filter", 1, default_value=(["box"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["box","gaussian","bartlett","catrom","hanning","blackman","sinc"]), menu_labels=(["Box Filter","Gaussian","Bartlett (triangle)","Catmull-Rom","Hanning","Blackman","Sinc (sharpening)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "filter", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_volumefilterwidth", "Volume Filter Width", 1, default_value=([1]), min=0.001, max=5, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "filterwidth", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_matte", "Matte shading", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "matte", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rayshade", "Raytrace Shading", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rayshade", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_1", "Sampling", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("geo_velocityblur", "Geometry Velocity Blur", default_value=False)
hou_parm_template3.setConditional( hou.parmCondType.DisableWhen, "{ allowmotionblur == 0 }")
hou_parm_template3.setTags({"spare_category": "Sampling"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_2", "Dicing", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_shadingquality", "Shading Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "shadingquality", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_flatness", "Dicing Flatness", 1, default_value=([0.05]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "flatness", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_raypredice", "Ray Predicing", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Predicing","Full Predicing","Precompute Bounds"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "raypredice", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_curvesurface", "Shade Curves As Surfaces", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "curvesurface", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_3", "Geometry", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rmbackface", "Backface Removal", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rmbackface", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("shop_geometrypath", "Procedural Shader", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"opfilter": "!!SHOP/GEOMETRY!!", "oprelative": ".", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_forcegeometry", "Force Procedural Geometry Output", default_value=True)
hou_parm_template3.setTags({"spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rendersubdcurves", "Render Polygon Curves As Subdivision (Mantra)", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rendersubdcurves", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_renderpoints", "Render As Points (Mantra)", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No Point Rendering","Render Only Points","Render Unconnected Points"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "renderpoints", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_renderpointsas", "Render Points As (Mantra)", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1"]), menu_labels=(["Spheres","Circles"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setConditional( hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "renderpointsas", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_usenforpoints", "Use N For Point Rendering", default_value=False)
hou_parm_template3.setConditional( hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "usenforpoints", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_pointscale", "Point Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setConditional( hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "pointscale", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_pscalediameter", "Treat Point Scale as Diameter Instead of Radius", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "pscalediameter", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_metavolume", "Metaballs as Volume", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "metavolume", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_coving", "Coving", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Coving","Coving for displacement/sub-d","Coving for all primitives"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "coving", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_materialoverride", "Material Override", 1, default_value=(["compact"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["none","full","compact"]), menu_labels=(["Disabled","Evaluate for Each Primitve/Point","Evaluate Once"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_overridedetail", "Ignore Geometry Attribute Shaders", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "overridedetail", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_procuseroottransform", "Proc Use Root Transform", default_value=True)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "procuseroottransform", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4_2", "Misc", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("use_dcolor", "Set Wireframe Color", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("dcolor", "Wireframe Color", 3, default_value=([1, 1, 1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("picking", "Viewport Selecting Enabled", default_value=True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("pickscript", "Select Script", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.FileReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"filechooser_mode": "read"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("caching", "Cache Object Transform", default_value=True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vport_shadeopen", "Shade Open Curves In Viewport", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vport_displayassubdiv", "Display as Subdivision in Viewport", default_value=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("vport_onionskin", "Onion Skinning", menu_items=(["off","xform","on"]), menu_labels=(["Off","Transform only","Full Deformation"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/geo1/stdswitcher1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("stdswitcher1")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/xOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("xOrd")
hou_parm.lock(False)
hou_parm.set("srt")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/rOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("rOrd")
hou_parm.lock(False)
hou_parm.set("xyz")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/geo1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/geo1/s parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("s")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/geo1/p parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("p")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/pr parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("pr")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/pre_xform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("pre_xform")
hou_parm.lock(False)
hou_parm.set("clean")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/keeppos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("keeppos")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/childcomp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("childcomp")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/constraints_on parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("constraints_on")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/constraints_path parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("constraints_path")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lookatpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("lookatpath")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lookupobjpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("lookupobjpath")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lookup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("lookup")
hou_parm.lock(False)
hou_parm.set("on")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/pathobjpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("pathobjpath")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/roll parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("roll")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("pos")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/uparmtype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("uparmtype")
hou_parm.lock(False)
hou_parm.set("arc")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/pathorient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("pathorient")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/up parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("up")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 1, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/bank parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("bank")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/shop_materialpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("shop_materialpath")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/shop_materialopts parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("shop_materialopts")
hou_parm.lock(False)
hou_parm.set("override")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/tdisplay parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("tdisplay")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/display parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("display")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/use_dcolor parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("use_dcolor")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/dcolor parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("dcolor")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/picking parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("picking")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/pickscript parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("pickscript")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/caching parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("caching")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vport_shadeopen parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vport_shadeopen")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vport_displayassubdiv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vport_displayassubdiv")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vport_onionskin parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vport_onionskin")
hou_parm.lock(False)
hou_parm.set("off")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/stdswitcher41 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("stdswitcher41")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/viewportlod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("viewportlod")
hou_parm.lock(False)
hou_parm.set("full")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_rendervisibility parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_rendervisibility")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_rendersubd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_rendersubd")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_subdstyle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_subdstyle")
hou_parm.lock(False)
hou_parm.set("mantra_catclark")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_subdgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_subdgroup")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_osd_quality parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_osd_quality")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_osd_vtxinterp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_osd_vtxinterp")
hou_parm.lock(False)
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_osd_fvarinterp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_osd_fvarinterp")
hou_parm.lock(False)
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/categories parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("categories")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/reflectmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("reflectmask")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/refractmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("refractmask")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lightmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("lightmask")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lightcategories parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("lightcategories")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_volumefilter parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_volumefilter")
hou_parm.lock(False)
hou_parm.set("box")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_volumefilterwidth parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_volumefilterwidth")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_matte parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_matte")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_rayshade parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_rayshade")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/geo_velocityblur parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("geo_velocityblur")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_shadingquality parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_shadingquality")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_flatness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_flatness")
hou_parm.lock(False)
hou_parm.set(0.050000000000000003)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_raypredice parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_raypredice")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_curvesurface parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_curvesurface")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_rmbackface parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_rmbackface")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/shop_geometrypath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("shop_geometrypath")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_forcegeometry parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_forcegeometry")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_rendersubdcurves parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_rendersubdcurves")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_renderpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_renderpoints")
hou_parm.lock(False)
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_renderpointsas parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_renderpointsas")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_usenforpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_usenforpoints")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_pointscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_pointscale")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_pscalediameter parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_pscalediameter")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_metavolume parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_metavolume")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_coving parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_coving")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_materialoverride parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_materialoverride")
hou_parm.lock(False)
hou_parm.set("compact")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_overridedetail parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_overridedetail")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/vm_procuseroottransform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm = hou_node.parm("vm_procuseroottransform")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("wirestyle", "rounded")
hou_node.setUserData("___Version___", "16.5.439")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("16.5.439")
# Update the parent node.
hou_parent = hou_node

# Code for /obj/geo1/sphere1
hou_node = hou_parent.createNode("sphere", "sphere1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.0235294, 1.10382))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/sphere1/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("type")
hou_parm.lock(False)
hou_parm.set("poly")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/surftype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("surftype")
hou_parm.lock(False)
hou_parm.set("quads")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/rad parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm_tuple = hou_node.parmTuple("rad")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/sphere1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/sphere1/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/orient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("orient")
hou_parm.lock(False)
hou_parm.set("y")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/freq parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("freq")
hou_parm.lock(False)
hou_parm.set(5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/rows parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("rows")
hou_parm.lock(False)
hou_parm.set(13)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/cols parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("cols")
hou_parm.lock(False)
hou_parm.set(24)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/orderu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("orderu")
hou_parm.lock(False)
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/orderv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("orderv")
hou_parm.lock(False)
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/imperfect parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("imperfect")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/upole parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("upole")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/accurate parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("accurate")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/sphere1/triangularpoles parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/sphere1")
hou_parm = hou_node.parm("triangularpoles")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "16.5.439")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("16.5.439")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/scatter1
hou_node = hou_parent.createNode("scatter::2.0", "scatter1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.628105, -0.0317974))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/scatter1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/stdswitcher1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("stdswitcher1")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/generateby parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("generateby")
hou_parm.lock(False)
hou_parm.set("bydensity")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/densityscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("densityscale")
hou_parm.lock(False)
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/usedensityattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("usedensityattrib")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/densityattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("densityattrib")
hou_parm.lock(False)
hou_parm.set("density")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/useareaattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("useareaattrib")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/areaattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("areaattrib")
hou_parm.lock(False)
hou_parm.set("area")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/forcetotal parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("forcetotal")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/npts parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("npts")
hou_parm.lock(False)
hou_parm.set(300)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/usedensitytexture parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("usedensitytexture")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/densitytexture parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("densitytexture")
hou_parm.lock(False)
hou_parm.set("default.pic")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/primcountattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("primcountattrib")
hou_parm.lock(False)
hou_parm.set("count")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/useemergencylimit parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("useemergencylimit")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/emergencylimit parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("emergencylimit")
hou_parm.lock(False)
hou_parm.set(1000000)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/seed parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("seed")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/overrideprimseed parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("overrideprimseed")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/primseedattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("primseedattrib")
hou_parm.lock(False)
hou_parm.set("primid")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/randomizeorder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("randomizeorder")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/relaxpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("relaxpoints")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/relaxiterations parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("relaxiterations")
hou_parm.lock(False)
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/scaleradiiby parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("scaleradiiby")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/usemaxradius parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("usemaxradius")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/maxradius parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("maxradius")
hou_parm.lock(False)
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/useprimnumattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("useprimnumattrib")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/primnumattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("primnumattrib")
hou_parm.lock(False)
hou_parm.set("sourceprim")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/useprimuvwattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("useprimuvwattrib")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/primuvwattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("primuvwattrib")
hou_parm.lock(False)
hou_parm.set("sourceprimuv")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/useoutputdensityattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("useoutputdensityattrib")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/outputdensityattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("outputdensityattrib")
hou_parm.lock(False)
hou_parm.set("density")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/useoutputradiusattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("useoutputradiusattrib")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/outputradiusattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("outputradiusattrib")
hou_parm.lock(False)
hou_parm.set("pscale")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/radiusintexturespace parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("radiusintexturespace")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/pointattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("pointattribs")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/vertattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("vertattribs")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/primattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("primattribs")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/scatter1/detailattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/scatter1")
hou_parm = hou_node.parm("detailattribs")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "16.5.439")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("16.5.439")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/voronoifracture1
hou_node = hou_parent.createNode("voronoifracture", "voronoifracture1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.0235294, -1.17389))
hou_node.bypass(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(True)
hou_node.setTemplateFlag(True)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/voronoifracture1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/fuse_points parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("fuse_points")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/fuse_dist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("fuse_dist")
hou_parm.lock(False)
hou_parm.set(0.001)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/fuse_updatenml parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("fuse_updatenml")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/createinside parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("createinside")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/connect parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("connect")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/cuspnormals parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("cuspnormals")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/cuspangle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("cuspangle")
hou_parm.lock(False)
hou_parm.set(15)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/cuspouternormals parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("cuspouternormals")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/cuspouterangle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("cuspouterangle")
hou_parm.lock(False)
hou_parm.set(60)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/docusp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("docusp")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/visualizepieces parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("visualizepieces")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/usecellptgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("usecellptgroup")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/cellgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("cellgroup")
hou_parm.lock(False)
hou_parm.set("0")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/clustermode parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("clustermode")
hou_parm.lock(False)
hou_parm.set("0")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/settings1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("settings1")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/triangulation parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("triangulation")
hou_parm.lock(False)
hou_parm.set("0")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/partition parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("partition")
hou_parm.lock(False)
hou_parm.set("1")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/cutplaneoffset parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("cutplaneoffset")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/optimizecutbycluster parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("optimizecutbycluster")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/cluster parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("cluster")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/deleteedges parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("deleteedges")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/addclusternoise parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("addclusternoise")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/clustersize parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm_tuple = hou_node.parmTuple("clustersize")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0.5, 0.5, 0.5))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/voronoifracture1/clusteroffset parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm_tuple = hou_node.parmTuple("clusteroffset")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/voronoifracture1/clusterjitter parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm_tuple = hou_node.parmTuple("clusterjitter")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/voronoifracture1/randomdetach parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("randomdetach")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/detachseed parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("detachseed")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/detachratio parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("detachratio")
hou_parm.lock(False)
hou_parm.set(0.10000000000000001)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/constraintnetwork parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("constraintnetwork")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/inclusterstrength parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("inclusterstrength")
hou_parm.lock(False)
hou_parm.set(-1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/outclusterstrength parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("outclusterstrength")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/clusterattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("clusterattr")
hou_parm.lock(False)
hou_parm.set("cluster")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/clusterattrtol parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("clusterattrtol")
hou_parm.lock(False)
hou_parm.set(1.0000000000000001e-05)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/fusedist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("fusedist")
hou_parm.lock(False)
hou_parm.set(0.001)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/addinteriordetail parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("addinteriordetail")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/viznoisescale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("viznoisescale")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/planar parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("planar")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/detailsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("detailsize")
hou_parm.lock(False)
hou_parm.set(0.25)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/intnoiseamp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("intnoiseamp")
hou_parm.lock(False)
hou_parm.set(0.10000000000000001)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/intnoisetype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("intnoisetype")
hou_parm.lock(False)
hou_parm.set("snoise")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/intnoisefreq parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm_tuple = hou_node.parmTuple("intnoisefreq")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((2.5, 2.5, 2.5))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/voronoifracture1/intnoiseoffset parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm_tuple = hou_node.parmTuple("intnoiseoffset")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/voronoifracture1/intnoiseturb parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("intnoiseturb")
hou_parm.lock(False)
hou_parm.set(3)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/hassdfinput parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("hassdfinput")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/depthsamplediv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("depthsamplediv")
hou_parm.lock(False)
hou_parm.set(50)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/clampmaxdisp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("clampmaxdisp")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/clampdepthpct parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("clampdepthpct")
hou_parm.lock(False)
hou_parm.set(0.90000000000000002)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/depthnoisescalebias parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("depthnoisescalebias")
hou_parm.lock(False)
hou_parm.set(0.84999999999999998)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/usedepthnoisescaleramp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("usedepthnoisescaleramp")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/depthnoisescaleramp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("depthnoisescaleramp")
hou_parm.lock(False)
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/newg parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("newg")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/groupprefix parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("groupprefix")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/groupinterior parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("groupinterior")
hou_parm.lock(False)
hou_parm.set("inside")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/groupexterior parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("groupexterior")
hou_parm.lock(False)
hou_parm.set("outside")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/newname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("newname")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/nameprefix parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("nameprefix")
hou_parm.lock(False)
hou_parm.set("piece")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/copyattributes parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("copyattributes")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/ptattributes parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("ptattributes")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/primattributes parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("primattributes")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/keepinternal parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("keepinternal")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/pieceattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("pieceattr")
hou_parm.lock(False)
hou_parm.set("piece")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/cellptattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("cellptattr")
hou_parm.lock(False)
hou_parm.set("cellpt")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/clipptattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("clipptattr")
hou_parm.lock(False)
hou_parm.set("clippt")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/outsideattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("outsideattr")
hou_parm.lock(False)
hou_parm.set("outside")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/depthattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("depthattr")
hou_parm.lock(False)
hou_parm.set("depth")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/depthnoisescaleramp1pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("depthnoisescaleramp1pos")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/depthnoisescaleramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("depthnoisescaleramp1value")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/depthnoisescaleramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("depthnoisescaleramp1interp")
hou_parm.lock(False)
hou_parm.set("catmull-rom")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/depthnoisescaleramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("depthnoisescaleramp2pos")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/depthnoisescaleramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("depthnoisescaleramp2value")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/voronoifracture1/depthnoisescaleramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/voronoifracture1")
hou_parm = hou_node.parm("depthnoisescaleramp2interp")
hou_parm.lock(False)
hou_parm.set("catmull-rom")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___toolid___", "geometry_voronoifracture")
hou_node.setUserData("___toolcount___", "2")
hou_node.setUserData("___Version___", "3")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("3")
# Code to establish connections for /obj/geo1/scatter1
hou_node = hou_parent.node("scatter1")
if hou_parent.node("sphere1") is not None:
    hou_node.setInput(0, hou_parent.node("sphere1"), 0)
# Code to establish connections for /obj/geo1/voronoifracture1
hou_node = hou_parent.node("voronoifracture1")
if hou_parent.node("sphere1") is not None:
    hou_node.setInput(0, hou_parent.node("sphere1"), 0)
if hou_parent.node("scatter1") is not None:
    hou_node.setInput(1, hou_parent.node("scatter1"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

