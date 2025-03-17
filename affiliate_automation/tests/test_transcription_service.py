import unittest
import os
import json
from unittest.mock import patch, MagicMock

# Import the transcription service
import sys
sys.path.append('/home/ubuntu/repos/0_Auto-coder-agent_Cursor_Roo_code')
from affiliate_automation.agent.audio_transcription.transcription_service import TranscriptionService

class TestTranscriptionService(unittest.TestCase):
    """音声文字起こしサービスのテスト"""
    
    def setUp(self):
        """テスト前の準備"""
        # 設定をモック
        self.config_patcher = patch('affiliate_automation.agent.audio_transcription.transcription_service.AI_TOOLS', {
            "audio_transcription": {
                "groq_whisper": {
                    "model": "whisper-large-v3",
                    "supported_formats": ["mp3", "wav"]
                }
            }
        })
        self.config_patcher.start()
        
        # APIキーをモック
        self.api_key_patcher = patch('affiliate_automation.agent.audio_transcription.transcription_service.GROQ_API_KEY', "mock_api_key")
        self.api_key_patcher.start()
        
        # サービスを初期化
        self.service = TranscriptionService()
    
    def tearDown(self):
        """テスト後のクリーンアップ"""
        self.config_patcher.stop()
        self.api_key_patcher.stop()
    
    def test_init(self):
        """初期化のテスト"""
        self.assertEqual(self.service.model, "whisper-large-v3")
        self.assertEqual(self.service.supported_formats, ["mp3", "wav"])
    
    @patch('groq.Groq')
    def test_transcribe_audio_success(self, mock_groq):
        """文字起こし成功のテスト"""
        # Groqクライアントのモック
        mock_client = MagicMock()
        mock_groq.return_value = mock_client
        
        # レスポンスのモック
        mock_response = MagicMock()
        mock_response.text = "これはテストの文字起こし結果です。"
        mock_client.audio.transcriptions.create.return_value = mock_response
        
        # テスト用の音声ファイルパス
        audio_path = "test.mp3"
        
        # 文字起こしを実行
        mock_open = MagicMock()
        with patch('builtins.open', mock_open):
            result = self.service.transcribe_audio(audio_path)
        
        # 結果を検証
        self.assertTrue(result["success"])
        self.assertEqual(result["text"], "これはテストの文字起こし結果です。")
        self.assertIn("processing_time", result)
        self.assertEqual(result["model"], "whisper-large-v3")
    
    def test_unsupported_format(self):
        """サポートされていない形式のテスト"""
        result = self.service.transcribe_audio("test.pdf")
        self.assertFalse(result["success"])
        self.assertIn("サポートされていないファイル形式", result["error"])
    
    @patch('groq.Groq')
    def test_transcribe_audio_error(self, mock_groq):
        """文字起こしエラーのテスト"""
        # Groqクライアントのモック
        mock_client = MagicMock()
        mock_groq.return_value = mock_client
        
        # エラーを発生させる
        mock_client.audio.transcriptions.create.side_effect = Exception("APIエラー")
        
        # テスト用の音声ファイルパス
        audio_path = "test.mp3"
        
        # 文字起こしを実行
        mock_open = MagicMock()
        with patch('builtins.open', mock_open):
            result = self.service.transcribe_audio(audio_path)
        
        # 結果を検証
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "APIエラー")
    
    def test_save_and_load_transcription(self):
        """文字起こし結果の保存と読み込みのテスト"""
        # テスト用の文字起こし結果
        transcription = {
            "success": True,
            "text": "これはテストの文字起こし結果です。",
            "processing_time": 1.23,
            "model": "whisper-large-v3"
        }
        
        # 一時ファイルパス
        temp_dir = "/tmp/transcription_test"
        os.makedirs(temp_dir, exist_ok=True)
        filepath = os.path.join(temp_dir, "test_transcription.json")
        
        # 保存のテスト
        with patch('builtins.open', MagicMock()):
            saved_path = self.service.save_transcription(transcription, filepath)
            self.assertEqual(saved_path, filepath)
        
        # 読み込みのテスト
        mock_file = MagicMock()
        mock_file.return_value.__enter__.return_value.read.return_value = json.dumps(transcription)
        with patch('builtins.open', mock_file):
            loaded = self.service.load_transcription(filepath)
            self.assertEqual(loaded, transcription)

if __name__ == '__main__':
    unittest.main()
