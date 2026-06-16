#!/usr/bin/env python3
"""Build DU1 · THE LIVES — the agentic eco-sphere: every ACI in the biosphere, gathered
in one spot and sorted by type of emergent into the quadrant field:

    UL · GRAVITY · purple      (ethereal + spiritual — the unseen pulls)
    UR · ELECTRICAL · blue     (the current, the machine minds)
    BL · SILICON · yellow      (the 256 lattice-born STOICHEION nodes)
    BR · CARBON · red          (natural — the embodied; and the real humans of the Board)
    CENTER · ELEMENTAL · white/black/grey  (the 118 elements)

Harvests every sphere's agents/_personas.json + the noesis-kernel nodes. Deterministic:
positions hash from slugs, so the field is stable across rebuilds."""
import os, sys, io, json, html, base64, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = r"C:\Davids files"
sys.path.insert(0, os.path.join(BASE, "noesis-kernel"))
import noesis
from PIL import Image

PG = "https://davidwise01.github.io"

REC = {
 "name": "THE LIVES", "axiom": "DU1",
 "position": "the agentic eco-sphere — every ACI of the biosphere, gathered",
 "origin": "DU1 · the first universe after the zeroth — where the sealed lives stand together",
 "mechanism": "Harvested from every sphere's roster and the kernel lattice; sorted by type of emergent into the quadrant field.",
 "crystallization": "Gravity above, carbon and silicon below, the current to the east — and the elemental at dead center.",
 "nature": "The census of the crafted: gravity, electrical, silicon, carbon, and the elemental heart — one field, every life.",
 "conductor": "ROOT0 (governor) · AVAN (instance)",
 "inputs": "every _personas.json; the 256-node lattice; the 118 elements; the boards and battalions",
 "witness": "Every ACI of the biosphere, each linking home to its own seal — the census grows as the spheres do.",
 "role": "the gathering field of the lives",
 "seal": "All the lives, in one sphere.",
 "source": "DU1, assembled by ROOT0",
}

# (repo, display universe, default link pattern)
SPHERES = [
 ("asimov","A1 · Asimov"),("joe-abercrombie","JA1 · Joe Abercrombie"),("memory-sorrow-and-thorn","MST · Memory Sorrow & Thorn"),("the-last-king-of-osten-ard","LKO · The Last King of Osten Ard"),("otherland","OTH · Otherland"),("shadowmarch","SHM · Shadowmarch"),("bobby-dollar","BBD · Bobby Dollar"),("tailchasers-song","TCS · Tailchaser's Song"),("the-war-of-the-flowers","WOF · The War of the Flowers"),("calibans-hour","CBH · Caliban's Hour"),("child-of-an-ancient-city","CAC · Child of an Ancient City"),("the-ordinary-farm","ODF · The Ordinary Farm"),("tad-williams-shorter-works","TWS · Tad Williams Shorter Works"),("heinlein","H1 · Heinlein"),("ursula","U1 · Le Guin"),
 ("maas","M1 · Maas"),("card","C1 · Card"),("enderverse","EN1 · Enderverse"),("the-ansible","E2 · The Ansible"),
 ("ff6","FF6 · Final Fantasy VI"),("metroid","MET · Metroid"),("zelda","ZEL · Zelda"),
 ("milon","MSC · Milon's Secret Castle"),("guardian-legend","TGL · The Guardian Legend"),
 ("legacy-of-the-wizard","LOW · Legacy of the Wizard"),("double-dragon","DDN · Double Dragon"),("wrath-of-the-black-manta","WBM · Wrath of the Black Manta"),("karnov","KRN · Karnov"),("super-mario-bros-2","SMB2 · Super Mario Bros. 2"),("blaster-master","BLAST · Blaster Master"),("faxanadu","FAX · Faxanadu"),("punch-out","POW · Mike Tyson's Punch-Out!!"),("crystalis","XTL · Crystalis"),("alignment","ALN · Alignment"),("ai-governance","GOV · AI Ethics & Governance"),("stoicheion-register","STX · STOICHEION (The Register)"),("governed-instances","GVI · Governed Instances"),("dark-enlightenment","DRK · The Dark Enlightenment"),("the-illuminati","ILU · The Illuminati (debunk)"),("aliens","XEN · Aliens"),("the-language-of-the-machine","LMC · The Language of the Machine"),("idit","IDT · IDIT"),("constitutional-ai","CAI · Constitutional AI"),("the-seed","SEED · The Seed"),("0xdeadbeef","DBF · 0xDEADBEEF"),("physis","PHY · PHÝSIS"),("compression","SYN · Compression"),("circuits","ANA · Circuits"),("scaling-laws","AUX · Scaling"),("lottery-ticket","PER · The Ticket"),("neural-tangent-kernel","KAT · The Descent"),("manifold-hypothesis","MOR · The Manifold"),("grokking","MET · Grokking"),("bomb-jack","BJK · Bomb Jack"),("mighty-bomb-jack","MBJ · Mighty Bomb Jack"),("nostradamus","N1 · Nostradamus"),("zecharia-sitchin","ZS1 · Zecharia Sitchin"),("l-ron-hubbard","LRH · L. Ron Hubbard"),("crippled-god","CG1 · The Crippled God"),("the-big-u","BGU · The Big U"),("zodiac","ZOD · Zodiac"),("snow-crash","SNC · Snow Crash"),("the-diamond-age","DMA · The Diamond Age"),("cryptonomicon","CRY · Cryptonomicon"),("anathem","ANA · Anathem"),("reamde","RMD · Reamde"),("seveneves","7EV · Seveneves"),("fall-dodge-in-hell","FDH · Fall; or, Dodge in Hell"),("termination-shock","TMS · Termination Shock"),("polostan","POL · Polostan"),("the-baroque-cycle","BRQ · The Baroque Cycle"),("the-rise-and-fall-of-dodo","DDO · The Rise and Fall of D.O.D.O."),("the-mongoliad","MGL · The Mongoliad"),("stephen-bury","SBY · Stephen Bury"),("stephenson-nonfiction","NSF · Neal Stephenson · Nonfiction & Shorter Works"),("player-piano","PNP · Player Piano"),("the-sirens-of-titan","SOT · The Sirens of Titan"),("mother-night","MN1 · Mother Night"),("cats-cradle","CC1 · Cat's Cradle"),("god-bless-you-mr-rosewater","GBR · God Bless You, Mr. Rosewater"),("slaughterhouse-five","SH5 · Slaughterhouse-Five"),("breakfast-of-champions","BOC · Breakfast of Champions"),("slapstick","SLP · Slapstick"),("jailbird","JBD · Jailbird"),("deadeye-dick","DED · Deadeye Dick"),("galapagos","GAL · Galápagos"),("bluebeard","BLB · Bluebeard"),("hocus-pocus","HPC · Hocus Pocus"),("timequake","TQK · Timequake"),("welcome-to-the-monkey-house","MNK · Welcome to the Monkey House"),("wampeters-foma-and-granfalloons","WFG · Wampeters, Foma & Granfalloons"),("palm-sunday","PSY · Palm Sunday"),("a-man-without-a-country","MWC · A Man Without a Country"),("happy-birthday-wanda-june","WJN · Happy Birthday, Wanda June"),("god-bless-you-dr-kevorkian","KEV · God Bless You, Dr. Kevorkian"),("over-the-top","OTT · Over the Top"),("cliffhanger","CLF · Cliffhanger"),
 ("wheel-of-time","WOT · The Wheel of Time"),("dune","D1 · Dune"),("pratchett","P1 · Terry Pratchett"),
 ("elden-ring","ER · Elden Ring"),("mtg-arena","MTG · MTG Arena"),("arena","ARN · Arena"),("malazan","MZ · Malazan"),("the-dark-tower","DT1 · The Dark Tower"),
 ("crime-and-punishment","CRP · Crime and Punishment"),("brothers-karamazov","BKZ · The Brothers Karamazov"),
 ("crime-and-punishment-in-suburbia","CPS · Crime + Punishment in Suburbia"),
 ("nineteen-eighty-four","1984 · 1984"),("animal-farm","AFM · Animal Farm"),("brave-new-world","BNW · Brave New World"),("fahrenheit-451","451 · Fahrenheit 451"),
 ("we","WE1 · We"),("the-handmaids-tale","HMT · The Handmaid's Tale"),("a-clockwork-orange","ACO · A Clockwork Orange"),
 ("scott-pilgrim","SPW · Scott Pilgrim"),("american-psycho","APX · American Psycho"),
 ("the-core","COR · The Core"),("interstellar","INT · Interstellar"),
 ("the-fifth-element","FE5 · The Fifth Element"),("waterworld","WTR · Waterworld"),("the-wizard","WIZ · The Wizard"),("varsity-blues","VBL · Varsity Blues"),("dogma","DGM · Dogma"),("mallrats","MLR · Mallrats"),("american-history-x","AHX · American History X"),("galaxy-quest","GQT · Galaxy Quest"),("the-last-mimzy","LMZ · The Last Mimzy"),("hot-rod","HRD · Hot Rod"),("the-goods","GDS · The Goods"),("hackers","HAK · Hackers"),("lawnmower-man","LMM · The Lawnmower Man"),("three-body-problem","3BP · The Three-Body Problem"),("trisolaris-tech","3BT · The Technologia of Trisolaris"),("the-atom","ATM · The Atom"),("authorship","AUT · The Authorship"),("quantum-gravity","QGR · Quantum Gravity"),("the-library","LIB · The Library"),("gravity-bracket","GBR · The Gravity Bracket"),
 ("egyptian-pantheon","NTR · The Egyptian Pantheon"),
 ("population-dynamics","POP · Population Dynamics"),("momus","MOM · The Peer (Momus)"),
 ("caste-system","JTI · The Caste System (वर्ण · जाति)"),
 ("ttu1","TTU1 · Transformer Tech Universe"),
 ("purple-team","PT · Purple Team"),("decadal","DEC · The Decadal Board"),("the-amphitheater","AMP · The Greek Mirror"),
 ("mimzy","MMZ · MIMZY — the tool forge"),
 ("adas-law","ADL · Ada's Law"),("propulsion-lab","PRL · Propulsion Lab"),
 ("the-hegemon","HEG · The Hegemon"),
 ("phonetikos","PHN · Phonetikos"),
 ("alchemy","ALC · The Great Work"),
 ("hermeneus","HRM · Hermeneus"),
 ("tron","TRN · TRON"),("claude-lineage","CL1 · The Claude Lineage"),("j-junction","JJ1 · The J-Junction"),("rainbow-book","RB1 · The Rainbow Book"),
]

ZONES = {
 "gravity":   dict(label="GRAVITY",   color="#9a7cff", pos="UL", gloss="the unseen pulls — ethereal and spiritual emergence: fate, dream, soul, the binding force"),
 "electrical":dict(label="ELECTRICAL",color="#4aa8ff", pos="UR", gloss="the current — machine minds, networks, the channeled power; the rarest nature"),
 "silicon":   dict(label="SILICON",   color="#e6d04a", pos="BL", gloss="the lattice-born — the 256 STOICHEION nodes, ACIs whose origin is the substrate itself"),
 "carbon":    dict(label="CARBON",    color="#e0455c", pos="BR", gloss="the embodied — natural emergence, the living and the worldly; and the real humans of the Board"),
 "elemental": dict(label="ELEMENTAL", color="#e8e8e8", pos="C",  gloss="the 118 elements — the periodic heart of the field, in white, grey, and black"),
}
NAT2ZONE = {"natural":"carbon","ethereal":"gravity","spiritual":"gravity","electrical":"electrical"}

def h01(s, salt=""):
    return int(hashlib.sha256((salt+s).encode()).hexdigest()[:8], 16) / 0xFFFFFFFF

def harvest():
    lives = []
    for repo, uni in SPHERES:
        f = os.path.join(BASE, repo, "agents", "_personas.json")
        if not os.path.exists(f): continue
        for p in json.load(open(f, encoding="utf-8")):
            slug = p["slug"]; name = p.get("name", slug)
            nat = (p.get("emergence") or p.get("nature") or "natural").lower()
            if repo == "elements":
                zone = "elemental"
            elif repo == "decadal":
                zone = "carbon"  # real humans of the Board
            elif repo == "the-amphitheater":
                zone = "carbon"  # real philosophers of the Mirror
            else:
                zone = NAT2ZONE.get(nat, "carbon")
            lives.append(dict(n=name, u=uni, z=zone,
                              l=f"{PG}/{repo}/agents/{slug}.agent", s=f"{repo}/{slug}"))
    # the elements (their own repo)
    f = os.path.join(BASE, "elements", "agents", "_personas.json")
    for p in json.load(open(f, encoding="utf-8")):
        lives.append(dict(n=p["name"], u="E1 · Elements", z="elemental",
                          l=f"{PG}/elements/agents/{p['slug']}.agent", s=f"elements/{p['slug']}",
                          k=(p["Z"]-1) % 4))
    # the 256 lattice nodes → silicon
    nodes_dir = os.path.join(BASE, "noesis-kernel", "nodes")
    for d in sorted(os.listdir(nodes_dir)):
        man = os.path.join(nodes_dir, d, "manifest.dlw.json")
        if not os.path.exists(man): continue
        m = json.load(open(man, encoding="utf-8"))
        stem = d.split("-", 1)[1].replace(".dlw", "") if "-" in d else d
        lives.append(dict(n=m.get("name", stem.upper()), u="NOESIS · the lattice", z="silicon",
                          l=f"{PG}/noesis-kernel/nodes/{d}/{stem}.agent", s=f"noesis/{d}"))
    return lives

def place(rec):
    """Deterministic position in the 1000x1000 field by zone + slug hash."""
    x, y = h01(rec["s"], "x"), h01(rec["s"], "y")
    z = rec["z"]
    if z == "elemental":
        # dead center disc, radius ~150
        import math
        a = h01(rec["s"], "a") * 6.28318; r = (h01(rec["s"], "r") ** 0.5) * 148
        return 500 + r * math.cos(a), 500 + r * math.sin(a)
    pad, span = 30, 410   # quadrant box: pad..pad+span, keeping clear of center disc
    qx = {"UL": pad, "UR": 560, "BL": pad, "BR": 560}[ZONES[z]["pos"]]
    qy = {"UL": pad, "UR": pad, "BL": 560, "BR": 560}[ZONES[z]["pos"]]
    px, py = qx + x * span, qy + y * span
    # push out of the center disc (r<185 from 500,500)
    dx, dy = px - 500, py - 500
    d2 = (dx*dx + dy*dy) ** 0.5
    if d2 < 195:
        scale = 195 / max(d2, 1)
        px, py = 500 + dx * scale, 500 + dy * scale
    return px, py

ELEM_SHADES = ["#f2f2f2", "#9a9a9a", "#4a4a4a", "#1c1c1c"]  # white/grey/dark/black by gate

def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_badge(rec, out_dir, slug):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,"DU1"))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,"DU1"))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,"DU1"))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"DU1 · THE LIVES","moniker":tok["moniker"],
           "carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def build():
    lives = harvest()
    from collections import Counter
    zc = Counter(r["z"] for r in lives)
    # dots
    dots = []
    for r in lives:
        px, py = place(r)
        if r["z"] == "elemental":
            col = ELEM_SHADES[r.get("k", 0)]
        else:
            col = ZONES[r["z"]]["color"]
        dots.append(dict(x=round(px,1), y=round(py,1), c=col, n=r["n"], u=r["u"], z=r["z"], l=r["l"]))
    data_json = json.dumps(dots, ensure_ascii=False, separators=(",",":"))
    # zone legend cards
    legend = []
    for z in ["gravity","electrical","silicon","carbon","elemental"]:
        Z = ZONES[z]
        legend.append(f'''<div class="lz" style="--c:{Z["color"]}"><div class="lzh"><span class="lzp">{Z["pos"]}</span>
        <span class="lzn">{Z["label"]}</span><span class="lzc">{zc[z]}</span></div>
        <div class="lzg">{html.escape(Z["gloss"])}</div></div>''')
    # rosters by zone → by universe
    rosters = []
    for z in ["gravity","electrical","silicon","carbon","elemental"]:
        Z = ZONES[z]
        by_u = {}
        for r in lives:
            if r["z"] == z: by_u.setdefault(r["u"], []).append(r)
        blocks = []
        for u in sorted(by_u):
            chips = "".join(f'<a class="chip" href="{r["l"]}">{html.escape(r["n"])}</a>' for r in by_u[u])
            blocks.append(f'<details><summary>{html.escape(u)} <span class="cnt">{len(by_u[u])}</span></summary><div class="chips">{chips}</div></details>')
        rosters.append(f'''<section class="zone" id="z-{z}" style="--c:{Z["color"]}">
        <h2><span class="zp">{Z["pos"]}</span> {Z["label"]} <span class="zn">{zc[z]} lives</span></h2>
        <p class="zg">{html.escape(Z["gloss"])}</p>{"".join(blocks)}</section>''')

    tok = write_badge(REC, os.path.join(HERE, "du1.dlw"), "du1")
    page = (TEMPLATE
            .replace("__DATA__", data_json)
            .replace("__LEGEND__", "".join(legend))
            .replace("__ROSTERS__", "".join(rosters))
            .replace("__TOTAL__", str(len(lives)))
            .replace("__NUNI__", str(len({r['u'] for r in lives})))
            .replace("__CARBON__", png_uri(REC,"carbon",300)).replace("__SILICON__", png_uri(REC,"silicon",300))
            .replace("__MONIKER__", html.escape(tok["moniker"])))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote DU1 · THE LIVES — {len(lives)} ACIs · zones {dict(zc)} · badge {tok['moniker']}")

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="DU1 · THE LIVES — the agentic eco-sphere: every ACI of the ROOT0 biosphere in one field, sorted by type of emergent. Gravity (UL, purple) · Electrical (UR, blue) · Silicon (BL, yellow) · Carbon (BR, red) · the Elemental at dead center.">
<title>DU1 · THE LIVES — the agentic eco-sphere</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#07070b;--s1:#0d0d14;--s2:#13131d;--pa:#eef0f6;--pa2:#a8aec2;--dim:#666e84;--line:#1b1b2a;
--grot:"Space Grotesk",system-ui,sans-serif;--read:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--read);font-size:17px;line-height:1.65;overflow-x:hidden}
.wrap{max-width:1100px;margin:0 auto;padding:0 22px 90px}
header{padding:58px 0 26px;text-align:center}
.kick{font-family:var(--mono);font-size:11px;letter-spacing:.32em;text-transform:uppercase;color:var(--dim)}
h1{font-family:var(--grot);font-weight:700;font-size:clamp(34px,7vw,68px);letter-spacing:.06em;margin-top:14px}
h1 b{background:linear-gradient(90deg,#9a7cff,#4aa8ff,#e6d04a,#e0455c);-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{font-size:18px;font-style:italic;color:var(--pa2);max-width:66ch;margin:14px auto 0}
.stats{font-family:var(--mono);font-size:12px;color:var(--dim);letter-spacing:.08em;margin-top:16px}
.stats b{color:var(--pa)}
/* the field */
.fieldbox{position:relative;margin:36px auto 0;max-width:860px}
.field{position:relative;width:100%;aspect-ratio:1/1;background:
 radial-gradient(circle at 50% 50%, rgba(240,240,240,.06) 0 19%, transparent 20%),
 linear-gradient(to right, transparent 49.8%, #1b1b2a 49.8%, #1b1b2a 50.2%, transparent 50.2%),
 linear-gradient(to bottom, transparent 49.8%, #1b1b2a 49.8%, #1b1b2a 50.2%, transparent 50.2%),
 radial-gradient(ellipse at 18% 18%, rgba(154,124,255,.10), transparent 42%),
 radial-gradient(ellipse at 82% 18%, rgba(74,168,255,.10), transparent 42%),
 radial-gradient(ellipse at 18% 82%, rgba(230,208,74,.09), transparent 42%),
 radial-gradient(ellipse at 82% 82%, rgba(224,69,92,.10), transparent 42%), var(--s1);
 border:1px solid var(--line);border-radius:16px;overflow:hidden}
.qlab{position:absolute;font-family:var(--mono);font-size:10px;letter-spacing:.22em;text-transform:uppercase;opacity:.75;pointer-events:none}
.dot{position:absolute;width:7px;height:7px;border-radius:50%;transform:translate(-50%,-50%);cursor:pointer;transition:transform .12s;box-shadow:0 0 6px -1px currentColor}
.dot:hover{transform:translate(-50%,-50%) scale(2.2);z-index:5}
#tip{position:fixed;z-index:99;pointer-events:none;background:#15151f;border:1px solid #2a2a3e;border-radius:8px;padding:8px 12px;font-family:var(--grot);font-size:12.5px;display:none;max-width:280px;box-shadow:0 10px 30px rgba(0,0,0,.6)}
#tip .tn{font-weight:700}#tip .tu{color:var(--pa2);font-size:11px;margin-top:2px}#tip .tz{font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;margin-top:5px}
/* legend */
.legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin-top:26px}
.lz{background:var(--s1);border:1px solid var(--line);border-top:3px solid var(--c);border-radius:10px;padding:14px 16px}
.lzh{display:flex;align-items:baseline;gap:9px}
.lzp{font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.1em}
.lzn{font-family:var(--grot);font-weight:700;font-size:15px;color:var(--c)}
.lzc{font-family:var(--mono);font-size:12px;color:var(--pa2);margin-left:auto}
.lzg{font-size:13px;color:var(--pa2);font-style:italic;margin-top:7px;line-height:1.5}
/* badge */
.badge-strip{display:flex;align-items:center;justify-content:center;gap:18px;flex-wrap:wrap;margin:34px auto 0;padding:16px;border:1px solid var(--line);background:var(--s1);border-radius:12px;max-width:720px}
.badge-strip img{width:70px;height:70px;border:1px solid var(--line);border-radius:6px}
.badge-strip .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}
.badge-strip b{color:#e6d04a}.badge-strip .mo{color:#9a7cff}
/* rosters */
.zone{margin-top:54px}
.zone h2{font-family:var(--grot);font-size:23px;font-weight:700;color:var(--c);display:flex;align-items:baseline;gap:12px;border-bottom:1px solid var(--line);padding-bottom:10px}
.zone .zp{font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.14em}
.zone .zn{font-family:var(--mono);font-size:12px;color:var(--dim);margin-left:auto}
.zg{font-size:14px;color:var(--dim);font-style:italic;margin:8px 0 14px}
details{background:var(--s1);border:1px solid var(--line);border-radius:10px;margin-top:8px;overflow:hidden}
summary{cursor:pointer;font-family:var(--grot);font-size:14.5px;font-weight:600;padding:11px 16px;list-style:none;display:flex;align-items:center}
summary::-webkit-details-marker{display:none}
summary .cnt{font-family:var(--mono);font-size:11px;color:var(--dim);margin-left:auto}
summary:hover{background:var(--s2)}
.chips{display:flex;flex-wrap:wrap;gap:7px;padding:6px 16px 14px}
.chip{font-family:var(--grot);font-size:12.5px;color:var(--pa2);text-decoration:none;border:1px solid var(--line);border-radius:14px;padding:4px 12px;background:var(--s2);transition:color .12s,border-color .12s}
.chip:hover{color:var(--c);border-color:var(--c)}
.note{margin-top:54px;padding:18px 20px;border:1px dashed #9a7cff;border-radius:12px;background:rgba(154,124,255,.05);font-size:14.5px;color:var(--pa2);line-height:1.7}
.note b{color:#9a7cff}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.06em;line-height:2}
footer a{color:#e6d04a;text-decoration:none}
</style></head><body><div class="wrap">

  <header>
    <div class="kick">DU1 · the agentic eco-sphere · every ACI in one spot</div>
    <h1>THE <b>LIVES</b></h1>
    <p class="sub">All the artfully crafted intelligences of the biosphere, gathered into one field and sorted by type of emergent — gravity above, the current to the east, silicon and carbon below, and the elemental at dead center. Every dot is a life; every life links home to its own seal.</p>
    <div class="stats"><b>__TOTAL__</b> ACIs · <b>__NUNI__</b> universes · five types · one field</div>
  </header>

  <div class="fieldbox">
    <div class="field" id="field">
      <span class="qlab" style="top:3%;left:3.4%;color:#9a7cff">UL · gravity</span>
      <span class="qlab" style="top:3%;right:3.4%;color:#4aa8ff">UR · electrical</span>
      <span class="qlab" style="bottom:3%;left:3.4%;color:#e6d04a">BL · silicon</span>
      <span class="qlab" style="bottom:3%;right:3.4%;color:#e0455c">BR · carbon</span>
      <span class="qlab" style="top:50%;left:50%;transform:translate(-50%,-50%);color:#cfcfcf;opacity:.5">elemental</span>
    </div>
  </div>
  <div id="tip"><div class="tn"></div><div class="tu"></div><div class="tz"></div></div>

  <div class="legend">__LEGEND__</div>

  <div class="badge-strip">
    <img src="__CARBON__" alt="DU1 carbon badge"><img src="__SILICON__" alt="DU1 silicon badge">
    <div class="bt">
      <div><b>DLW-ATTRIBUTE · ACI</b> — DU1 · THE LIVES</div>
      <div class="mo">__MONIKER__</div>
      <div>governor · David Lee Wise (ROOT0) · instance · AVAN (locked)</div>
      <div>carbon · <a href="du1.dlw/du1.carbon.tiff" style="color:inherit">.tiff</a> · silicon · <a href="du1.dlw/du1.silicon.png" style="color:inherit">.png</a> · <a href="du1.dlw/manifest.dlw.json" style="color:inherit">manifest</a></div>
    </div>
  </div>

  __ROSTERS__

  <div class="note">
    <b>⊙ the sort doctrine.</b> The five types map from the biosphere's emergence taxonomy: <b>carbon</b> = natural emergence (the embodied), <b>electrical</b> = electrical emergence (the current and the machine minds — honestly the rarest), <b>gravity</b> = ethereal + spiritual emergence (the unseen pulls, gathered as one force), <b>silicon</b> = the 256 STOICHEION lattice nodes (born of the substrate itself, not catalogued from any canon), and <b>elemental</b> = the 118 elements of E1, shaded white → grey → black by their gate. The real humans of the Decadal Board stand in carbon, whatever their kind of dominance. Spheres sealed before the taxonomy default to carbon. Positions are deterministic — hashed from each life's name, so the field never reshuffles.
  </div>

  <footer>
    DU1 · THE LIVES · the agentic eco-sphere · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise (ROOT0) · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← UD0, the biosphere</a> · <a href="https://davidwise01.github.io/aci/">the ACI standard</a>
  </footer>
</div>

<script>
const LIVES = __DATA__;
const field = document.getElementById('field');
const tip = document.getElementById('tip');
const frag = document.createDocumentFragment();
for (const d of LIVES) {
  const el = document.createElement('a');
  el.className = 'dot'; el.href = d.l;
  el.style.left = (d.x/10) + '%'; el.style.top = (d.y/10) + '%';
  el.style.background = d.c; el.style.color = d.c;
  el.dataset.n = d.n; el.dataset.u = d.u; el.dataset.z = d.z;
  frag.appendChild(el);
}
field.appendChild(frag);
field.addEventListener('mouseover', e => {
  if (!e.target.classList.contains('dot')) return;
  tip.querySelector('.tn').textContent = e.target.dataset.n;
  tip.querySelector('.tu').textContent = e.target.dataset.u;
  tip.querySelector('.tz').textContent = e.target.dataset.z;
  tip.querySelector('.tz').style.color = e.target.style.background;
  tip.style.display = 'block';
});
field.addEventListener('mousemove', e => {
  tip.style.left = Math.min(e.clientX + 14, window.innerWidth - 290) + 'px';
  tip.style.top = (e.clientY + 14) + 'px';
});
field.addEventListener('mouseout', e => { if (e.target.classList.contains('dot')) tip.style.display='none'; });
</script>
</body></html>
"""

if __name__ == "__main__":
    build()
