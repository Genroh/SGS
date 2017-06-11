Author : Genroh

スクストでメンバー編成するときのメンバー・メモカを最適化したかった。

仕様決まったらここに書くんだけど、まだmemoca.txtのアレが決まってないです（ないです
memoca.txtはmemoca.csvに改名しました。

仕様案：TeamとMemberにそれぞれ番号をつけて(アザーズはチーム0とか)個人を区別するのはどうか。
	↑とりあえずそれですすめてみよう
	[TeamNo, MemNo, HP, ATK, 収束数, Rare, Name] メモカ情報、同一メンバーのカードの区別は未定
	RarelityはSR以上限定で、SR, SRu(究極), UR, EXR(持ってないけどな)
	チーム0、メンバー0をマルチメモカに設定。
	[TeamNo, MemNo, 親愛度, Name, Card1, Card2] メンバー情報
	Member.py と Memoca.pyにそれぞれのクラスを作成した。
	Memoca.pyにflagを追加するかの検討中。
