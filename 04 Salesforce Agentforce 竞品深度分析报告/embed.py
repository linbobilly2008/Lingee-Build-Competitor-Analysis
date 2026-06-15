import base64, io, os, re
from PIL import Image
BASE="/sessions/sweet-inspiring-meitner/mnt/outputs/screenshots/Agentforce Studio截图原图"
HTML="/sessions/sweet-inspiring-meitner/mnt/outputs/agentforce_report.html"
M={
"__IMG_canvas__":"智能体/01_Agentforce生成器_画布视图.png",
"__IMG_convo__":"智能体/01_新建智能体_对话创建.png",
"__IMG_script__":"智能体/01_Agentforce生成器_脚本视图.png",
"__IMG_subagent_tool__":"智能体/01_Agentforce生成器_子智能体_选择:添加工具_创建自定义工具.png",
"__IMG_routing__":"智能体/01_Agentforce生成器_连接_路由.png",
"__IMG_retriever__":"数据/05_数据_检索器_检索器生成器_个别检索器_配置检索器结果.png",
"__IMG_vector__":"数据/06_数据_搜索索引_新建搜索索引_高级设置_搜索索引生成器_向量化.png",
"__IMG_prompt__":"提示模板（新开页面）/03_提示模板_提示生成器.png",
"__IMG_agentexchange__":"设置Einstein/设置_Einstein_Agentforce注册表_MCP服务器_从AgentExchange添加.png",
"__IMG_gateway__":"设置Einstein/设置_Einstein_Agentforce网关_策略_新建MCP服务器策略.png",
"__IMG_test__":"测试套件/02_测试套件_测试个案_选择评分器_自定义评分器.png",
"__IMG_trace__":"智能体/01_Agentforce生成器_预览_模拟模式_跟踪.png",
"__IMG_version__":"智能体/01_Agentforce生成器_版本提交.png",
"__IMG_analytics__":"分析/09_分析_概述_信任度.png",
"__IMG_optimize__":"优化/11_优化_会话和意图_会话详情1.png",
"__IMG_dx__":"08_Agentforce DX.png",
"__IMG_trustlayer__":"设置Einstein/设置_Einstein_Einstein生成式AI_Einstein 信任层_数据屏蔽1.png",
}
def datauri(path, maxw=1180, q=80):
    im=Image.open(path).convert("RGB")
    if im.width>maxw:
        im=im.resize((maxw,int(im.height*maxw/im.width)), Image.LANCZOS)
    buf=io.BytesIO(); im.save(buf,format="JPEG",quality=q,optimize=True)
    return "data:image/jpeg;base64,"+base64.b64encode(buf.getvalue()).decode()
html=open(HTML,encoding="utf-8").read()
miss=[]; total=0
for ph,rel in M.items():
    p=os.path.join(BASE,rel)
    if not os.path.exists(p): miss.append(rel); continue
    uri=datauri(p); total+=len(uri)
    html=html.replace(ph,uri)
open(HTML,"w",encoding="utf-8").write(html)
left=re.findall(r"__IMG_[a-z_]+__",html)
print("missing files:",miss)
print("remaining placeholders:",set(left))
print("embedded bytes (approx MB):",round(total/1e6,2))
print("html size MB:",round(os.path.getsize(HTML)/1e6,2))
