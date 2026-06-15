p="agentforce_report.html"; h=open(p,encoding="utf-8").read()
def rep(old,new):
    global h
    if h.count(old)<1: raise SystemExit("NOT FOUND: "+old[:60])
    h=h.replace(old,new,1)

# C.8 before 附C src
add='''      <h3>C.8 企业部署边界与本地化缺口（帮助文档"平台参考/信任层限制/区域语言"，已精读）</h3>
      <p>这是评估"企业级落地与中国市场适配"最关键的一组官方边界信息：</p>
      <table>
        <thead><tr><th style="width:200px">边界项</th><th>官方口径</th><th style="width:96px">对灵基含义</th></tr></thead>
        <tbody>
          <tr><td>可用版本/许可</td><td>仅 Enterprise / Performance / Unlimited / Developer 版，且需 Einstein for Sales/Platform/Service 等<b>付费附加许可</b>；按智能体类型而异。</td><td><span class="n">成本门槛</span></td></tr>
          <tr><td>速率限制(Rate Limits)</td><td>存在<b>按模型的速率限制</b>，提额需联系客户经理。</td><td><span class="w">吞吐受限</span></td></tr>
          <tr><td>地理感知路由</td><td>LLM 请求路由到离实例<b>最近的服务器</b>(geo-aware)，涉及数据驻留/合规。</td><td><span class="s">可借鉴</span></td></tr>
          <tr><td>信任层掩码对"智能体"失效</td><td>官方原文："<b>Data masking for LLMs is disabled for agents</b>"；掩码主要作用于嵌入式生成式功能(Service Replies/Work Summaries)，而非自主智能体。</td><td><span class="n">需注意(平衡)</span></td></tr>
          <tr><td>掩码语言覆盖</td><td>基于<b>字段</b>的掩码支持所有 Salesforce 语言；基于<b>模式</b>的 PII 掩码仅支持<b>英/法/德/意/日/西</b>——<b>不含中文</b>。</td><td><span class="s">本地化机会</span></td></tr>
          <tr><td>沙盒限制</td><td>信任层在 Sandbox 暂存环境可用但有限制；Data 360 对象接地不可在暂存测试；沙盒与生产配置可能不同步。</td><td><span class="w">交付摩擦</span></td></tr>
          <tr><td>权限</td><td>Prompt Builder 需 Prompt Template Manager 权限集；查看掩码报表需 Data Cloud User。</td><td>—</td></tr>
        </tbody>
      </table>
      <div class="callout borrow"><div class="tag">✅ 由"边界"反推的两条灵基机会</div><ul>
        <li><b>原生中文 PII/合规掩码</b>：Salesforce 基于模式的掩码不覆盖中文，灵基以"中文优先 + 字段级/模式级双掩码 + 适配《个人信息保护法》/数据出境"做差异化，是国央企采购硬通货。</li>
        <li><b>掩码对智能体同样生效</b>：把"数据掩码/脱敏在自主智能体链路中也默认生效"作为卖点，正好补 Agentforce"masking disabled for agents"的空档。</li>
      </ul></div>
      <div class="callout risk"><div class="tag">⚠️ 平衡更正（对前文的修正）</div><p style="margin:4px 0">前文第 6/8 节将"信任层数据掩码"作为 Agentforce 强项；据官方《信任层限制》需补一条平衡：<b>该掩码对自主"智能体"默认是关闭的</b>，主要覆盖嵌入式生成式功能。引用其"合规前置"优势时应注明此边界。</p></div>

'''
rep('      <div class="src"><b>附C 来源：</b>', add+'      <div class="src"><b>附C 来源：</b>')

# extend src links
rep('<a href="https://www.salesforce.com/blog/salesforce-2026-forrester-wave-b2b/">Forrester Wave 2026</a>',
    '<a href="https://help.salesforce.com/s/articleView?id=ai.generative_ai_parent_reference.htm&type=5">平台参考</a> · <a href="https://help.salesforce.com/s/articleView?id=ai.generative_ai_trust_limits.htm&type=5">信任层限制</a> · <a href="https://help.salesforce.com/s/articleView?id=ai.generative_ai_trust_lang_region.htm&type=5">区域与语言支持</a> · <a href="https://www.salesforce.com/blog/salesforce-2026-forrester-wave-b2b/">Forrester Wave 2026</a>')

# §6 balance nuance
rep('让管理员无需在每个智能体里重复配置合规——这对受监管行业的采购决策极为关键。',
    '让管理员无需在每个智能体里重复配置合规——这对受监管行业的采购决策极为关键。<b>但需平衡指出（官方《信任层限制》）：数据掩码对自主"智能体"默认关闭、主要作用于嵌入式生成式功能；且基于模式的 PII 掩码不支持中文（详见附C·C.8）——这恰是灵基的本地化机会。</b>')

# update 附B gap line
rep('帮助文档"Einstein 平台参考"(对象/限制/区域等参考资料)、纯营销页(概述/工作原理/why/for-employees)、以及需交互输入的"弹性信用计算器"(避免编造数字)。',
    '纯营销页(概述/工作原理/why/for-employees)与需交互输入的"弹性信用计算器"(避免编造数字)。<b>帮助文档"Einstein 平台参考/信任层限制/区域语言支持"已于本轮精读，企业部署边界写入附C·C.8。</b>')

open(p,"w",encoding="utf-8").write(h)
print("OK size MB:",round(len(h.encode('utf-8'))/1e6,2))
