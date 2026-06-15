p="agentforce_report.html"
h=open(p,encoding="utf-8").read()
def rep(old,new,n=1,required=True):
    global h
    c=h.count(old)
    if c<1 and required: raise SystemExit("NOT FOUND: "+old[:60])
    h=h.replace(old,new,n)
    return c

# R1 KPI box (section 2)
rep('<div class="b"><div class="n">18,000+</div><div class="l">付费客户 / 121 国（截至 Q3 FY26）</div></div>',
    '<div class="b"><div class="n">9,500+</div><div class="l">付费成交（+50% QoQ，Q3 FY26；ARR +330% YoY）</div></div>')

# R2 section 7 platform numbers
rep('平台整体：18,000+ 付费客户 / 121 国；某客服部署自主解决率约 84%、仅 2% 需人工升级(官方案例)；Agentforce + Data 360 ARR 约 14 亿美元、9,500+ 付费成交(Salesforce 披露口径)。',
    '平台整体（Salesforce Q3 FY26 披露口径，2025-12-03）：自发布累计约 18,500 笔成交，其中 9,500+ 付费成交(+50% QoQ)；Agentforce ARR 半年突破 5 亿美元(+330% YoY)，Agentforce + Data 360 ARR 约 14 亿美元(+114% YoY)；LLM 网关累计处理约 3.2 万亿 tokens。某客服案例自主解决率约 84%、仅 2% 需人工升级。<b>更正：早前表述"18,000+ 付费客户/121 国"系把"累计成交数"误读为"客户数"，"121 国"未能核实，已修正。</b>')

# R3 deflection
rep('报税周自主解决 <b>70%</b> 在线咨询；首 24 小时处理 1,000+ 客户互动；预计偏转 65% 服务请求。',
    '报税周自主解决 <b>70%</b> 在线咨询；首 24 小时处理 1,000+ 客户互动（官方案例）。')

# R4 67% wording
rep('Salesforce 自身《连接性报告》预测<b>多智能体采用率到 2027 年将增长 67%</b>。',
    'Salesforce《第 11 次连接性基准报告》（2025 年 10–11 月、1,050 名 IT 领导）：组织平均使用 12 个智能体，<b>预计两年内智能体数量增长 67%</b>，但约 50% 智能体仍处"孤岛"未编排。')

# R5 GPT-5 Mini caveat (figure 8 caption only — uses ' + ' after)
rep('模型选择(GPT-5 Mini) + ','模型选择(该演示组织选用 GPT-5 Mini) + ')

# R6 analytics demo-data caveat (figure 15)
rep('信任 Tab 含"指令遵循率"与"平均毒性评分(0.12)"。来源：分析/09_分析_概述_信任度',
    '信任 Tab 含"指令遵循率"与"平均毒性评分(0.12)"。<b>注：图中数值来自 Developer Edition 演示组织的样本数据，非 Agentforce 产品性能基准，不可外推。</b>来源：分析/09_分析_概述_信任度')

# R8 competitive quadrant caveat
rep('横轴"通用 ↔ 业务垂直"、纵轴"自建框架 ↔ 平台开箱"：',
    '<span class="pill r">分析推断</span>（象限为简化示意、非量化定位）横轴"通用 ↔ 业务垂直"、纵轴"自建框架 ↔ 平台开箱"：')

# R11 73 tools caveat (appendix)
rep('资产库 73 个预置工具(Slack/CDP/安全/Knowledge等)',
    '资产库预置工具（该演示环境为 73 个，数量随版本/许可变化；Slack/CDP/安全/Knowledge 等）')

# R7 evidence legend after cover note
rep('为发布期能力，以官方 GA 为准。</div>',
    '为发布期能力，以官方 GA 为准。</div>\n      <div class="card"><b>证据强度图例（全文适用）：</b> <span class="pill b">实证·截图</span> 直接来自 196 张产品截图；<span class="pill b">官方文档</span> Salesforce 官网/帮助中心（信任层章节已在浏览器内逐条核验）；<span class="pill b">第三方</span> Gartner/IDC/财报/媒体；<span class="pill r">分析推断</span> 为本报告分析判断、非客观事实，需谨慎对待。完整证据强度、已更正项与待补研清单见文末「附B 证据强度与待修正」。</div>')

# R9 TOC entry for 附B
rep('      <a href="#sec-ref"><span class="num">附</span>参考材料说明</a>',
    '      <a href="#sec-evidence"><span class="num">附B</span>证据强度与待修正</a>\n      <a href="#sec-ref"><span class="num">附</span>参考材料说明</a>')

# R10 insert 附B section before ref
evi = '''    <!-- ===== 附B 证据强度与待修正 ===== -->
    <section id="sec-evidence">
      <h2 class="sec"><span class="idx">附B</span>证据强度与待修正说明</h2>
      <p class="lead">应你要求，本节透明披露各结论的证据来源与强度，标注属于「分析推断」的内容，列出已更正的事实性问题与仍需进一步核验/补研之处。</p>

      <h3>本轮核验补充（相对前两版）</h3>
      <p>① <b>全部 196 张截图</b>：逐张下采样核对，约 40 张单独打开精读、其余为同一流程的连续步骤/空态等变体（按规范化描述归并，未逐张独立展开）。② <b>帮助文档</b>「Agentforce 和 Einstein 生成式人工智能」为 JavaScript 单页应用，常规抓取仅得加载壳；本轮已<b>在浏览器内打开并逐条核验「爱因斯坦信任层」章节</b>——零数据保留政策、LLM 数据掩码、毒性评分审查、审计追踪、"通过引用建立信任"均与文档一致，第 6/8 节相关结论据此得到原文支撑。其余子章节（人工智能项目成功、设计和实现代理、爱因斯坦平台参考、提示生成器、生成式 AI 分析、<b>Agentforce Grid</b>、<b>爱因斯坦数据棱镜 Einstein Data Prism</b>）本轮仅浏览目录结构，<b>未逐篇精读</b>。③ 关键商业数字已回查 Salesforce 财报与官方案例。</p>

      <h3>各章节证据强度</h3>
      <table>
        <thead><tr><th style="width:180px">章节</th><th>主要证据</th><th style="width:90px">强度</th></tr></thead>
        <tbody>
          <tr><td>3 产品概览 / 4 功能模块 / 5 全生命周期</td><td>196 张截图直接佐证为主，辅以官方文档</td><td><span class="s">强</span></td></tr>
          <tr><td>6 用户体验</td><td>截图直证 + 信任层文档原文核验；评审判断含主观成分</td><td><span class="s">较强</span></td></tr>
          <tr><td>8 技术壁垒（信任层/数据/平台原语）</td><td>信任层文档已核验；Atlas 内部机制部分依赖工程博客与第三方解读</td><td><span class="w">中</span></td></tr>
          <tr><td>7 商业模式（定价/财务/案例）</td><td>财报 + 官方定价页 + 第三方测算；数字有口径差，已更正</td><td><span class="w">中</span></td></tr>
          <tr><td>9 市场定位</td><td>Gartner/IDC + 官方叙事；竞争象限为分析推断</td><td><span class="w">中</span></td></tr>
          <tr><td>2 核心结论 / 10 规划建议</td><td>综合以上的<b>分析判断与建议</b>，非客观事实</td><td><span class="n">分析推断</span></td></tr>
        </tbody>
      </table>

      <h3>已更正的事实性问题（本轮）</h3>
      <div class="callout risk"><div class="tag">⚠️ 已更正</div><ul>
        <li><b>"18,000+ 付费客户 / 121 国" → 更正</b>：Q3 FY26 实为"自发布累计约 18,500 笔成交、其中 9,500+ 付费成交(+50% QoQ)"；"客户数"系对"成交数"的误读，"121 国"未能核实，已移除。</li>
        <li><b>多智能体"67%"措辞 → 精确化</b>：为"组织平均 12 个智能体、预计两年内数量 +67%"（第 11 次连接性基准报告，1,050 名 IT 领导），非笼统"采用率"。</li>
        <li><b>1-800Accountant"预计偏转 65%" → 移除</b>：保留官方确证口径（报税周自主解决 70%、24 小时内 1,000+ 互动）。</li>
        <li><b>演示数据加注</b>：分析模块数字（参与率 52.38%/成功率 34.04%/质量分等）、资产库"73 个工具"、模型"GPT-5 Mini"均为 Developer Edition 演示组织口径，已在相应图注/附录标注"非产品基准、随版本变化"。</li>
      </ul></div>

      <h3>属于「分析推断」、需谨慎对待</h3>
      <div class="callout risk"><div class="tag">⚠️ 分析推断（非事实）</div><ul>
        <li>第 <b>10 节全部规划建议</b>、第 2 节"TOP6 可借鉴/风险"的<b>优先级排序</b>、第 9 节<b>竞争格局象限</b>——均为本报告的分析判断与建议，供决策参考，不应作为 Salesforce 客观事实引用。</li>
        <li>全文"<b>灵基应/宜……</b>"等措辞均为建议而非结论。</li>
        <li>"Agentforce 最强护城河是工程化闭环/数据底座"等<b>定性判断</b>系基于证据的推断，非官方表述。</li>
      </ul></div>

      <h3>仍建议进一步核验 / 补研</h3>
      <div class="callout borrow"><div class="tag">✅ 后续可补</div><ul>
        <li>帮助文档其余子章节（设计和实现代理、平台参考、提示生成器、生成式 AI 分析）逐篇精读；补研本报告<b>未覆盖</b>的 <b>Agentforce Grid</b> 与 <b>Einstein Data Prism（爱因斯坦数据棱镜）</b>两个文档主题。</li>
        <li>定价（$2/会话、弹性信用单价）以最新官方定价页/计算器为准，随合同与版本浮动。</li>
        <li>客户成功指标（84% 自主解决 / Wiley 213% ROI / 1-800Accountant 70%）均为<b>单个客户官方案例</b>，非平台普适值，引用时须标注主体与场景。</li>
        <li>Summer '26 多智能体编排、Atlas 3.0、A2A 等以官方 GA 为准。</li>
        <li>如需"每张截图独立成行 + 配缩略图"的完整图录，可在附 A 基础上进一步扩展。</li>
      </ul></div>

      <div class="src"><b>本节核验来源：</b><a href="https://help.salesforce.com/s/articleView?id=ai.generative_ai_trust_layer.htm&type=5">Einstein 信任层帮助文档（浏览器内核验）</a>；<a href="https://www.salesforce.com/news/press-releases/2025/12/03/fy26-q3-earnings/">Salesforce Q3 FY26 财报</a>；<a href="https://www.salesforce.com/news/stories/connectivity-report-announcement-2026/">第 11 次连接性基准报告</a>；<a href="https://www.salesforce.com/customer-stories/wiley/">Wiley 案例</a>；<a href="https://1800accountant.com/blog/how-1800accountant-uses-agentforce">1-800Accountant 案例</a>。</div>
    </section>

'''
rep('    <!-- ===== 附 参考材料 ===== -->', evi+'    <!-- ===== 附 参考材料 ===== -->')

open(p,"w",encoding="utf-8").write(h)
print("OK; size MB:",round(len(h.encode('utf-8'))/1e6,2))
