# Inventario de Japan Rail Explorer

> Generado automáticamente por `tools/inventory.py` a partir de los datos (2026-09-23). No lo edites a mano: cambia `config/` y vuelve a generar.

## Resumen

**Progreso de la hoja de ruta: 111 de 180 tareas.**

| Región | Líneas | Estaciones | Trenes actuales | Trenes históricos |
|---|--:|--:|--:|--:|
| Shinkansen 新幹線 | 10 | 118 | 12 | 8 |
| Tokio 東京 | 138 | 1657 | 63 | 23 |
| Kioto 京都 | 36 | 431 | 20 | 2 |
| Ōsaka 大阪 | 61 | 705 | 14 | 0 |
| Kōbe 神戸 | 27 | 315 | 2 | 1 |
| Nagoya 名古屋 | 33 | 525 | 6 | 1 |
| Fukuoka 福岡 | 25 | 367 | 4 | 0 |
| Sapporo 札幌 | 21 | 396 | 13 | 3 |
| Sendai 仙台 | 13 | 210 | 2 | 0 |
| Hiroshima 広島 | 17 | 268 | 4 | 0 |
| Tranvías de otras ciudades 路面電車 | 39 | 630 | 4 | 0 |
| **Total** | **420** | **5540** | **144** | **38** |

- Fotos de trenes: **182 de 182** (100 %).
- Estaciones con datos curiosos: **82 de 5540** (1 %).
- Datos curiosos en total: **600**.

## Cobertura de Japón

Todas las estaciones que OpenStreetMap tiene en cada prefectura, comparadas con las nuestras (`tools/audit_coverage.py`, 2026-09-23).

**5641 de 9580 estaciones de Japón (59 %).** Una prefectura está completa cuando no le falta ninguna.

| Prefectura | Estaciones | Tenemos | Faltan | Cobertura |
|---|--:|--:|--:|--:|
| 01 Hokkaidō ✅ | 447 | 447 | 0 | 100 % |
| 02 Aomori | 157 | 5 | 152 | 3 % |
| 03 Iwate | 187 | 9 | 178 | 5 % |
| 04 Miyagi ✅ | 156 | 156 | 0 | 100 % |
| 05 Akita | 144 | 4 | 140 | 3 % |
| 06 Yamagata | 121 | 17 | 104 | 14 % |
| 07 Fukushima | 188 | 3 | 185 | 2 % |
| 08 Ibaraki | 137 | 10 | 127 | 7 % |
| 09 Tochigi | 146 | 19 | 127 | 13 % |
| 10 Gunma | 140 | 8 | 132 | 6 % |
| 11 Saitama ✅ | 234 | 234 | 0 | 100 % |
| 12 Chiba ✅ | 346 | 346 | 0 | 100 % |
| 13 Tokio ✅ | 783 | 783 | 0 | 100 % |
| 14 Kanagawa ✅ | 381 | 381 | 0 | 100 % |
| 15 Niigata | 202 | 9 | 193 | 4 % |
| 16 Toyama | 212 | 26 | 186 | 12 % |
| 17 Ishikawa | 75 | 3 | 72 | 4 % |
| 18 Fukui | 134 | 30 | 104 | 22 % |
| 19 Yamanashi | 73 | 0 | 73 | 0 % |
| 20 Nagano | 259 | 10 | 249 | 4 % |
| 21 Gifu | 189 | 7 | 182 | 4 % |
| 22 Shizuoka | 224 | 10 | 214 | 4 % |
| 23 Aichi ✅ | 493 | 493 | 0 | 100 % |
| 24 Mie | 234 | 25 | 209 | 11 % |
| 25 Shiga ✅ | 122 | 122 | 0 | 100 % |
| 26 Kioto ✅ | 242 | 242 | 0 | 100 % |
| 27 Ōsaka ✅ | 554 | 554 | 0 | 100 % |
| 28 Hyōgo ✅ | 385 | 385 | 0 | 100 % |
| 29 Nara ✅ | 128 | 128 | 0 | 100 % |
| 30 Wakayama | 121 | 20 | 101 | 17 % |
| 31 Tottori | 73 | 0 | 73 | 0 % |
| 32 Shimane | 116 | 0 | 116 | 0 % |
| 33 Okayama | 167 | 21 | 146 | 13 % |
| 34 Hiroshima ✅ | 278 | 278 | 0 | 100 % |
| 35 Yamaguchi | 156 | 9 | 147 | 6 % |
| 36 Tokushima | 76 | 0 | 76 | 0 % |
| 37 Kagawa | 93 | 0 | 93 | 0 % |
| 38 Ehime | 155 | 64 | 91 | 41 % |
| 39 Kōchi ✅ | 196 | 196 | 0 | 100 % |
| 40 Fukuoka ✅ | 350 | 350 | 0 | 100 % |
| 41 Saga | 80 | 9 | 71 | 11 % |
| 42 Nagasaki | 145 | 46 | 99 | 32 % |
| 43 Kumamoto | 168 | 51 | 117 | 30 % |
| 44 Ōita | 85 | 0 | 85 | 0 % |
| 45 Miyazaki | 78 | 0 | 78 | 0 % |
| 46 Kagoshima ✅ | 131 | 131 | 0 | 100 % |
| 47 Okinawa | 19 | 0 | 19 | 0 % |

Qué líneas faltan en cada una, en [AUDITORIA.md](AUDITORIA.md).

## Lo que hay

### Shinkansen 新幹線

| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |
|---|---|---|--:|---|---|--:|
| 東海 | [Tōkaidō Shinkansen](https://japanrail.alvaroom.org/#/line/tokaido-shinkansen) | JR Central | 17 | Serie N700S, Serie N700A | Serie 0, Serie 100, Serie 300, Serie 700 | 5 |
| 山陽 | [San'yō Shinkansen](https://japanrail.alvaroom.org/#/line/sanyo-shinkansen) | JR West | 19 | Serie N700S, Serie N700A, Serie N700 7000/8000, Serie 500, Serie 700 | Serie 0, Serie 100, Serie 300 | 4 |
| 九州 | [Kyūshū Shinkansen](https://japanrail.alvaroom.org/#/line/kyushu-shinkansen) | JR Kyushu | 12 | Serie N700 7000/8000, Serie 800 | — | 3 |
| 西九 | [Nishi-Kyūshū Shinkansen](https://japanrail.alvaroom.org/#/line/nishi-kyushu-shinkansen) | JR Kyushu | 5 | Serie N700S 8000 (Kamome) | — | 2 |
| 東北 | [Tōhoku Shinkansen](https://japanrail.alvaroom.org/#/line/tohoku-shinkansen) | JR East | 23 | Serie E5, Serie H5, Serie E6, Serie E8, Serie E7 / W7 | Serie 200, Serie 400, Serie E1 «Max», Serie E4 «Max», Serie E3 | 4 |
| 北海 | [Hokkaidō Shinkansen](https://japanrail.alvaroom.org/#/line/hokkaido-shinkansen) | JR Hokkaido | 4 | Serie E5, Serie H5 | — | 3 |
| 上越 | [Jōetsu Shinkansen](https://japanrail.alvaroom.org/#/line/joetsu-shinkansen) | JR East | 10 | Serie E7 / W7 | Serie 200, Serie E1 «Max», Serie E4 «Max» | 3 |
| 北陸 | [Hokuriku Shinkansen](https://japanrail.alvaroom.org/#/line/hokuriku-shinkansen) | JR East | 19 | Serie E7 / W7 | — | 4 |
| 山形 | [Yamagata Shinkansen](https://japanrail.alvaroom.org/#/line/yamagata-shinkansen) | JR East | 11 | Serie E8 | Serie 400 | 3 |
| 秋田 | [Akita Shinkansen](https://japanrail.alvaroom.org/#/line/akita-shinkansen) | JR East | 6 | Serie E6 | Serie E3 | 2 |

### Tokio 東京

| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |
|---|---|---|--:|---|---|--:|
| JY | [Línea Yamanote](https://japanrail.alvaroom.org/#/line/yamanote) | JR East | 30 | Serie E235 | Serie 101, Serie 103, Serie 205, Serie E231-500 | 6 |
| JC | [Línea Chūō (rápido)](https://japanrail.alvaroom.org/#/line/chuo-rapid) | JR East | 24 | Serie E233-0 | Serie 101, Serie 103, Serie 201 | 3 |
| JB | [Línea Chūō-Sōbu (local)](https://japanrail.alvaroom.org/#/line/chuo-sobu) | JR East | 39 | Serie E231-500 | Serie 101, Serie 103, Serie 201, Serie 205, Serie 209 | 2 |
| JK | [Línea Keihin-Tōhoku / Negishi](https://japanrail.alvaroom.org/#/line/keihin-tohoku) | JR East | 47 | Serie E233-1000 | Serie 101, Serie 103, Serie 205, Serie 209 | 3 |
| JA | [Línea Saikyō](https://japanrail.alvaroom.org/#/line/saikyo) | JR East | 19 | Serie E233-7000, Sōtetsu serie 12000 | Serie 103, Serie 205 | 2 |
| JO | [Línea Sōbu (rápido)](https://japanrail.alvaroom.org/#/line/sobu-rapid) | JR East | 10 | Serie E235-1000 | — | 2 |
| G | [Línea Ginza](https://japanrail.alvaroom.org/#/line/ginza) | Tokyo Metro | 19 | Tokyo Metro serie 1000 | Tokyo Metro serie 01 | 4 |
| M | [Línea Marunouchi](https://japanrail.alvaroom.org/#/line/marunouchi) | Tokyo Metro | 28 | Tokyo Metro serie 2000 | Serie 300/400/500 (Marunouchi), Tokyo Metro serie 02 | 2 |
| H | [Línea Hibiya](https://japanrail.alvaroom.org/#/line/hibiya) | Tokyo Metro | 22 | Tokyo Metro serie 13000, Tōbu serie 70000 | Serie 3000 (Hibiya), Tokyo Metro serie 03 | 2 |
| T | [Línea Tōzai](https://japanrail.alvaroom.org/#/line/tozai) | Tokyo Metro | 23 | Tokyo Metro serie 15000 | Serie 5000 (Tōzai) | 3 |
| C | [Línea Chiyoda](https://japanrail.alvaroom.org/#/line/chiyoda) | Tokyo Metro | 20 | Tokyo Metro serie 16000, Serie E233-2000, Odakyū serie 4000 | Tokyo Metro serie 6000 | 2 |
| Y | [Línea Yūrakuchō](https://japanrail.alvaroom.org/#/line/yurakucho) | Tokyo Metro | 24 | Tokyo Metro serie 17000 | Tokyo Metro serie 7000 | 2 |
| Z | [Línea Hanzōmon](https://japanrail.alvaroom.org/#/line/hanzomon) | Tokyo Metro | 14 | Tokyo Metro serie 18000, Tōkyū serie 2020 | — | 2 |
| N | [Línea Namboku](https://japanrail.alvaroom.org/#/line/namboku) | Tokyo Metro | 19 | Tokyo Metro serie 9000 | — | 3 |
| F | [Línea Fukutoshin](https://japanrail.alvaroom.org/#/line/fukutoshin) | Tokyo Metro | 16 | Tokyo Metro serie 17000, Tōbu serie 50000 | — | 2 |
| A | [Línea Asakusa](https://japanrail.alvaroom.org/#/line/asakusa) | Toei | 20 | Toei serie 5500, Keikyū serie N1000, Keisei serie 3100 | Toei serie 5300 | 2 |
| I | [Línea Mita](https://japanrail.alvaroom.org/#/line/mita) | Toei | 27 | Toei serie 6500 | Toei serie 6000 | 2 |
| S | [Línea Shinjuku](https://japanrail.alvaroom.org/#/line/shinjuku) | Toei | 21 | Toei serie 10-300, Keiō serie 5000 | Toei serie 10-000 | 1 |
| E | [Línea Ōedo](https://japanrail.alvaroom.org/#/line/oedo) | Toei | 38 | Toei serie 12-000 | — | 4 |
| SA | [Tranvía Arakawa (Tokyo Sakura Tram)](https://japanrail.alvaroom.org/#/line/arakawa) | Toei | 30 | Toei serie 8900 | Toei serie 7000 (tranvía) | 3 |
| NT | [Nippori-Toneri Liner](https://japanrail.alvaroom.org/#/line/nippori-toneri) | Toei | 13 | Nippori-Toneri Liner serie 300, Nippori-Toneri Liner serie 330 | — | 1 |
| U | [Yurikamome](https://japanrail.alvaroom.org/#/line/yurikamome) | Yurikamome | 16 | Yurikamome serie 7300 | — | 2 |
| MO | [Monorraíl de Tokio](https://japanrail.alvaroom.org/#/line/tokyo-monorail) | Tokyo Monorail | 11 | Tokyo Monorail serie 10000 | — | 2 |
| R | [Línea Rinkai](https://japanrail.alvaroom.org/#/line/rinkai) | Tokyo Waterfront (TWR) | 8 | TWR serie 70-000 | — | 2 |
| JE | [Línea Keiyō](https://japanrail.alvaroom.org/#/line/keiyo) | JR East | 18 | Serie E233-5000 | — | 2 |
| JI | [JR Uchibō](https://japanrail.alvaroom.org/#/line/uchibo) | JR East | 29 | — | — | 1 |
| JE | [JR Sotobō](https://japanrail.alvaroom.org/#/line/sotobo) | JR East | 26 | — | — | 1 |
| JO | [JR Sōbu (Chiba–Chōshi)](https://japanrail.alvaroom.org/#/line/sobu-main) | JR East | 32 | — | — | 1 |
| JO | [JR Narita](https://japanrail.alvaroom.org/#/line/narita-line) | JR East | 22 | — | — | 0 |
| JO | [JR Narita (ramal de Abiko)](https://japanrail.alvaroom.org/#/line/narita-abiko) | JR East | 12 | — | — | 0 |
| JO | [JR Tōgane](https://japanrail.alvaroom.org/#/line/togane) | JR East | 5 | — | — | 0 |
| JI | [JR Kururi](https://japanrail.alvaroom.org/#/line/kururi) | JR East | 14 | — | — | 1 |
| JO | [JR Kashima](https://japanrail.alvaroom.org/#/line/kashima) | JR East | 5 | — | — | 1 |
| KM | [Kominato Tetsudō](https://japanrail.alvaroom.org/#/line/kominato) | Kominato Tetsudō | 18 | — | — | 2 |
| IS | [Isumi Tetsudō](https://japanrail.alvaroom.org/#/line/isumi) | Isumi Tetsudō | 14 | — | — | 1 |
| CD | [Chōshi Dentetsu](https://japanrail.alvaroom.org/#/line/choshi) | Chōshi Dentetsu | 10 | — | — | 2 |
| DR | [Disney Resort Line](https://japanrail.alvaroom.org/#/line/disney-resort) | Maihama Resort Line | 4 | — | — | 2 |
| JJ | [Línea Jōban (rápido)](https://japanrail.alvaroom.org/#/line/joban-rapid) | JR East | 10 | Serie E231-0, Serie E531 | — | 1 |
| JL | [Línea Jōban (local)](https://japanrail.alvaroom.org/#/line/joban-local) | JR East | 12 | Serie E233-2000, Odakyū serie 4000 | — | 1 |
| JM | [Línea Musashino](https://japanrail.alvaroom.org/#/line/musashino) | JR East | 27 | Serie E231-0 | — | 2 |
| JN | [Línea Nambu](https://japanrail.alvaroom.org/#/line/nambu) | JR East | 26 | Serie E233-8000 | — | 1 |
| JH | [Línea Yokohama](https://japanrail.alvaroom.org/#/line/yokohama-line) | JR East | 20 | Serie E233-6000 | — | 1 |
| JT | [Línea Tōkaidō (JT)](https://japanrail.alvaroom.org/#/line/tokaido-jt) | JR East | 21 | Serie E233-3000, Serie E231-1000 | — | 2 |
| JO | [Línea Yokosuka](https://japanrail.alvaroom.org/#/line/yokosuka) | JR East | 19 | Serie E235-1000 | — | 2 |
| JS | [Línea Shōnan-Shinjuku](https://japanrail.alvaroom.org/#/line/shonan-shinjuku) | JR East | 16 | Serie E231-1000 | — | 1 |
| JU | [Línea Utsunomiya](https://japanrail.alvaroom.org/#/line/utsunomiya) | JR East | 34 | Serie E233-3000, Serie E231-1000 | — | 1 |
| JU | [Línea Takasaki](https://japanrail.alvaroom.org/#/line/takasaki) | JR East | 24 | Serie E233-3000, Serie E231-1000 | — | 1 |
| JC | [Línea Ōme](https://japanrail.alvaroom.org/#/line/ome) | JR East | 25 | Serie E233-0 | — | 1 |
| TY | [Tōkyū Tōyoko](https://japanrail.alvaroom.org/#/line/tokyu-toyoko) | Tōkyū | 21 | Tōkyū serie 5000, Sōtetsu serie 20000 | Tōkyū serie 5000 «Aogaeru» | 2 |
| DT | [Tōkyū Den-en-toshi](https://japanrail.alvaroom.org/#/line/tokyu-denentoshi) | Tōkyū | 27 | Tōkyū serie 5000, Tōkyū serie 2020 | — | 2 |
| MG | [Tōkyū Meguro](https://japanrail.alvaroom.org/#/line/tokyu-meguro) | Tōkyū | 13 | Tōkyū serie 5000, Tōkyū serie 3020, Sōtetsu serie 20000 | Tōkyū serie 5000 «Aogaeru» | 1 |
| OM | [Tōkyū Ōimachi](https://japanrail.alvaroom.org/#/line/tokyu-oimachi) | Tōkyū | 15 | — | — | 0 |
| IK | [Tōkyū Ikegami](https://japanrail.alvaroom.org/#/line/tokyu-ikegami) | Tōkyū | 15 | Tōkyū serie 1000 | — | 0 |
| TM | [Tōkyū Tamagawa](https://japanrail.alvaroom.org/#/line/tokyu-tamagawa) | Tōkyū | 7 | Tōkyū serie 1000 | — | 0 |
| SG | [Tōkyū Setagaya](https://japanrail.alvaroom.org/#/line/tokyu-setagaya) | Tōkyū | 10 | Tōkyū serie 300 (Setagaya) | — | 2 |
| OH | [Odakyū Odawara](https://japanrail.alvaroom.org/#/line/odakyu-odawara) | Odakyū | 47 | Romancecar GSE (serie 70000), Odakyū serie 5000, Odakyū serie 4000 | Romancecar LSE (serie 7000), Romancecar HiSE (serie 10000), Romancecar VSE (serie 50000) | 2 |
| CO | [JR Chūō (Takao–Ōtsuki)](https://japanrail.alvaroom.org/#/line/chuo-otsuki) | JR East | 9 | — | — | 2 |
| MI | [Inclinado de la presa de Miyagase](https://japanrail.alvaroom.org/#/line/miyagase-incline) | Prefectura de Kanagawa | 2 | — | — | 1 |
| OH | [Hakone Tozan](https://japanrail.alvaroom.org/#/line/hakone-tozan) | Hakone Tozan | 11 | — | — | 3 |
| OH | [Funicular de Hakone (Gōra–Sōunzan)](https://japanrail.alvaroom.org/#/line/hakone-tozan-cable) | Hakone Tozan | 6 | — | — | 1 |
| ID | [Izuhakone Daiyūzan](https://japanrail.alvaroom.org/#/line/izuhakone-daiyuzan) | Izuhakone Tetsudō | 12 | — | — | 1 |
| OY | [Funicular del monte Ōyama](https://japanrail.alvaroom.org/#/line/oyama-cable) | Ōyama Kankō Dentetsu | 3 | — | — | 1 |
| CB | [JR Gotemba](https://japanrail.alvaroom.org/#/line/gotemba) | JR Central | 19 | — | — | 2 |
| OE | [Odakyū Enoshima](https://japanrail.alvaroom.org/#/line/odakyu-enoshima) | Odakyū | 17 | Odakyū serie 5000 | — | 1 |
| KO | [Keiō](https://japanrail.alvaroom.org/#/line/keio) | Keiō | 32 | Keiō serie 5000 | — | 2 |
| KO | [Keiō Takao](https://japanrail.alvaroom.org/#/line/keio-takao) | Keiō | 7 | Keiō serie 5000 | — | 1 |
| IN | [Keiō Inokashira](https://japanrail.alvaroom.org/#/line/keio-inokashira) | Keiō | 17 | Keiō serie 1000 | — | 1 |
| SI | [Seibu Ikebukuro](https://japanrail.alvaroom.org/#/line/seibu-ikebukuro) | Seibu | 31 | Seibu 001 «Laview», Seibu serie 40000 | Seibu 10000 «New Red Arrow» | 1 |
| CR | [Chichibu Tetsudō](https://japanrail.alvaroom.org/#/line/chichibu) | Chichibu Tetsudō | 37 | — | — | 2 |
| SI | [Seibu Chichibu](https://japanrail.alvaroom.org/#/line/seibu-chichibu) | Seibu | 6 | — | — | 2 |
| TI | [Tōbu Isesaki (norte)](https://japanrail.alvaroom.org/#/line/tobu-isesaki) | Tōbu | 26 | — | — | 1 |
| TN | [Tōbu Nikkō](https://japanrail.alvaroom.org/#/line/tobu-nikko) | Tōbu | 26 | — | — | 1 |
| SS | [Seibu Shinjuku](https://japanrail.alvaroom.org/#/line/seibu-shinjuku) | Seibu | 29 | Seibu serie 40000, Seibu 10000 «New Red Arrow» | — | 1 |
| TS | [Tōbu Skytree](https://japanrail.alvaroom.org/#/line/tobu-skytree) | Tōbu | 30 | Tōbu 500 «Revaty», Tōbu N100 «SPACIA X», Tōbu serie 70000 | — | 2 |
| TJ | [Tōbu Tōjō](https://japanrail.alvaroom.org/#/line/tobu-tojo) | Tōbu | 39 | Tōbu serie 50000 | — | 1 |
| KK | [Keikyū principal](https://japanrail.alvaroom.org/#/line/keikyu-main) | Keikyū | 49 | Keikyū serie N1000, Keikyū serie 2100 | Keikyū serie 800 | 2 |
| KK | [Keikyū Aeropuerto](https://japanrail.alvaroom.org/#/line/keikyu-airport) | Keikyū | 7 | Keikyū serie N1000 | — | 0 |
| KS | [Keisei principal](https://japanrail.alvaroom.org/#/line/keisei-main) | Keisei | 42 | Keisei AE «Skyliner», Keisei serie 3100 | Keisei AE (1.er Skyliner) | 1 |
| KS | [Keisei Oshiage](https://japanrail.alvaroom.org/#/line/keisei-oshiage) | Keisei | 6 | Keisei serie 3100 | — | 0 |
| TX | [Tsukuba Express](https://japanrail.alvaroom.org/#/line/tsukuba-express) | Tsukuba Express | 20 | Tsukuba Express TX-3000 | — | 2 |
| SO | [Sōtetsu principal](https://japanrail.alvaroom.org/#/line/sotetsu) | Sōtetsu | 18 | Sōtetsu serie 20000, Sōtetsu serie 12000 | — | 1 |
| TK | [Funicular del monte Takao](https://japanrail.alvaroom.org/#/line/takao-cable) | Takao Tozan Dentetsu | 2 | — | — | 2 |
| MT | [Funicular del monte Mitake](https://japanrail.alvaroom.org/#/line/mitake-cable) | Mitake Tozan Railway | 2 | — | — | 1 |
| AP | [Asukarugo (parque de Asukayama)](https://japanrail.alvaroom.org/#/line/asukayama) | Distrito de Kita (Tokio) | 2 | — | — | 2 |
| SR | [Sakura Rail (Matsuchiyama)](https://japanrail.alvaroom.org/#/line/sakura-rail) | Matsuchiyama Shōden | 3 | — | — | 1 |
| TT | [Monorraíl de Tama](https://japanrail.alvaroom.org/#/line/tama-monorail) | Tama Monorail | 19 | Monorraíl de Tama serie 1000 | — | 0 |
| EN | [Enoden](https://japanrail.alvaroom.org/#/line/enoden) | Enoden | 15 | Enoden serie 1000 | — | 2 |
| SMR | [Shōnan Monorail](https://japanrail.alvaroom.org/#/line/shonan-monorail) | Shōnan Monorail | 8 | Shōnan Monorail serie 5000 | — | 3 |
| B | [Metro de Yokohama: línea Azul](https://japanrail.alvaroom.org/#/line/yokohama-blue) | Metro de Yokohama | 32 | Metro de Yokohama serie 3000, Metro de Yokohama serie 4000 | — | 1 |
| G | [Metro de Yokohama: línea Verde](https://japanrail.alvaroom.org/#/line/yokohama-green) | Metro de Yokohama | 10 | Metro de Yokohama serie 10000 | — | 0 |
| MM | [Línea Minatomirai](https://japanrail.alvaroom.org/#/line/minatomirai) | Minatomirai | 6 | Tōkyū serie 5000 | — | 1 |
| CM | [Monorraíl de Chiba (línea 2)](https://japanrail.alvaroom.org/#/line/chiba-monorail) | Chiba Monorail | 15 | Monorraíl de Chiba serie 0 «Urban Flyer» | — | 2 |
| CM | [Monorraíl de Chiba (línea 1)](https://japanrail.alvaroom.org/#/line/chiba-monorail-1) | Chiba Monorail | 6 | Monorraíl de Chiba serie 0 «Urban Flyer» | — | 0 |
| KK | [Keikyū Kurihama](https://japanrail.alvaroom.org/#/line/keikyu-kurihama) | Keikyū | 9 | Keikyū serie N1000 | — | 1 |
| KK | [Keikyū Zushi](https://japanrail.alvaroom.org/#/line/keikyu-zushi) | Keikyū | 4 | Keikyū serie N1000 | — | 0 |
| KK | [Keikyū Daishi](https://japanrail.alvaroom.org/#/line/keikyu-daishi) | Keikyū | 7 | Keikyū serie N1000 | — | 1 |
| KS | [Keisei Kanamachi](https://japanrail.alvaroom.org/#/line/keisei-kanamachi) | Keisei | 3 | — | — | 1 |
| KS | [Keisei Chiba](https://japanrail.alvaroom.org/#/line/keisei-chiba) | Keisei | 10 | — | — | 0 |
| KS | [Keisei Chihara](https://japanrail.alvaroom.org/#/line/keisei-chihara) | Keisei | 6 | — | — | 0 |
| SL | [Keisei Matsudo](https://japanrail.alvaroom.org/#/line/keisei-matsudo) | Keisei | 24 | — | — | 1 |
| HS | [Hokusō / Narita Sky Access](https://japanrail.alvaroom.org/#/line/hokuso) | Hokusō | 15 | Keisei AE «Skyliner», Keisei serie 3100 | — | 1 |
| KS | [Keisei Higashi-Narita](https://japanrail.alvaroom.org/#/line/keisei-higashi-narita) | Keisei | 2 | — | — | 0 |
| SR | [Shibayama Railway](https://japanrail.alvaroom.org/#/line/shibayama) | Shibayama Railway | 2 | — | — | 1 |
| KO | [Keiō Nueva Línea](https://japanrail.alvaroom.org/#/line/keio-new) | Keiō | 4 | Keiō serie 5000 | — | 0 |
| KO | [Keiō Sagamihara](https://japanrail.alvaroom.org/#/line/keio-sagamihara) | Keiō | 12 | Keiō serie 5000 | — | 0 |
| KO | [Keiō Keibajō](https://japanrail.alvaroom.org/#/line/keio-keibajo) | Keiō | 2 | — | — | 1 |
| KO | [Keiō Dōbutsuen](https://japanrail.alvaroom.org/#/line/keio-dobutsuen) | Keiō | 2 | — | — | 1 |
| OT | [Odakyū Tama](https://japanrail.alvaroom.org/#/line/odakyu-tama) | Odakyū | 8 | — | — | 0 |
| SS | [Seibu Haijima](https://japanrail.alvaroom.org/#/line/seibu-haijima) | Seibu | 8 | — | — | 0 |
| SK | [Seibu Kokubunji](https://japanrail.alvaroom.org/#/line/seibu-kokubunji) | Seibu | 5 | — | — | 0 |
| ST | [Seibu Tamako](https://japanrail.alvaroom.org/#/line/seibu-tamako) | Seibu | 7 | — | — | 0 |
| SW | [Seibu Tamagawa](https://japanrail.alvaroom.org/#/line/seibu-tamagawa) | Seibu | 6 | — | — | 1 |
| SI | [Seibu Sayama](https://japanrail.alvaroom.org/#/line/seibu-sayama) | Seibu | 3 | — | — | 0 |
| SY | [Seibu Yamaguchi (Leo Liner)](https://japanrail.alvaroom.org/#/line/seibu-yamaguchi) | Seibu | 3 | — | — | 1 |
| SK | [Seibu Seibu-en](https://japanrail.alvaroom.org/#/line/seibu-seibuen) | Seibu | 2 | — | — | 0 |
| SI | [Seibu Yūrakuchō](https://japanrail.alvaroom.org/#/line/seibu-yurakucho) | Seibu | 3 | Tokyo Metro serie 17000, Seibu serie 40000 | — | 0 |
| SI | [Seibu Toshima](https://japanrail.alvaroom.org/#/line/seibu-toshima) | Seibu | 2 | — | — | 1 |
| TS | [Tōbu Kameido](https://japanrail.alvaroom.org/#/line/tobu-kameido) | Tōbu | 5 | — | — | 0 |
| TS | [Tōbu Daishi](https://japanrail.alvaroom.org/#/line/tobu-daishi) | Tōbu | 2 | — | — | 1 |
| TD | [Tōbu Urban Park](https://japanrail.alvaroom.org/#/line/tobu-urban-park) | Tōbu | 35 | — | — | 0 |
| TJ | [Tōbu Ogose](https://japanrail.alvaroom.org/#/line/tobu-ogose) | Tōbu | 8 | — | — | 0 |
| KD | [Tōkyū Kodomonokuni](https://japanrail.alvaroom.org/#/line/tokyu-kodomonokuni) | Tōkyū | 3 | — | — | 1 |
| SH | [Tōkyū Shin-Yokohama](https://japanrail.alvaroom.org/#/line/tokyu-shin-yokohama) | Tōkyū | 3 | Tōkyū serie 3020, Sōtetsu serie 20000 | — | 1 |
| SO | [Sōtetsu Izumino](https://japanrail.alvaroom.org/#/line/sotetsu-izumino) | Sōtetsu | 8 | Sōtetsu serie 20000 | — | 0 |
| SO | [Sōtetsu Shin-Yokohama](https://japanrail.alvaroom.org/#/line/sotetsu-shin-yokohama) | Sōtetsu | 3 | Sōtetsu serie 20000, Sōtetsu serie 12000 | — | 0 |
| JI | [JR Tsurumi](https://japanrail.alvaroom.org/#/line/tsurumi) | JR East | 13 | — | — | 1 |
| JN | [JR Nambu (ramal Hama-Kawasaki)](https://japanrail.alvaroom.org/#/line/nambu-branch) | JR East | 5 | — | — | 0 |
| 相模 | [JR Sagami](https://japanrail.alvaroom.org/#/line/sagami) | JR East | 18 | — | — | 0 |
| JC | [JR Itsukaichi](https://japanrail.alvaroom.org/#/line/itsukaichi) | JR East | 7 | — | — | 0 |
| 八高 | [JR Hachikō](https://japanrail.alvaroom.org/#/line/hachiko) | JR East | 24 | — | — | 1 |
| 川越 | [JR Kawagoe](https://japanrail.alvaroom.org/#/line/kawagoe) | JR East | 11 | — | — | 0 |
| SR | [Saitama Rapid Railway](https://japanrail.alvaroom.org/#/line/saitama-rapid) | Saitama Rapid Railway | 8 | Tokyo Metro serie 9000 | — | 1 |
| TR | [Tōyō Rapid](https://japanrail.alvaroom.org/#/line/toyo-rapid) | Tōyō Rapid | 9 | Tokyo Metro serie 15000 | — | 0 |
| NS | [New Shuttle](https://japanrail.alvaroom.org/#/line/new-shuttle) | New Shuttle | 13 | — | — | 1 |
| SL | [Kanazawa Seaside Line](https://japanrail.alvaroom.org/#/line/kanazawa-seaside) | Yokohama Seaside Line | 13 | — | — | 1 |
| DL | [Disney Resort Line](https://japanrail.alvaroom.org/#/line/disney-resort-line) | Maihama Resort Line | 4 | — | — | 1 |
| RN | [Ryūtetsu Nagareyama](https://japanrail.alvaroom.org/#/line/ryutetsu) | Ryūtetsu | 6 | — | — | 1 |
| YM | [Yamaman Yukarigaoka](https://japanrail.alvaroom.org/#/line/yamaman) | Yamaman | 6 | — | — | 1 |

### Kioto 京都

| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |
|---|---|---|--:|---|---|--:|
| K | [Línea Karasuma](https://japanrail.alvaroom.org/#/line/karasuma) | Metro de Kioto | 15 | Metro de Kioto serie 10, Metro de Kioto serie 20, Kintetsu serie 3220 | — | 3 |
| T | [Línea Tōzai (Kioto)](https://japanrail.alvaroom.org/#/line/kyoto-tozai) | Metro de Kioto | 17 | Metro de Kioto serie 50, Keihan serie 800 | — | 3 |
| A | [Línea JR Kyōto](https://japanrail.alvaroom.org/#/line/jr-kyoto) | JR West | 17 | Serie 225, Serie 223, Serie 321, Serie 281 «Haruka», Serie 683 «Thunderbird» | — | 2 |
| E | [Línea Sagano](https://japanrail.alvaroom.org/#/line/sagano) | JR West | 16 | Serie 221 | — | 2 |
| E | [JR San'in (Sonobe–Fukuchiyama)](https://japanrail.alvaroom.org/#/line/sanin-fukuchiyama) | JR West | 17 | — | — | 1 |
| L | [JR Maizuru](https://japanrail.alvaroom.org/#/line/maizuru) | JR West | 6 | — | — | 1 |
| E | [JR Obama](https://japanrail.alvaroom.org/#/line/obama) | JR West | 24 | — | — | 1 |
| F | [Tango: línea Miyafuku](https://japanrail.alvaroom.org/#/line/tango-miyafuku) | Kyōto Tango Tetsudō | 14 | — | — | 1 |
| M | [Tango: línea Miyamai](https://japanrail.alvaroom.org/#/line/tango-miyamai) | Kyōto Tango Tetsudō | 7 | — | — | 1 |
| T | [Tango: línea Miyatoyo](https://japanrail.alvaroom.org/#/line/tango-miyatoyo) | Kyōto Tango Tetsudō | 13 | — | — | 1 |
| V | [JR Kansai (Kamo–Kameyama)](https://japanrail.alvaroom.org/#/line/kansai-east) | JR West | 12 | — | — | 1 |
| EC | [Funicular de Eizan](https://japanrail.alvaroom.org/#/line/eizan-cable) | Randen (Keifuku) | 2 | — | — | 2 |
| AC | [Funicular de Amanohashidate](https://japanrail.alvaroom.org/#/line/amanohashidate-cable) | Tango Kairiku Kōtsū | 2 | — | — | 1 |
| D | [Línea Nara](https://japanrail.alvaroom.org/#/line/nara-line) | JR West | 21 | Serie 221 | — | 2 |
| KH | [Línea principal Keihan](https://japanrail.alvaroom.org/#/line/keihan-main) | Keihan | 42 | Keihan serie 8000, Keihan serie 13000 | Keihan serie 3000 (1971) | 3 |
| KH | [Línea Keihan Uji](https://japanrail.alvaroom.org/#/line/keihan-uji) | Keihan | 8 | Keihan serie 13000 | — | 1 |
| HK | [Línea Hankyu Kyōto](https://japanrail.alvaroom.org/#/line/hankyu-kyoto) | Hankyu | 28 | Hankyu serie 9300, Hankyu serie 1300 | Hankyu serie 6300 | 2 |
| HK | [Línea Hankyu Arashiyama](https://japanrail.alvaroom.org/#/line/hankyu-arashiyama) | Hankyu | 4 | — | — | 1 |
| B | [Línea Kintetsu Kyōto](https://japanrail.alvaroom.org/#/line/kintetsu-kyoto) | Kintetsu | 26 | Kintetsu serie 3220, Kintetsu 19200 «Aoniyoshi» | — | 1 |
| A | [Randen: línea Arashiyama](https://japanrail.alvaroom.org/#/line/randen-arashiyama) | Randen (Keifuku) | 13 | Tranvías del Randen | — | 3 |
| B | [Randen: línea Kitano](https://japanrail.alvaroom.org/#/line/randen-kitano) | Randen (Keifuku) | 10 | Tranvías del Randen | — | 1 |
| E | [Eiden: línea Eizan](https://japanrail.alvaroom.org/#/line/eizan-main) | Eiden (Eizan) | 8 | Eiden serie 900 «Kirara», Eiden «Hiei» (serie 700) | — | 1 |
| E | [Eiden: línea Kurama](https://japanrail.alvaroom.org/#/line/eizan-kurama) | Eiden (Eizan) | 10 | Eiden serie 900 «Kirara» | — | 2 |
| トロ | [Tren turístico Sagano (Torokko)](https://japanrail.alvaroom.org/#/line/sagano-scenic) | Sagano Scenic Railway | 4 | Tren Torokko (Sagano) | — | 3 |
| OT | [Keihan Keishin](https://japanrail.alvaroom.org/#/line/keihan-keishin) | Keihan | 7 | Keihan serie 800 | — | 1 |
| OT | [Keihan Ishiyama-Sakamoto](https://japanrail.alvaroom.org/#/line/keihan-ishiyama) | Keihan | 21 | — | — | 1 |
| B | [JR Kosei](https://japanrail.alvaroom.org/#/line/kosei) | JR West | 21 | Serie 225, Serie 223, Serie 683 «Thunderbird» | — | 1 |
| A | [JR Biwako](https://japanrail.alvaroom.org/#/line/biwako) | JR West | 23 | Serie 225, Serie 223 | — | 0 |
| A | [JR Hokuriku (Maibara–Ōmi-Shiotsu)](https://japanrail.alvaroom.org/#/line/hokuriku-shiga) | JR West | 10 | — | — | 1 |
| A | [JR Tōkaidō (Maibara–Sekigahara)](https://japanrail.alvaroom.org/#/line/tokaido-maibara) | JR Central | 5 | — | — | 1 |
| OR | [Ōmi Tetsudō (principal)](https://japanrail.alvaroom.org/#/line/omi-main) | Ōmi Tetsudō | 25 | — | — | 2 |
| OR | [Ōmi Tetsudō: Yōkaichi](https://japanrail.alvaroom.org/#/line/omi-yokaichi) | Ōmi Tetsudō | 7 | — | — | 0 |
| OR | [Ōmi Tetsudō: Taga](https://japanrail.alvaroom.org/#/line/omi-taga) | Ōmi Tetsudō | 3 | — | — | 1 |
| C | [JR Kusatsu](https://japanrail.alvaroom.org/#/line/kusatsu-line) | JR West | 10 | — | — | 1 |
| SG | [Shigaraki Kōgen Tetsudō](https://japanrail.alvaroom.org/#/line/shigaraki) | Shigaraki Kōgen Tetsudō | 6 | — | — | 1 |
| SC | [Funicular de Sakamoto](https://japanrail.alvaroom.org/#/line/sakamoto-cable) | Hieizan Tetsudō | 4 | — | — | 2 |

### Ōsaka 大阪

| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |
|---|---|---|--:|---|---|--:|
| O | [JR Ōsaka Loop Line](https://japanrail.alvaroom.org/#/line/osaka-loop) | JR West | 19 | Serie 323 | Serie 103, Serie 201 | 2 |
| P | [JR Yumesaki](https://japanrail.alvaroom.org/#/line/yumesaki) | JR West | 4 | — | — | 1 |
| M | [Osaka Metro Midōsuji](https://japanrail.alvaroom.org/#/line/midosuji) | Osaka Metro | 20 | Osaka Metro serie 30000 | — | 3 |
| T | [Osaka Metro Tanimachi](https://japanrail.alvaroom.org/#/line/tanimachi) | Osaka Metro | 26 | Osaka Metro serie 30000 | — | 0 |
| Y | [Osaka Metro Yotsubashi](https://japanrail.alvaroom.org/#/line/yotsubashi) | Osaka Metro | 11 | — | — | 0 |
| C | [Osaka Metro Chūō](https://japanrail.alvaroom.org/#/line/chuo-osaka) | Osaka Metro | 15 | Osaka Metro serie 400 | — | 2 |
| S | [Osaka Metro Sennichimae](https://japanrail.alvaroom.org/#/line/sennichimae) | Osaka Metro | 14 | — | — | 0 |
| K | [Osaka Metro Sakaisuji](https://japanrail.alvaroom.org/#/line/sakaisuji) | Osaka Metro | 10 | Osaka Metro serie 66 | — | 1 |
| N | [Osaka Metro Nagahori Tsurumi-ryokuchi](https://japanrail.alvaroom.org/#/line/nagahori) | Osaka Metro | 17 | Osaka Metro serie 70 | — | 1 |
| I | [Osaka Metro Imazatosuji](https://japanrail.alvaroom.org/#/line/imazatosuji) | Osaka Metro | 11 | — | — | 0 |
| P | [New Tram (Nankō Port Town)](https://japanrail.alvaroom.org/#/line/new-tram) | Osaka Metro | 10 | — | — | 0 |
| NK | [Nankai principal](https://japanrail.alvaroom.org/#/line/nankai-main) | Nankai | 41 | Nankai 50000 «Rapi:t», Nankai serie 8300 | — | 1 |
| NK | [Nankai Aeropuerto](https://japanrail.alvaroom.org/#/line/nankai-airport) | Nankai | 3 | Nankai 50000 «Rapi:t» | — | 1 |
| MZ | [Mizuma Tetsudō](https://japanrail.alvaroom.org/#/line/mizuma) | Mizuma Tetsudō | 10 | — | — | 1 |
| M | [Kita-Ōsaka Kyūkō](https://japanrail.alvaroom.org/#/line/kita-osaka-kyuko) | Kita-Ōsaka Kyūkō | 6 | — | — | 2 |
| Z | [Funicular de Nishi-Shigi](https://japanrail.alvaroom.org/#/line/nishi-shigi-cable) | Kintetsu | 2 | — | — | 1 |
| NK | [Nankai Tanagawa](https://japanrail.alvaroom.org/#/line/nankai-tanagawa) | Nankai | 4 | — | — | 1 |
| WN | [Wing Shuttle (ala norte)](https://japanrail.alvaroom.org/#/line/wing-shuttle-norte) | Aeropuerto de Kansai | 3 | — | — | 1 |
| WS | [Wing Shuttle (ala sur)](https://japanrail.alvaroom.org/#/line/wing-shuttle-sur) | Aeropuerto de Kansai | 2 | — | — | 1 |
| NK | [Nankai Kōya](https://japanrail.alvaroom.org/#/line/nankai-koya) | Nankai | 42 | Nankai serie 8300 | — | 1 |
| HS | [Hanshin principal](https://japanrail.alvaroom.org/#/line/hanshin-main) | Hanshin | 33 | Hanshin 5700 «Jet Silver», Hanshin serie 1000 | — | 1 |
| HS | [Hanshin Namba](https://japanrail.alvaroom.org/#/line/hanshin-namba) | Hanshin | 11 | Hanshin serie 1000 | — | 0 |
| HK | [Hankyu Kōbe](https://japanrail.alvaroom.org/#/line/hankyu-kobe) | Hankyu | 16 | Hankyu serie 1000 | — | 0 |
| HK | [Hankyu Takarazuka](https://japanrail.alvaroom.org/#/line/hankyu-takarazuka) | Hankyu | 19 | Hankyu serie 1000 | — | 1 |
| A | [Kintetsu Namba](https://japanrail.alvaroom.org/#/line/kintetsu-namba) | Kintetsu | 3 | Kintetsu 19200 «Aoniyoshi», Hanshin serie 1000, Kintetsu 80000 «Hinotori», Kintetsu 50000 «Shimakaze» | — | 0 |
| A | [Kintetsu Nara](https://japanrail.alvaroom.org/#/line/kintetsu-nara) | Kintetsu | 19 | Kintetsu 19200 «Aoniyoshi», Hanshin serie 1000 | — | 1 |
| D | [Kintetsu Ōsaka](https://japanrail.alvaroom.org/#/line/kintetsu-osaka) | Kintetsu | 48 | Kintetsu 80000 «Hinotori», Kintetsu 50000 «Shimakaze» | — | 1 |
| MO | [Monorraíl de Ōsaka](https://japanrail.alvaroom.org/#/line/osaka-monorail) | Osaka Monorail | 14 | Monorraíl de Ōsaka serie 3000 | — | 1 |
| HN | [Tranvía Hankai](https://japanrail.alvaroom.org/#/line/hankai) | Hankai Tramway | 31 | Hankai Mo 161 | — | 1 |
| HN | [Tranvía Hankai: Uemachi](https://japanrail.alvaroom.org/#/line/hankai-uemachi) | Hankai Tramway | 10 | — | — | 0 |
| R | [JR Hanwa](https://japanrail.alvaroom.org/#/line/hanwa) | JR West | 35 | Serie 281 «Haruka» | — | 2 |
| R | [JR Hanwa (ramal Higashi-Hagoromo)](https://japanrail.alvaroom.org/#/line/hanwa-branch) | JR West | 2 | — | — | 0 |
| G | [JR Takarazuka](https://japanrail.alvaroom.org/#/line/jr-takarazuka) | JR West | 22 | Serie 321 | — | 0 |
| H | [JR Gakkentoshi (Katamachi)](https://japanrail.alvaroom.org/#/line/katamachi) | JR West | 24 | Serie 321 | — | 0 |
| Q | [JR Yamatoji](https://japanrail.alvaroom.org/#/line/yamatoji) | JR West | 18 | — | — | 1 |
| H | [JR Tōzai](https://japanrail.alvaroom.org/#/line/jr-tozai) | JR West | 9 | Serie 321 | — | 0 |
| F | [JR Osaka Higashi](https://japanrail.alvaroom.org/#/line/osaka-higashi) | JR West | 15 | — | — | 1 |
| U | [JR Sakurai (Man'yō Mahoroba)](https://japanrail.alvaroom.org/#/line/sakurai) | JR West | 14 | — | — | 1 |
| F | [Kintetsu Minami-Ōsaka](https://japanrail.alvaroom.org/#/line/kintetsu-minami-osaka) | Kintetsu | 28 | — | — | 1 |
| O | [Kintetsu Nagano](https://japanrail.alvaroom.org/#/line/kintetsu-nagano) | Kintetsu | 8 | — | — | 0 |
| N | [Kintetsu Dōmyōji](https://japanrail.alvaroom.org/#/line/kintetsu-domyoji) | Kintetsu | 3 | — | — | 0 |
| P | [Kintetsu Gose](https://japanrail.alvaroom.org/#/line/kintetsu-gose) | Kintetsu | 4 | — | — | 0 |
| C | [Kintetsu Keihanna](https://japanrail.alvaroom.org/#/line/kintetsu-keihanna) | Kintetsu | 8 | — | — | 0 |
| G | [Kintetsu Ikoma](https://japanrail.alvaroom.org/#/line/kintetsu-ikoma) | Kintetsu | 12 | — | — | 0 |
| B | [Kintetsu Kashihara](https://japanrail.alvaroom.org/#/line/kintetsu-kashihara) | Kintetsu | 17 | — | — | 1 |
| F | [Kintetsu Yoshino](https://japanrail.alvaroom.org/#/line/kintetsu-yoshino) | Kintetsu | 16 | — | — | 2 |
| T | [JR Wakayama](https://japanrail.alvaroom.org/#/line/wakayama-line) | JR West | 36 | — | — | 1 |
| Y | [Funicular de Ikoma](https://japanrail.alvaroom.org/#/line/ikoma-cable) | Kintetsu | 5 | — | — | 2 |
| H | [Kintetsu Tenri](https://japanrail.alvaroom.org/#/line/kintetsu-tenri) | Kintetsu | 4 | — | — | 0 |
| I | [Kintetsu Tawaramoto](https://japanrail.alvaroom.org/#/line/kintetsu-tawaramoto) | Kintetsu | 8 | — | — | 0 |
| J | [Kintetsu Shigi](https://japanrail.alvaroom.org/#/line/kintetsu-shigi) | Kintetsu | 3 | — | — | 0 |
| HK | [Hankyu Senri](https://japanrail.alvaroom.org/#/line/hankyu-senri) | Hankyu | 11 | Osaka Metro serie 66 | — | 0 |
| HK | [Hankyu Minoo](https://japanrail.alvaroom.org/#/line/hankyu-minoo) | Hankyu | 4 | — | — | 1 |
| SB | [Nankai Semboku](https://japanrail.alvaroom.org/#/line/nankai-semboku) | Nankai | 6 | — | — | 1 |
| NK | [Nankai Shiomibashi](https://japanrail.alvaroom.org/#/line/nankai-shiomibashi) | Nankai | 6 | — | — | 1 |
| NK | [Nankai Takashinohama](https://japanrail.alvaroom.org/#/line/nankai-takashinohama) | Nankai | 3 | — | — | 0 |
| KH | [Keihan Katano](https://japanrail.alvaroom.org/#/line/keihan-katano) | Keihan | 8 | — | — | 0 |
| KH | [Keihan Nakanoshima](https://japanrail.alvaroom.org/#/line/keihan-nakanoshima) | Keihan | 5 | — | — | 0 |
| MO | [Monorraíl de Ōsaka (ramal de Saito)](https://japanrail.alvaroom.org/#/line/osaka-monorail-saito) | Osaka Monorail | 5 | Monorraíl de Ōsaka serie 3000 | — | 0 |
| NS | [Nose Dentetsu Myōken](https://japanrail.alvaroom.org/#/line/nose-myoken) | Nose Dentetsu | 14 | — | — | 1 |
| NS | [Nose Dentetsu Nissei](https://japanrail.alvaroom.org/#/line/nose-nissei) | Nose Dentetsu | 2 | — | — | 0 |

### Kōbe 神戸

| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |
|---|---|---|--:|---|---|--:|
| A | [Línea JR Kōbe](https://japanrail.alvaroom.org/#/line/jr-kobe) | JR West | 28 | Serie 225, Serie 223 | — | 2 |
| S | [Metro de Kōbe: Seishin-Yamate](https://japanrail.alvaroom.org/#/line/kobe-seishin) | Metro de Kōbe | 17 | Metro de Kōbe serie 6000 | — | 1 |
| K | [Metro de Kōbe: Kaigan](https://japanrail.alvaroom.org/#/line/kobe-kaigan) | Metro de Kōbe | 10 | — | — | 0 |
| P | [Port Liner](https://japanrail.alvaroom.org/#/line/port-liner) | Kobe New Transit | 12 | Port Liner serie 2000 | Port Liner serie 8000 | 1 |
| R | [Rokkō Liner](https://japanrail.alvaroom.org/#/line/rokko-liner) | Kobe New Transit | 6 | — | — | 0 |
| HK | [Hankyu Imazu](https://japanrail.alvaroom.org/#/line/hankyu-imazu) | Hankyu | 10 | — | — | 1 |
| HK | [Hankyu Itami](https://japanrail.alvaroom.org/#/line/hankyu-itami) | Hankyu | 4 | — | — | 0 |
| HK | [Hankyu Kōyō](https://japanrail.alvaroom.org/#/line/hankyu-koyo) | Hankyu | 3 | — | — | 0 |
| HS | [Hanshin Mukogawa](https://japanrail.alvaroom.org/#/line/hanshin-mukogawa) | Hanshin | 4 | — | — | 0 |
| I | [JR Kakogawa](https://japanrail.alvaroom.org/#/line/kakogawa) | JR West | 21 | — | — | 1 |
| J | [JR Bantan](https://japanrail.alvaroom.org/#/line/bantan) | JR West | 18 | — | — | 1 |
| K | [JR Kishin (Himeji–Kōzuki)](https://japanrail.alvaroom.org/#/line/kishin) | JR West | 13 | — | — | 1 |
| A | [JR Sanyō (Akashi–Kamigōri)](https://japanrail.alvaroom.org/#/line/sanyo-main-west) | JR West | 20 | — | — | 1 |
| G | [JR Fukuchiyama (Sasayamaguchi–Fukuchiyama)](https://japanrail.alvaroom.org/#/line/fukuchiyama-north) | JR West | 10 | — | — | 1 |
| HJ | [Hōjō Tetsudō](https://japanrail.alvaroom.org/#/line/hojo) | Hōjō Tetsudō | 8 | — | — | 1 |
| CZ | [Chizu Express](https://japanrail.alvaroom.org/#/line/chizu) | Chizu Kyūkō | 14 | — | — | 1 |
| A | [JR Akō](https://japanrail.alvaroom.org/#/line/ako) | JR West | 10 | — | — | 1 |
| MC | [Funicular de Maya](https://japanrail.alvaroom.org/#/line/maya-cable) | Ayuntamiento de Kōbe | 2 | — | — | 1 |
| RC | [Funicular de Rokkō](https://japanrail.alvaroom.org/#/line/rokko-cable) | Rokkō Maya Tetsudō | 2 | — | — | 1 |
| SY | [Sanyō Aboshi](https://japanrail.alvaroom.org/#/line/sanyo-aboshi) | Sanyō Dentetsu | 7 | — | — | 1 |
| A | [JR San'in (Yanase–Igumi)](https://japanrail.alvaroom.org/#/line/sanin-hyogo) | JR West | 19 | — | — | 1 |
| HS | [Kōbe Kōsoku](https://japanrail.alvaroom.org/#/line/kobe-kosoku) | Kōbe Kōsoku | 9 | — | — | 1 |
| KB | [Kōbe Dentetsu Arima](https://japanrail.alvaroom.org/#/line/kobe-electric-arima) | Kōbe Dentetsu | 16 | — | — | 1 |
| KB | [Kōbe Dentetsu Sanda](https://japanrail.alvaroom.org/#/line/kobe-electric-sanda) | Kōbe Dentetsu | 10 | — | — | 0 |
| KB | [Kōbe Dentetsu Ao](https://japanrail.alvaroom.org/#/line/kobe-electric-ao) | Kōbe Dentetsu | 20 | — | — | 0 |
| KB | [Kōbe Dentetsu Kōen-toshi](https://japanrail.alvaroom.org/#/line/kobe-electric-koen-toshi) | Kōbe Dentetsu | 6 | — | — | 0 |
| SY | [Sanyō Dentetsu](https://japanrail.alvaroom.org/#/line/sanyo-electric) | Sanyō Dentetsu | 43 | — | — | 1 |

### Nagoya 名古屋

| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |
|---|---|---|--:|---|---|--:|
| H | [Metro de Nagoya: Higashiyama](https://japanrail.alvaroom.org/#/line/nagoya-higashiyama) | Metro de Nagoya | 22 | Metro de Nagoya serie N1000 | — | 1 |
| M | [Metro de Nagoya: Meijō](https://japanrail.alvaroom.org/#/line/nagoya-meijo) | Metro de Nagoya | 28 | — | — | 1 |
| E | [Metro de Nagoya: Meikō](https://japanrail.alvaroom.org/#/line/nagoya-meiko) | Metro de Nagoya | 7 | — | — | 0 |
| T | [Metro de Nagoya: Tsurumai](https://japanrail.alvaroom.org/#/line/nagoya-tsurumai) | Metro de Nagoya | 20 | Metro de Nagoya serie N3000 | — | 0 |
| S | [Metro de Nagoya: Sakura-dōri](https://japanrail.alvaroom.org/#/line/nagoya-sakuradori) | Metro de Nagoya | 21 | — | — | 0 |
| K | [Metro de Nagoya: Kamiiida](https://japanrail.alvaroom.org/#/line/nagoya-kamiiida) | Metro de Nagoya | 2 | — | — | 0 |
| NH | [Meitetsu principal](https://japanrail.alvaroom.org/#/line/meitetsu-main) | Meitetsu | 60 | Meitetsu 2000 «μSKY», Meitetsu serie 9500 | Meitetsu 7000 «Panorama Car» | 1 |
| MU | [Meitetsu Mikawa](https://japanrail.alvaroom.org/#/line/meitetsu-mikawa) | Meitetsu | 24 | — | — | 1 |
| BS | [Meitetsu Bisai](https://japanrail.alvaroom.org/#/line/meitetsu-bisai) | Meitetsu | 23 | — | — | 1 |
| GN | [Meitetsu Gamagōri](https://japanrail.alvaroom.org/#/line/meitetsu-gamagori) | Meitetsu | 11 | — | — | 1 |
| GN | [Meitetsu Nishio](https://japanrail.alvaroom.org/#/line/meitetsu-nishio) | Meitetsu | 14 | — | — | 0 |
| TB | [Meitetsu Tsushima](https://japanrail.alvaroom.org/#/line/meitetsu-tsushima) | Meitetsu | 8 | — | — | 0 |
| HM | [Meitetsu Hiromi](https://japanrail.alvaroom.org/#/line/meitetsu-hiromi) | Meitetsu | 12 | — | — | 0 |
| TK | [Meitetsu Toyokawa](https://japanrail.alvaroom.org/#/line/meitetsu-toyokawa) | Meitetsu | 6 | — | — | 1 |
| KC | [Meitetsu Chita Nueva](https://japanrail.alvaroom.org/#/line/meitetsu-chita-new) | Meitetsu | 6 | — | — | 1 |
| CH | [Meitetsu Chikkō](https://japanrail.alvaroom.org/#/line/meitetsu-chikko) | Meitetsu | 2 | — | — | 1 |
| AL | [Aichi Loop Line](https://japanrail.alvaroom.org/#/line/aichi-loop) | Aichi Kanjō Tetsudō | 23 | — | — | 1 |
| JH | [Jōhoku Line](https://japanrail.alvaroom.org/#/line/johoku) | Tōkai Kōtsū Jigyō | 6 | — | — | 1 |
| CD | [JR Iida (Toyohashi–Nagashino)](https://japanrail.alvaroom.org/#/line/iida) | JR Central | 27 | — | — | 1 |
| CE | [JR Taketoyo](https://japanrail.alvaroom.org/#/line/taketoyo) | JR Central | 10 | — | — | 1 |
| CA | [JR Tōkaidō (Toyohashi–Ōgaki)](https://japanrail.alvaroom.org/#/line/tokaido-aichi) | JR Central | 57 | — | — | 1 |
| CF | [JR Chūō Oeste (Nagoya–Nakatsugawa)](https://japanrail.alvaroom.org/#/line/chuo-west) | JR Central | 29 | — | — | 1 |
| CJ | [JR Kansai (Nagoya–Kameyama)](https://japanrail.alvaroom.org/#/line/kansai-nagoya) | JR Central | 30 | — | — | 0 |
| TA | [Meitetsu Tokoname](https://japanrail.alvaroom.org/#/line/meitetsu-tokoname) | Meitetsu | 24 | Meitetsu 2000 «μSKY» | — | 0 |
| TA | [Meitetsu Aeropuerto](https://japanrail.alvaroom.org/#/line/meitetsu-airport) | Meitetsu | 3 | Meitetsu 2000 «μSKY» | — | 1 |
| IY | [Meitetsu Inuyama](https://japanrail.alvaroom.org/#/line/meitetsu-inuyama) | Meitetsu | 20 | Meitetsu serie 9500 | — | 1 |
| ST | [Meitetsu Seto](https://japanrail.alvaroom.org/#/line/meitetsu-seto) | Meitetsu | 20 | — | — | 1 |
| KM | [Meitetsu Komaki](https://japanrail.alvaroom.org/#/line/meitetsu-komaki) | Meitetsu | 14 | — | — | 0 |
| KC | [Meitetsu Kōwa](https://japanrail.alvaroom.org/#/line/meitetsu-kowa) | Meitetsu | 20 | — | — | 0 |
| TT | [Meitetsu Toyota](https://japanrail.alvaroom.org/#/line/meitetsu-toyota) | Meitetsu | 9 | — | — | 1 |
| E | [Kintetsu Nagoya](https://japanrail.alvaroom.org/#/line/kintetsu-nagoya) | Kintetsu | 53 | — | — | 2 |
| AN | [Aonami Line](https://japanrail.alvaroom.org/#/line/aonami) | Aonami Line | 11 | Aonami serie 1000 | — | 1 |
| L | [Linimo](https://japanrail.alvaroom.org/#/line/linimo) | Aichi Rapid Transit | 9 | Linimo serie 100 | — | 2 |

### Fukuoka 福岡

| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |
|---|---|---|--:|---|---|--:|
| JA | [JR Kagoshima (Mojikō–Ōmuta)](https://japanrail.alvaroom.org/#/line/kagoshima-main-fukuoka) | JR Kyushu | 72 | — | — | 1 |
| JF | [JR Nippō (Kokura–Yanagigaura)](https://japanrail.alvaroom.org/#/line/nippo) | JR Kyushu | 23 | — | — | 0 |
| JC | [JR Chikuhō (Fukuhoku Yutaka)](https://japanrail.alvaroom.org/#/line/chikuho-main) | JR Kyushu | 31 | — | — | 1 |
| JC | [JR Sasaguri](https://japanrail.alvaroom.org/#/line/sasaguri) | JR Kyushu | 12 | — | — | 0 |
| JI | [JR Hita-Hikosan](https://japanrail.alvaroom.org/#/line/hitahikosan) | JR Kyushu | 16 | — | — | 0 |
| JD | [JR Kyūdai (Yufu Kōgen)](https://japanrail.alvaroom.org/#/line/kyudai) | JR Kyushu | 16 | — | — | 0 |
| JJ | [JR Gotōji](https://japanrail.alvaroom.org/#/line/gotoji) | JR Kyushu | 5 | — | — | 0 |
| JR | [JR Hakata-Minami](https://japanrail.alvaroom.org/#/line/hakata-minami) | JR West | 2 | — | — | 2 |
| CK | [Chikuhō Dentetsu](https://japanrail.alvaroom.org/#/line/chikuho-dentetsu) | Chikuhō Denki Tetsudō | 22 | — | — | 1 |
| AM | [Amagi Tetsudō](https://japanrail.alvaroom.org/#/line/amagi) | Amagi Tetsudō | 12 | — | — | 0 |
| AM | [Nishitetsu Amagi](https://japanrail.alvaroom.org/#/line/nishitetsu-amagi) | Nishitetsu | 12 | — | — | 0 |
| HC | [Heisei Chikuhō: línea Ita](https://japanrail.alvaroom.org/#/line/heisei-ita) | Heisei Chikuhō Tetsudō | 15 | — | — | 0 |
| HC | [Heisei Chikuhō: línea Tagawa](https://japanrail.alvaroom.org/#/line/heisei-tagawa) | Heisei Chikuhō Tetsudō | 17 | — | — | 0 |
| HC | [Heisei Chikuhō: línea Itoda](https://japanrail.alvaroom.org/#/line/heisei-itoda) | Heisei Chikuhō Tetsudō | 6 | — | — | 0 |
| KM | [Monorraíl de Kitakyūshū](https://japanrail.alvaroom.org/#/line/kitakyushu-monorail) | Kitakyūshū Kōsoku Tetsudō | 13 | — | — | 1 |
| MR | [Mojikō Retro (Shiokaze)](https://japanrail.alvaroom.org/#/line/mojiko-retro) | Heisei Chikuhō Tetsudō | 4 | — | — | 2 |
| HS | [Slope Car del monte Hiko](https://japanrail.alvaroom.org/#/line/hikosan-slope) | Slope Car del monte Hiko | 4 | — | — | 1 |
| K | [Metro de Fukuoka: Kūkō](https://japanrail.alvaroom.org/#/line/fukuoka-kuko) | Metro de Fukuoka | 13 | Metro de Fukuoka serie 2000 | — | 1 |
| H | [Metro de Fukuoka: Hakozaki](https://japanrail.alvaroom.org/#/line/fukuoka-hakozaki) | Metro de Fukuoka | 7 | Metro de Fukuoka serie 2000 | — | 0 |
| N | [Metro de Fukuoka: Nanakuma](https://japanrail.alvaroom.org/#/line/fukuoka-nanakuma) | Metro de Fukuoka | 18 | Metro de Fukuoka serie 3000 | — | 1 |
| T | [Nishitetsu Tenjin-Ōmuta](https://japanrail.alvaroom.org/#/line/nishitetsu-omuta) | Nishitetsu | 50 | Nishitetsu serie 9000 | — | 1 |
| NK | [Nishitetsu Kaizuka](https://japanrail.alvaroom.org/#/line/nishitetsu-kaizuka) | Nishitetsu | 10 | — | — | 0 |
| D | [Nishitetsu Dazaifu](https://japanrail.alvaroom.org/#/line/nishitetsu-dazaifu) | Nishitetsu | 3 | — | — | 1 |
| JK | [JR Chikuhi](https://japanrail.alvaroom.org/#/line/chikuhi) | JR Kyushu | 21 | Metro de Fukuoka serie 2000 | — | 1 |
| JD | [JR Kashii](https://japanrail.alvaroom.org/#/line/kashii) | JR Kyushu | 16 | Serie BEC819 «DENCHA» | — | 1 |

### Sapporo 札幌

| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |
|---|---|---|--:|---|---|--:|
| N | [Metro de Sapporo: Namboku](https://japanrail.alvaroom.org/#/line/sapporo-namboku) | Transporte de Sapporo | 16 | Metro de Sapporo serie 5000 | — | 2 |
| T | [Metro de Sapporo: Tōzai](https://japanrail.alvaroom.org/#/line/sapporo-tozai) | Transporte de Sapporo | 19 | Metro de Sapporo serie 8000 | — | 0 |
| H | [Metro de Sapporo: Tōhō](https://japanrail.alvaroom.org/#/line/sapporo-toho) | Transporte de Sapporo | 14 | Metro de Sapporo serie 9000 | Metro de Sapporo serie 7000 | 0 |
| SC | [Tranvía de Sapporo](https://japanrail.alvaroom.org/#/line/sapporo-tram) | Transporte de Sapporo | 24 | Sapporo A1200 «Polaris», Tranvía de Sapporo 3300, Tranvía de Sapporo 8500, Tranvía de Sapporo 1100 «Sirius» | — | 2 |
| S | [JR Hakodate (Otaru–Sapporo)](https://japanrail.alvaroom.org/#/line/hakodate-s) | JR Hokkaido | 15 | JR Hokkaidō serie 721, JR Hokkaidō serie 731, JR Hokkaidō serie 733, JR Hokkaidō serie 735, JR Hokkaidō Kiha 201 | Serie 711 «el tren rojo» | 3 |
| A | [JR Hakodate (Sapporo–Iwamizawa)](https://japanrail.alvaroom.org/#/line/hakodate-a) | JR Hokkaido | 13 | JR Hokkaidō serie 721, JR Hokkaidō serie 731, JR Hokkaidō serie 733, JR Hokkaidō serie 735, JR Hokkaidō serie 789 | Serie 711 «el tren rojo», JR Hokkaidō serie 785 | 2 |
| H | [JR Chitose](https://japanrail.alvaroom.org/#/line/chitose) | JR Hokkaido | 16 | JR Hokkaidō serie 721, JR Hokkaidō serie 731, JR Hokkaidō serie 733, JR Hokkaidō serie 735 | Serie 711 «el tren rojo», JR Hokkaidō serie 785 | 2 |
| AP | [JR Chitose (ramal del aeropuerto)](https://japanrail.alvaroom.org/#/line/chitose-airport) | JR Hokkaido | 2 | JR Hokkaidō serie 721, JR Hokkaidō serie 733 | JR Hokkaidō serie 785 | 2 |
| G | [JR Gakuentoshi (Sasshō)](https://japanrail.alvaroom.org/#/line/sassho) | JR Hokkaido | 15 | JR Hokkaidō serie 721, JR Hokkaidō serie 731, JR Hokkaidō serie 733 | — | 2 |
| S | [JR Hakodate (Hakodate–Otaru)](https://japanrail.alvaroom.org/#/line/hakodate-yamasen) | JR Hokkaido | 43 | — | — | 1 |
| A | [JR Hakodate (Iwamizawa–Asahikawa)](https://japanrail.alvaroom.org/#/line/hakodate-asahikawa) | JR Hokkaido | 17 | — | — | 0 |
| K | [JR Sekishō](https://japanrail.alvaroom.org/#/line/sekisho) | JR Hokkaido | 7 | — | — | 2 |
| SR | [Sorachi Tetsudō](https://japanrail.alvaroom.org/#/line/sorachi) | Sorachi Tetsudō | 3 | — | — | 0 |
| H | [JR Muroran](https://japanrail.alvaroom.org/#/line/muroran) | JR Hokkaido | 48 | — | — | 1 |
| K | [JR Nemuro (Hanasaki)](https://japanrail.alvaroom.org/#/line/nemuro) | JR Hokkaido | 50 | — | — | 1 |
| W | [JR Sōya](https://japanrail.alvaroom.org/#/line/soya) | JR Hokkaido | 35 | — | — | 1 |
| A | [JR Sekihoku](https://japanrail.alvaroom.org/#/line/sekihoku) | JR Hokkaido | 31 | — | — | 1 |
| B | [JR Senmō](https://japanrail.alvaroom.org/#/line/senmo) | JR Hokkaido | 24 | — | — | 2 |
| F | [JR Furano](https://japanrail.alvaroom.org/#/line/furano) | JR Hokkaido | 18 | — | — | 1 |
| H | [JR Hidaka](https://japanrail.alvaroom.org/#/line/hidaka) | JR Hokkaido | 4 | — | — | 1 |
|  | [Dōnan Isaribi Tetsudō](https://japanrail.alvaroom.org/#/line/donan-isaribi) | Dōnan Isaribi Tetsudō | 12 | — | — | 2 |

### Sendai 仙台

| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |
|---|---|---|--:|---|---|--:|
|  | [JR Tōhoku (Fukushima–Ichinoseki)](https://japanrail.alvaroom.org/#/line/tohoku-main) | JR East | 48 | — | — | 1 |
|  | [JR Tōhoku: ramal de Rifu](https://japanrail.alvaroom.org/#/line/rifu) | JR East | 3 | — | — | 1 |
| AB | [Abukuma Kyūkō](https://japanrail.alvaroom.org/#/line/abukuma) | Abukuma Kyūkō | 24 | — | — | 1 |
|  | [JR Ishinomaki](https://japanrail.alvaroom.org/#/line/ishinomaki) | JR East | 14 | — | — | 1 |
|  | [JR Kesennuma (tramo de tren)](https://japanrail.alvaroom.org/#/line/kesennuma-rail) | JR East | 6 | — | — | 1 |
|  | [JR Jōban (Sendai–Shinchi)](https://japanrail.alvaroom.org/#/line/joban-sendai) | JR East | 11 | — | — | 1 |
|  | [JR Rikuu East](https://japanrail.alvaroom.org/#/line/rikuu-east) | JR East | 23 | — | — | 1 |
|  | [JR Ōfunato (tramo de tren)](https://japanrail.alvaroom.org/#/line/ofunato-rail) | JR East | 14 | — | — | 2 |
| N | [Metro de Sendai: Namboku](https://japanrail.alvaroom.org/#/line/sendai-namboku) | Metro de Sendai | 17 | Metro de Sendai serie 1000N | — | 0 |
| T | [Metro de Sendai: Tōzai](https://japanrail.alvaroom.org/#/line/sendai-tozai) | Metro de Sendai | 13 | Metro de Sendai serie 2000 | — | 1 |
| JR | [JR Senseki](https://japanrail.alvaroom.org/#/line/senseki) | JR East | 32 | — | — | 1 |
| JR | [JR Senzan](https://japanrail.alvaroom.org/#/line/senzan) | JR East | 20 | — | — | 1 |
| SAT | [Sendai Airport Access](https://japanrail.alvaroom.org/#/line/sendai-airport) | JR East | 8 | — | — | 0 |

### Hiroshima 広島

| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |
|---|---|---|--:|---|---|--:|
| G | [JR Sanyō (Itozaki–Ōtake)](https://japanrail.alvaroom.org/#/line/sanyo-hiroshima) | JR West | 48 | — | — | 1 |
| Y | [JR Kure](https://japanrail.alvaroom.org/#/line/kure) | JR West | 28 | — | — | 1 |
| P | [JR Geibi](https://japanrail.alvaroom.org/#/line/geibi) | JR West | 44 | — | — | 1 |
| Z | [JR Fukuen](https://japanrail.alvaroom.org/#/line/fukuen) | JR West | 27 | — | — | 0 |
| IB | [Ibara Tetsudō](https://japanrail.alvaroom.org/#/line/ibara) | Ibara Tetsudō | 12 | — | — | 1 |
| E | [JR Kisuki](https://japanrail.alvaroom.org/#/line/kisuki) | JR West | 18 | — | — | 2 |
| 1 | [Hiroden: línea 1](https://japanrail.alvaroom.org/#/line/hiroden-1) | Hiroden | 25 | Hiroden 5100 «Green Mover Max», Hiroden 1000 «Green Mover LEX», Hiroden serie 650 (supervivientes de la bomba) | — | 1 |
| 2 | [Hiroden: línea 2](https://japanrail.alvaroom.org/#/line/hiroden-2) | Hiroden | 39 | Hiroden 5100 «Green Mover Max» | — | 1 |
| 3 | [Hiroden: línea 3](https://japanrail.alvaroom.org/#/line/hiroden-3) | Hiroden | 18 | Hiroden 1000 «Green Mover LEX» | — | 0 |
| 5 | [Hiroden: línea 5](https://japanrail.alvaroom.org/#/line/hiroden-5) | Hiroden | 17 | Hiroden 1000 «Green Mover LEX» | — | 0 |
| 6 | [Hiroden: línea 6](https://japanrail.alvaroom.org/#/line/hiroden-6) | Hiroden | 18 | — | — | 0 |
| 7 | [Hiroden: línea 7](https://japanrail.alvaroom.org/#/line/hiroden-7) | Hiroden | 26 | — | — | 0 |
| 8 | [Hiroden: línea 8](https://japanrail.alvaroom.org/#/line/hiroden-8) | Hiroden | 12 | — | — | 0 |
| 9 | [Hiroden: línea 9 (Hakushima)](https://japanrail.alvaroom.org/#/line/hiroden-9) | Hiroden | 5 | — | — | 0 |
| L | [Hiroden: línea circular](https://japanrail.alvaroom.org/#/line/hiroden-loop) | Hiroden | 21 | — | — | 0 |
| A | [Astram](https://japanrail.alvaroom.org/#/line/astram) | Astram | 22 | Astram serie 7000 | — | 1 |
| B | [JR Kabe](https://japanrail.alvaroom.org/#/line/kabe) | JR West | 16 | — | — | 0 |

### Tranvías de otras ciudades 路面電車

| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |
|---|---|---|--:|---|---|--:|
| 1 | [Nagasaki: línea 1](https://japanrail.alvaroom.org/#/line/nagasaki-1) | Tranvía de Nagasaki | 26 | — | — | 1 |
| 2 | [Nagasaki: línea 2](https://japanrail.alvaroom.org/#/line/nagasaki-2) | Tranvía de Nagasaki | 30 | — | — | 0 |
| 3 | [Nagasaki: línea 3](https://japanrail.alvaroom.org/#/line/nagasaki-3) | Tranvía de Nagasaki | 24 | — | — | 0 |
| 4 | [Nagasaki: línea 4](https://japanrail.alvaroom.org/#/line/nagasaki-4) | Tranvía de Nagasaki | 10 | — | — | 0 |
| 5 | [Nagasaki: línea 5](https://japanrail.alvaroom.org/#/line/nagasaki-5) | Tranvía de Nagasaki | 13 | — | — | 0 |
| A | [Kumamoto: línea A](https://japanrail.alvaroom.org/#/line/kumamoto-a) | Tranvía de Kumamoto | 26 | Kumamoto serie 9700 | — | 1 |
| B | [Kumamoto: línea B](https://japanrail.alvaroom.org/#/line/kumamoto-b) | Tranvía de Kumamoto | 28 | Kumamoto serie 9700 | — | 0 |
| 1 | [Kagoshima: línea 1](https://japanrail.alvaroom.org/#/line/kagoshima-1) | Tranvía de Kagoshima | 24 | — | — | 1 |
| 2 | [Kagoshima: línea 2](https://japanrail.alvaroom.org/#/line/kagoshima-2) | Tranvía de Kagoshima | 20 | — | — | 0 |
| 2 | [Hakodate: línea 2](https://japanrail.alvaroom.org/#/line/hakodate-2) | Tranvía de Hakodate | 23 | — | — | 1 |
| 5 | [Hakodate: línea 5](https://japanrail.alvaroom.org/#/line/hakodate-5) | Tranvía de Hakodate | 23 | — | — | 0 |
| H | [Okayama: línea Higashiyama](https://japanrail.alvaroom.org/#/line/okayama-higashiyama) | Okayama Dentetsu | 10 | Okayama 9200 «MOMO» | — | 1 |
| S | [Okayama: línea Seikibashi](https://japanrail.alvaroom.org/#/line/okayama-seikibashi) | Okayama Dentetsu | 9 | Okayama 9200 «MOMO» | — | 0 |
| 伊野 | [Tosaden: línea Ino](https://japanrail.alvaroom.org/#/line/tosaden-ino) | Tosaden Kōtsū | 33 | — | — | 1 |
| 後免 | [Tosaden: línea Gomen](https://japanrail.alvaroom.org/#/line/tosaden-gomen) | Tosaden Kōtsū | 34 | — | — | 0 |
| P | [Toyama: línea del puerto (Portram)](https://japanrail.alvaroom.org/#/line/toyama-port) | Toyama Chihō Railway | 10 | Portram TLR0600 | — | 1 |
| T | [Toyama Chihō: línea principal](https://japanrail.alvaroom.org/#/line/toyama-main) | Toyama Chihō Railway | 9 | — | — | 1 |
| T | [Toyama Chihō: línea Tateyama](https://japanrail.alvaroom.org/#/line/toyama-tateyama) | Toyama Chihō Railway | 10 | — | — | 1 |
| 1 | [Matsuyama: tranvía circular](https://japanrail.alvaroom.org/#/line/iyotetsu-loop) | Iyotetsu | 21 | «Botchan Ressha» | — | 1 |
| 6 | [Matsuyama: línea Honmachi](https://japanrail.alvaroom.org/#/line/iyotetsu-honmachi) | Iyotetsu | 7 | — | — | 0 |
| IY | [Iyotetsu Takahama](https://japanrail.alvaroom.org/#/line/iyotetsu-takahama) | Iyotetsu | 10 | — | — | 0 |
| IY | [Iyotetsu Yokogawara](https://japanrail.alvaroom.org/#/line/iyotetsu-yokogawara) | Iyotetsu | 15 | — | — | 0 |
| IY | [Iyotetsu Gunchū](https://japanrail.alvaroom.org/#/line/iyotetsu-gunchu) | Iyotetsu | 12 | — | — | 0 |
| T | [Toyohashi: tranvía Azumada](https://japanrail.alvaroom.org/#/line/toyohashi-azumada) | Toyohashi Railroad | 20 | — | — | 0 |
| A | [Toyohashi Atsumi](https://japanrail.alvaroom.org/#/line/toyohashi-atsumi) | Toyohashi Railroad | 16 | — | — | 0 |
| D | [JR Dosan](https://japanrail.alvaroom.org/#/line/dosan) | jr-shikoku | 62 | — | — | 2 |
| GN | [Tosa Kuroshio: Gomen–Nahari](https://japanrail.alvaroom.org/#/line/kuroshio-asa) | Tosa Kuroshio Tetsudō | 21 | — | — | 2 |
| TK | [Tosa Kuroshio: Nakamura](https://japanrail.alvaroom.org/#/line/kuroshio-nakamura) | Tosa Kuroshio Tetsudō | 15 | — | — | 1 |
| TK | [Tosa Kuroshio: Sukumo](https://japanrail.alvaroom.org/#/line/kuroshio-sukumo) | Tosa Kuroshio Tetsudō | 8 | — | — | 1 |
| G | [JR Yodo](https://japanrail.alvaroom.org/#/line/yodo) | jr-shikoku | 19 | — | — | 2 |
| TD | [Tosaden: línea Sanbashi](https://japanrail.alvaroom.org/#/line/tosaden-sambashi) | Tosaden Kōtsū | 11 | — | — | 0 |
| JK | [JR Ibusuki-Makurazaki](https://japanrail.alvaroom.org/#/line/ibusuki) | JR Kyushu | 36 | — | — | 3 |
| JA | [JR Kagoshima (Sendai–Kagoshima)](https://japanrail.alvaroom.org/#/line/kagoshima-main-south) | JR Kyushu | 14 | — | — | 1 |
| JF | [JR Nippō (Miyazaki–Kagoshima)](https://japanrail.alvaroom.org/#/line/nippo-south) | JR Kyushu | 18 | — | — | 1 |
| OR | [Hisatsu Orange Tetsudō](https://japanrail.alvaroom.org/#/line/hisatsu-orange) | Hisatsu Orange Tetsudō | 28 | — | — | 2 |
|  | [JR Hisatsu](https://japanrail.alvaroom.org/#/line/hisatsu) | JR Kyushu | 18 | — | — | 3 |
|  | [JR Kitto](https://japanrail.alvaroom.org/#/line/kitto) | JR Kyushu | 17 | — | — | 1 |
|  | [JR Nichinan](https://japanrail.alvaroom.org/#/line/nichinan) | JR Kyushu | 28 | — | — | 1 |
| F | [Fukui: línea Fukubu](https://japanrail.alvaroom.org/#/line/fukui-fukubu) | Fukui Railway | 24 | — | — | 1 |

## Huecos detectados

Salen solos de los datos: son buenas tareas pequeñas para ir completando.

- **Líneas sin trenes actuales** (253): [JR San'in (Sonobe–Fukuchiyama)](https://japanrail.alvaroom.org/#/line/sanin-fukuchiyama), [JR Maizuru](https://japanrail.alvaroom.org/#/line/maizuru), [JR Obama](https://japanrail.alvaroom.org/#/line/obama), [Tango: línea Miyafuku](https://japanrail.alvaroom.org/#/line/tango-miyafuku), [Tango: línea Miyamai](https://japanrail.alvaroom.org/#/line/tango-miyamai), [Tango: línea Miyatoyo](https://japanrail.alvaroom.org/#/line/tango-miyatoyo), [JR Kansai (Kamo–Kameyama)](https://japanrail.alvaroom.org/#/line/kansai-east), [Funicular de Eizan](https://japanrail.alvaroom.org/#/line/eizan-cable), [Funicular de Amanohashidate](https://japanrail.alvaroom.org/#/line/amanohashidate-cable), [Línea Hankyu Arashiyama](https://japanrail.alvaroom.org/#/line/hankyu-arashiyama), [JR Uchibō](https://japanrail.alvaroom.org/#/line/uchibo), [JR Sotobō](https://japanrail.alvaroom.org/#/line/sotobo), [JR Sōbu (Chiba–Chōshi)](https://japanrail.alvaroom.org/#/line/sobu-main), [JR Narita](https://japanrail.alvaroom.org/#/line/narita-line), [JR Narita (ramal de Abiko)](https://japanrail.alvaroom.org/#/line/narita-abiko), [JR Tōgane](https://japanrail.alvaroom.org/#/line/togane), [JR Kururi](https://japanrail.alvaroom.org/#/line/kururi), [JR Kashima](https://japanrail.alvaroom.org/#/line/kashima), [Kominato Tetsudō](https://japanrail.alvaroom.org/#/line/kominato), [Isumi Tetsudō](https://japanrail.alvaroom.org/#/line/isumi), [Chōshi Dentetsu](https://japanrail.alvaroom.org/#/line/choshi), [Disney Resort Line](https://japanrail.alvaroom.org/#/line/disney-resort), [Tōkyū Ōimachi](https://japanrail.alvaroom.org/#/line/tokyu-oimachi), [JR Chūō (Takao–Ōtsuki)](https://japanrail.alvaroom.org/#/line/chuo-otsuki), [Inclinado de la presa de Miyagase](https://japanrail.alvaroom.org/#/line/miyagase-incline), [Hakone Tozan](https://japanrail.alvaroom.org/#/line/hakone-tozan), [Funicular de Hakone (Gōra–Sōunzan)](https://japanrail.alvaroom.org/#/line/hakone-tozan-cable), [Izuhakone Daiyūzan](https://japanrail.alvaroom.org/#/line/izuhakone-daiyuzan), [Funicular del monte Ōyama](https://japanrail.alvaroom.org/#/line/oyama-cable), [JR Gotemba](https://japanrail.alvaroom.org/#/line/gotemba), [Chichibu Tetsudō](https://japanrail.alvaroom.org/#/line/chichibu), [Seibu Chichibu](https://japanrail.alvaroom.org/#/line/seibu-chichibu), [Tōbu Isesaki (norte)](https://japanrail.alvaroom.org/#/line/tobu-isesaki), [Tōbu Nikkō](https://japanrail.alvaroom.org/#/line/tobu-nikko), [Funicular del monte Takao](https://japanrail.alvaroom.org/#/line/takao-cable), [Funicular del monte Mitake](https://japanrail.alvaroom.org/#/line/mitake-cable), [Asukarugo (parque de Asukayama)](https://japanrail.alvaroom.org/#/line/asukayama), [Sakura Rail (Matsuchiyama)](https://japanrail.alvaroom.org/#/line/sakura-rail), [JR Yumesaki](https://japanrail.alvaroom.org/#/line/yumesaki), [Osaka Metro Yotsubashi](https://japanrail.alvaroom.org/#/line/yotsubashi), [Osaka Metro Sennichimae](https://japanrail.alvaroom.org/#/line/sennichimae), [Osaka Metro Imazatosuji](https://japanrail.alvaroom.org/#/line/imazatosuji), [New Tram (Nankō Port Town)](https://japanrail.alvaroom.org/#/line/new-tram), [Mizuma Tetsudō](https://japanrail.alvaroom.org/#/line/mizuma), [Kita-Ōsaka Kyūkō](https://japanrail.alvaroom.org/#/line/kita-osaka-kyuko), [Funicular de Nishi-Shigi](https://japanrail.alvaroom.org/#/line/nishi-shigi-cable), [Nankai Tanagawa](https://japanrail.alvaroom.org/#/line/nankai-tanagawa), [Wing Shuttle (ala norte)](https://japanrail.alvaroom.org/#/line/wing-shuttle-norte), [Wing Shuttle (ala sur)](https://japanrail.alvaroom.org/#/line/wing-shuttle-sur), [Tranvía Hankai: Uemachi](https://japanrail.alvaroom.org/#/line/hankai-uemachi), [Metro de Kōbe: Kaigan](https://japanrail.alvaroom.org/#/line/kobe-kaigan), [Rokkō Liner](https://japanrail.alvaroom.org/#/line/rokko-liner), [Keihan Ishiyama-Sakamoto](https://japanrail.alvaroom.org/#/line/keihan-ishiyama), [JR Hokuriku (Maibara–Ōmi-Shiotsu)](https://japanrail.alvaroom.org/#/line/hokuriku-shiga), [JR Tōkaidō (Maibara–Sekigahara)](https://japanrail.alvaroom.org/#/line/tokaido-maibara), [Keisei Kanamachi](https://japanrail.alvaroom.org/#/line/keisei-kanamachi), [Keisei Chiba](https://japanrail.alvaroom.org/#/line/keisei-chiba), [Keisei Chihara](https://japanrail.alvaroom.org/#/line/keisei-chihara), [Keisei Matsudo](https://japanrail.alvaroom.org/#/line/keisei-matsudo), [Keisei Higashi-Narita](https://japanrail.alvaroom.org/#/line/keisei-higashi-narita), [Shibayama Railway](https://japanrail.alvaroom.org/#/line/shibayama), [Keiō Keibajō](https://japanrail.alvaroom.org/#/line/keio-keibajo), [Keiō Dōbutsuen](https://japanrail.alvaroom.org/#/line/keio-dobutsuen), [Odakyū Tama](https://japanrail.alvaroom.org/#/line/odakyu-tama), [Seibu Haijima](https://japanrail.alvaroom.org/#/line/seibu-haijima), [Seibu Kokubunji](https://japanrail.alvaroom.org/#/line/seibu-kokubunji), [Seibu Tamako](https://japanrail.alvaroom.org/#/line/seibu-tamako), [Seibu Tamagawa](https://japanrail.alvaroom.org/#/line/seibu-tamagawa), [Seibu Sayama](https://japanrail.alvaroom.org/#/line/seibu-sayama), [Seibu Yamaguchi (Leo Liner)](https://japanrail.alvaroom.org/#/line/seibu-yamaguchi), [Seibu Seibu-en](https://japanrail.alvaroom.org/#/line/seibu-seibuen), [Seibu Toshima](https://japanrail.alvaroom.org/#/line/seibu-toshima), [Tōbu Kameido](https://japanrail.alvaroom.org/#/line/tobu-kameido), [Tōbu Daishi](https://japanrail.alvaroom.org/#/line/tobu-daishi), [Tōbu Urban Park](https://japanrail.alvaroom.org/#/line/tobu-urban-park), [Tōbu Ogose](https://japanrail.alvaroom.org/#/line/tobu-ogose), [Tōkyū Kodomonokuni](https://japanrail.alvaroom.org/#/line/tokyu-kodomonokuni), [JR Tsurumi](https://japanrail.alvaroom.org/#/line/tsurumi), [JR Nambu (ramal Hama-Kawasaki)](https://japanrail.alvaroom.org/#/line/nambu-branch), [JR Sagami](https://japanrail.alvaroom.org/#/line/sagami), [JR Itsukaichi](https://japanrail.alvaroom.org/#/line/itsukaichi), [JR Hachikō](https://japanrail.alvaroom.org/#/line/hachiko), [JR Kawagoe](https://japanrail.alvaroom.org/#/line/kawagoe), [New Shuttle](https://japanrail.alvaroom.org/#/line/new-shuttle), [Kanazawa Seaside Line](https://japanrail.alvaroom.org/#/line/kanazawa-seaside), [Disney Resort Line](https://japanrail.alvaroom.org/#/line/disney-resort-line), [Ryūtetsu Nagareyama](https://japanrail.alvaroom.org/#/line/ryutetsu), [Yamaman Yukarigaoka](https://japanrail.alvaroom.org/#/line/yamaman), [JR Hanwa (ramal Higashi-Hagoromo)](https://japanrail.alvaroom.org/#/line/hanwa-branch), [JR Yamatoji](https://japanrail.alvaroom.org/#/line/yamatoji), [JR Osaka Higashi](https://japanrail.alvaroom.org/#/line/osaka-higashi), [JR Sakurai (Man'yō Mahoroba)](https://japanrail.alvaroom.org/#/line/sakurai), [Kintetsu Minami-Ōsaka](https://japanrail.alvaroom.org/#/line/kintetsu-minami-osaka), [Kintetsu Nagano](https://japanrail.alvaroom.org/#/line/kintetsu-nagano), [Kintetsu Dōmyōji](https://japanrail.alvaroom.org/#/line/kintetsu-domyoji), [Kintetsu Gose](https://japanrail.alvaroom.org/#/line/kintetsu-gose), [Kintetsu Keihanna](https://japanrail.alvaroom.org/#/line/kintetsu-keihanna), [Kintetsu Ikoma](https://japanrail.alvaroom.org/#/line/kintetsu-ikoma), [Kintetsu Kashihara](https://japanrail.alvaroom.org/#/line/kintetsu-kashihara), [Kintetsu Yoshino](https://japanrail.alvaroom.org/#/line/kintetsu-yoshino), [JR Wakayama](https://japanrail.alvaroom.org/#/line/wakayama-line), [Funicular de Ikoma](https://japanrail.alvaroom.org/#/line/ikoma-cable), [Kintetsu Tenri](https://japanrail.alvaroom.org/#/line/kintetsu-tenri), [Kintetsu Tawaramoto](https://japanrail.alvaroom.org/#/line/kintetsu-tawaramoto), [Kintetsu Shigi](https://japanrail.alvaroom.org/#/line/kintetsu-shigi), [Hankyu Imazu](https://japanrail.alvaroom.org/#/line/hankyu-imazu), [Hankyu Itami](https://japanrail.alvaroom.org/#/line/hankyu-itami), [Hankyu Minoo](https://japanrail.alvaroom.org/#/line/hankyu-minoo), [Hankyu Kōyō](https://japanrail.alvaroom.org/#/line/hankyu-koyo), [Hanshin Mukogawa](https://japanrail.alvaroom.org/#/line/hanshin-mukogawa), [JR Kakogawa](https://japanrail.alvaroom.org/#/line/kakogawa), [JR Bantan](https://japanrail.alvaroom.org/#/line/bantan), [JR Kishin (Himeji–Kōzuki)](https://japanrail.alvaroom.org/#/line/kishin), [JR Sanyō (Akashi–Kamigōri)](https://japanrail.alvaroom.org/#/line/sanyo-main-west), [JR Fukuchiyama (Sasayamaguchi–Fukuchiyama)](https://japanrail.alvaroom.org/#/line/fukuchiyama-north), [Hōjō Tetsudō](https://japanrail.alvaroom.org/#/line/hojo), [Chizu Express](https://japanrail.alvaroom.org/#/line/chizu), [JR Akō](https://japanrail.alvaroom.org/#/line/ako), [Funicular de Maya](https://japanrail.alvaroom.org/#/line/maya-cable), [Funicular de Rokkō](https://japanrail.alvaroom.org/#/line/rokko-cable), [Sanyō Aboshi](https://japanrail.alvaroom.org/#/line/sanyo-aboshi), [JR San'in (Yanase–Igumi)](https://japanrail.alvaroom.org/#/line/sanin-hyogo), [Ōmi Tetsudō (principal)](https://japanrail.alvaroom.org/#/line/omi-main), [Ōmi Tetsudō: Yōkaichi](https://japanrail.alvaroom.org/#/line/omi-yokaichi), [Ōmi Tetsudō: Taga](https://japanrail.alvaroom.org/#/line/omi-taga), [JR Kusatsu](https://japanrail.alvaroom.org/#/line/kusatsu-line), [Shigaraki Kōgen Tetsudō](https://japanrail.alvaroom.org/#/line/shigaraki), [Funicular de Sakamoto](https://japanrail.alvaroom.org/#/line/sakamoto-cable), [Kōbe Kōsoku](https://japanrail.alvaroom.org/#/line/kobe-kosoku), [Nankai Semboku](https://japanrail.alvaroom.org/#/line/nankai-semboku), [Nankai Shiomibashi](https://japanrail.alvaroom.org/#/line/nankai-shiomibashi), [Nankai Takashinohama](https://japanrail.alvaroom.org/#/line/nankai-takashinohama), [Keihan Katano](https://japanrail.alvaroom.org/#/line/keihan-katano), [Keihan Nakanoshima](https://japanrail.alvaroom.org/#/line/keihan-nakanoshima), [Kōbe Dentetsu Arima](https://japanrail.alvaroom.org/#/line/kobe-electric-arima), [Kōbe Dentetsu Sanda](https://japanrail.alvaroom.org/#/line/kobe-electric-sanda), [Kōbe Dentetsu Ao](https://japanrail.alvaroom.org/#/line/kobe-electric-ao), [Kōbe Dentetsu Kōen-toshi](https://japanrail.alvaroom.org/#/line/kobe-electric-koen-toshi), [Sanyō Dentetsu](https://japanrail.alvaroom.org/#/line/sanyo-electric), [Nose Dentetsu Myōken](https://japanrail.alvaroom.org/#/line/nose-myoken), [Nose Dentetsu Nissei](https://japanrail.alvaroom.org/#/line/nose-nissei), [Metro de Nagoya: Meijō](https://japanrail.alvaroom.org/#/line/nagoya-meijo), [Metro de Nagoya: Meikō](https://japanrail.alvaroom.org/#/line/nagoya-meiko), [Metro de Nagoya: Sakura-dōri](https://japanrail.alvaroom.org/#/line/nagoya-sakuradori), [Metro de Nagoya: Kamiiida](https://japanrail.alvaroom.org/#/line/nagoya-kamiiida), [Meitetsu Mikawa](https://japanrail.alvaroom.org/#/line/meitetsu-mikawa), [Meitetsu Bisai](https://japanrail.alvaroom.org/#/line/meitetsu-bisai), [Meitetsu Gamagōri](https://japanrail.alvaroom.org/#/line/meitetsu-gamagori), [Meitetsu Nishio](https://japanrail.alvaroom.org/#/line/meitetsu-nishio), [Meitetsu Tsushima](https://japanrail.alvaroom.org/#/line/meitetsu-tsushima), [Meitetsu Hiromi](https://japanrail.alvaroom.org/#/line/meitetsu-hiromi), [Meitetsu Toyokawa](https://japanrail.alvaroom.org/#/line/meitetsu-toyokawa), [Meitetsu Chita Nueva](https://japanrail.alvaroom.org/#/line/meitetsu-chita-new), [Meitetsu Chikkō](https://japanrail.alvaroom.org/#/line/meitetsu-chikko), [Aichi Loop Line](https://japanrail.alvaroom.org/#/line/aichi-loop), [Jōhoku Line](https://japanrail.alvaroom.org/#/line/johoku), [JR Iida (Toyohashi–Nagashino)](https://japanrail.alvaroom.org/#/line/iida), [JR Taketoyo](https://japanrail.alvaroom.org/#/line/taketoyo), [JR Tōkaidō (Toyohashi–Ōgaki)](https://japanrail.alvaroom.org/#/line/tokaido-aichi), [JR Chūō Oeste (Nagoya–Nakatsugawa)](https://japanrail.alvaroom.org/#/line/chuo-west), [JR Kansai (Nagoya–Kameyama)](https://japanrail.alvaroom.org/#/line/kansai-nagoya), [Meitetsu Seto](https://japanrail.alvaroom.org/#/line/meitetsu-seto), [Meitetsu Komaki](https://japanrail.alvaroom.org/#/line/meitetsu-komaki), [Meitetsu Kōwa](https://japanrail.alvaroom.org/#/line/meitetsu-kowa), [Meitetsu Toyota](https://japanrail.alvaroom.org/#/line/meitetsu-toyota), [Kintetsu Nagoya](https://japanrail.alvaroom.org/#/line/kintetsu-nagoya), [JR Sanyō (Itozaki–Ōtake)](https://japanrail.alvaroom.org/#/line/sanyo-hiroshima), [JR Kure](https://japanrail.alvaroom.org/#/line/kure), [JR Geibi](https://japanrail.alvaroom.org/#/line/geibi), [JR Fukuen](https://japanrail.alvaroom.org/#/line/fukuen), [Ibara Tetsudō](https://japanrail.alvaroom.org/#/line/ibara), [JR Kagoshima (Mojikō–Ōmuta)](https://japanrail.alvaroom.org/#/line/kagoshima-main-fukuoka), [JR Nippō (Kokura–Yanagigaura)](https://japanrail.alvaroom.org/#/line/nippo), [JR Chikuhō (Fukuhoku Yutaka)](https://japanrail.alvaroom.org/#/line/chikuho-main), [JR Sasaguri](https://japanrail.alvaroom.org/#/line/sasaguri), [JR Hita-Hikosan](https://japanrail.alvaroom.org/#/line/hitahikosan), [JR Kyūdai (Yufu Kōgen)](https://japanrail.alvaroom.org/#/line/kyudai), [JR Gotōji](https://japanrail.alvaroom.org/#/line/gotoji), [JR Hakata-Minami](https://japanrail.alvaroom.org/#/line/hakata-minami), [Chikuhō Dentetsu](https://japanrail.alvaroom.org/#/line/chikuho-dentetsu), [Amagi Tetsudō](https://japanrail.alvaroom.org/#/line/amagi), [Nishitetsu Amagi](https://japanrail.alvaroom.org/#/line/nishitetsu-amagi), [Heisei Chikuhō: línea Ita](https://japanrail.alvaroom.org/#/line/heisei-ita), [Heisei Chikuhō: línea Tagawa](https://japanrail.alvaroom.org/#/line/heisei-tagawa), [Heisei Chikuhō: línea Itoda](https://japanrail.alvaroom.org/#/line/heisei-itoda), [Monorraíl de Kitakyūshū](https://japanrail.alvaroom.org/#/line/kitakyushu-monorail), [Mojikō Retro (Shiokaze)](https://japanrail.alvaroom.org/#/line/mojiko-retro), [Slope Car del monte Hiko](https://japanrail.alvaroom.org/#/line/hikosan-slope), [JR Kisuki](https://japanrail.alvaroom.org/#/line/kisuki), [Nishitetsu Kaizuka](https://japanrail.alvaroom.org/#/line/nishitetsu-kaizuka), [Nishitetsu Dazaifu](https://japanrail.alvaroom.org/#/line/nishitetsu-dazaifu), [JR Tōhoku (Fukushima–Ichinoseki)](https://japanrail.alvaroom.org/#/line/tohoku-main), [JR Tōhoku: ramal de Rifu](https://japanrail.alvaroom.org/#/line/rifu), [Abukuma Kyūkō](https://japanrail.alvaroom.org/#/line/abukuma), [JR Ishinomaki](https://japanrail.alvaroom.org/#/line/ishinomaki), [JR Kesennuma (tramo de tren)](https://japanrail.alvaroom.org/#/line/kesennuma-rail), [JR Jōban (Sendai–Shinchi)](https://japanrail.alvaroom.org/#/line/joban-sendai), [JR Rikuu East](https://japanrail.alvaroom.org/#/line/rikuu-east), [JR Hakodate (Hakodate–Otaru)](https://japanrail.alvaroom.org/#/line/hakodate-yamasen), [JR Hakodate (Iwamizawa–Asahikawa)](https://japanrail.alvaroom.org/#/line/hakodate-asahikawa), [JR Sekishō](https://japanrail.alvaroom.org/#/line/sekisho), [JR Ōfunato (tramo de tren)](https://japanrail.alvaroom.org/#/line/ofunato-rail), [Sorachi Tetsudō](https://japanrail.alvaroom.org/#/line/sorachi), [JR Muroran](https://japanrail.alvaroom.org/#/line/muroran), [JR Nemuro (Hanasaki)](https://japanrail.alvaroom.org/#/line/nemuro), [JR Sōya](https://japanrail.alvaroom.org/#/line/soya), [JR Sekihoku](https://japanrail.alvaroom.org/#/line/sekihoku), [JR Senmō](https://japanrail.alvaroom.org/#/line/senmo), [JR Furano](https://japanrail.alvaroom.org/#/line/furano), [JR Hidaka](https://japanrail.alvaroom.org/#/line/hidaka), [Dōnan Isaribi Tetsudō](https://japanrail.alvaroom.org/#/line/donan-isaribi), [JR Senseki](https://japanrail.alvaroom.org/#/line/senseki), [JR Senzan](https://japanrail.alvaroom.org/#/line/senzan), [Sendai Airport Access](https://japanrail.alvaroom.org/#/line/sendai-airport), [Hiroden: línea 6](https://japanrail.alvaroom.org/#/line/hiroden-6), [Hiroden: línea 7](https://japanrail.alvaroom.org/#/line/hiroden-7), [Hiroden: línea 8](https://japanrail.alvaroom.org/#/line/hiroden-8), [Hiroden: línea 9 (Hakushima)](https://japanrail.alvaroom.org/#/line/hiroden-9), [Hiroden: línea circular](https://japanrail.alvaroom.org/#/line/hiroden-loop), [JR Kabe](https://japanrail.alvaroom.org/#/line/kabe), [Nagasaki: línea 1](https://japanrail.alvaroom.org/#/line/nagasaki-1), [Nagasaki: línea 2](https://japanrail.alvaroom.org/#/line/nagasaki-2), [Nagasaki: línea 3](https://japanrail.alvaroom.org/#/line/nagasaki-3), [Nagasaki: línea 4](https://japanrail.alvaroom.org/#/line/nagasaki-4), [Nagasaki: línea 5](https://japanrail.alvaroom.org/#/line/nagasaki-5), [Kagoshima: línea 1](https://japanrail.alvaroom.org/#/line/kagoshima-1), [Kagoshima: línea 2](https://japanrail.alvaroom.org/#/line/kagoshima-2), [Hakodate: línea 2](https://japanrail.alvaroom.org/#/line/hakodate-2), [Hakodate: línea 5](https://japanrail.alvaroom.org/#/line/hakodate-5), [Tosaden: línea Ino](https://japanrail.alvaroom.org/#/line/tosaden-ino), [Tosaden: línea Gomen](https://japanrail.alvaroom.org/#/line/tosaden-gomen), [Toyama Chihō: línea principal](https://japanrail.alvaroom.org/#/line/toyama-main), [Toyama Chihō: línea Tateyama](https://japanrail.alvaroom.org/#/line/toyama-tateyama), [Matsuyama: línea Honmachi](https://japanrail.alvaroom.org/#/line/iyotetsu-honmachi), [Iyotetsu Takahama](https://japanrail.alvaroom.org/#/line/iyotetsu-takahama), [Iyotetsu Yokogawara](https://japanrail.alvaroom.org/#/line/iyotetsu-yokogawara), [Iyotetsu Gunchū](https://japanrail.alvaroom.org/#/line/iyotetsu-gunchu), [Toyohashi: tranvía Azumada](https://japanrail.alvaroom.org/#/line/toyohashi-azumada), [Toyohashi Atsumi](https://japanrail.alvaroom.org/#/line/toyohashi-atsumi), [JR Dosan](https://japanrail.alvaroom.org/#/line/dosan), [Tosa Kuroshio: Gomen–Nahari](https://japanrail.alvaroom.org/#/line/kuroshio-asa), [Tosa Kuroshio: Nakamura](https://japanrail.alvaroom.org/#/line/kuroshio-nakamura), [Tosa Kuroshio: Sukumo](https://japanrail.alvaroom.org/#/line/kuroshio-sukumo), [JR Yodo](https://japanrail.alvaroom.org/#/line/yodo), [Tosaden: línea Sanbashi](https://japanrail.alvaroom.org/#/line/tosaden-sambashi), [JR Ibusuki-Makurazaki](https://japanrail.alvaroom.org/#/line/ibusuki), [JR Kagoshima (Sendai–Kagoshima)](https://japanrail.alvaroom.org/#/line/kagoshima-main-south), [JR Nippō (Miyazaki–Kagoshima)](https://japanrail.alvaroom.org/#/line/nippo-south), [Hisatsu Orange Tetsudō](https://japanrail.alvaroom.org/#/line/hisatsu-orange), [JR Hisatsu](https://japanrail.alvaroom.org/#/line/hisatsu), [JR Kitto](https://japanrail.alvaroom.org/#/line/kitto), [JR Nichinan](https://japanrail.alvaroom.org/#/line/nichinan), [Fukui: línea Fukubu](https://japanrail.alvaroom.org/#/line/fukui-fukubu)
- **Trenes sin foto** (0): ninguna 🎉
- **Líneas con numeración incompleta** (72): [JR Sōbu (Chiba–Chōshi)](https://japanrail.alvaroom.org/#/line/sobu-main), [Línea Utsunomiya](https://japanrail.alvaroom.org/#/line/utsunomiya), [JR Gotemba](https://japanrail.alvaroom.org/#/line/gotemba), [Odakyū Enoshima](https://japanrail.alvaroom.org/#/line/odakyu-enoshima), [Tōbu Isesaki (norte)](https://japanrail.alvaroom.org/#/line/tobu-isesaki), [Tōbu Nikkō](https://japanrail.alvaroom.org/#/line/tobu-nikko), [Nankai Tanagawa](https://japanrail.alvaroom.org/#/line/nankai-tanagawa), [Hanshin Namba](https://japanrail.alvaroom.org/#/line/hanshin-namba), [Kintetsu Ōsaka](https://japanrail.alvaroom.org/#/line/kintetsu-osaka), [Tranvía Hankai](https://japanrail.alvaroom.org/#/line/hankai), [Keihan Keishin](https://japanrail.alvaroom.org/#/line/keihan-keishin), [Monorraíl de Chiba (línea 2)](https://japanrail.alvaroom.org/#/line/chiba-monorail), [Monorraíl de Chiba (línea 1)](https://japanrail.alvaroom.org/#/line/chiba-monorail-1), [Keisei Matsudo](https://japanrail.alvaroom.org/#/line/keisei-matsudo), [Hokusō / Narita Sky Access](https://japanrail.alvaroom.org/#/line/hokuso), [Keiō Dōbutsuen](https://japanrail.alvaroom.org/#/line/keio-dobutsuen), [Odakyū Tama](https://japanrail.alvaroom.org/#/line/odakyu-tama), [Seibu Sayama](https://japanrail.alvaroom.org/#/line/seibu-sayama), [Seibu Yamaguchi (Leo Liner)](https://japanrail.alvaroom.org/#/line/seibu-yamaguchi), [Tōbu Ogose](https://japanrail.alvaroom.org/#/line/tobu-ogose), [Sōtetsu Shin-Yokohama](https://japanrail.alvaroom.org/#/line/sotetsu-shin-yokohama), [Saitama Rapid Railway](https://japanrail.alvaroom.org/#/line/saitama-rapid), [Kintetsu Nagano](https://japanrail.alvaroom.org/#/line/kintetsu-nagano), [Kintetsu Gose](https://japanrail.alvaroom.org/#/line/kintetsu-gose), [Kintetsu Ikoma](https://japanrail.alvaroom.org/#/line/kintetsu-ikoma), [Kintetsu Shigi](https://japanrail.alvaroom.org/#/line/kintetsu-shigi), [Hankyu Senri](https://japanrail.alvaroom.org/#/line/hankyu-senri), [Hankyu Imazu](https://japanrail.alvaroom.org/#/line/hankyu-imazu), [Hankyu Itami](https://japanrail.alvaroom.org/#/line/hankyu-itami), [Hanshin Mukogawa](https://japanrail.alvaroom.org/#/line/hanshin-mukogawa), [JR Fukuchiyama (Sasayamaguchi–Fukuchiyama)](https://japanrail.alvaroom.org/#/line/fukuchiyama-north), [Ōmi Tetsudō (principal)](https://japanrail.alvaroom.org/#/line/omi-main), [Ōmi Tetsudō: Yōkaichi](https://japanrail.alvaroom.org/#/line/omi-yokaichi), [Kōbe Kōsoku](https://japanrail.alvaroom.org/#/line/kobe-kosoku), [Nankai Shiomibashi](https://japanrail.alvaroom.org/#/line/nankai-shiomibashi), [Nankai Takashinohama](https://japanrail.alvaroom.org/#/line/nankai-takashinohama), [Keihan Katano](https://japanrail.alvaroom.org/#/line/keihan-katano), [Kōbe Dentetsu Ao](https://japanrail.alvaroom.org/#/line/kobe-electric-ao), [Meitetsu Mikawa](https://japanrail.alvaroom.org/#/line/meitetsu-mikawa), [Meitetsu Bisai](https://japanrail.alvaroom.org/#/line/meitetsu-bisai), [Meitetsu Tsushima](https://japanrail.alvaroom.org/#/line/meitetsu-tsushima), [Meitetsu Hiromi](https://japanrail.alvaroom.org/#/line/meitetsu-hiromi), [JR Iida (Toyohashi–Nagashino)](https://japanrail.alvaroom.org/#/line/iida), [JR Tōkaidō (Toyohashi–Ōgaki)](https://japanrail.alvaroom.org/#/line/tokaido-aichi), [JR Chūō Oeste (Nagoya–Nakatsugawa)](https://japanrail.alvaroom.org/#/line/chuo-west), [JR Kansai (Nagoya–Kameyama)](https://japanrail.alvaroom.org/#/line/kansai-nagoya), [Meitetsu Tokoname](https://japanrail.alvaroom.org/#/line/meitetsu-tokoname), [Meitetsu Inuyama](https://japanrail.alvaroom.org/#/line/meitetsu-inuyama), [Meitetsu Komaki](https://japanrail.alvaroom.org/#/line/meitetsu-komaki), [Meitetsu Kōwa](https://japanrail.alvaroom.org/#/line/meitetsu-kowa), [Meitetsu Toyota](https://japanrail.alvaroom.org/#/line/meitetsu-toyota), [Kintetsu Nagoya](https://japanrail.alvaroom.org/#/line/kintetsu-nagoya), [Linimo](https://japanrail.alvaroom.org/#/line/linimo), [JR Sanyō (Itozaki–Ōtake)](https://japanrail.alvaroom.org/#/line/sanyo-hiroshima), [JR Kure](https://japanrail.alvaroom.org/#/line/kure), [JR Geibi](https://japanrail.alvaroom.org/#/line/geibi), [JR Kagoshima (Mojikō–Ōmuta)](https://japanrail.alvaroom.org/#/line/kagoshima-main-fukuoka), [JR Nippō (Kokura–Yanagigaura)](https://japanrail.alvaroom.org/#/line/nippo), [JR Chikuhō (Fukuhoku Yutaka)](https://japanrail.alvaroom.org/#/line/chikuho-main), [JR Sasaguri](https://japanrail.alvaroom.org/#/line/sasaguri), [Chikuhō Dentetsu](https://japanrail.alvaroom.org/#/line/chikuho-dentetsu), [Metro de Fukuoka: Hakozaki](https://japanrail.alvaroom.org/#/line/fukuoka-hakozaki), [JR Gakuentoshi (Sasshō)](https://japanrail.alvaroom.org/#/line/sassho), [JR Hakodate (Iwamizawa–Asahikawa)](https://japanrail.alvaroom.org/#/line/hakodate-asahikawa), [JR Sekishō](https://japanrail.alvaroom.org/#/line/sekisho), [JR Sōya](https://japanrail.alvaroom.org/#/line/soya), [JR Sekihoku](https://japanrail.alvaroom.org/#/line/sekihoku), [JR Senmō](https://japanrail.alvaroom.org/#/line/senmo), [Okayama: línea Higashiyama](https://japanrail.alvaroom.org/#/line/okayama-higashiyama), [Toyama Chihō: línea Tateyama](https://japanrail.alvaroom.org/#/line/toyama-tateyama), [JR Dosan](https://japanrail.alvaroom.org/#/line/dosan), [Tosa Kuroshio: Gomen–Nahari](https://japanrail.alvaroom.org/#/line/kuroshio-asa)
- **Trenes sin datos curiosos** (139 de 182).
- **Líneas sin trenes históricos** (383 de 420):
  - Shinkansen: [Kyūshū Shinkansen](https://japanrail.alvaroom.org/#/line/kyushu-shinkansen), [Nishi-Kyūshū Shinkansen](https://japanrail.alvaroom.org/#/line/nishi-kyushu-shinkansen), [Hokkaidō Shinkansen](https://japanrail.alvaroom.org/#/line/hokkaido-shinkansen), [Hokuriku Shinkansen](https://japanrail.alvaroom.org/#/line/hokuriku-shinkansen)
  - Tokio: [Línea Sōbu (rápido)](https://japanrail.alvaroom.org/#/line/sobu-rapid), [Línea Hanzōmon](https://japanrail.alvaroom.org/#/line/hanzomon), [Línea Namboku](https://japanrail.alvaroom.org/#/line/namboku), [Línea Fukutoshin](https://japanrail.alvaroom.org/#/line/fukutoshin), [Línea Ōedo](https://japanrail.alvaroom.org/#/line/oedo), [Nippori-Toneri Liner](https://japanrail.alvaroom.org/#/line/nippori-toneri), [Yurikamome](https://japanrail.alvaroom.org/#/line/yurikamome), [Monorraíl de Tokio](https://japanrail.alvaroom.org/#/line/tokyo-monorail), [Línea Rinkai](https://japanrail.alvaroom.org/#/line/rinkai), [Línea Keiyō](https://japanrail.alvaroom.org/#/line/keiyo), [JR Uchibō](https://japanrail.alvaroom.org/#/line/uchibo), [JR Sotobō](https://japanrail.alvaroom.org/#/line/sotobo), [JR Sōbu (Chiba–Chōshi)](https://japanrail.alvaroom.org/#/line/sobu-main), [JR Narita](https://japanrail.alvaroom.org/#/line/narita-line), [JR Narita (ramal de Abiko)](https://japanrail.alvaroom.org/#/line/narita-abiko), [JR Tōgane](https://japanrail.alvaroom.org/#/line/togane), [JR Kururi](https://japanrail.alvaroom.org/#/line/kururi), [JR Kashima](https://japanrail.alvaroom.org/#/line/kashima), [Kominato Tetsudō](https://japanrail.alvaroom.org/#/line/kominato), [Isumi Tetsudō](https://japanrail.alvaroom.org/#/line/isumi), [Chōshi Dentetsu](https://japanrail.alvaroom.org/#/line/choshi), [Disney Resort Line](https://japanrail.alvaroom.org/#/line/disney-resort), [Línea Jōban (rápido)](https://japanrail.alvaroom.org/#/line/joban-rapid), [Línea Jōban (local)](https://japanrail.alvaroom.org/#/line/joban-local), [Línea Musashino](https://japanrail.alvaroom.org/#/line/musashino), [Línea Nambu](https://japanrail.alvaroom.org/#/line/nambu), [Línea Yokohama](https://japanrail.alvaroom.org/#/line/yokohama-line), [Línea Tōkaidō (JT)](https://japanrail.alvaroom.org/#/line/tokaido-jt), [Línea Yokosuka](https://japanrail.alvaroom.org/#/line/yokosuka), [Línea Shōnan-Shinjuku](https://japanrail.alvaroom.org/#/line/shonan-shinjuku), [Línea Utsunomiya](https://japanrail.alvaroom.org/#/line/utsunomiya), [Línea Takasaki](https://japanrail.alvaroom.org/#/line/takasaki), [Línea Ōme](https://japanrail.alvaroom.org/#/line/ome), [Tōkyū Den-en-toshi](https://japanrail.alvaroom.org/#/line/tokyu-denentoshi), [Tōkyū Ōimachi](https://japanrail.alvaroom.org/#/line/tokyu-oimachi), [Tōkyū Ikegami](https://japanrail.alvaroom.org/#/line/tokyu-ikegami), [Tōkyū Tamagawa](https://japanrail.alvaroom.org/#/line/tokyu-tamagawa), [Tōkyū Setagaya](https://japanrail.alvaroom.org/#/line/tokyu-setagaya), [JR Chūō (Takao–Ōtsuki)](https://japanrail.alvaroom.org/#/line/chuo-otsuki), [Inclinado de la presa de Miyagase](https://japanrail.alvaroom.org/#/line/miyagase-incline), [Hakone Tozan](https://japanrail.alvaroom.org/#/line/hakone-tozan), [Funicular de Hakone (Gōra–Sōunzan)](https://japanrail.alvaroom.org/#/line/hakone-tozan-cable), [Izuhakone Daiyūzan](https://japanrail.alvaroom.org/#/line/izuhakone-daiyuzan), [Funicular del monte Ōyama](https://japanrail.alvaroom.org/#/line/oyama-cable), [JR Gotemba](https://japanrail.alvaroom.org/#/line/gotemba), [Odakyū Enoshima](https://japanrail.alvaroom.org/#/line/odakyu-enoshima), [Keiō](https://japanrail.alvaroom.org/#/line/keio), [Keiō Takao](https://japanrail.alvaroom.org/#/line/keio-takao), [Keiō Inokashira](https://japanrail.alvaroom.org/#/line/keio-inokashira), [Chichibu Tetsudō](https://japanrail.alvaroom.org/#/line/chichibu), [Seibu Chichibu](https://japanrail.alvaroom.org/#/line/seibu-chichibu), [Tōbu Isesaki (norte)](https://japanrail.alvaroom.org/#/line/tobu-isesaki), [Tōbu Nikkō](https://japanrail.alvaroom.org/#/line/tobu-nikko), [Seibu Shinjuku](https://japanrail.alvaroom.org/#/line/seibu-shinjuku), [Tōbu Skytree](https://japanrail.alvaroom.org/#/line/tobu-skytree), [Tōbu Tōjō](https://japanrail.alvaroom.org/#/line/tobu-tojo), [Keikyū Aeropuerto](https://japanrail.alvaroom.org/#/line/keikyu-airport), [Keisei Oshiage](https://japanrail.alvaroom.org/#/line/keisei-oshiage), [Tsukuba Express](https://japanrail.alvaroom.org/#/line/tsukuba-express), [Sōtetsu principal](https://japanrail.alvaroom.org/#/line/sotetsu), [Funicular del monte Takao](https://japanrail.alvaroom.org/#/line/takao-cable), [Funicular del monte Mitake](https://japanrail.alvaroom.org/#/line/mitake-cable), [Asukarugo (parque de Asukayama)](https://japanrail.alvaroom.org/#/line/asukayama), [Sakura Rail (Matsuchiyama)](https://japanrail.alvaroom.org/#/line/sakura-rail), [Monorraíl de Tama](https://japanrail.alvaroom.org/#/line/tama-monorail), [Enoden](https://japanrail.alvaroom.org/#/line/enoden), [Shōnan Monorail](https://japanrail.alvaroom.org/#/line/shonan-monorail), [Metro de Yokohama: línea Azul](https://japanrail.alvaroom.org/#/line/yokohama-blue), [Metro de Yokohama: línea Verde](https://japanrail.alvaroom.org/#/line/yokohama-green), [Línea Minatomirai](https://japanrail.alvaroom.org/#/line/minatomirai), [Monorraíl de Chiba (línea 2)](https://japanrail.alvaroom.org/#/line/chiba-monorail), [Monorraíl de Chiba (línea 1)](https://japanrail.alvaroom.org/#/line/chiba-monorail-1), [Keikyū Kurihama](https://japanrail.alvaroom.org/#/line/keikyu-kurihama), [Keikyū Zushi](https://japanrail.alvaroom.org/#/line/keikyu-zushi), [Keikyū Daishi](https://japanrail.alvaroom.org/#/line/keikyu-daishi), [Keisei Kanamachi](https://japanrail.alvaroom.org/#/line/keisei-kanamachi), [Keisei Chiba](https://japanrail.alvaroom.org/#/line/keisei-chiba), [Keisei Chihara](https://japanrail.alvaroom.org/#/line/keisei-chihara), [Keisei Matsudo](https://japanrail.alvaroom.org/#/line/keisei-matsudo), [Hokusō / Narita Sky Access](https://japanrail.alvaroom.org/#/line/hokuso), [Keisei Higashi-Narita](https://japanrail.alvaroom.org/#/line/keisei-higashi-narita), [Shibayama Railway](https://japanrail.alvaroom.org/#/line/shibayama), [Keiō Nueva Línea](https://japanrail.alvaroom.org/#/line/keio-new), [Keiō Sagamihara](https://japanrail.alvaroom.org/#/line/keio-sagamihara), [Keiō Keibajō](https://japanrail.alvaroom.org/#/line/keio-keibajo), [Keiō Dōbutsuen](https://japanrail.alvaroom.org/#/line/keio-dobutsuen), [Odakyū Tama](https://japanrail.alvaroom.org/#/line/odakyu-tama), [Seibu Haijima](https://japanrail.alvaroom.org/#/line/seibu-haijima), [Seibu Kokubunji](https://japanrail.alvaroom.org/#/line/seibu-kokubunji), [Seibu Tamako](https://japanrail.alvaroom.org/#/line/seibu-tamako), [Seibu Tamagawa](https://japanrail.alvaroom.org/#/line/seibu-tamagawa), [Seibu Sayama](https://japanrail.alvaroom.org/#/line/seibu-sayama), [Seibu Yamaguchi (Leo Liner)](https://japanrail.alvaroom.org/#/line/seibu-yamaguchi), [Seibu Seibu-en](https://japanrail.alvaroom.org/#/line/seibu-seibuen), [Seibu Yūrakuchō](https://japanrail.alvaroom.org/#/line/seibu-yurakucho), [Seibu Toshima](https://japanrail.alvaroom.org/#/line/seibu-toshima), [Tōbu Kameido](https://japanrail.alvaroom.org/#/line/tobu-kameido), [Tōbu Daishi](https://japanrail.alvaroom.org/#/line/tobu-daishi), [Tōbu Urban Park](https://japanrail.alvaroom.org/#/line/tobu-urban-park), [Tōbu Ogose](https://japanrail.alvaroom.org/#/line/tobu-ogose), [Tōkyū Kodomonokuni](https://japanrail.alvaroom.org/#/line/tokyu-kodomonokuni), [Tōkyū Shin-Yokohama](https://japanrail.alvaroom.org/#/line/tokyu-shin-yokohama), [Sōtetsu Izumino](https://japanrail.alvaroom.org/#/line/sotetsu-izumino), [Sōtetsu Shin-Yokohama](https://japanrail.alvaroom.org/#/line/sotetsu-shin-yokohama), [JR Tsurumi](https://japanrail.alvaroom.org/#/line/tsurumi), [JR Nambu (ramal Hama-Kawasaki)](https://japanrail.alvaroom.org/#/line/nambu-branch), [JR Sagami](https://japanrail.alvaroom.org/#/line/sagami), [JR Itsukaichi](https://japanrail.alvaroom.org/#/line/itsukaichi), [JR Hachikō](https://japanrail.alvaroom.org/#/line/hachiko), [JR Kawagoe](https://japanrail.alvaroom.org/#/line/kawagoe), [Saitama Rapid Railway](https://japanrail.alvaroom.org/#/line/saitama-rapid), [Tōyō Rapid](https://japanrail.alvaroom.org/#/line/toyo-rapid), [New Shuttle](https://japanrail.alvaroom.org/#/line/new-shuttle), [Kanazawa Seaside Line](https://japanrail.alvaroom.org/#/line/kanazawa-seaside), [Disney Resort Line](https://japanrail.alvaroom.org/#/line/disney-resort-line), [Ryūtetsu Nagareyama](https://japanrail.alvaroom.org/#/line/ryutetsu), [Yamaman Yukarigaoka](https://japanrail.alvaroom.org/#/line/yamaman)
  - Kioto: [Línea Karasuma](https://japanrail.alvaroom.org/#/line/karasuma), [Línea Tōzai (Kioto)](https://japanrail.alvaroom.org/#/line/kyoto-tozai), [Línea JR Kyōto](https://japanrail.alvaroom.org/#/line/jr-kyoto), [Línea Sagano](https://japanrail.alvaroom.org/#/line/sagano), [JR San'in (Sonobe–Fukuchiyama)](https://japanrail.alvaroom.org/#/line/sanin-fukuchiyama), [JR Maizuru](https://japanrail.alvaroom.org/#/line/maizuru), [JR Obama](https://japanrail.alvaroom.org/#/line/obama), [Tango: línea Miyafuku](https://japanrail.alvaroom.org/#/line/tango-miyafuku), [Tango: línea Miyamai](https://japanrail.alvaroom.org/#/line/tango-miyamai), [Tango: línea Miyatoyo](https://japanrail.alvaroom.org/#/line/tango-miyatoyo), [JR Kansai (Kamo–Kameyama)](https://japanrail.alvaroom.org/#/line/kansai-east), [Funicular de Eizan](https://japanrail.alvaroom.org/#/line/eizan-cable), [Funicular de Amanohashidate](https://japanrail.alvaroom.org/#/line/amanohashidate-cable), [Línea Nara](https://japanrail.alvaroom.org/#/line/nara-line), [Línea Keihan Uji](https://japanrail.alvaroom.org/#/line/keihan-uji), [Línea Hankyu Arashiyama](https://japanrail.alvaroom.org/#/line/hankyu-arashiyama), [Línea Kintetsu Kyōto](https://japanrail.alvaroom.org/#/line/kintetsu-kyoto), [Randen: línea Arashiyama](https://japanrail.alvaroom.org/#/line/randen-arashiyama), [Randen: línea Kitano](https://japanrail.alvaroom.org/#/line/randen-kitano), [Eiden: línea Eizan](https://japanrail.alvaroom.org/#/line/eizan-main), [Eiden: línea Kurama](https://japanrail.alvaroom.org/#/line/eizan-kurama), [Tren turístico Sagano (Torokko)](https://japanrail.alvaroom.org/#/line/sagano-scenic), [Keihan Keishin](https://japanrail.alvaroom.org/#/line/keihan-keishin), [Keihan Ishiyama-Sakamoto](https://japanrail.alvaroom.org/#/line/keihan-ishiyama), [JR Kosei](https://japanrail.alvaroom.org/#/line/kosei), [JR Biwako](https://japanrail.alvaroom.org/#/line/biwako), [JR Hokuriku (Maibara–Ōmi-Shiotsu)](https://japanrail.alvaroom.org/#/line/hokuriku-shiga), [JR Tōkaidō (Maibara–Sekigahara)](https://japanrail.alvaroom.org/#/line/tokaido-maibara), [Ōmi Tetsudō (principal)](https://japanrail.alvaroom.org/#/line/omi-main), [Ōmi Tetsudō: Yōkaichi](https://japanrail.alvaroom.org/#/line/omi-yokaichi), [Ōmi Tetsudō: Taga](https://japanrail.alvaroom.org/#/line/omi-taga), [JR Kusatsu](https://japanrail.alvaroom.org/#/line/kusatsu-line), [Shigaraki Kōgen Tetsudō](https://japanrail.alvaroom.org/#/line/shigaraki), [Funicular de Sakamoto](https://japanrail.alvaroom.org/#/line/sakamoto-cable)
  - Ōsaka: [JR Yumesaki](https://japanrail.alvaroom.org/#/line/yumesaki), [Osaka Metro Midōsuji](https://japanrail.alvaroom.org/#/line/midosuji), [Osaka Metro Tanimachi](https://japanrail.alvaroom.org/#/line/tanimachi), [Osaka Metro Yotsubashi](https://japanrail.alvaroom.org/#/line/yotsubashi), [Osaka Metro Chūō](https://japanrail.alvaroom.org/#/line/chuo-osaka), [Osaka Metro Sennichimae](https://japanrail.alvaroom.org/#/line/sennichimae), [Osaka Metro Sakaisuji](https://japanrail.alvaroom.org/#/line/sakaisuji), [Osaka Metro Nagahori Tsurumi-ryokuchi](https://japanrail.alvaroom.org/#/line/nagahori), [Osaka Metro Imazatosuji](https://japanrail.alvaroom.org/#/line/imazatosuji), [New Tram (Nankō Port Town)](https://japanrail.alvaroom.org/#/line/new-tram), [Nankai principal](https://japanrail.alvaroom.org/#/line/nankai-main), [Nankai Aeropuerto](https://japanrail.alvaroom.org/#/line/nankai-airport), [Mizuma Tetsudō](https://japanrail.alvaroom.org/#/line/mizuma), [Kita-Ōsaka Kyūkō](https://japanrail.alvaroom.org/#/line/kita-osaka-kyuko), [Funicular de Nishi-Shigi](https://japanrail.alvaroom.org/#/line/nishi-shigi-cable), [Nankai Tanagawa](https://japanrail.alvaroom.org/#/line/nankai-tanagawa), [Wing Shuttle (ala norte)](https://japanrail.alvaroom.org/#/line/wing-shuttle-norte), [Wing Shuttle (ala sur)](https://japanrail.alvaroom.org/#/line/wing-shuttle-sur), [Nankai Kōya](https://japanrail.alvaroom.org/#/line/nankai-koya), [Hanshin principal](https://japanrail.alvaroom.org/#/line/hanshin-main), [Hanshin Namba](https://japanrail.alvaroom.org/#/line/hanshin-namba), [Hankyu Kōbe](https://japanrail.alvaroom.org/#/line/hankyu-kobe), [Hankyu Takarazuka](https://japanrail.alvaroom.org/#/line/hankyu-takarazuka), [Kintetsu Namba](https://japanrail.alvaroom.org/#/line/kintetsu-namba), [Kintetsu Nara](https://japanrail.alvaroom.org/#/line/kintetsu-nara), [Kintetsu Ōsaka](https://japanrail.alvaroom.org/#/line/kintetsu-osaka), [Monorraíl de Ōsaka](https://japanrail.alvaroom.org/#/line/osaka-monorail), [Tranvía Hankai](https://japanrail.alvaroom.org/#/line/hankai), [Tranvía Hankai: Uemachi](https://japanrail.alvaroom.org/#/line/hankai-uemachi), [JR Hanwa](https://japanrail.alvaroom.org/#/line/hanwa), [JR Hanwa (ramal Higashi-Hagoromo)](https://japanrail.alvaroom.org/#/line/hanwa-branch), [JR Takarazuka](https://japanrail.alvaroom.org/#/line/jr-takarazuka), [JR Gakkentoshi (Katamachi)](https://japanrail.alvaroom.org/#/line/katamachi), [JR Yamatoji](https://japanrail.alvaroom.org/#/line/yamatoji), [JR Tōzai](https://japanrail.alvaroom.org/#/line/jr-tozai), [JR Osaka Higashi](https://japanrail.alvaroom.org/#/line/osaka-higashi), [JR Sakurai (Man'yō Mahoroba)](https://japanrail.alvaroom.org/#/line/sakurai), [Kintetsu Minami-Ōsaka](https://japanrail.alvaroom.org/#/line/kintetsu-minami-osaka), [Kintetsu Nagano](https://japanrail.alvaroom.org/#/line/kintetsu-nagano), [Kintetsu Dōmyōji](https://japanrail.alvaroom.org/#/line/kintetsu-domyoji), [Kintetsu Gose](https://japanrail.alvaroom.org/#/line/kintetsu-gose), [Kintetsu Keihanna](https://japanrail.alvaroom.org/#/line/kintetsu-keihanna), [Kintetsu Ikoma](https://japanrail.alvaroom.org/#/line/kintetsu-ikoma), [Kintetsu Kashihara](https://japanrail.alvaroom.org/#/line/kintetsu-kashihara), [Kintetsu Yoshino](https://japanrail.alvaroom.org/#/line/kintetsu-yoshino), [JR Wakayama](https://japanrail.alvaroom.org/#/line/wakayama-line), [Funicular de Ikoma](https://japanrail.alvaroom.org/#/line/ikoma-cable), [Kintetsu Tenri](https://japanrail.alvaroom.org/#/line/kintetsu-tenri), [Kintetsu Tawaramoto](https://japanrail.alvaroom.org/#/line/kintetsu-tawaramoto), [Kintetsu Shigi](https://japanrail.alvaroom.org/#/line/kintetsu-shigi), [Hankyu Senri](https://japanrail.alvaroom.org/#/line/hankyu-senri), [Hankyu Minoo](https://japanrail.alvaroom.org/#/line/hankyu-minoo), [Nankai Semboku](https://japanrail.alvaroom.org/#/line/nankai-semboku), [Nankai Shiomibashi](https://japanrail.alvaroom.org/#/line/nankai-shiomibashi), [Nankai Takashinohama](https://japanrail.alvaroom.org/#/line/nankai-takashinohama), [Keihan Katano](https://japanrail.alvaroom.org/#/line/keihan-katano), [Keihan Nakanoshima](https://japanrail.alvaroom.org/#/line/keihan-nakanoshima), [Monorraíl de Ōsaka (ramal de Saito)](https://japanrail.alvaroom.org/#/line/osaka-monorail-saito), [Nose Dentetsu Myōken](https://japanrail.alvaroom.org/#/line/nose-myoken), [Nose Dentetsu Nissei](https://japanrail.alvaroom.org/#/line/nose-nissei)
  - Kōbe: [Línea JR Kōbe](https://japanrail.alvaroom.org/#/line/jr-kobe), [Metro de Kōbe: Seishin-Yamate](https://japanrail.alvaroom.org/#/line/kobe-seishin), [Metro de Kōbe: Kaigan](https://japanrail.alvaroom.org/#/line/kobe-kaigan), [Rokkō Liner](https://japanrail.alvaroom.org/#/line/rokko-liner), [Hankyu Imazu](https://japanrail.alvaroom.org/#/line/hankyu-imazu), [Hankyu Itami](https://japanrail.alvaroom.org/#/line/hankyu-itami), [Hankyu Kōyō](https://japanrail.alvaroom.org/#/line/hankyu-koyo), [Hanshin Mukogawa](https://japanrail.alvaroom.org/#/line/hanshin-mukogawa), [JR Kakogawa](https://japanrail.alvaroom.org/#/line/kakogawa), [JR Bantan](https://japanrail.alvaroom.org/#/line/bantan), [JR Kishin (Himeji–Kōzuki)](https://japanrail.alvaroom.org/#/line/kishin), [JR Sanyō (Akashi–Kamigōri)](https://japanrail.alvaroom.org/#/line/sanyo-main-west), [JR Fukuchiyama (Sasayamaguchi–Fukuchiyama)](https://japanrail.alvaroom.org/#/line/fukuchiyama-north), [Hōjō Tetsudō](https://japanrail.alvaroom.org/#/line/hojo), [Chizu Express](https://japanrail.alvaroom.org/#/line/chizu), [JR Akō](https://japanrail.alvaroom.org/#/line/ako), [Funicular de Maya](https://japanrail.alvaroom.org/#/line/maya-cable), [Funicular de Rokkō](https://japanrail.alvaroom.org/#/line/rokko-cable), [Sanyō Aboshi](https://japanrail.alvaroom.org/#/line/sanyo-aboshi), [JR San'in (Yanase–Igumi)](https://japanrail.alvaroom.org/#/line/sanin-hyogo), [Kōbe Kōsoku](https://japanrail.alvaroom.org/#/line/kobe-kosoku), [Kōbe Dentetsu Arima](https://japanrail.alvaroom.org/#/line/kobe-electric-arima), [Kōbe Dentetsu Sanda](https://japanrail.alvaroom.org/#/line/kobe-electric-sanda), [Kōbe Dentetsu Ao](https://japanrail.alvaroom.org/#/line/kobe-electric-ao), [Kōbe Dentetsu Kōen-toshi](https://japanrail.alvaroom.org/#/line/kobe-electric-koen-toshi), [Sanyō Dentetsu](https://japanrail.alvaroom.org/#/line/sanyo-electric)
  - Nagoya: [Metro de Nagoya: Higashiyama](https://japanrail.alvaroom.org/#/line/nagoya-higashiyama), [Metro de Nagoya: Meijō](https://japanrail.alvaroom.org/#/line/nagoya-meijo), [Metro de Nagoya: Meikō](https://japanrail.alvaroom.org/#/line/nagoya-meiko), [Metro de Nagoya: Tsurumai](https://japanrail.alvaroom.org/#/line/nagoya-tsurumai), [Metro de Nagoya: Sakura-dōri](https://japanrail.alvaroom.org/#/line/nagoya-sakuradori), [Metro de Nagoya: Kamiiida](https://japanrail.alvaroom.org/#/line/nagoya-kamiiida), [Meitetsu Mikawa](https://japanrail.alvaroom.org/#/line/meitetsu-mikawa), [Meitetsu Bisai](https://japanrail.alvaroom.org/#/line/meitetsu-bisai), [Meitetsu Gamagōri](https://japanrail.alvaroom.org/#/line/meitetsu-gamagori), [Meitetsu Nishio](https://japanrail.alvaroom.org/#/line/meitetsu-nishio), [Meitetsu Tsushima](https://japanrail.alvaroom.org/#/line/meitetsu-tsushima), [Meitetsu Hiromi](https://japanrail.alvaroom.org/#/line/meitetsu-hiromi), [Meitetsu Toyokawa](https://japanrail.alvaroom.org/#/line/meitetsu-toyokawa), [Meitetsu Chita Nueva](https://japanrail.alvaroom.org/#/line/meitetsu-chita-new), [Meitetsu Chikkō](https://japanrail.alvaroom.org/#/line/meitetsu-chikko), [Aichi Loop Line](https://japanrail.alvaroom.org/#/line/aichi-loop), [Jōhoku Line](https://japanrail.alvaroom.org/#/line/johoku), [JR Iida (Toyohashi–Nagashino)](https://japanrail.alvaroom.org/#/line/iida), [JR Taketoyo](https://japanrail.alvaroom.org/#/line/taketoyo), [JR Tōkaidō (Toyohashi–Ōgaki)](https://japanrail.alvaroom.org/#/line/tokaido-aichi), [JR Chūō Oeste (Nagoya–Nakatsugawa)](https://japanrail.alvaroom.org/#/line/chuo-west), [JR Kansai (Nagoya–Kameyama)](https://japanrail.alvaroom.org/#/line/kansai-nagoya), [Meitetsu Tokoname](https://japanrail.alvaroom.org/#/line/meitetsu-tokoname), [Meitetsu Aeropuerto](https://japanrail.alvaroom.org/#/line/meitetsu-airport), [Meitetsu Inuyama](https://japanrail.alvaroom.org/#/line/meitetsu-inuyama), [Meitetsu Seto](https://japanrail.alvaroom.org/#/line/meitetsu-seto), [Meitetsu Komaki](https://japanrail.alvaroom.org/#/line/meitetsu-komaki), [Meitetsu Kōwa](https://japanrail.alvaroom.org/#/line/meitetsu-kowa), [Meitetsu Toyota](https://japanrail.alvaroom.org/#/line/meitetsu-toyota), [Kintetsu Nagoya](https://japanrail.alvaroom.org/#/line/kintetsu-nagoya), [Aonami Line](https://japanrail.alvaroom.org/#/line/aonami), [Linimo](https://japanrail.alvaroom.org/#/line/linimo)
  - Fukuoka: [JR Kagoshima (Mojikō–Ōmuta)](https://japanrail.alvaroom.org/#/line/kagoshima-main-fukuoka), [JR Nippō (Kokura–Yanagigaura)](https://japanrail.alvaroom.org/#/line/nippo), [JR Chikuhō (Fukuhoku Yutaka)](https://japanrail.alvaroom.org/#/line/chikuho-main), [JR Sasaguri](https://japanrail.alvaroom.org/#/line/sasaguri), [JR Hita-Hikosan](https://japanrail.alvaroom.org/#/line/hitahikosan), [JR Kyūdai (Yufu Kōgen)](https://japanrail.alvaroom.org/#/line/kyudai), [JR Gotōji](https://japanrail.alvaroom.org/#/line/gotoji), [JR Hakata-Minami](https://japanrail.alvaroom.org/#/line/hakata-minami), [Chikuhō Dentetsu](https://japanrail.alvaroom.org/#/line/chikuho-dentetsu), [Amagi Tetsudō](https://japanrail.alvaroom.org/#/line/amagi), [Nishitetsu Amagi](https://japanrail.alvaroom.org/#/line/nishitetsu-amagi), [Heisei Chikuhō: línea Ita](https://japanrail.alvaroom.org/#/line/heisei-ita), [Heisei Chikuhō: línea Tagawa](https://japanrail.alvaroom.org/#/line/heisei-tagawa), [Heisei Chikuhō: línea Itoda](https://japanrail.alvaroom.org/#/line/heisei-itoda), [Monorraíl de Kitakyūshū](https://japanrail.alvaroom.org/#/line/kitakyushu-monorail), [Mojikō Retro (Shiokaze)](https://japanrail.alvaroom.org/#/line/mojiko-retro), [Slope Car del monte Hiko](https://japanrail.alvaroom.org/#/line/hikosan-slope), [Metro de Fukuoka: Kūkō](https://japanrail.alvaroom.org/#/line/fukuoka-kuko), [Metro de Fukuoka: Hakozaki](https://japanrail.alvaroom.org/#/line/fukuoka-hakozaki), [Metro de Fukuoka: Nanakuma](https://japanrail.alvaroom.org/#/line/fukuoka-nanakuma), [Nishitetsu Tenjin-Ōmuta](https://japanrail.alvaroom.org/#/line/nishitetsu-omuta), [Nishitetsu Kaizuka](https://japanrail.alvaroom.org/#/line/nishitetsu-kaizuka), [Nishitetsu Dazaifu](https://japanrail.alvaroom.org/#/line/nishitetsu-dazaifu), [JR Chikuhi](https://japanrail.alvaroom.org/#/line/chikuhi), [JR Kashii](https://japanrail.alvaroom.org/#/line/kashii)
  - Sapporo: [Metro de Sapporo: Namboku](https://japanrail.alvaroom.org/#/line/sapporo-namboku), [Metro de Sapporo: Tōzai](https://japanrail.alvaroom.org/#/line/sapporo-tozai), [Tranvía de Sapporo](https://japanrail.alvaroom.org/#/line/sapporo-tram), [JR Gakuentoshi (Sasshō)](https://japanrail.alvaroom.org/#/line/sassho), [JR Hakodate (Hakodate–Otaru)](https://japanrail.alvaroom.org/#/line/hakodate-yamasen), [JR Hakodate (Iwamizawa–Asahikawa)](https://japanrail.alvaroom.org/#/line/hakodate-asahikawa), [JR Sekishō](https://japanrail.alvaroom.org/#/line/sekisho), [Sorachi Tetsudō](https://japanrail.alvaroom.org/#/line/sorachi), [JR Muroran](https://japanrail.alvaroom.org/#/line/muroran), [JR Nemuro (Hanasaki)](https://japanrail.alvaroom.org/#/line/nemuro), [JR Sōya](https://japanrail.alvaroom.org/#/line/soya), [JR Sekihoku](https://japanrail.alvaroom.org/#/line/sekihoku), [JR Senmō](https://japanrail.alvaroom.org/#/line/senmo), [JR Furano](https://japanrail.alvaroom.org/#/line/furano), [JR Hidaka](https://japanrail.alvaroom.org/#/line/hidaka), [Dōnan Isaribi Tetsudō](https://japanrail.alvaroom.org/#/line/donan-isaribi)
  - Sendai: [JR Tōhoku (Fukushima–Ichinoseki)](https://japanrail.alvaroom.org/#/line/tohoku-main), [JR Tōhoku: ramal de Rifu](https://japanrail.alvaroom.org/#/line/rifu), [Abukuma Kyūkō](https://japanrail.alvaroom.org/#/line/abukuma), [JR Ishinomaki](https://japanrail.alvaroom.org/#/line/ishinomaki), [JR Kesennuma (tramo de tren)](https://japanrail.alvaroom.org/#/line/kesennuma-rail), [JR Jōban (Sendai–Shinchi)](https://japanrail.alvaroom.org/#/line/joban-sendai), [JR Rikuu East](https://japanrail.alvaroom.org/#/line/rikuu-east), [JR Ōfunato (tramo de tren)](https://japanrail.alvaroom.org/#/line/ofunato-rail), [Metro de Sendai: Namboku](https://japanrail.alvaroom.org/#/line/sendai-namboku), [Metro de Sendai: Tōzai](https://japanrail.alvaroom.org/#/line/sendai-tozai), [JR Senseki](https://japanrail.alvaroom.org/#/line/senseki), [JR Senzan](https://japanrail.alvaroom.org/#/line/senzan), [Sendai Airport Access](https://japanrail.alvaroom.org/#/line/sendai-airport)
  - Hiroshima: [JR Sanyō (Itozaki–Ōtake)](https://japanrail.alvaroom.org/#/line/sanyo-hiroshima), [JR Kure](https://japanrail.alvaroom.org/#/line/kure), [JR Geibi](https://japanrail.alvaroom.org/#/line/geibi), [JR Fukuen](https://japanrail.alvaroom.org/#/line/fukuen), [Ibara Tetsudō](https://japanrail.alvaroom.org/#/line/ibara), [JR Kisuki](https://japanrail.alvaroom.org/#/line/kisuki), [Hiroden: línea 1](https://japanrail.alvaroom.org/#/line/hiroden-1), [Hiroden: línea 2](https://japanrail.alvaroom.org/#/line/hiroden-2), [Hiroden: línea 3](https://japanrail.alvaroom.org/#/line/hiroden-3), [Hiroden: línea 5](https://japanrail.alvaroom.org/#/line/hiroden-5), [Hiroden: línea 6](https://japanrail.alvaroom.org/#/line/hiroden-6), [Hiroden: línea 7](https://japanrail.alvaroom.org/#/line/hiroden-7), [Hiroden: línea 8](https://japanrail.alvaroom.org/#/line/hiroden-8), [Hiroden: línea 9 (Hakushima)](https://japanrail.alvaroom.org/#/line/hiroden-9), [Hiroden: línea circular](https://japanrail.alvaroom.org/#/line/hiroden-loop), [Astram](https://japanrail.alvaroom.org/#/line/astram), [JR Kabe](https://japanrail.alvaroom.org/#/line/kabe)
  - Tranvías de otras ciudades: [Nagasaki: línea 1](https://japanrail.alvaroom.org/#/line/nagasaki-1), [Nagasaki: línea 2](https://japanrail.alvaroom.org/#/line/nagasaki-2), [Nagasaki: línea 3](https://japanrail.alvaroom.org/#/line/nagasaki-3), [Nagasaki: línea 4](https://japanrail.alvaroom.org/#/line/nagasaki-4), [Nagasaki: línea 5](https://japanrail.alvaroom.org/#/line/nagasaki-5), [Kumamoto: línea A](https://japanrail.alvaroom.org/#/line/kumamoto-a), [Kumamoto: línea B](https://japanrail.alvaroom.org/#/line/kumamoto-b), [Kagoshima: línea 1](https://japanrail.alvaroom.org/#/line/kagoshima-1), [Kagoshima: línea 2](https://japanrail.alvaroom.org/#/line/kagoshima-2), [Hakodate: línea 2](https://japanrail.alvaroom.org/#/line/hakodate-2), [Hakodate: línea 5](https://japanrail.alvaroom.org/#/line/hakodate-5), [Okayama: línea Higashiyama](https://japanrail.alvaroom.org/#/line/okayama-higashiyama), [Okayama: línea Seikibashi](https://japanrail.alvaroom.org/#/line/okayama-seikibashi), [Tosaden: línea Ino](https://japanrail.alvaroom.org/#/line/tosaden-ino), [Tosaden: línea Gomen](https://japanrail.alvaroom.org/#/line/tosaden-gomen), [Toyama: línea del puerto (Portram)](https://japanrail.alvaroom.org/#/line/toyama-port), [Toyama Chihō: línea principal](https://japanrail.alvaroom.org/#/line/toyama-main), [Toyama Chihō: línea Tateyama](https://japanrail.alvaroom.org/#/line/toyama-tateyama), [Matsuyama: tranvía circular](https://japanrail.alvaroom.org/#/line/iyotetsu-loop), [Matsuyama: línea Honmachi](https://japanrail.alvaroom.org/#/line/iyotetsu-honmachi), [Iyotetsu Takahama](https://japanrail.alvaroom.org/#/line/iyotetsu-takahama), [Iyotetsu Yokogawara](https://japanrail.alvaroom.org/#/line/iyotetsu-yokogawara), [Iyotetsu Gunchū](https://japanrail.alvaroom.org/#/line/iyotetsu-gunchu), [Toyohashi: tranvía Azumada](https://japanrail.alvaroom.org/#/line/toyohashi-azumada), [Toyohashi Atsumi](https://japanrail.alvaroom.org/#/line/toyohashi-atsumi), [JR Dosan](https://japanrail.alvaroom.org/#/line/dosan), [Tosa Kuroshio: Gomen–Nahari](https://japanrail.alvaroom.org/#/line/kuroshio-asa), [Tosa Kuroshio: Nakamura](https://japanrail.alvaroom.org/#/line/kuroshio-nakamura), [Tosa Kuroshio: Sukumo](https://japanrail.alvaroom.org/#/line/kuroshio-sukumo), [JR Yodo](https://japanrail.alvaroom.org/#/line/yodo), [Tosaden: línea Sanbashi](https://japanrail.alvaroom.org/#/line/tosaden-sambashi), [JR Ibusuki-Makurazaki](https://japanrail.alvaroom.org/#/line/ibusuki), [JR Kagoshima (Sendai–Kagoshima)](https://japanrail.alvaroom.org/#/line/kagoshima-main-south), [JR Nippō (Miyazaki–Kagoshima)](https://japanrail.alvaroom.org/#/line/nippo-south), [Hisatsu Orange Tetsudō](https://japanrail.alvaroom.org/#/line/hisatsu-orange), [JR Hisatsu](https://japanrail.alvaroom.org/#/line/hisatsu), [JR Kitto](https://japanrail.alvaroom.org/#/line/kitto), [JR Nichinan](https://japanrail.alvaroom.org/#/line/nichinan), [Fukui: línea Fukubu](https://japanrail.alvaroom.org/#/line/fukui-fukubu)
- **Grandes estaciones (3+ líneas) sin datos curiosos** (194): [Chiba](https://japanrail.alvaroom.org/#/station/chiba) (6), [Kanayama](https://japanrail.alvaroom.org/#/station/kanayama) (6), [Kyobashi](https://japanrail.alvaroom.org/#/station/kyobashi-osaka) (5), [Inari-machi](https://japanrail.alvaroom.org/#/station/inari-machi) (5), [Hatchobori](https://japanrail.alvaroom.org/#/station/hatchobori-hiroshima) (5), [Hondori](https://japanrail.alvaroom.org/#/station/hondori) (5), [Tokaichi-machi](https://japanrail.alvaroom.org/#/station/tokaichi-machi) (5), [Osaki](https://japanrail.alvaroom.org/#/station/osaki) (4), [Kanda](https://japanrail.alvaroom.org/#/station/kanda) (4), [Yotsuya](https://japanrail.alvaroom.org/#/station/yotsuya) (4), [Ichigaya](https://japanrail.alvaroom.org/#/station/ichigaya) (4), [Nishi-Funabashi](https://japanrail.alvaroom.org/#/station/nishi-funabashi) (4), [Urawa](https://japanrail.alvaroom.org/#/station/urawa) (4), [Nerima](https://japanrail.alvaroom.org/#/station/nerima) (4), [Himeji](https://japanrail.alvaroom.org/#/station/himeji) (4), [Kokura](https://japanrail.alvaroom.org/#/station/kokura) (4), [Fukushima](https://japanrail.alvaroom.org/#/station/fukushima) (4), [Takasaki](https://japanrail.alvaroom.org/#/station/takasaki) (4), [Osaka-Umeda](https://japanrail.alvaroom.org/#/station/osaka-umeda) (4), [Keisei-Narita](https://japanrail.alvaroom.org/#/station/keisei-narita) (4), [Totsuka](https://japanrail.alvaroom.org/#/station/totsuka) (4), [Haijima](https://japanrail.alvaroom.org/#/station/haijima) (4), [Hiyoshi](https://japanrail.alvaroom.org/#/station/hiyoshi-tokyo) (4), [Shin-Imaimiya](https://japanrail.alvaroom.org/#/station/shin-imaimiya) (4), [Kintetsu-Nagoya](https://japanrail.alvaroom.org/#/station/kintetsu-nagoya) (4), [Meitetsu Nagoya](https://japanrail.alvaroom.org/#/station/meitetsu-nagoya) (4), [Yokogawa](https://japanrail.alvaroom.org/#/station/yokogawa) (4), [Sapporo](https://japanrail.alvaroom.org/#/station/sapporo-2) (4), [Kanayama-cho](https://japanrail.alvaroom.org/#/station/kanayama-cho) (4), [Ebisu-cho](https://japanrail.alvaroom.org/#/station/ebisu-cho) (4), [Tate-machi](https://japanrail.alvaroom.org/#/station/tate-machi) (4), [Kamiya-cho-higashi](https://japanrail.alvaroom.org/#/station/kamiya-cho-higashi) (4), [Fukuro-machi](https://japanrail.alvaroom.org/#/station/fukuro-machi) (4), [Chuden-mae](https://japanrail.alvaroom.org/#/station/chuden-mae) (4), [Shiyakusho-mae](https://japanrail.alvaroom.org/#/station/shiyakusho-mae) (4), [Takano-bashi](https://japanrail.alvaroom.org/#/station/takano-bashi) (4), [Nisseki-byoin-mae](https://japanrail.alvaroom.org/#/station/nisseki-byoin-mae) (4), [Hiroden-honsha-mae](https://japanrail.alvaroom.org/#/station/hiroden-honsha-mae) (4), [Minami-machi 6-chome](https://japanrail.alvaroom.org/#/station/minami-machi-6-chome) (4), [Kamiya-cho-nishi](https://japanrail.alvaroom.org/#/station/kamiya-cho-nishi) (4), [Genbaku Dome-mae](https://japanrail.alvaroom.org/#/station/genbaku-dome-mae) (4), [Honkawa-cho](https://japanrail.alvaroom.org/#/station/honkawa-cho) (4), [Dobashi](https://japanrail.alvaroom.org/#/station/dobashi) (4), [Hotarujaya](https://japanrail.alvaroom.org/#/station/hotarujaya) (4), [Shinnakagawa-machi](https://japanrail.alvaroom.org/#/station/shinnakagawa-machi) (4), [Shindaiku-machi](https://japanrail.alvaroom.org/#/station/shindaiku-machi) (4), [Suwajinja Shrine](https://japanrail.alvaroom.org/#/station/suwajinja-shrine) (4), [City Hall](https://japanrail.alvaroom.org/#/station/city-hall) (4), [Gotanda](https://japanrail.alvaroom.org/#/station/gotanda) (3), [Yoyogi](https://japanrail.alvaroom.org/#/station/yoyogi) (3), [Yurakucho](https://japanrail.alvaroom.org/#/station/yurakucho) (3), [Ochanomizu](https://japanrail.alvaroom.org/#/station/ochanomizu) (3), [Nakano](https://japanrail.alvaroom.org/#/station/nakano) (3), [Ogikubo](https://japanrail.alvaroom.org/#/station/ogikubo) (3), [Kokubunji](https://japanrail.alvaroom.org/#/station/kokubunji) (3), [Tachikawa](https://japanrail.alvaroom.org/#/station/tachikawa) (3), [Hachioji](https://japanrail.alvaroom.org/#/station/hachioji) (3), [Takao](https://japanrail.alvaroom.org/#/station/takao) (3), [Kinshicho](https://japanrail.alvaroom.org/#/station/kinshicho) (3), [Funabashi](https://japanrail.alvaroom.org/#/station/funabashi) (3), [Inage](https://japanrail.alvaroom.org/#/station/inage) (3), [Saitama-Shintoshin](https://japanrail.alvaroom.org/#/station/saitama-shintoshin) (3), [Oimachi](https://japanrail.alvaroom.org/#/station/oimachi) (3), [Kamata](https://japanrail.alvaroom.org/#/station/kamata) (3), [Kawasaki](https://japanrail.alvaroom.org/#/station/kawasaki) (3), [Nihombashi](https://japanrail.alvaroom.org/#/station/nihombashi) (3), [Aoyama-itchome](https://japanrail.alvaroom.org/#/station/aoyama-itchome) (3), [Omote-sando](https://japanrail.alvaroom.org/#/station/omote-sando) (3), [Shinjuku-sanchome](https://japanrail.alvaroom.org/#/station/shinjuku-sanchome) (3), [Kasumigaseki](https://japanrail.alvaroom.org/#/station/kasumigaseki) (3), [Hibiya](https://japanrail.alvaroom.org/#/station/hibiya) (3), [Minami-Senju](https://japanrail.alvaroom.org/#/station/minami-senju) (3), [Kudanshita](https://japanrail.alvaroom.org/#/station/kudanshita) (3), [Wakoshi](https://japanrail.alvaroom.org/#/station/wakoshi) (3), [Kotake-mukaihara](https://japanrail.alvaroom.org/#/station/kotake-mukaihara) (3), [Nagatacho](https://japanrail.alvaroom.org/#/station/nagatacho) (3), [Shin-kiba](https://japanrail.alvaroom.org/#/station/shin-kiba) (3), [Jimbocho](https://japanrail.alvaroom.org/#/station/jimbocho) (3), [Nishi-Akashi](https://japanrail.alvaroom.org/#/station/nishi-akashi) (3), [Aioi](https://japanrail.alvaroom.org/#/station/aioi) (3), [Fukuyama](https://japanrail.alvaroom.org/#/station/fukuyama) (3), [Mihara](https://japanrail.alvaroom.org/#/station/mihara) (3), [Kurume](https://japanrail.alvaroom.org/#/station/kurume) (3), [Sendai (Kagoshima)](https://japanrail.alvaroom.org/#/station/sendai-kagoshima) (3), [Kagoshima-Chuo](https://japanrail.alvaroom.org/#/station/kagoshima-chuo) (3), [Ichinoseki](https://japanrail.alvaroom.org/#/station/ichinoseki) (3), [Kumagaya](https://japanrail.alvaroom.org/#/station/kumagaya) (3), [Yamashina](https://japanrail.alvaroom.org/#/station/yamashina) (3), [Rokujizo](https://japanrail.alvaroom.org/#/station/rokujizo) (3), [Fukuchiyama](https://japanrail.alvaroom.org/#/station/fukuchiyama) (3), [Miyazu](https://japanrail.alvaroom.org/#/station/miyazu) (3), [Temmabashi](https://japanrail.alvaroom.org/#/station/temmabashi) (3), [Juso](https://japanrail.alvaroom.org/#/station/juso) (3), [Yamato-Saidaiji](https://japanrail.alvaroom.org/#/station/yamato-saidaiji) (3), [Chiba-Minato](https://japanrail.alvaroom.org/#/station/chiba-minato) (3), [Abiko](https://japanrail.alvaroom.org/#/station/abiko) (3), [Matsudo](https://japanrail.alvaroom.org/#/station/matsudo) (3), [Kashiwa](https://japanrail.alvaroom.org/#/station/kashiwa) (3), [Nagatsuta](https://japanrail.alvaroom.org/#/station/nagatsuta) (3), [Hashimoto](https://japanrail.alvaroom.org/#/station/hashimoto-tokyo) (3), [Fujisawa](https://japanrail.alvaroom.org/#/station/fujisawa) (3), [Tamagawa](https://japanrail.alvaroom.org/#/station/tamagawa) (3), [Ebina](https://japanrail.alvaroom.org/#/station/ebina) (3), [Shonandai](https://japanrail.alvaroom.org/#/station/shonandai) (3), [Takahatafudo](https://japanrail.alvaroom.org/#/station/takahatafudo) (3), [Yorii](https://japanrail.alvaroom.org/#/station/yorii) (3), [Tobu-Dobutsu-Koen](https://japanrail.alvaroom.org/#/station/tobu-dobutsu-koen) (3), [Higashi-Murayama](https://japanrail.alvaroom.org/#/station/higashi-murayama) (3), [Keisei Takasago](https://japanrail.alvaroom.org/#/station/keisei-takasago) (3), [Keisei Tsudanuma](https://japanrail.alvaroom.org/#/station/keisei-tsudanuma) (3), [Nishikujo](https://japanrail.alvaroom.org/#/station/nishikujo) (3), [Morinomiya](https://japanrail.alvaroom.org/#/station/morinomiya) (3), [Nakatsu](https://japanrail.alvaroom.org/#/station/nakatsu) (3), [Hommachi](https://japanrail.alvaroom.org/#/station/hommachi) (3), [Tenjinbashisuji-rokuchome](https://japanrail.alvaroom.org/#/station/tenjinbashisuji-rokuchome) (3), [Imazato](https://japanrail.alvaroom.org/#/station/imazato) (3), [Tengachaya](https://japanrail.alvaroom.org/#/station/tengachaya) (3), [Shigino](https://japanrail.alvaroom.org/#/station/shigino) (3), [Kishinosato-tamade](https://japanrail.alvaroom.org/#/station/kishinosato-tamade) (3), [Sumiyoshi](https://japanrail.alvaroom.org/#/station/sumiyoshi-kobe) (3), [Kobe-Sannomiya](https://japanrail.alvaroom.org/#/station/kobe-sannomiya) (3), [Motomachi](https://japanrail.alvaroom.org/#/station/motomachi) (3), [Tsukaguchi](https://japanrail.alvaroom.org/#/station/tsukaguchi) (3), [Ikoma](https://japanrail.alvaroom.org/#/station/ikoma) (3), [Amagasaki](https://japanrail.alvaroom.org/#/station/amagasaki-osaka) (3), [Shin-Nagata](https://japanrail.alvaroom.org/#/station/shin-nagata) (3), [Shin-Kamagaya](https://japanrail.alvaroom.org/#/station/shin-kamagaya) (3), [Sanda](https://japanrail.alvaroom.org/#/station/sanda) (3), [Oji](https://japanrail.alvaroom.org/#/station/oji-osaka) (3), [Kashiharajingu-mae](https://japanrail.alvaroom.org/#/station/kashiharajingu-mae) (3), [Hojo Railways Ao](https://japanrail.alvaroom.org/#/station/hojo-railways-ao) (3), [Kibukawa](https://japanrail.alvaroom.org/#/station/kibukawa) (3), [Hatta](https://japanrail.alvaroom.org/#/station/hatta) (3), [Ozone](https://japanrail.alvaroom.org/#/station/ozone) (3), [Jingu-mae](https://japanrail.alvaroom.org/#/station/jingu-mae) (3), [Sanno](https://japanrail.alvaroom.org/#/station/sanno) (3), [Nishi-Biwajima](https://japanrail.alvaroom.org/#/station/nishi-biwajima) (3), [Meitetsu-Ichinomiya](https://japanrail.alvaroom.org/#/station/meitetsu-ichinomiya) (3), [Yatomi](https://japanrail.alvaroom.org/#/station/yatomi) (3), [Inuyama](https://japanrail.alvaroom.org/#/station/inuyama) (3), [Shin-Toyohashi](https://japanrail.alvaroom.org/#/station/shin-toyohashi) (3), [Yagyu-bashi](https://japanrail.alvaroom.org/#/station/yagyu-bashi) (3), [Sashima-raibu](https://japanrail.alvaroom.org/#/station/sashima-raibu) (3), [Komoto](https://japanrail.alvaroom.org/#/station/komoto) (3), [Shin-Hakushima](https://japanrail.alvaroom.org/#/station/shin-hakushima) (3), [Kurosaki](https://japanrail.alvaroom.org/#/station/kurosaki) (3), [Kurosaki-Ekimae](https://japanrail.alvaroom.org/#/station/kurosaki-ekimae) (3), [Nishi-Kurosaki](https://japanrail.alvaroom.org/#/station/nishi-kurosaki) (3), [Kumanishi](https://japanrail.alvaroom.org/#/station/kumanishi) (3), [Kaizuka](https://japanrail.alvaroom.org/#/station/kaizuka-fukuoka) (3), [Jono](https://japanrail.alvaroom.org/#/station/jono) (3), [Tagawa-Gotoji](https://japanrail.alvaroom.org/#/station/tagawa-gotoji) (3), [Tagawa Ita](https://japanrail.alvaroom.org/#/station/tagawa-ita) (3), [Odori](https://japanrail.alvaroom.org/#/station/odori) (3), [Iwamizawa](https://japanrail.alvaroom.org/#/station/iwamizawa) (3), [Minami-Chitose](https://japanrail.alvaroom.org/#/station/minami-chitose) (3), [Nagamachi](https://japanrail.alvaroom.org/#/station/nagamachi) (3), [Kogota](https://japanrail.alvaroom.org/#/station/kogota) (3), [Asahikawa](https://japanrail.alvaroom.org/#/station/asahikawa) (3), [Miyuki-bashi](https://japanrail.alvaroom.org/#/station/miyuki-bashi) (3), [Hirodaifuzokugakkou-mae](https://japanrail.alvaroom.org/#/station/hirodaifuzokugakkou-mae) (3), [Kenbyoin-mae](https://japanrail.alvaroom.org/#/station/kenbyoin-mae) (3), [Ujina 2-chome](https://japanrail.alvaroom.org/#/station/ujina-2-chome) (3), [Ujina 3-chome](https://japanrail.alvaroom.org/#/station/ujina-3-chome) (3), [Ujina 4-chome](https://japanrail.alvaroom.org/#/station/ujina-4-chome) (3), [Ujina 5-chome](https://japanrail.alvaroom.org/#/station/ujina-5-chome) (3), [Kaigan-dori](https://japanrail.alvaroom.org/#/station/kaigan-dori) (3), [Motoujina-guchi](https://japanrail.alvaroom.org/#/station/motoujina-guchi) (3), [Hiroshima Port](https://japanrail.alvaroom.org/#/station/hiroshima-port) (3), [Nishihamano-machi](https://japanrail.alvaroom.org/#/station/nishihamano-machi) (3), [Shinchi Chinatown](https://japanrail.alvaroom.org/#/station/shinchi-chinatown) (3), [Nagasaki-ekimae](https://japanrail.alvaroom.org/#/station/nagasaki-ekimae) (3), [Yachiyo-machi](https://japanrail.alvaroom.org/#/station/yachiyo-machi) (3), [Stadium City South](https://japanrail.alvaroom.org/#/station/stadium-city-south) (3), [Stadium City North](https://japanrail.alvaroom.org/#/station/stadium-city-north) (3), [Mori-machi](https://japanrail.alvaroom.org/#/station/mori-machi) (3), [Urakami-ekimae](https://japanrail.alvaroom.org/#/station/urakami-ekimae) (3), [University Hospital](https://japanrail.alvaroom.org/#/station/university-hospital) (3), [Atomic Bomb Museum](https://japanrail.alvaroom.org/#/station/atomic-bomb-museum) (3), [Peace Park](https://japanrail.alvaroom.org/#/station/peace-park) (3), [Ohashi](https://japanrail.alvaroom.org/#/station/ohashi-nagasaki) (3), [Urakami Tram Depot](https://japanrail.alvaroom.org/#/station/urakami-tram-depot) (3), [Iwayabashi](https://japanrail.alvaroom.org/#/station/iwayabashi) (3), [Nagasaki University](https://japanrail.alvaroom.org/#/station/nagasaki-university) (3), [Wakaba-machi](https://japanrail.alvaroom.org/#/station/wakaba-machi) (3), [Chitose-machi](https://japanrail.alvaroom.org/#/station/chitose-machi) (3), [Showamachi-dori](https://japanrail.alvaroom.org/#/station/showamachi-dori) (3), [Sumiyoshi](https://japanrail.alvaroom.org/#/station/sumiyoshi-nagasaki) (3), [Akasako](https://japanrail.alvaroom.org/#/station/akasako) (3), [Meganebashi Bridge](https://japanrail.alvaroom.org/#/station/meganebashi-bridge) (3), [Hamano-machi Arcade](https://japanrail.alvaroom.org/#/station/hamano-machi-arcade) (3), [Korimoto](https://japanrail.alvaroom.org/#/station/korimoto) (3), [Harimayabashi](https://japanrail.alvaroom.org/#/station/harimayabashi) (3), [Matsuyama City](https://japanrail.alvaroom.org/#/station/matsuyama-city) (3)

## Lo que queda

La lista de huecos respecto a OpenStreetMap está en [AUDITORIA.md](AUDITORIA.md) (`tools/audit_coverage.py`).

Por fases. Las casillas de líneas, trenes y regiones se marcan solas cuando existen en los datos.

### Fase 1 · Completar Tokio (27/27)

_Muchas líneas de metro «se acaban» en el mapa donde en realidad siguen por redes privadas o por otras líneas de JR._

**JR East que faltan**

- [x] Línea Keiyō (JE) — Tokio–Soga, hacia Disneyland
- [x] Línea Jōban (JJ/JL) — Ueno/Shinagawa–Toride
- [x] Línea Musashino (JM) — el anillo exterior
- [x] Línea Nambu (JN)
- [x] Línea Yokohama (JH)
- [x] Línea Tōkaidō (JT) — Tokio–Odawara/Atami
- [x] Línea Yokosuka (JO) — hacia Kamakura
- [x] Línea Shōnan-Shinjuku (JS)
- [x] Líneas Utsunomiya y Takasaki / Ueno-Tokyo Line (JU)
- [x] Línea Ōme (JC) — hacia las montañas de Okutama

**Compañías privadas de Tokio**

- [x] Tōkyū Tōyoko — Shibuya–Yokohama
- [x] Tōkyū Den-en-toshi
- [x] Tōkyū Meguro, Ōimachi, Ikegami y Tamagawa
- [x] Tōkyū Setagaya (tranvía)
- [x] Odakyū Odawara (y el Romancecar) — Shinjuku–Hakone
- [x] Keiō, Takao e Inokashira
- [x] Seibu Ikebukuro y Shinjuku
- [x] Tōbu Skytree y Tōjō
- [x] Keikyū principal y del aeropuerto de Haneda
- [x] Keisei principal y Skyliner (Narita)
- [x] Tsukuba Express — Akihabara–Tsukuba
- [x] Sōtetsu
- [x] Monorraíl de Tama
- [x] Enoden — Fujisawa–Kamakura, junto al mar
- [x] Shōnan Monorail — monorraíl suspendido Ōfuna–Enoshima

**Yokohama**

- [x] Metro de Yokohama: líneas Azul y Verde
- [x] Línea Minatomirai

### Fase 2 · Ōsaka y el resto de Kansai (18/18)

_Kioto ya llega hasta Ōsaka y Nara por varias líneas; falta el centro de Ōsaka y Kōbe._

**Ōsaka**

- [x] Región «Ōsaka» con su botón en el mapa
- [x] JR Ōsaka Loop Line (el «Yamanote» de Ōsaka)
- [x] Osaka Metro Midōsuji
- [x] Resto de Osaka Metro (Tanimachi, Yotsubashi, Chūō, Sennichimae, Sakaisuji, Nagahori Tsurumi-ryokuchi, Imazatosuji, New Tram)
- [x] Nankai (y el Rapi:t al aeropuerto de Kansai)
- [x] Hanshin — Ōsaka–Kōbe
- [x] Hankyu Kōbe y Takarazuka
- [x] Kintetsu Nara y Ōsaka
- [x] Monorraíl de Ōsaka
- [x] Tranvía Hankai

**Kōbe y alrededores**

- [x] Metro de Kōbe
- [x] Port Liner y Rokkō Liner
- [x] Línea JR Kōbe (A)

**Kioto: lo que falta**

- [x] Keihan Keishin e Ishiyama-Sakamoto (hacia el lago Biwa)
- [x] JR Kosei y Biwako (B / A)
- [x] Randen: tranvías
- [x] Nippori-Toneri Liner: sus trenes

**Otros**

- [x] Monorraíl de Chiba — el monorraíl suspendido más largo del mundo

### Fase 2b · Completar Tokio y Kansai (huecos detectados) (27/29)

_Salen de la auditoría contra OpenStreetMap (AUDITORIA.md): ramales y líneas urbanas que faltan en las zonas ya hechas._

**Tokio · ramales de compañías que ya están**

- [x] Keikyū Kurihama (hasta Misakiguchi), Zushi y Daishi
- [x] Keisei Kanamachi — Shibamata (Tora-san)
- [x] Keisei Chiba, Chihara y Matsudo (ex Shin-Keisei)
- [x] Hokusō / Narita Sky Access, Keisei Higashi-Narita y Shibayama
- [x] Keiō Nueva Línea (Hatsudai, Hatagaya), Sagamihara, Keibajō y Dōbutsuen
- [x] Odakyū Tama
- [x] Seibu: Haijima, Kokubunji, Tamako, Tamagawa, Sayama, Yamaguchi, Seibu-en, Yūrakuchō y Toshima (estudio de Harry Potter)
- [x] Tōbu Kameido, Daishi, Urban Park y Ogose
- [x] Tōkyū Kodomonokuni y Shin-Yokohama; Sōtetsu Izumino y Shin-Yokohama
- [x] Tokyo Metro Chiyoda: ramal de Kita-Ayase
- [x] JR Tsurumi, ramal Nambu, Sagami, Itsukaichi, Hachikō y Kawagoe

**Tokio · otras compañías del área metropolitana**

- [x] Saitama Rapid Railway y Tōyō Rapid (continúan las líneas Namboku y Tōzai)
- [x] New Shuttle, Kanazawa Seaside Line y Disney Resort Line
- [x] Ryūtetsu (Nagareyama) y Yamaman Yukarigaoka

**Kansai · ramales de compañías que ya están**

- [x] JR West: Hanwa, Takarazuka, Gakkentoshi (Katamachi), Yamatoji, JR Tōzai, Osaka Higashi y Sakurai
- [x] Kintetsu: Minami-Ōsaka, Nagano, Dōmyōji, Gose, Keihanna, Ikoma, Tenri, Tawaramoto y Shigi
- [x] Hankyu: Senri, Imazu, Itami, Minoo y Kōyō
- [x] Hanshin Mukogawa y Kōbe Kōsoku
- [x] Nankai: Semboku, Shiomibashi y Takashinohama
- [x] Keihan Katano y Nakanoshima
- [x] Monorraíl de Ōsaka: ramal de Saito

**Kansai · otras compañías**

- [x] Kōbe Dentetsu (Arima, Sanda, Ao y Kōen-toshi)
- [x] Sanyō Dentetsu (Kōbe–Himeji)
- [x] Nose Dentetsu (Myōken y Nissei)

**Periferia (más lejos; mejor para fases posteriores)**

- [x] JR en Chiba: Sōbu principal, Narita, Uchibō, Sotobō, Tōgane y Kururi
- [ ] JR Gotemba y tramos lejanos de la Jōban y la Tōhoku
- [ ] Kantō Railway (Jōsō, Ryūgasaki) e Izuhakone Daiyūzan
- [x] Seibu Chichibu, Tōbu Nikkō e Isesaki (hacia Nikkō y Chichibu)
- [x] Isumi y Kominato (trenes rurales de Chiba)

### Fase 3 · Otras ciudades (6/6)

_Una ciudad por vez, empezando por las de redes más interesantes._

**Ciudades**

- [x] Nagoya: metro y Meitetsu
- [x] Fukuoka: metro, Nishitetsu
- [x] Sapporo: metro de ruedas de goma y tranvía
- [x] Sendai: metro
- [x] Hiroshima: tranvía (Hiroden), la mayor red de tranvía de Japón
- [x] Tranvías de Nagasaki, Kumamoto, Kagoshima, Hakodate, Okayama, Kōchi, Toyama, Matsuyama, Toyohashi y Fukui

### Fase 3b · Completar las ciudades de la fase 3 (4/13)

_Detectado por la auditoría: ramales y líneas regionales de esas ciudades._

**Nagoya y alrededores**

- [ ] Ramales de Meitetsu (Mikawa, Nishio, Bisai, Tsushima, Takehana, Hiromi, Kakamigahara)
- [ ] Aichi Loop, Jōhoku, JR Taketoyo y JR Taita
- [ ] Yokkaichi Asunarou, Sangi Railway y ramales de Kintetsu (Yunoyama, Suzuka)
- [x] JR Chūō West (Nagoya–Nakatsugawa)
- [ ] Yutorito (autobús guiado de Nagoya)

**Fukuoka, Hiroshima y otras**

- [ ] JR en Fukuoka: Kagoshima principal (Hakata–Mojikō), Sasaguri y Fukuhoku Yutaka
- [x] JR en Hiroshima: Sanyō, Kure y Geibi
- [ ] JR Hakodate principal (Sapporo–Otaru) e Isaribi (Hakodate)
- [ ] JR en Nagasaki: principal y Ōmura
- [ ] JR en Kumamoto: Hōhi y Misumi
- [ ] JR en Shikoku y Okayama: Yosan, Uno, Kibi, Akō y Seto-Ōhashi
- [x] Ramal de Rifu (Sendai) y JR Iida (Toyohashi)
- [x] Monorraíl de Kitakyūshū

### Fase 3c · Japón, prefectura a prefectura (16/47)

_Cada prefectura se cierra del todo (líneas, estaciones, numeración, trenes y fotos) antes de pasar a la siguiente. Se marca sola cuando tools/audit_coverage.py no le encuentra ni una estación de menos: el recuento sale de todas las estaciones que OpenStreetMap tiene en su área administrativa._

**Hokkaidō**

- [x] 01 Hokkaidō

**Tōhoku**

- [ ] 02 Aomori
- [ ] 03 Iwate
- [x] 04 Miyagi
- [ ] 05 Akita
- [ ] 06 Yamagata
- [ ] 07 Fukushima

**Kantō**

- [ ] 08 Ibaraki
- [ ] 09 Tochigi
- [ ] 10 Gunma
- [x] 11 Saitama
- [x] 12 Chiba
- [x] 13 Tokio
- [x] 14 Kanagawa

**Chūbu**

- [ ] 15 Niigata
- [ ] 16 Toyama
- [ ] 17 Ishikawa
- [ ] 18 Fukui
- [ ] 19 Yamanashi
- [ ] 20 Nagano
- [ ] 21 Gifu
- [ ] 22 Shizuoka
- [x] 23 Aichi

**Kansai**

- [ ] 24 Mie
- [x] 25 Shiga
- [x] 26 Kioto
- [x] 27 Ōsaka
- [x] 28 Hyōgo
- [x] 29 Nara
- [ ] 30 Wakayama

**Chūgoku**

- [ ] 31 Tottori
- [ ] 32 Shimane
- [ ] 33 Okayama
- [x] 34 Hiroshima
- [ ] 35 Yamaguchi

**Shikoku**

- [ ] 36 Tokushima
- [ ] 37 Kagawa
- [ ] 38 Ehime
- [x] 39 Kōchi

**Kyūshū y Okinawa**

- [x] 40 Fukuoka
- [ ] 41 Saga
- [ ] 42 Nagasaki
- [ ] 43 Kumamoto
- [ ] 44 Ōita
- [ ] 45 Miyazaki
- [x] 46 Kagoshima
- [ ] 47 Okinawa

### Fase 4 · Líneas y trenes especiales (5/13)

_Lo que hace único el tren en Japón, más allá del día a día._

**Líneas turísticas y de montaña**

- [x] Hakone Tozan — zigzags de montaña
- [ ] Ferrocarril de la garganta de Kurobe
- [ ] Ōigawa — trenes de vapor y Abt
- [ ] Línea Gonō, junto al mar de Japón
- [ ] Línea Tadami
- [ ] Fujikyū — hacia el monte Fuji

**Expresos limitados y nocturnos**

- [ ] Sunrise Izumo / Seto — el último tren nocturno regular
- [x] Odakyū Romancecar
- [ ] Narita Express
- [x] Haruka (aeropuerto de Kansai)
- [x] Thunderbird
- [x] Kintetsu Hinotori
- [ ] Trenes de vapor (SL Yamaguchi, SL Taiju…)

### Fase 5 · Shinkansen: servicios y futuro (1/8)

**Servicios y ramales**

- [ ] Servicios (Nozomi, Hikari, Kodama, Hayabusa…) y en qué estaciones para cada uno
- [x] Ramal Hakata-Minami
- [ ] Ramal de Gala-Yuzawa (estación de esquí)
- [ ] Serie E2 (actual/histórico, fechas por confirmar)
- [ ] Doctor Yellow (923), el tren amarillo de inspección

**En obras o proyectadas**

- [ ] Chūō Shinkansen (maglev) — Shinagawa–Nagoya, en construcción
- [ ] Prolongación del Hokkaidō Shinkansen a Sapporo (en obras)
- [ ] Prolongación del Hokuriku Shinkansen de Tsuruga a Ōsaka (proyecto)

### Fase 6 · Funciones de la web (7/15)

**Fluidez (hecho)**

- [x] Transiciones al pasar el ratón y al pulsar en listas, fichas y mapa
- [x] El panel entra con un fundido en vez de repintarse de golpe
- [x] Recordar la posición de la lista al volver atrás
- [x] Esqueleto de carga mientras llegan los datos
- [x] Listas largas que solo se pintan al verse (content-visibility)
- [x] La línea del mapa se engorda al pasar por encima

**Explorar**

- [ ] Buscar ruta entre dos estaciones (transbordos, líneas)
- [ ] Línea del tiempo: aperturas de líneas y trenes por año
- [ ] Récords: estación más profunda, línea más antigua, tren más rápido…
- [ ] Página de cada compañía (operador)
- [ ] Estaciones: año de apertura y viajeros diarios

**Técnico**

- [ ] URLs con versión en JS/CSS para que Cloudflare nunca sirva una versión vieja
- [ ] Vista previa al compartir enlaces (Open Graph: imagen y descripción)
- [ ] Interfaz también en inglés
- [x] Reducir el peso de las fotos (WebP + miniaturas)

### Fase 7 · Contenido (0/4)

**Textos y fotos**

- [ ] Fotos de estaciones (Wikimedia Commons)
- [ ] Más datos curiosos de estaciones (ver huecos detectados)
- [ ] Datos curiosos para los trenes que no tienen
- [ ] Trenes históricos para las líneas que no tienen (ver huecos detectados)

