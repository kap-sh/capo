"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidOutputFolder``."""

import zapros
from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class InvalidOutputFolder_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidOutputFolder_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidOutputFolder_:
    out: InvalidOutputFolder_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidOutputFolder(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidOutputFolder``."""

    code: str | None = "InvalidOutputFolder"

    def __init__(
        self,
        data: InvalidOutputFolder_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidOutputFolder",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidOutputFolder":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
