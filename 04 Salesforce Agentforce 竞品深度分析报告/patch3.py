p="agentforce_report.html"; h=open(p,encoding="utf-8").read()
log=[]
def rep(old,new,req=True):
    global h
    c=h.count(old)
    log.append((c, old[:46]))
    if c<1 and req: raise SystemExit("NOT FOUND: "+old[:70])
    h=h.replace(old,new,1)

# 1) TOC: add 附C after 附B (i.e., before 附 ref)
rep('      <a href="#sec-ref"><span class="num">附</span>参考材料说明</a>',
    '      <a href="#sec-officialdocs"><span class="num">附C</span>官方文档精读核证</a>\n      <a href="#sec-ref"><span class="num">附</span>参考材料说明</a>')

# 2) Upgrade 附B table rows
rep('<tr><td>3 产品概览 / 4 功能模块 / 5 全生命周期</td><td>196 张截图直接佐证为主，辅以官方文档</td><td><span class="s">强</span></td></tr>',
    '<tr><td>3 产品概览 / 4 功能模块 / 5 全生命周期</td><td>196 张截图直证 + 开发者指南官方原文佐证（Agent Script/Actions/测试三法/会话 Trace 导出，见附C）</td><td><span class="s">强（已升级）</span></td></tr>')
rep('<tr><td>8 技术壁垒（信任层/数据/平台原语）</td><td>信任层文档已核验；Atlas 内部机制部分依赖工程博客与第三方解读</td><td><span class="w">中</span></td></tr>',
    '<tr><td>8 技术壁垒（信任层/数据/平台原语）</td><td>信任层文档已核验；Atlas 评估框架/路线图官方页佐证（附C）；唯"飞轮"内部细节仍依赖工程博客解读</td><td><span class="s">较强（已升级）</span></td></tr>')
rep('<tr><td>9 市场定位</td><td>Gartner/IDC + 官方叙事；竞争象限为分析推断</td><td><span class="w">中</span></td></tr>',
    '<tr><td>9 市场定位</td><td>Forrester Wave 客服方案 Q1 2026 列 Salesforce 为 Leader（并示警定价/ROI，见附C）+ Gartner/IDC；唯竞争象限仍为分析推断</td><td><span class="s">较强（已升级）</span></td></tr>')

# 3) Update 附B gap line (Grid/Data Prism now covered)
rep('帮助文档其余子章节（设计和实现代理、平台参考、提示生成器、生成式 AI 分析）逐篇精读；补研本报告<b>未覆盖</b>的 <b>Agentforce Grid</b> 与 <b>Einstein Data Prism（爱因斯坦数据棱镜）</b>两个文档主题。',
    '<b>已补：</b>Agentforce Grid 与 Einstein Data Prism（爱因斯坦数据棱镜）已精读并写入<b>附C</b>；开发者指南 get-started/agents/actions 已官方精读。<b>仍可继续：</b>帮助文档"设计和实现代理/平台参考"等子章节为 JS 单页应用、本轮渲染受限未逐屏精读，可后续补。')

# 4) §9 summary: insert Forrester sentence
rep('但承受行业级 ROI 与兑现质疑。灵基应<b>同象限错位</b>',
    '但承受行业级 ROI 与兑现质疑（Forrester Wave 客服方案 Q1 2026 在肯定其 Leader 地位的同时，亦点名"定价复杂、AI 智能体价值兑现较慢"——与本报告风险判断一致）。灵基应<b>同象限错位</b>')

# 5) §4.2 heading rename note
rep('4.2 子智能体(Topic)与工具(Action)：分层结构是核心抽象',
    '4.2 子智能体(Topic／2026-04 官方更名 Subagent)与工具(Action)：分层结构是核心抽象')

# 6) §4 summary: append official + Grid note
rep('需规避的是把过多专业配置暴露给业务用户，以及对尚未 GA 的编排/DSL 过度对标。</div>',
    '需规避的是把过多专业配置暴露给业务用户，以及对尚未 GA 的编排/DSL 过度对标。<br><b>官方佐证（附C）：</b>开发者指南证实 Agent Script 即"自然语言指令 + 确定性表达式(if/else、转换、变量、选择子智能体/动作)"的混合编排；另 Winter ’26 新增 <b>Agentforce Grid</b>（AI 原生电子表格，批量跑智能体/动作并回归）与 <b>Einstein Data Prism</b>（语义接地层降幻觉）两项值得灵基借鉴的能力。</div>')

# 7) Insert 附C before 附 ref
C = '''    <!-- ===== 附C 官方文档精读核证 ===== -->
    <section id="sec-officialdocs">
      <h2 class="sec"><span class="idx">附C</span>官方文档精读核证（开发者指南 + 帮助文档）</h2>
      <p class="lead">应你要求，对此前"仅引用未精读"的<b>开发者指南</b>与<b>帮助文档</b>做了浏览器内精读，用一手官方表述强化结论，并补全此前未覆盖的两个主题。下列每条均给出官方出处；据此第 4/5/8/9 节的证据强度已在「附B」上调。</p>

      <h3>C.1 开发者指南 developer.salesforce.com（已精读）</h3>
      <table>
        <thead><tr><th style="width:220px">官方要点</th><th>原文/含义</th><th style="width:90px">印证</th></tr></thead>
        <tbody>
          <tr><td>Agentforce 定位</td><td>"the agent-driven layer of the Salesforce Platform … AI agents work side-by-side with employees … 24/7；Trust Layer securely connects your data with LLMs."</td><td>§3 / §8</td></tr>
          <tr><td>Topic→Subagent 改名</td><td>"Beginning in April 2026, agent topics are now called subagents."（功能不变）</td><td>§4 术语</td></tr>
          <tr><td>Agent Script 定义</td><td>"自然语言指令 + 程序化表达式：用表达式定义 if/else、transitions、set/modify/compare 变量、选择 subagents 与 actions；构建不依赖 LLM 解释的可预测工作流。"</td><td>§4.1/4.2（升级）</td></tr>
          <tr><td>开发/集成全家桶</td><td>Agent Script、Agentforce DX(CLI/VS Code)、Python SDK、Agent API(REST)、Custom Connections、Mobile SDK(iOS/Android)、Enhanced Chat v2、In-App Chat SDK(人在环升级带完整上下文)、ADL API、Export Session Tracing Data(整段会话 Trace 统一 JSON)。</td><td>§4/§5（升级）</td></tr>
          <tr><td>测试三法</td><td>Testing Center(UI/CSV/无自定义评估)、Agentforce DX(CLI/YAML/支持自定义评估)、Testing API(代码/XML/支持自定义评估)。</td><td>§5（升级）</td></tr>
          <tr><td>Actions 来源</td><td>Apex REST、AuraEnabled、Named Query(SOQL)、Apex Invocable Method；Lightning Types 富 UI；Apex Citations（为知识/PDF/URL 生成内联引文）。</td><td>§4.2/4.3</td></tr>
        </tbody>
      </table>

      <h3>C.2 帮助文档 help.salesforce.com（信任层逐条核验 + Atlas 官方页）</h3>
      <ul>
        <li><b>Einstein 信任层（原文核验）：</b>零数据保留政策、LLM 数据掩码、毒性评分审查、审计追踪、"通过引用建立信任"——第 6/8 节据原文确认。</li>
        <li><b>Atlas 评估框架（官方"What's next"）：</b>评估 <i>action outcomes / inputs / outputs / planning accuracy / subagent classification / planner state</i>，按 <i>accuracy / latency / cost to serve / trust</i> 优化，专为 CRM 业务场景，并称"发布了全球首个 LLM 基准"。→ 把第 5/8 节"工程化评估"从截图推断升级为官方佐证。</li>
        <li><b>Atlas 路线图（官方）：</b>多意图(multi-intent)、多模态(语音/视觉)、多智能体(A2A)。→ 印证 §4.6 与语音能力。</li>
      </ul>

      <h3>C.3 此前未覆盖、现已补全的两个主题</h3>
      <div class="grid2">
        <div class="card"><h4>Agentforce Grid（Winter ’26）</h4><p class="muted">内置 Salesforce 的<b>"AI 原生电子表格"</b>：Data 列(CSV/Salesforce/Data Cloud) + Action 列(提示模板/已建智能体/内联提示，及公式/更新记录/调用流等确定性动作)；可对大量记录<b>批量跑 AI 工作流</b>、挖掘洞察、<b>批量测试多轮对话</b>；按行列扫描发现差异/异常，点开单元格看完整 API 响应。</p><p><span class="pill g">借鉴</span> 用"表格范式"做批量智能体/动作执行与回归，是企业规模化+可观测的新交互。</p></div>
        <div class="card"><h4>Einstein Data Prism</h4><p class="muted">生成式 AI 的<b>"语义接地层"</b>：为 Data Cloud schema 补充语义描述、把自然语言短语与数据字段对齐，回传聚焦的接地数据以<b>降低幻觉</b>。</p><p><span class="pill g">借鉴</span> 在数据中台之上建"语义层"，提升 自然语言→ERP 数据 的检索准确率。</p></div>
      </div>

      <h3>C.4 第三方/分析机构强化（市场定位）</h3>
      <ul>
        <li><b>Forrester Wave：客户服务解决方案 Q1 2026</b> —— Salesforce 列为 <b>Leader</b>（企业级规模 + Agentforce Service 势能），同时<b>明确点名"定价复杂、AI 智能体价值兑现较慢"为注意点</b>（独立印证本报告"定价/ROI"风险判断）。其余 Leader：Microsoft、Pegasystems、ServiceNow。</li>
        <li><b>规模数据（官方/媒体）：</b>约一年处理 300 万次服务对话；支持工单同比 -8%（约 17 万件更少）；月工作流约 30 亿。<span class="muted">（"18,500"在不同口径下被表述为"成交/客户"，引用时需注明口径。）</span></li>
      </ul>

      <div class="src"><b>附C 来源：</b><a href="https://developer.salesforce.com/docs/ai/agentforce/guide/get-started.html">开发者指南·Get Started</a> · <a href="https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-agents.html">APIs & SDKs</a> · <a href="https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-actions.html">Actions</a>；<a href="https://www.salesforce.com/agentforce/what-is-a-reasoning-engine/atlas/">Atlas 推理引擎页</a>；<a href="https://help.salesforce.com/s/articleView?id=ai.generative_ai_trust_layer.htm&type=5">信任层文档</a>；<a href="https://help.salesforce.com/s/articleView?id=ai.agentforce_grid.htm&language=en_US&type=5">Agentforce Grid</a> · <a href="https://help.salesforce.com/s/articleView?id=ai.generative_ai_prism.htm&language=en_US&type=5">Einstein Data Prism</a>；<a href="https://www.salesforce.com/blog/salesforce-2026-forrester-wave-b2b/">Forrester Wave 2026</a> 及 <a href="https://www.cxtoday.com/ai-automation-in-cx/the-forrester-wave-says-ai-will-run-customer-service-cx-leaders-need-a-new-operating-model/">客服方案 Q1 2026 解读</a>。</div>
    </section>

'''
rep('    <!-- ===== 附 参考材料 ===== -->', C+'    <!-- ===== 附 参考材料 ===== -->')

open(p,"w",encoding="utf-8").write(h)
for c,s in log: print(c, s)
print("size MB:", round(len(h.encode('utf-8'))/1e6,2))
