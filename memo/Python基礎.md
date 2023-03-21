# Pythonで気をつけるところ
## 基礎編

1.「/」の後にコメントが書けない<br>

2.bool型でfalse扱いされるケース<br>
　*空値<br>
　*数値のゼロ<br>
　*空文字、空のリスト<br>
　逆に、上記以外はtrueとなる。

3.複数行文字列<br>
　「'''」「"""」で複数行の文字列を表現する。

## データ型
1.暗黙の型変換はしない<br>

```python
result = 15 + '20'
```
<br>
　20がintに変換されず、TypeErrorとなる。<br>

```python
result = 15 + int('20')
```
<br>
　上記のようにint/strで型変換する。<br>
<br>


## 演算子
1.「=」での代入は参照渡し<br>
　ミュータブル（リストなど）の変数で、同じアドレスを指す変数が２つある場合、一方を変更すると、もうひとつも変更される。<br>
　イミュータブル（intなど）は変更されない。<br>
　イミュータブルはオブジェクトの中身の書き換えはできず、オブジェクトそのものが入れ替わる。<br>
　JavaのStringに近い？ <br>

2.比較演算子の連結<br>
　以下の書き方も可能<br>
```python
if 50 <= x <= 100:
```

## 制御構文
1.空のブロックの書き方<br>
```python
if i == 5:
    # なにもしない
```
<br>
　上記は、「IndentationError」が発生。<br>
　なんらかの文があることを期待しているため。<br>

```python
if i == 5:
    pass
```
<br>
　上記のようにpass命令を使う。<br>
　pass命令はなにもしないが、意味のある文とみなされる。<br>
<br>

2.複数行コメントもインデント<br>
```python
if i == 5:
    '''
    コメント
    '''
```
<br>
　上記はOKで、インデントがないとNGになる。<br>
　ただし、#のコメントはインデントがなくてもOK。<br>
<br>

3.switch文がない<br>

4.for文はオブジェクトのループ<br>
　他言語（PHPなど）のforeachと同じ？
　
```python
data = ['イチゴ','みかん','バナナ']

for value in data:
    print(value)
```
<br>
　指定回数の繰り返しはrangeを使う。<br>

```python
for i in range(1,6):
    print(i)
```
<br>
　rangeでオブジェクトを作って、オブジェクトの要素をループするイメージ。<br>
<br>
5.for/whileに対するelse<br>
　breadzせずにループが終わった場合に実行される。<br>
```python
for i in range(1,6):
    if i == 100:
        break
else:
    print('ループの最後まで実行')
```
<br>
　5以下で判定した場合はelseは実行されない。<br>
<br>
　ループをネストした時は、elseを使ってループを2回以上抜けられる。<br>
　ただし、フラグを使ってループを抜けた方がわかりやすい。<br>
<br>

6.for/whileに対するelse<br>
　例外が発生しなかった場合の処理となる。<br>
　finallyはJavaなどと同じく、例外の有無にかかわらず実行される。<br>

## 標準ライブラリ
1.文字列検索<br>
　文字列が見つからない場合。<br>
　　find/rfind：-1を返す。<br>
　　index/rindex：ValueErrorの例外を返す。<br>

　なお、単純な有無（文字列が含まれるか）判定であれば、in演算子を使った方がいい。<br>

2.文字列置換<br>
　replace、translateともに、元の文字列を書き換えるのではなく、新しい文字列を返す。
<br>
　また、translateは1文字単位で変換マッピングを用意する。<br>

3.datetimeの加減算<br>
　timedeltaを使って、日付の加算、減算を行う。
```python
import datetime

dt = datetime.datetime(2023, 3, 21, 19, 40, 35, 495)
dt_add = dt + datetime.timedelta(days=10, hours=2)
dt_sub = dt - datetime.timedelta(weeks=2)
```
3.日付の差分<br>
　datetime、date、time同士で、「-」を使う。<br>
　戻り値は、timedeltaオブジェクトになる。




