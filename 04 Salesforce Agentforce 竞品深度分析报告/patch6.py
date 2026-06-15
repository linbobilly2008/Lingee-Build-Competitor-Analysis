F="Salesforce_Agentforce_竞品深度分析_v3_20260615.html"; h=open(F,encoding="utf-8").read()
def rep(old,new):
    global h
    if h.count(old)<1: raise SystemExit("NOT FOUND: "+old[:60])
    h=h.replace(old,new,1)

# A) 30 年 -> 30 余年 (all)
h=h.replace("30 年","30 余年")

# B) §7.1 pricing — replace table+notes with verified 3-model structure
old71='''      <p>2025 年 5 月起 Salesforce 重构 Agentforce 定价，提供多种消费/订阅组合：</p>
      <table>
        <thead><tr><th>计价单元</th><th>单价(参考)</th><th>说明</th></tr></thead>
        <tbody>
          <tr><td>Agentforce 会话(Conversation)</td><td>≈ $2 / 会话</td><td>一次会话=与用户 24 小时交互窗口；主要面向外部客户智能体；需预购，且与弹性信用不在同一环境混用。</td></tr>
          <tr><td>弹性信用(Flex Credits)</td><td>标准动作 20 信用≈$0.10；语音动作 30 信用≈$0.15</td><td>按动作消耗；信用以 10 万一档≈$500 购买($0.005/信用)。</td></tr>
          <tr><td>按用户订阅 / Data 360 捆绑</td><td>合同制</td><td>与 Data 360(原 Data Cloud)打包，形成"数据+智能体"组合售卖。</td></tr>
        </tbody>
      </table>
      <p class="muted">Salesforce 提供"弹性信用定价计算器"帮助测算，但第三方普遍指出：会话/信用口径复杂、用量难预测、易超支，是采购决策的主要顾虑。</p>'''
new71='''      <p>Agentforce 提供<b>三种相互独立的计价模型</b>（2025–2026 口径，已多源交叉核验）：</p>
      <table>
        <thead><tr><th style="width:150px">模型</th><th>价格</th><th>关键规则</th></tr></thead>
        <tbody>
          <tr><td>按对话 Conversation</td><td>$2 / 次会话（多币种：€2 / AU$2.80 / ¥240 日元 / 20kr / £1.60）</td><td>一次会话=与用户的一段连贯会话；<b>仅支持预购、不可与 Flex Credits 混用</b>；当单次会话动作数 &gt;20 时更划算。</td></tr>
          <tr><td>弹性信用 Flex Credits</td><td>$500 / 10 万信用（标准动作 20 信用≈$0.10；语音动作 30 信用≈$0.15）</td><td>预购/预承诺/按需付费；<b>未用额度不滚存、超额无罚金</b>；动作数 &lt;20/会话时更划算。</td></tr>
          <tr><td>按用户订阅 Per-User</td><td>Agentforce 附加包 $125、行业附加包 $150、<b>Agentforce 1 版 $550</b>/用户/月（含大额年度信用池）</td><td>席位内<b>不计量使用(unmetered)</b>，缓解成本焦虑；适合全员部署。</td></tr>
        </tbody>
      </table>
      <div class="note">免费层 + 用量可视化：<b>Salesforce Foundations</b> 免费层含 Agent Builder / Prompt Builder、20 万 Flex 信用、25 万 Data Cloud 信用，及<b>前 1,000 次会话免费</b>；所有用量型产品配 <b>Digital Wallet</b> 实时追踪消耗。决策经验法则：会话内动作 &gt;20 选"按对话"、&lt;20 选"弹性信用"。</div>
      <p class="muted">注：<b>官方定价页本身不公开每单位价格</b>（$/会话、$/信用以 AE/计算器为准）——印证"定价不透明"。第三方普遍指出会话/信用口径复杂、用量难预测、易超支；叠加"<b>额度不滚存 + 三模型不可混用</b>"，增加选择复杂度，是采购的主要顾虑。<span class="pill b">本节据竞品报告B补全并经第三方多源核验</span></p>'''
rep(old71,new71)

# C) §7.2 customer cases — broaden logos, keep verified
old72='''      <div class="grid3">
        <div class="card"><h4>1-800Accountant</h4><p class="muted">报税周自主解决 <b>70%</b> 在线咨询；首 24 小时处理 1,000+ 客户互动（官方案例）。</p></div>
        <div class="card"><h4>Wiley</h4><p class="muted">自助服务效率提升 <b>40%+</b>；Service Cloud 集成实现 <b>213% ROI</b>。</p></div>
        <div class="card"><h4>OpenTable</h4><p class="muted">处理数万次会话(订位变更/菜单/用餐问题)，显著降低等待时间。</p></div>
      </div>'''
new72='''      <div class="grid3">
        <div class="card"><h4>1-800Accountant <span class="pill g">已核验</span></h4><p class="muted">报税周自主解决 <b>70%</b> 在线咨询；首 24 小时处理 1,000+ 客户互动（官方案例）。</p></div>
        <div class="card"><h4>Wiley <span class="pill g">已核验</span></h4><p class="muted">自助服务效率提升 <b>40%+</b>；Service Cloud 集成实现 <b>213% ROI</b>、节省约 $23 万。</p></div>
        <div class="card"><h4>OpenTable <span class="pill g">已核验</span></h4><p class="muted">处理数万次会话(订位变更/菜单/用餐问题)，显著降低等待时间。</p></div>
      </div>
      <p class="muted">更多官方公开标杆客户（<span class="pill b">官方公开、未逐一独立核验</span>，来源：官网/可观测性新闻稿/竞品报告B）：<b>SharkNinja、Indeed、Heathrow、Equinox、Fujitsu、Finnair、Prudential、Engine、Nexo、Reddit</b> 等，覆盖服务、销售、营销、商务与内部员工五大场景；其中 1-800Accountant、Engine 为可观测性工具试点客户。</p>'''
rep(old72,new72)

# D) §8.1 Atlas enhance — append components/ReAct/safety
old81='它用 <b>Chain-of-Thought + ReAct</b> 在"Topics(意图)"上推理并遵守业务规则；标准请求端到端约 2–5 秒。Summer \'26 升级到 <b>Atlas 3.0</b> 作为多智能体编排的协调层。</p>'
new81=('它用 <b>Chain-of-Thought + ReAct（Reason→Act→Observe 循环）</b>在"Topics/子智能体(意图)"上推理并遵守业务规则；标准请求端到端约 2–5 秒。Summer \'26 升级到 <b>Atlas 3.0</b> 作为多智能体编排的协调层。</p>'
 '\n      <p><span class="pill b">据官方工程博客/Atlas 页与第三方解读补全</span> 更细的引擎视图可拆为<b>五组件</b>：Planner(规划)、Action Selector(选工具)、Tool Engine(执行 Flow/Apex/API/MCP)、Memory(短期对话+长期知识)、<b>Reflectors(反思器，评估结果并决定是否重规划/自纠错)</b>；并叠加三类<b>安全控制</b>：白名单(限定可调用工具)、验证器(执行前校验参数)、步数限制器(防无限循环)。引擎<b>模型无关(model-agnostic)</b>，可切换底层 LLM 而不改推理逻辑。<span class="pill r">注：竞品报告B 关于"Agent Script 为 TypeScript 开源语言/github 仓库/config:model=gpt-4o 语法"等具体说法，与官方开发者指南不符，本报告未采纳（详见附D）。</span></p>')
rep(old81,new81)

open(F,"w",encoding="utf-8").write(h)
print("patch6 OK; 30余年:", h.count("30 余年"), "| size MB:", round(len(h.encode('utf-8'))/1e6,2))
