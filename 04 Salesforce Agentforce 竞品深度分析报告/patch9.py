F="Salesforce_Agentforce_竞品深度分析_v3_20260615.html"; h=open(F,encoding="utf-8").read()
def rep(o,n):
    global h
    if h.count(o)<1: raise SystemExit("NF: "+o[:50])
    h=h.replace(o,n,1)

# F1 §2 KPI 84% mislabel
rep('<div class="b"><div class="n">~84%</div><div class="l">客服场景自主解决率（官方案例）</div></div>',
    '<div class="b"><div class="n">~84–85%</div><div class="l">Salesforce 自身 Help 部署(Customer Zero)，非平台普适</div></div>')

# F2 §2 risk Beta/GA staleness
rep('多智能体编排、评分器、健康监控等多为 Beta/发布期能力，避免对标尚未 GA 的承诺。',
    '多智能体编排已于 2026-06-15 GA，但评分器、健康监控、ADL API/高级 A2A 等部分能力仍 Beta；避免对标尚未 GA 的周边承诺。')

# F3 §4 module summary staleness
rep('需规避的是把过多专业配置暴露给业务用户，以及对尚未 GA 的编排/DSL 过度对标。',
    '需规避的是把过多专业配置暴露给业务用户，以及对仍处 Beta 的周边能力/尚未稳定的 DSL 过度对标（多智能体编排核心已于 2026-06-15 GA）。')

# F4 dates
rep('<span>更新时间：</span>2026-06-11',
    '<span>更新时间：</span>2026-06-11（初版）· 2026-06-15（v3 修订）')
rep('更新时间：2026-06-11 · 面向金蝶灵基 Build 智能体构建能力研发','更新时间：2026-06-15（v3 修订版）· 面向金蝶灵基 Build 智能体构建能力研发')

# F5 IDC overclaim
rep('<span class="chip">Gartner / IDC 第三方验证</span>','<span class="chip">Gartner（公开新闻稿）/ 行业第三方验证</span>')
rep('Gartner、IDC 及行业媒体的','Gartner（公开新闻稿）及行业媒体的')
rep('IDC/行业采用率统计(2026)。','行业采用率统计（公开二级资料，2026）。')
rep('采用率/ROI 统计：IDC 与行业报告(2026)','采用率/ROI 统计：行业公开报告(2026，二级资料)')

# F6 cover note GA framing
rep("Summer '26（2026-06-15 GA）的多智能体编排、Atlas 3.0、A2A 等为发布期能力，以官方 GA 为准。",
    "Summer '26 的多智能体编排、Atlas 3.0、A2A、MCP 集成已于 2026-06-15 GA；ADL API、高级 A2A 配置等周边仍 Beta（详见附C·C.9）。")

# F7 §8.2 trust layer caveat cross-ref
rep('PII 屏蔽、零数据保留、毒性检测、审计——把"可信"做进架构，而非应用层补丁。',
    'PII 屏蔽、零数据保留、毒性检测、审计——把"可信"做进架构，而非应用层补丁。（边界：数据掩码对自主"智能体"默认关闭、且模式掩码不支持中文，见 §6/附C·C.8。）')

# F8 YAML wording
rep('脚本视图是 YAML/DSL 形态的智能体定义','脚本视图是 YAML 风格的结构化文本（DSL）形态的智能体定义')

# F9 国内最 overclaims -> 分析推断
rep('是当前国内同类最稀缺的能力。','据我们观察，是国内同类产品普遍较薄弱的环节（分析推断）。')
rep('这是当前国内同类产品最大空白。','据我们观察，这是国内同类产品普遍较薄弱的环节（分析推断）。')

# F10 §8.2 20年
rep('复用 20 年沉淀的业务逻辑与集成','复用二十余年沉淀的业务逻辑与集成')

open(F,"w",encoding="utf-8").write(h)
print("patch9 OK size MB:",round(len(h.encode('utf-8'))/1e6,2))
