"""Generated from Smithy shape ``com.amazonaws.ssm#TooManyTagsError``."""

import zapros
from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class TooManyTagsError_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyTagsError_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyTagsError_:
    out: TooManyTagsError_ = {}  # type: ignore[typeddict-item]
    return out


class TooManyTagsError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#TooManyTagsError``."""

    code: str | None = "TooManyTagsError"

    def __init__(
        self,
        data: TooManyTagsError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyTagsError":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
