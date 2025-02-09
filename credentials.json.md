# `credentials.json` の書式

## 通常

```json
[
  {
    "enable": true,
    "username": "<ユーザー名>",
    "email": "<メールアドレス>",
    "password": "<パスワード>"
  }
]
```

##### `enable`

このアカウントでリプライ爆弾を行わない際は、true のところを false にすると、そのアカウントで爆が行われない

##### `username`

@抜きのユーザー名

##### `email`

メールアドレス。省略する際は`null`と記述する

##### `password`

パスワード

## 例

```json
[
  {
    "enable": true,
    "username": "test810114514",
    "email": null,
    "password": "114514"
  }
]
```

## 複数アカウントを追加したいとき

```json
[
  {
    "enable": true,
    "username": "test810114514",
    "email": null,
    "password": "114514"
  },
  {
    "enable": true,
    "username": "test8101145142",
    "email": "114514@example.com",
    "password": "114514"
  }
]
```

json の記法に則ってください。
