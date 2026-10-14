"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidCommandId``."""

import zapros
from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class InvalidCommandId_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidCommandId_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidCommandId_:
    out: InvalidCommandId_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidCommandId(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidCommandId``."""

    code: str | None = "InvalidCommandId"

    def __init__(
        self,
        data: InvalidCommandId_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCommandId",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidCommandId":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
