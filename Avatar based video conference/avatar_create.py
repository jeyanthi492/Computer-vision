import py_avataaars as pa
from PIL import Image



#DEFAULT,TWINKLE,CLOSE,SQUINT
def avatar_create(*x):
    if len(x)==10:
      option_skin_color, option_top_type, option_hat_color, option_hair_color, option_accessories_type,option_clothe_type,option_clothe_graphic_type,option_clothe_color,option_facial_hair_type,option_facial_hair_color=x
      option_mouth_type, option_eyes_type="SMILE","DEFAULT"
    else:
        option_skin_color, option_top_type, option_hat_color, option_hair_color, option_accessories_type, option_clothe_type, option_clothe_graphic_type, option_clothe_color, option_facial_hair_type, option_facial_hair_color,option_mouth_type,option_eyes_type = x

    avatar = pa.PyAvataaar(style=pa.AvatarStyle.TRANSPARENT,
                           skin_color=eval('pa.SkinColor.%s' % option_skin_color),
                           top_type=eval('pa.TopType.SHORT_HAIR_SHORT_FLAT.%s' % option_top_type),
                           hat_color=eval('pa.Color.%s' % option_hat_color),
                           hair_color=eval('pa.HairColor.%s' % option_hair_color),
                           mouth_type=eval('pa.MouthType.%s'%option_mouth_type),
                           eye_type=eval('pa.EyesType.%s'%option_eyes_type),
                           accessories_type=eval('pa.AccessoriesType.%s' % option_accessories_type),
                           clothe_type=eval('pa.ClotheType.%s' % option_clothe_type),
                           clothe_graphic_type=eval('pa.ClotheGraphicType.%s' % option_clothe_graphic_type),
                           clothe_color = eval('pa.Color.%s' % option_clothe_color),
                           facial_hair_type=eval('pa.FacialHairType.%s' % option_facial_hair_type),
                           facial_hair_color=eval('pa.HairColor.%s' % option_facial_hair_color),
                           nose_type=pa.NoseType.DEFAULT,

    )
    avatar.render_png_file("AVATAR_2.png")


#avatar_create("PALE","HAT","BLACK","BLACK","KURT","GRAPHIC_SHIRT","BAT","BLUE_01","DEFAULT","BLACK")

