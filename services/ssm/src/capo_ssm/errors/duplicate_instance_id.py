"""Generated from Smithy shape ``com.amazonaws.ssm#DuplicateInstanceId``."""

import zapros
from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class DuplicateInstanceId_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateInstanceId_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateInstanceId_:
    out: DuplicateInstanceId_ = {}  # type: ignore[typeddict-item]
    return out


class DuplicateInstanceId(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#DuplicateInstanceId``."""

    code: str | None = "DuplicateInstanceId"

    def __init__(
        self,
        data: DuplicateInstanceId_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateInstanceId",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DuplicateInstanceId":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
