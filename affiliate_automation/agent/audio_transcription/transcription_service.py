"""
音声文字起こしサービスモジュール

このモジュールはGroq Whisper APIを使用して音声ファイルをテキストに変換します。
"""

import os
import logging
import time
import json
from typing import Dict, Any, Optional, List
from datetime import datetime

# Import configuration
import sys
sys.path.append('/home/ubuntu/repos/0_Auto-coder-agent_Cursor_Roo_code')
from affiliate_automation.config.config import AI_TOOLS, GROQ_API_KEY

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("/home/ubuntu/repos/0_Auto-coder-agent_Cursor_Roo_code/affiliate_automation/logs/transcription_service.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("TranscriptionService")

class TranscriptionService:
    """
    Groq Whisper APIを使用した音声文字起こしサービス。
    
    このクラスは音声ファイルをテキストに変換するための機能を提供します。
    高速なGroq Whisper APIを使用して、様々な形式の音声ファイルを処理できます。
    """
    
    def __init__(self):
        """
        音声文字起こしサービスを初期化します。
        """
        self.transcription_config = AI_TOOLS.get("audio_transcription", {}).get("groq_whisper", {})
        if not self.transcription_config:
            logger.error("音声文字起こし設定が見つかりません")
            raise ValueError("音声文字起こし設定が見つかりません")
            
        self.groq_api_key = os.environ.get("GROQ_API_KEY", GROQ_API_KEY)
        self.supported_formats = self.transcription_config.get("supported_formats", [])
        self.model = self.transcription_config.get("model", "whisper-large-v3")
        
        logger.info("音声文字起こしサービスが初期化されました")
    
    def transcribe_audio(self, audio_path: str, language: Optional[str] = None) -> Dict[str, Any]:
        """
        音声ファイルを文字起こしします。
        
        Args:
            audio_path: 音声ファイルのパス
            language: 音声の言語（オプション）
            
        Returns:
            文字起こし結果を含む辞書
        """
        logger.info(f"音声ファイルの文字起こしを開始: {audio_path}")
        
        # ファイル形式を確認
        file_extension = audio_path.split('.')[-1].lower()
        if file_extension not in self.supported_formats:
            logger.error(f"サポートされていないファイル形式: {file_extension}")
            return {
                "success": False,
                "error": f"サポートされていないファイル形式: {file_extension}",
                "supported_formats": self.supported_formats
            }
        
        # Groq APIを呼び出して文字起こし
        try:
            from groq import Groq
            
            client = Groq(api_key=self.groq_api_key)
            
            start_time = time.time()
            
            with open(audio_path, "rb") as audio_file:
                # APIリクエストのパラメータを設定
                params = {
                    "model": self.model,
                    "file": audio_file,
                    "response_format": "verbose_json"
                }
                
                # 言語が指定されている場合は追加
                if language:
                    params["language"] = language
                
                # 文字起こしを実行
                response = client.audio.transcriptions.create(**params)
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            # レスポンスを処理
            if hasattr(response, 'text'):
                transcription_text = response.text
            else:
                transcription_text = str(response)
            
            # 結果を返す
            result = {
                "success": True,
                "text": transcription_text,
                "processing_time": elapsed_time,
                "model": self.model,
                "language": language,
                "timestamp": datetime.now().isoformat()
            }
            
            logger.info(f"文字起こし完了: {len(transcription_text)} 文字, 処理時間: {elapsed_time:.2f} 秒")
            return result
            
        except Exception as e:
            logger.error(f"文字起こし中にエラーが発生しました: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def save_transcription(self, transcription: Dict[str, Any], filepath: Optional[str] = None) -> str:
        """
        文字起こし結果をファイルに保存します。
        
        Args:
            transcription: 文字起こし結果
            filepath: 保存先のファイルパス（オプション）
            
        Returns:
            保存先のファイルパス
        """
        if filepath is None:
            # タイムスタンプを使用してファイル名を生成
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = f"/home/ubuntu/affiliate_automation/data/transcriptions/transcription_{timestamp}.json"
        
        # ディレクトリが存在することを確認
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 文字起こし結果をファイルに保存
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(transcription, f, indent=2, ensure_ascii=False)
            
        logger.info(f"文字起こし結果を保存しました: {filepath}")
        return filepath
    
    def load_transcription(self, filepath: str) -> Dict[str, Any]:
        """
        ファイルから文字起こし結果を読み込みます。
        
        Args:
            filepath: 文字起こし結果のファイルパス
            
        Returns:
            読み込んだ文字起こし結果
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                transcription = json.load(f)
                
            logger.info(f"文字起こし結果を読み込みました: {filepath}")
            return transcription
        except FileNotFoundError:
            logger.error(f"文字起こしファイルが見つかりません: {filepath}")
            raise FileNotFoundError(f"文字起こしファイルが見つかりません: {filepath}")
        except json.JSONDecodeError:
            logger.error(f"文字起こしファイルのJSONが無効です: {filepath}")
            raise ValueError(f"文字起こしファイルのJSONが無効です: {filepath}")
