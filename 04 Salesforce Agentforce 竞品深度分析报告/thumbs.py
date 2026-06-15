import os
from PIL import Image
SRC="/sessions/sweet-inspiring-meitner/mnt/outputs/screenshots/Agentforce Studio截图原图"
DST="/sessions/sweet-inspiring-meitner/mnt/outputs/_thumbs"
n=0
for root,_,files in os.walk(SRC):
    for f in files:
        if not f.lower().endswith(".png"): continue
        sp=os.path.join(root,f)
        rel=os.path.relpath(sp,SRC)
        dp=os.path.join(DST,os.path.splitext(rel)[0]+".jpg")
        os.makedirs(os.path.dirname(dp),exist_ok=True)
        try:
            im=Image.open(sp).convert("RGB")
            w=1000
            if im.width>w: im=im.resize((w,int(im.height*w/im.width)),Image.LANCZOS)
            im.save(dp,format="JPEG",quality=72,optimize=True)
            n+=1
        except Exception as e:
            print("ERR",rel,e)
print("thumbs created:",n)
