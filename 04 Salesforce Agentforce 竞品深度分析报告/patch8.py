F="Salesforce_Agentforce_竞品深度分析_v3_20260615.html"; h=open(F,encoding="utf-8").read()
def rep(old,new):
    global h
    if h.count(old)<1: raise SystemExit("NOT FOUND: "+old[:60])
    h=h.replace(old,new,1)

# 1) §7.2 84% precise annotation
rep('某客服案例自主解决率约 84%、仅 2% 需人工升级。',
    '<b>84–85% 自主解决率</b>来自 Salesforce <b>自身在 help.salesforce.com 的部署</b>（Agentforce "Customer Zero"，自 2024-10 累计 100 万+ 会话）——属厂商自有部署，非平台普适值、亦非第三方客户案例。')

# 2) 附B callout title + items -> closed
rep('✅ 后续可补','✅ 补研收尾（本轮已闭环）')
rep('<b>仍未深读（低边际价值、已知不影响结论）：</b>纯营销页(概述/工作原理/why/for-employees)与需交互输入的"弹性信用计算器"(避免编造数字)。',
    '<b>本轮补研收尾：</b>营销页(概述/工作原理/why/for-employees)已抽查，确认为营销 FAQ/简介、无超出已覆盖内容的实质信息；弹性信用计算器已查看其输入流程（不编造金额）——详见 <b>C.9</b>。')
rep('定价（$2/会话、弹性信用单价）以最新官方定价页/计算器为准，随合同与版本浮动。',
    '<b>✅ 定价</b>：三模型与免费层已核验并写入 §7.1；每单位价格官方页不公开，以 AE/计算器实时输出为准、随合同浮动（计算器机制见 C.9）。')
rep('客户成功指标（84% 自主解决 / Wiley 213% ROI / 1-800Accountant 70%）均为<b>单个客户官方案例</b>，非平台普适值，引用时须标注主体与场景。',
    '<b>✅ 客户指标主体已标注</b>：84–85%=Salesforce 自身 Help 部署(Customer Zero)；Wiley 213% ROI、1-800Accountant 70% 为单客户官方案例——主体与场景见 <b>C.9</b>。')
rep("Summer '26 多智能体编排、Atlas 3.0、A2A 等以官方 GA 为准。",
    '<b>✅ GA 状态已核实</b>：Summer \'26 已于 2026-06-15 GA（多智能体编排核心 / Atlas 3.0 / A2A / MCP 集成）；ADL API、高级 A2A 配置、"Orchestrate Other Agents"文档仍 Beta（见 C.9）。')

# 3) 附C C.9 before src
addC9='''      <h3>C.9 补研收尾：营销页 / 计算器 / GA 状态 / 客户指标主体（本轮闭环）</h3>
      <table>
        <thead><tr><th style="width:150px">原"待补研"项</th><th>本轮处理结果（官方核实）</th></tr></thead>
        <tbody>
          <tr><td>纯营销页</td><td>how-it-works / why / for-employees 已浏览器精读：均为营销 FAQ/简介，<b>无超出已覆盖内容的实质信息</b>；for-employees 重申员工智能体跨 <b>Lightning / Mobile / Slack</b> 三端。→ 缺口关闭（确认低价值）。</td></tr>
          <tr><td>弹性信用计算器</td><td>已实测其流程：<b>选行业 → 选公司规模 → 选产品线(Agentforce / Data 360) → 添加用例(Sales/Service Agent 等) → 折算为 Flex Credits 估算</b>；页面明示"Estimates, not guarantees"，<b>不公开每单位价格</b>。→ 机制已核实；具体金额以官方计算器实时输出为准，本报告不编造。</td></tr>
          <tr><td>Summer '26 GA 状态</td><td>已核实（2026-06-15 发布）：<b>多智能体编排核心（编排者/专才委派/Atlas 3.0 路由/上下文交接）、Atlas 推理引擎 3.0、A2A 协议、MCP 集成 已 GA</b>；<b>ADL API、高级 A2A 配置、"Orchestrate Other Agents"文档仍 Beta</b>。→ 由"以官方 GA 为准"更新为"核心已 GA、部分周边 Beta"。</td></tr>
          <tr><td>客户指标主体/场景</td><td>已逐条标注主体与场景（见下）。</td></tr>
        </tbody>
      </table>
      <ul>
        <li><b>84–85% 自主解决</b> = Salesforce <b>自身 help.salesforce.com 部署（Agentforce "Customer Zero"）</b>，自 2024-10 累计 <b>100 万+</b> 会话——厂商自有部署，非平台普适、非第三方。</li>
        <li><b>Wiley</b>：<b>213% ROI</b>、案例解决率 +40%、节省约 <b>$23 万</b>、季节性坐席上手快 50% —— 教育出版业，Service Cloud + Agentforce 官方案例。</li>
        <li><b>1-800Accountant</b>：报税周<b>自主解决 70%</b>、24 小时内 1,000+ 互动 —— 财税客服场景官方案例。</li>
        <li><b>OpenTable</b>：处理数万次会话（订位变更/菜单/用餐问题）—— 餐饮预订场景官方案例。</li>
      </ul>
      <div class="callout risk"><div class="tag">⚠️ 引用纪律</div><p style="margin:4px 0">以上客户数字均为<b>单一客户/厂商自有部署</b>的官方口径，<b>不可外推为 Agentforce 平台普适表现</b>；对外引用须同时注明"主体 + 场景 + 来源"。</p></div>

'''
rep('      <div class="src"><b>附C 来源：</b>', addC9+'      <div class="src"><b>附C 来源：</b>')

# 4) extend 附C src with new links
rep('<a href="https://www.salesforce.com/blog/salesforce-2026-forrester-wave-b2b/">Forrester Wave 2026</a>',
    '<a href="https://www.salesforce.com/news/stories/summer-2026-product-release-announcement/">Summer \'26 发布公告(GA)</a> · <a href="https://www.salesforce.com/customer-stories/agentforce-for-customer-support/">Customer Zero(自身 Help 84–85%)</a> · <a href="https://www.salesforce.com/agentforce/pricing/calculator/">弹性信用计算器</a> · <a href="https://www.salesforce.com/blog/salesforce-2026-forrester-wave-b2b/">Forrester Wave 2026</a>')

open(F,"w",encoding="utf-8").write(h)
print("patch8 OK size MB:", round(len(h.encode('utf-8'))/1e6,2))
