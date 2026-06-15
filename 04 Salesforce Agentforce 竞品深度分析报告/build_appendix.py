import re, html as H
cat = open("_catalog.md", encoding="utf-8").read().splitlines()

# --- convert catalog markdown -> appendix HTML ---
out = []
out.append('<section id="sec-appendix">')
out.append('<h2 class="sec"><span class="idx">附A</span>全量截图分析（196 张 / 10 模块）</h2>')
out.append('<p class="lead">本附录对用户提供的 <b>全部 196 张 Agentforce Studio 截图逐张分析</b>（按模块组织，可展开查看每张截图的功能说明）。每个模块含「模块综合」，文末为本轮全量分析相对首版报告的新增洞察。</p>')

def flush_ul(buf):
    if buf:
        out.append("<ul>"+"".join(f"<li>{x}</li>" for x in buf)+"</ul>")
        buf.clear()

ulbuf=[]
in_module=False
mode=None  # None | 'modules' | 'conclusion'

def close_module():
    global in_module
    if in_module:
        flush_ul(ulbuf)
        out.append("</div></details>")
        in_module=False

def md_inline(s):
    s=H.escape(s)
    s=re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s=re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    return s

for raw in cat:
    line=raw.rstrip()
    if not line.strip():
        continue
    if line.startswith("# "):  # catalog title
        continue
    if line.startswith("## 模块"):
        close_module()
        flush_ul(ulbuf)
        title=md_inline(line[3:].strip())
        out.append(f'<details open><summary>{title}</summary><div class="card" style="margin-top:10px">')
        in_module=True
        mode='modules'
        continue
    if line.startswith("## 全量分析结论"):
        close_module()
        flush_ul(ulbuf)
        mode='conclusion'
        out.append('<div class="callout borrow" style="margin-top:18px"><div class="tag">🔎 全量分析新增洞察（相对首版报告）</div>')
        continue
    if line.startswith("### "):
        flush_ul(ulbuf)
        out.append(f'<h4>{md_inline(line[4:].strip())}</h4>')
        continue
    if line.startswith("- "):
        ulbuf.append(md_inline(line[2:].strip()))
        continue
    m=re.match(r'^\d+\.\s+(.*)', line)
    if m:
        ulbuf.append(md_inline(m.group(1)))
        continue
    if line.startswith("---"):
        flush_ul(ulbuf)
        continue
    if line.startswith("=>"):
        flush_ul(ulbuf)
        out.append(f'<p class="note">{md_inline(line[2:].strip())}</p>')
        continue
    # plain paragraph
    flush_ul(ulbuf)
    out.append(f'<p>{md_inline(line)}</p>')

# close any open
flush_ul(ulbuf)
if mode=='conclusion':
    out.append('</div>')  # close callout
close_module()
out.append('<div class="src"><b>来源：</b>用户提供「Agentforce Studio 截图原图」196 张（10 模块）逐张分析；本附录为完整证据清单，正文图 1–17 为其中关键截图。</div>')
out.append('</section>')
appendix = "\n".join(out)

# --- inject into report ---
p="agentforce_report.html"
h=open(p,encoding="utf-8").read()

# 1) TOC entry before the 附 ref link
toc_old='      <a href="#sec-ref"><span class="num">附</span>参考材料说明</a>'
toc_new='      <a href="#sec-appendix"><span class="num">附A</span>全量截图分析（196张）</a>\n'+toc_old
assert toc_old in h, "TOC anchor not found"
h=h.replace(toc_old, toc_new, 1)

# 2) insert appendix before sec-ref section
anchor='    <!-- ===== 附 参考材料 ===== -->'
assert anchor in h, "ref section anchor not found"
h=h.replace(anchor, appendix+"\n\n"+anchor, 1)

# 3) JS uses #toc a list dynamically -> fine. Update cover methodology note to assert full analysis
note_old='每个章节均标注来源链接，结论区分「可借鉴点」与「需规避风险」。'
note_new='每个章节均标注来源链接，结论区分「可借鉴点」与「需规避风险」；<b>全部 196 张截图已逐张分析，完整清单见文末「附A 全量截图分析」</b>。'
h=h.replace(note_old, note_new, 1)

open(p,"w",encoding="utf-8").write(h)
print("appendix chars:",len(appendix))
print("details blocks:",appendix.count("<details"))
print("li items:",appendix.count("<li>"))
print("html size MB:",round(len(h.encode('utf-8'))/1e6,2))
