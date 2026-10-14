"""Generated from Smithy shape ``com.amazonaws.codepipeline#WebhookNotFoundException``."""

import zapros
from typing_extensions import TypedDict

from capo_codepipeline.errors import ServiceError


class WebhookNotFoundException_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookNotFoundException_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> WebhookNotFoundException_:
    out: WebhookNotFoundException_ = {}  # type: ignore[typeddict-item]
    return out


class WebhookNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#WebhookNotFoundException``."""

    code: str | None = "WebhookNotFoundException"

    def __init__(
        self,
        data: WebhookNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WebhookNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "WebhookNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
