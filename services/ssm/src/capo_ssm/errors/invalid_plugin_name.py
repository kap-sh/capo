"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidPluginName``."""

import zapros
from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class InvalidPluginName_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPluginName_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPluginName_:
    out: InvalidPluginName_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidPluginName(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidPluginName``."""

    code: str | None = "InvalidPluginName"

    def __init__(
        self,
        data: InvalidPluginName_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPluginName",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidPluginName":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
