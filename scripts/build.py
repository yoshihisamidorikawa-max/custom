from pathlib import Path
import re,html,os
from urllib.parse import urlparse
site_url=os.environ.get("SITE_URL", "https://preview-jimny-after04.buddica-custom-jimny.pages.dev").rstrip("/")
if urlparse(site_url).scheme != "https" or not urlparse(site_url).netloc:
 raise ValueError("SITE_URL must be an absolute HTTPS origin")
page_url=html.escape(site_url+"/jimny/", quote=True)
image_url=html.escape(site_url+"/jimny/assets/ogp.png", quote=True)
root=Path(__file__).resolve().parents[1]
# Reviewed After_04 content, shared by both responsive layouts.
full=[('フロント','CL20グリル（エンブレムレス）\nブラックLEDヘッドライト'),('足まわり','2インチリフトアップ\nキャリパーカバー\n（BUDDICAロゴ入り）'),('タイヤ・ホイール','ランドフット GWD＋オプカン R/T\n225/70R16\nタイヤ・ホイール各5本'),('ルーフ','スクエアルーフラック'),('リア','CL20 2型リアバンパー ASSY\nCL20 リアEXバンパー\nスペアタイヤオフセットブラケット'),('フロント下部','CL20バンパー\nスキッドプレート'),('室内装備','シートベルト（BUDDICAロゴ入り）\nカメラ・モニター\nシートカバー')]
light=[('フロント','CL20グリル（エンブレムレス）'),('足まわり','1インチリフトアップ\nキャリパーカバー（BUDDICAロゴ入り）'),('タイヤ・ホイール','ランドフット GWD\nグラントレック R/T01\n185/85R16（4本）'),('ルーフ','スクエアルーフラック'),('リア','リアゲートボックス\nリアラダー'),('オーニング','セミオート・タープ付き'),('室内装備','シートベルト（BUDDICAロゴ入り）\nカメラ・モニター\nラゲッジネットM')]
def img(name,alt,cls='',lazy=True):return f'<img src="assets/{name}" alt="{alt}" class="{cls}" '+('loading="lazy" ' if lazy else 'fetchpriority="high" ')+ 'decoding="async">'
def button(text,href=None,dark=False,small=False):return f'<'+('a href="'+href+'"' if href else 'button type="button" data-contact')+f' class="button {"dark" if dark else ""} {"small" if small else ""}">{text}'+('' if small else img('fa62b.svg','','arrow',False))+('</a>' if href else '</button>')
def price(n,label='車両込み参考価格'):return f'<div class="price"><p>{label}</p><div><strong>{n}</strong><b>万円〜</b><small>（税込）</small></div></div>'
def badge(option=False):return f'<span class="badge {"option" if option else ""}">{"オプション" if option else "標準装備"}</span>'
def notes():return '<p class="note">※参考販売価格はR6年式中古車（オーディオ無し）をベース車両とした価格となります。<br>※諸費用、オプション費用などは含まれておりません。<br>※写真はイメージです。実際の仕様、色、装着場所、装着状態などが異なる場合があります。</p>'
cards=''
for ident,en,jp,tag,n,photo in [('full','FULL CUSTOM','フルカスタム','大胆に、遊ぶ。','342.5','87dab.png'),('light','LIGHT CUSTOM','ライトカスタム','軽やかに、遊ぶ。','283.2','f68a7.png')]:
 cards+=f'<article class="compare-card {ident}"><div class="card-title"><h3>{en}</h3><p class="note">{jp}</p><p class="tagline">{tag}</p></div>{img(photo,jp+"側面","compare-photo")}{price(n)}{button(jp+"を詳しく見る","#"+ident)}</article>'
sections=''
for idx,(ident,en,jp,n,cost,photo,spec,lead) in enumerate([('full','FULL CUSTOM','フルカスタム','342.5','133.5','87dab.png',full,'2インチリフトアップで、存在感を。'),('light','LIGHT CUSTOM','ライトカスタム','283.2','74.2','f68a7.png',light,'1インチリフトアップで、日常に遊び心を。')],1):
 grid=''.join(f'<div class="spec-item"><h4><span>{i:02}</span>{title}</h4><p>{html.escape(body).replace(chr(10),"<br>")}</p></div>' for i,(title,body) in enumerate(spec,1))
 if ident=='full':
  opt=f'<div class="option-copy"><div class="option-head">{badge(True)}<span class="note">別途費用</span></div><p class="bold">バンパー仕様：ブラック（標準）／メッキ（オプション）</p><h4>メッキバンパー／オーバーフェンダー（開発中）／専用ホイール（マットブラック）</h4><p class="note">※オーバーフェンダーの仕様・価格は検討中です。<br>※タイヤ・ホイール無しで、ご自身で別途購入することも可能です。</p></div><div class="option-photos"><figure>{img("d333a.png","フロント（メッキ）")}<figcaption>フロント（メッキ）</figcaption></figure><figure>{img("24bf9.png","リア（メッキ）")}<figcaption>リア（メッキ）</figcaption></figure></div>'
 else:opt=f'<div class="option-copy"><div class="option-head">{badge(True)}<span class="note">別途費用</span></div><h4>専用ホイール（マットブラック）</h4><p class="note">※参考販売価格にオプション費用は含みません。<br>※タイヤ・ホイール無しで、ご自身で別途購入することも可能です。</p></div>'
 sections+=f'<section id="{ident}" class="section style-section {ident}"><div class="wrap"><div class="style-heading"><div><p class="eyebrow">STYLE 0{idx}</p><h2>{en}</h2><p class="sub">{jp}</p><h3>{lead.replace("で、",'で、<br class="sp-only">')}</h3></div><div class="style-price">{price(n,"車両込み参考価格（ブラック仕様）" if ident=="full" else "車両込み参考価格")}<p class="bold">うちカスタム費用 {cost}万円〜（税込）</p></div></div>{img(photo,jp+"側面","style-photo")}<div class="equipment"><div class="equipment-heading"><p class="eyebrow">EQUIPMENT</p>{badge()}</div><div class="spec-grid">{grid}</div></div><div class="option-panel">{opt}</div></div></section>'
detail=''
for photo,title,desc,cls in [('ef86f.png','CL20グリル（エンブレムレス）','フロントの印象を引き締めるグリル。',''),('00ac3.png','キャリパーカバー（BUDDICAロゴ入り）','足まわりにロゴ入りのアクセント。',''),('233d9.png','スクエアルーフラック','ルーフまわりの存在感を高めるラック。',''),('353c5.png','シートベルト（BUDDICAロゴ入り）','室内にもロゴ入りのオレンジを。','cover')]:
 detail+=f'<article class="detail-card">{img(photo,title,cls)}<div>{badge()}<h3>{title}</h3><p class="note">{desc}</p></div></article>'
page=f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>BUDDICA × C.L.LINK カスタムジムニー｜After_04確認用</title><meta name="description" content="BUDDICAとC.L.LINKが仕上げたカスタムジムニー。FULL CUSTOMとLIGHT CUSTOM、2つのスタイルをご紹介。"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png" sizes="180x180">
<meta property="og:type" content="website">
<meta property="og:locale" content="ja_JP">
<meta property="og:site_name" content="BUDDICA">
<meta property="og:title" content="BUDDICA × C.L.LINK カスタムジムニー">
<meta property="og:description" content="BUDDICAとC.L.LINKが仕上げたカスタムジムニー。FULL CUSTOMとLIGHT CUSTOM、2つのスタイルをご紹介。">
<meta property="og:url" content="{page_url}">
<meta property="og:image" content="{image_url}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="BUDDICA × C.L.LINK カスタムジムニー誕生。オレンジの背景に黒いカスタムジムニー。">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="BUDDICA × C.L.LINK カスタムジムニー">
<meta name="twitter:description" content="FULL CUSTOMとLIGHT CUSTOM、2つのスタイルをご紹介。">
<meta name="twitter:image" content="{image_url}">
<meta name="twitter:image:alt" content="BUDDICA × C.L.LINK カスタムジムニー誕生。">
<link rel="stylesheet" href="style.css"></head><body>
<a class="skip-link" href="#main">本文へ移動</a>
<header><a href="#" aria-label="ページ先頭">{img('89c2d.svg','BUDDICA × C.L.LINK','logo pc-logo',False)}{img('49323.svg','BUDDICA × C.L.LINK','logo sp-logo',False)}</a><nav aria-label="メインナビゲーション"><a class="en" href="#full">FULL CUSTOM</a><a class="en" href="#light">LIGHT CUSTOM</a>{button('先行受注のご相談',small=True)}</nav></header>
<nav class="mobile-nav" aria-label="スタイル"><a href="#full">FULL CUSTOM</a><a href="#light">LIGHT CUSTOM</a></nav>
<main id="main"><section class="hero"><picture><source media="(max-width: 767px)" srcset="assets/0285e.png">{img('9fd0f.png','BUDDICA × C.L.LINK カスタムジムニー完成車','hero-car',False)}</picture><div class="hero-copy"><p class="eyebrow">BUDDICA × C.L.LINK &nbsp;CUSTOM JIMNY</p><p class="hero-lead">BUDDICAとC.L.LINKが仕上げた、</p><h1>カスタムジムニー<br>誕生。</h1><p class="status"><picture><source media="(max-width:767px)" srcset="assets/47b59.svg">{img('5830c.svg','','',False)}</picture>先行受注受付中</p>{button('2つのスタイルを見る','#compare',True)}</div></section>
<section id="compare" class="section compare"><div class="wrap"><div class="center-heading"><p class="eyebrow">2 STYLES</p><h2>あなたの「好き」に合う、<br class="sp-only">2つのスタイル。</h2></div><div class="compare-grid">{cards}</div><p class="note">※参考価格はR6年式中古車（オーディオ無し）をベースとしています。諸費用・オプション費用は別途。フルカスタムはブラック仕様の価格です。<br>※フルの車両写真はオーバーフェンダー装着イメージです（別途オプション・仕様検討中）。</p></div></section>
{sections}
<section id="detail" class="section detail"><div class="wrap"><div class="detail-heading"><p class="eyebrow">DETAIL</p><h2>細部にも、<br class="sp-only">BUDDICAらしさを。</h2><p class="sub">FULL CUSTOM・LIGHT CUSTOM <br class="sp-only">共通の標準装備です。</p></div><div class="detail-grid">{detail}</div><div class="option-strip">{badge(True)}<p>メッキバンパー（FULL）<span> ／ </span>オーバーフェンダー（FULL・開発中）<span> ／ </span>専用ホイール マットブラック（FULL・LIGHT）</p></div></div></section>
<section class="section final-cta"><div class="wrap"><p class="eyebrow">PRE ORDER</p><h2>あなたの一台を、<br class="sp-only">ここから。</h2><p>先行受注受付中</p>{button('先行受注について相談する',dark=True)}</div></section></main>
<footer><div class="wrap"><div class="footer-top"><a href="#" aria-label="ページ先頭">{img('596a9.svg','BUDDICA × C.L.LINK','pc-footer')}{img('55995.svg','BUDDICA × C.L.LINK','sp-footer')}</a><nav aria-label="フッターナビゲーション"><a class="en" href="#full">FULL CUSTOM</a><a class="en" href="#light">LIGHT CUSTOM</a><a class="en" href="#detail">DETAIL</a><button class="text-button" data-contact>先行受注のご相談</button></nav></div>{notes()}</div></footer>
<div class="fixed-cta">{button('先行受注について相談する')}</div>
<dialog id="contact-dialog" aria-labelledby="dialog-title"><h2 id="dialog-title">確認用ページです</h2><p>先行受注のご相談先は現在設定待ちです。<br>このページからお問い合わせは送信されません。</p><form method="dialog"><button class="button dark">閉じる</button></form></dialog><script src="app.js" defer></script></body></html>'''
(root/'public/jimny/index.html').write_text(page)
