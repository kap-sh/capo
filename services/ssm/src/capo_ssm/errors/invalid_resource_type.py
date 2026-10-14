"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidResourceType``."""

import zapros
from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class InvalidResourceType_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidResourceType_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidResourceType_:
    out: InvalidResourceType_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidResourceType(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidResourceType``."""

    code: str | None = "InvalidResourceType"

    def __init__(
        self,
        data: InvalidResourceType_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceType",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidResourceType":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
