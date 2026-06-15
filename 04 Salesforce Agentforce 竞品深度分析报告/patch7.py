F="Salesforce_Agentforce_竞品深度分析_v3_20260615.html"; h=open(F,encoding="utf-8").read()
def rep(old,new):
    global h
    if h.count(old)<1: raise SystemExit("NOT FOUND: "+old[:60])
    h=h.replace(old,new,1)

# TOC entry
rep('      <a href="#sec-ref"><span class="num">附</span>参考材料说明</a>',
    '      <a href="#sec-crosscheck"><span class="num">附D</span>三版报告交叉核对与改动清单</a>\n      <a href="#sec-ref"><span class="num">附</span>参考材料说明</a>')

D='''    <!-- ===== 附D 三版交叉核对 ===== -->
    <section id="sec-crosscheck">
      <h2 class="sec"><span class="idx">附D</span>三版报告交叉核对与改动清单</h2>
      <p class="lead">本节将本报告（Claude 版）与你提供的另两版报告——<b>报告A</b>（约 89KB、Codex/QoderWork 之一，保守严谨、逐条标注证据等级）与<b>报告B</b>（约 291KB、另一版，逐屏极细、信息量最大）——逐模块比对，说明本 v3 合入了哪些改进、拒绝了哪些不准确说法，并给出改动清单。<b>仅改动内容，未改报告框架、样式与产品缩略图。</b></p>

      <h3>D.1 总体评价</h3>
      <ul>
        <li><b>报告A：</b>结论保守、可核验，逐条用【分析推断】/【规划建议】/【证据限制】分级；客户与定价不堆数字。与本报告在"masking 对智能体失效""平台后台化割裂"等判断<b>高度一致</b>。</li>
        <li><b>报告B：</b>覆盖最全、细节最多（含逐屏截图解读、三模型定价、客户 logo、Atlas 五组件）；但<b>夹带个别疑似臆造的具体技术细节</b>（见 D.3），引用需甄别。</li>
        <li><b>本报告（基准）：</b>以"196 张截图 + 官方一手文档浏览器内核验"为锚，证据强度分级（附B）、官方精读（附C）、部署边界（C.8）。本 v3 在保持准确性的前提下，吸收 A/B 的可靠增量。</li>
      </ul>

      <h3>D.2 本次合入的改进（v3 采纳 A/B）</h3>
      <table>
        <thead><tr><th style="width:120px">模块</th><th>改动</th><th>来源</th><th style="width:120px">采纳理由</th></tr></thead>
        <tbody>
          <tr><td>7.1 定价</td><td>升级为<b>三模型完整结构</b>：会话 $2（多币种）/ 弹性信用 $500·10万（不滚存·无罚金）/ 按用户 $125–$550（Agentforce 1 $550 含年度信用池）；新增 Foundations 免费层(前 1,000 次会话)与 Digital Wallet、">20 动作选会话"决策法则。</td><td>报告B + 第三方多源核验</td><td>更完整且经独立核验，显著提升 §7 准确度</td></tr>
          <tr><td>7.2 客户案例</td><td>在已核验案例外，<b>扩充官方公开 logo</b>（SharkNinja/Indeed/Heathrow/Equinox/Fujitsu/Finnair/Prudential/Engine/Nexo/Reddit），并明确标注"未逐一独立核验"。</td><td>报告B/A</td><td>覆盖更全，同时诚实分级</td></tr>
          <tr><td>8.1 Atlas</td><td>补充<b>五组件（含 Reflectors 反思器）+ ReAct(Reason-Act-Observe) + 安全控制（白名单/验证器/步数限制）+ 模型无关</b>，标注证据来源。</td><td>报告B + 官方工程博客/Atlas 页</td><td>与官方一致，增强技术壁垒深度</td></tr>
          <tr><td>全局</td><td>金蝶管理实践年限由"30 年"改为"<b>30 余年</b>"模糊表述。</td><td>你的人工裁定</td><td>规避 30/33 年口径争议</td></tr>
        </tbody>
      </table>

      <h3>D.3 未采纳：报告B 中疑似不准确/无法核实的说法（保留本报告口径）</h3>
      <table>
        <thead><tr><th style="width:170px">项</th><th>报告B 的说法</th><th>本报告口径（更准确）</th></tr></thead>
        <tbody>
          <tr><td>Agent Script 性质</td><td>"基于 TypeScript 的<b>开源</b>语言、缩进敏感、托管于 <b>github.com/salesforce/agentscript</b>、<code>config: model=gpt-4o, temperature=0.7</code> 语法、before/after_reasoning 钩子"</td><td>官方开发者指南只称其为"自然语言指令 + 程序化表达式(if/else、transitions、变量、选择子智能体/动作)的声明式脚本"；<b>未见开源/TypeScript/该 github 仓库/上述语法</b>，截图脚本视图字段为 agent_label/agent_template/developer_name/agent_type。→ 疑似臆造，不采纳。</td></tr>
          <tr><td>会话变量命名</td><td>"以 <code>$Session</code> 命名空间组织，如 $Session.UserId / $Session.ChannelId"</td><td>截图实际变量为 EndUserId / RoutableId / ContactId / ChannelType（来源"消息传递会话"）。→ 以截图为准，不采纳 $Session 命名。</td></tr>
          <tr><td>规模数字</td><td>"处理超过 <b>100 万</b>次客户支持请求""2100 万+ 开发者"</td><td>本报告采用 Salesforce Q3 FY26 财报口径（3.2 万亿 tokens、9,500+ 付费成交等）；开发者生态等营销数字不作为结论。→ 口径不同，保留更可核验者。</td></tr>
          <tr><td>子智能体/工具计数</td><td>"二十余种预置子智能体""数十种预置工具"</td><td>本报告只就截图可数者表述（如资产库该演示环境 73 个工具），不外推为产品级总量。</td></tr>
        </tbody>
      </table>
      <p class="muted">说明：上述"不采纳"不代表报告B 整体不可信——其结构与多数功能描述准确且详尽；仅这几处具体技术细节缺乏官方支撑，按"宁缺毋滥"原则排除。</p>

      <h3>D.4 三版互相印证、可信度高的共识结论</h3>
      <ul>
        <li><b>Agentforce 不是"会创建智能体"，而是"构建—测试—发布—观测—优化"的全生命周期运营平台</b>（三版一致）。</li>
        <li><b>Trust Layer 的数据掩码"对自主智能体默认失效"</b>——报告A 与本报告均明确指出（B 未强调），是重要的平衡判断。</li>
        <li><b>"确定性三明治" + 测试/Trace 前置 + MCP 工具治理</b>三项为核心可借鉴点（三版一致）。</li>
        <li><b>风险：平台后台化割裂、消费式计价成本焦虑、通用 vs ERP 垂直的定位选择</b>（三版一致）。</li>
      </ul>

      <h3>D.5 改动点清单（v3 相对上一版 / changelog）</h3>
      <ol>
        <li>【§7.1】定价表重写为三模型完整结构 + 免费层/Digital Wallet/决策法则（来源：报告B + 第三方核验）。</li>
        <li>【§7.2】客户案例：保留 3 个已核验案例并加"已核验"标签；新增官方公开 logo 列表并标"未逐一独立核验"。</li>
        <li>【§8.1】Atlas：补五组件(含 Reflectors)+ReAct+安全控制+模型无关，并加一条"未采纳 B 的 Agent Script 臆造说法"提示。</li>
        <li>【全局】"30 年"→"30 余年"（5 处）。</li>
        <li>【新增】本附D：三版交叉核对、采纳/未采纳清单、共识结论与本 changelog。</li>
        <li>【未改】报告整体框架、前端样式、产品截图/缩略图（图 1–17）、附A/附B/附C/C.8 及其余结论一律保持不变。</li>
      </ol>

      <div class="src"><b>附D 依据：</b>用户提供的报告A（Salesforce_Agentforce_竞品分析_20260611.html）、报告B（…_v2_20260612.html）逐段比对；定价交叉核验见 <a href="https://www.jitendrazaa.com/blog/salesforce/salesforce-agentforce-credits-cost-model-complete-guide-2026/">Agentforce 定价 2026 指南</a> 等多源；Agent Script 口径见 <a href="https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-agents.html">开发者指南</a>。</div>
    </section>

'''
rep('    <!-- ===== 附 参考材料 ===== -->', D+'    <!-- ===== 附 参考材料 ===== -->')

open(F,"w",encoding="utf-8").write(h)
print("patch7 OK size MB:", round(len(h.encode('utf-8'))/1e6,2))
