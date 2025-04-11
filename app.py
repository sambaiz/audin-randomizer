import streamlit as st
import random
from datetime import datetime
import secrets

# 1人の島のリスト
single_person_islands = [
    "スカイ島",
    "ロフォーテン",
    "マン島",
    "シェットランド諸島",
    "フェロー諸島"
]

# 表の島のリスト（裏の島とフエゴ島を除く）
front_islands = [
    "スカイ島",
    "ロフォーテン",
    "マン島",
    "シェットランド諸島",
    "フェロー諸島",
    "アイスランド",
    "グリーンランド",
    "アウター・ヘブリディーズ",
    "アイラ島"
]

# 表の島と裏の島の対応関係
island_pairs = {
    "マン島": "リムリック",
    "ロフォーテン": "オークニー",
    "スカイ島": "ウェックスフォード",
    "シェットランド諸島": "ビュルネイ島",
    "フェロー諸島": "バフィン島",
    "アイラ島": "ウォーターフォード",
    "アウター・ヘブリディーズ": "コーク",
    "アイスランド": "ラブラドール島",
    "グリーンランド": "ニューファンドランド",
}

# ページ設定
st.set_page_config(
    page_title="オーディンの祝祭の島 ランダマイザ",
    page_icon="🏝️",
    layout="centered"
)

# タイトル
st.title("🏝️ オーディンの祝祭の島 ランダマイザ")
st.markdown("---")

# 説明文
st.markdown("""
このアプリは、オーディンの祝祭の島から8つの島をランダムに選びます。
- フエゴ島は必ず含まれます
- 1人の島（スカイ島、ロフォーテン、マン島、シェットランド諸島、フェロー諸島）が少なくとも1つ含まれます
- 裏の島は選ばれませんが、対応する裏の島がある場合は表示されます
- 同じ日付であれば、同じ結果が表示されます
- シャッフルボタンをクリックすると、新しい結果が生成されます
""")

# クエリパラメータからシードを取得
query_params = st.experimental_get_query_params()
seed = query_params.get("seed", [None])[0]

# シードが指定されていない場合はランダムなシードを生成
if seed is None:
    seed = secrets.token_hex(8)

# シードをシード値として使用
random.seed(seed)

# 1人の島を1つランダムに選択
selected_single_island = random.choice(single_person_islands)

# 残りの表の島から5つを選択（1人の島を除く）
remaining_front_islands = [island for island in front_islands if island != selected_single_island]
if len(remaining_front_islands) < 5:
    st.error("表の島の数が不足しています。")
    st.stop()
selected_remaining_islands = random.sample(remaining_front_islands, 5)

# 結果を組み合わせる（合計8つになるように）
selected_islands = selected_remaining_islands + [selected_single_island, "フエゴ島"]

# 結果を表示
st.markdown("### 選ばれた島:")
st.markdown(f"*シード: {seed}*")

for i, island in enumerate(selected_islands, 1):
    if island in island_pairs:
        st.markdown(f"{i}. {island} - 裏: {island_pairs[island]}")
    else:
        st.markdown(f"{i}. {island}")

# 現在のURLを表示
current_url = st.experimental_get_query_params()
st.markdown("### 現在のURL:")
url = f"https://audin-randomizer.streamlit.app/?seed={seed}"
st.code(url, language="text")

# URLをコピーするボタン
if st.button("URLをコピー"):
    st.markdown(f"""
    <script>
        navigator.clipboard.writeText("{url}");
        alert("URLをクリップボードにコピーしました。");
    </script>
    """, unsafe_allow_html=True)

# シャッフルボタン
if st.button("シャッフル"):
    # 新しいシードを生成
    new_seed = secrets.token_hex(8)
    # URLを更新
    st.experimental_set_query_params(seed=new_seed)
    # ページをリロード
    st.experimental_rerun()

# フッター
st.markdown("---")
st.markdown("© 2024 オーディンの祝祭の島 ランダマイザ")