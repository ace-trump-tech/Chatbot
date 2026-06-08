import abc

from astrbot.core.config import 摆烂仙君Config
from astrbot.core.platform.astr_message_event import AstrMessageEvent
from astrbot.core.platform.message_type import MessageType


class HandlerFilter(abc.ABC):
    @abc.abstractmethod
    def filter(self, event: AstrMessageEvent, cfg: 摆烂仙君Config) -> bool:
        """是否应当被过滤"""
        raise NotImplementedError


__all__ = ["摆烂仙君Config", "AstrMessageEvent", "HandlerFilter", "MessageType"]
