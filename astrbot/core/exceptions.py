from __future__ import annotations


class 摆烂仙君Error(Exception):
    """Base exception for all 摆烂仙君 errors."""


class ProviderNotFoundError(摆烂仙君Error):
    """Raised when a specified provider is not found."""


class EmptyModelOutputError(摆烂仙君Error):
    """Raised when the model response contains no usable assistant output."""


class KnowledgeBaseUploadError(摆烂仙君Error):
    """Raised when knowledge base upload fails with a user-facing message."""

    def __init__(
        self,
        *,
        stage: str,
        user_message: str,
        details: dict | None = None,
    ) -> None:
        super().__init__(user_message)
        self.stage = stage
        self.user_message = user_message
        self.details = details or {}

    def __str__(self) -> str:
        return self.user_message
