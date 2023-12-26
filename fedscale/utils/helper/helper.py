import logging
from typing import Union
from p2p_server.rpc.rpc_client import TorrentCommunication


# 使用基类TorrentCommunication, 将grpc作为控制信息的通信后端
# 需要实现bt_broadcast(将torrent广播给某些client)
class TorrentCommunicationRPC(TorrentCommunication):
    def __init__(self, rank: int, logger: logging.Logger):
        super().__init__(rank, logger)

    def create_torrent(self, path: str):
        torrent, status = self.rpc_client.create_torrent(path)
        if not status:
            raise Exception("create torrent error")
        self.logger.debug("create torrent ok")

        return torrent

    def bt_broadcast(self, data_path: Union[str, None]):
        # For TorrentCommunication with RPC, this is deprecated.
        pass
