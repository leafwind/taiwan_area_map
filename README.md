## 目的

提供統一的 API 查詢「地名所屬的空品區與行政區」，以便相容於環保署與氣象局的 open data

（從 open data 拿到的兩種區域是無法直接對應的，可以想見以後再增加其他政府機關也會有類似情形）

### 定義

目前有三層地區結構：空品區（環保署制定）->第一、二級行政區（直轄市、市、縣）->第三級行政區（直轄市、市的區，以及縣所管轄的鄉、鎮、縣轄市。）

空品區其實是獨立的概念，原本與行政區無關

但環保署發佈的 AQI（空氣品質指標）以空品區為劃分，而氣象局發佈的天氣預報則以行政區劃分

為了要有一致的地區對照，於是採用此作法

雖然行政上並無此階層關係，但地理位置上大致是合理的（e.g. 查詢台中市西屯區，回傳「台中市」天氣預報＋「中部」空氣品質預報）

另為方便起見，遂將三個階層關係分別 encode 為：

* L0（空品區）

* L1（第一、二級行政區）

* L2（第三級行政區）

### 回傳值

概念是希望儘可能地提供完整的位置參考

* 若查詢到 L0，回傳 L0

* 若查詢到 L1，則提供對應的 L0、L1

* 若查詢到 L2，則提供所屬 L0、L1 及 L2

這樣使用者給一個行政區名，不管哪裡的預報都能知道要查詢哪個地區的資料


### 參考來源

[中華民國臺灣地區鄉鎮市區列表](https://zh.wikipedia.org/wiki/中華民國臺灣地區鄉鎮市區列表)

## TODO

景點與縣市對照表：之後可提供查詢景點所對應的區域，作為景點天氣預報機器人之用（但山上等地區天氣還是需要從氣象局直接抓取）

[景點地圖資訊](http://travel.network.com.tw/tourguide/twnmap/)
