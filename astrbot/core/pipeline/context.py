from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from astrbot.core.config import 摆烂仙君Config

from .context_utils import call_event_hook, call_handler

if TYPE_CHECKING:
    from astrbot.core.star import PluginManager


@dataclass
class PipelineContext:
    """上下文对象，包含管道执行所需的上下文信息"""

    astrbot_config: 摆烂仙君Config  # 摆烂仙君 配置对象
    plugin_manager: PluginManager  # 插件管理器对象
    astrbot_config_id: str
    call_handler = call_handler
    call_event_hook = call_event_hook
