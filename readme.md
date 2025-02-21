# Auto-coder-agent_Cursor_Roo_code

## 概要
このプロジェクトは、CursorとRooを使用した自動コーディングエージェントのためのコードベースです。
SpecStoryを統合し、AIとの対話履歴を効果的に管理・活用します。

## 特徴
- Cursor AIとの対話履歴の自動保存
- ストーリーベースの開発管理
- ログ駆動開発（LDD）の実践
- 多言語対応（日本語/英語）

## ディレクトリ構造
```
.
├── .cursor/           # Cursor関連の設定とルール
│   └── rules/        # Cursorのルールファイル
├── .specstory/       # 仕様とストーリーの履歴
│   ├── config.mdc    # SpecStory設定
│   ├── templates/    # ストーリーテンプレート
│   ├── current/      # 現在のストーリー
│   ├── archive/      # 完了したストーリー
│   └── history/      # 履歴ファイル
├── EN/               # 英語版ドキュメント
├── JA/               # 日本語版ドキュメント
├── docs/             # プロジェクトドキュメント
├── logs/             # ログファイル
├── xnotes/           # 追加のノートと記録
├── @logging_template.mdc    # ロギングテンプレート
└── @memory-bank.mdc        # メモリバンク
```

## セットアップ
1. リポジトリのクローン:
```bash
git clone https://github.com/ShunsukeHayashi/Auto-coder-agent_Cursor_Roo_code.git
```

2. 必要なツール:
- Cursor（最新版）
- PowerShell 7以上
- Git
- SpecStory Cursor Extension

3. SpecStoryの設定:
- Cursor拡張機能のインストール
- `.specstory/config.mdc`の設定確認
- 必要に応じてテンプレートのカスタマイズ

## 使用方法

### 基本的な使用方法
1. Cursorでプロジェクトを開く
2. AIとの対話を開始
3. 対話履歴は自動的に`.specstory/history/`に保存

### ストーリーの作成
1. `.specstory/templates/`のテンプレートを使用
2. 新しいストーリーは`.specstory/current/`に作成
3. 完了したストーリーは`.specstory/archive/`に移動

### ログ駆動開発
1. 各操作は`@logging_template.mdc`に従ってログ記録
2. システムログは`logs/`ディレクトリに保存
3. メモリバンク（`@memory-bank.mdc`）で状態管理

詳細な使用方法は `docs/` ディレクトリ内のドキュメントを参照してください。

## ワークフロー
1. ストーリーの作成（Draft）
2. レビューと承認（In Review → Approved）
3. 実装（In Progress）
4. テストと検証（Testing）
5. 完了と保管（Completed → Archived）

## 貢献
1. このリポジトリをフォーク
2. 新しいブランチを作成
3. 変更を加える
4. プルリクエストを送信

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。

## 関連リンク
- [SpecStory公式サイト](https://specstory.com/)
- [Cursor公式サイト](https://cursor.sh/)
- [プロジェクトドキュメント](./docs/)
