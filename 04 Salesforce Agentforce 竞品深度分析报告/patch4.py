p="agentforce_report.html"; h=open(p,encoding="utf-8").read()
def rep(old,new):
    global h
    if h.count(old)<1: raise SystemExit("NOT FOUND: "+old[:70])
    h=h.replace(old,new,1)

# 1) Insert C.5/C.6/C.7 before 附C src line
add = '''      <h3>C.5 上下文工程指南（salesforce.com/agentforce/guide/，已精读）— 可直接落地的最佳实践</h3>
      <div class="callout borrow"><div class="tag">✅ 可借鉴（官方最佳实践，强证据）</div><ul>
        <li><b>"确定性三明治(deterministic sandwich)"</b>：代码控制对话的开头与结尾，中段交给 AI 自然语言——入口与收尾完全可控。</li>
        <li><b>脚本管业务逻辑、指令只管语言风格</b>：把数据校验/强制顺序交给脚本，措辞交给 LLM，去除自然语言提示的"猜测性"。</li>
        <li><b>命名即路由</b>：子智能体/动作命名要清晰，推理引擎按名称选路径；<b>小而可复用脚本</b>（如身份校验）跨子智能体复用，策略变更只改一处。</li>
        <li><b>上游一次性取数 + 会话变量传递上下文</b>：动作前先取全所需数据以降时延/降 LLM 调用，变量在子智能体间传递避免重复提问。</li>
        <li><b>if-then 合规逻辑 + 显式退出条件</b>：如"先校验会员等级再给折扣"；明确子智能体何时交回主智能体/结束会话。</li>
        <li><b>选型纪律（官方原文）</b>："别把智能体设计成线性聊天机器人；流程固定就用 Flow Builder，Agentforce Script 留给杂乱/不可预测的人类输入。"→ 对灵基同样适用：能用确定性流程的别上 LLM。</li>
      </ul></div>

      <h3>C.6 全生命周期官方 taxonomy（帮助文档"设计和实现代理"，已精读）</h3>
      <p>官方把智能体生命周期定义为：<b>构想 Ideate → 搭建组织 Set Up → 构建/配置 Build·Configure → 测试 Test → 部署到渠道 Deploy → 监控 Monitor → 扩展 Extend</b>。每阶段配官方资源——例如 Set Up 阶段含 Trust Layer / Data 360 接地 / 数据库(Data Library) / 检索增强(RAG)；Test 阶段含"测试工具与策略"。可用版本：Enterprise / Performance / Unlimited / Developer（按智能体类型需附加许可）。→ 与本报告第 5 节"全生命周期管理"的阶段划分一致，已据此校准为官方 taxonomy。</p>

      <h3>C.7 商业模式与开放协议官方口径（定价页 / 多智能体页 / MCP 页，已精读）</h3>
      <ul>
        <li><b>两种计价（官方）</b>：<b>Flex Credits</b>（最灵活/可扩展、成本对齐价值、Digital Wallet 提供更细颗粒用量、可选 PayGo 或预承诺购买）与 <b>Conversations</b>（统一定价、面向外部客户智能体）；Agentforce Voice 用 Flex Credits 计价。<b>关键：官方定价页未公开每单位价格</b>（$/会话、$/信用以 AE/计算器为准）——印证本报告"定价不透明"的判断。</li>
        <li><b>MCP（官方）</b>：Model Context Protocol 是"由 Anthropic 提出的开放标准"，规定 AI 模型如何连接外部工具/系统/数据；Agentforce 支持连接 MCP 服务器与"Agentforce 互操作(Interoperability)"。</li>
        <li><b>多智能体编排（官方）</b>：主智能体作为单一联系点，把任务路由给最合适的专才智能体；可连接第三方智能体；并提供治理与安全。</li>
      </ul>

'''
rep('      <div class="src"><b>附C 来源：</b>', add+'      <div class="src"><b>附C 来源：</b>')

# 2) Expand 附C src with new links
rep('<a href="https://www.salesforce.com/blog/salesforce-2026-forrester-wave-b2b/">Forrester Wave 2026</a>',
    '<a href="https://www.salesforce.com/agentforce/guide/">上下文工程指南</a> · <a href="https://www.salesforce.com/agentforce/multi-agent-orchestration/">多智能体编排</a> · <a href="https://www.salesforce.com/agentforce/mcp-support/">MCP 支持</a> · <a href="https://www.salesforce.com/agentforce/pricing/">定价页</a> · <a href="https://help.salesforce.com/s/articleView?id=ai.copilot_intro.htm&language=en_US&type=5">设计和实现代理(生命周期 taxonomy)</a> · <a href="https://www.salesforce.com/blog/salesforce-2026-forrester-wave-b2b/">Forrester Wave 2026</a>')

# 3) §5 summary append official taxonomy
rep('<b>生命周期小结：</b>',
    '<b>生命周期小结：</b><span class="pill b">官方佐证</span> 帮助文档将生命周期定义为"构想→搭建→构建/配置→测试→部署→监控→扩展"，与本节划分一致（详见附C）。 ')

# 4) Update 附B gap line to reflect this round
rep('<b>已补：</b>Agentforce Grid 与 Einstein Data Prism（爱因斯坦数据棱镜）已精读并写入<b>附C</b>；开发者指南 get-started/agents/actions 已官方精读。<b>仍可继续：</b>帮助文档"设计和实现代理/平台参考"等子章节为 JS 单页应用、本轮渲染受限未逐屏精读，可后续补。',
    '<b>已补（最近两轮）：</b>开发者指南(get-started/agents/actions)、上下文工程指南、多智能体编排、MCP 支持、定价页、Atlas 页、帮助文档"设计和实现代理"(含官方生命周期 taxonomy)、Agentforce Grid、Einstein Data Prism——均已在浏览器内精读并写入<b>附C</b>。<b>仍未深读（低边际价值、已知不影响结论）：</b>帮助文档"Einstein 平台参考"(对象/限制/区域等参考资料)、纯营销页(概述/工作原理/why/for-employees)、以及需交互输入的"弹性信用计算器"(避免编造数字)。')

open(p,"w",encoding="utf-8").write(h)
print("OK size MB:", round(len(h.encode('utf-8'))/1e6,2))
