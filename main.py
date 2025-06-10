import argparse
from asyncio import CancelledError
from asyncio import run

from src.application import TikTokDownloader


async def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="抖音/TikTok下载器")
    parser.add_argument(
        "--server", 
        action="store_true", 
        help="启动API服务器模式"
    )
    parser.add_argument(
        "--host", 
        default="127.0.0.1", 
        help="API服务器主机地址 (默认: 127.0.0.1)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=5555, 
        help="API服务器端口 (默认: 5555)"
    )
    parser.add_argument(
        "--log-level",
        default="info",
        choices=["critical", "error", "warning", "info", "debug", "trace"],
        help="日志级别 (默认: info)"
    )
    
    args = parser.parse_args()
    
    async with TikTokDownloader() as downloader:
        try:
            if args.server:
                # 如果指定了--server参数，直接启动API服务器
                await downloader.run_server(
                    host=args.host,
                    port=args.port,
                    log_level=args.log_level
                )
            else:
                # 否则运行正常的交互模式
                await downloader.run()
        except (
                KeyboardInterrupt,
                CancelledError,
        ):
            return


if __name__ == "__main__":
    run(main())
