"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidOutputLocation``."""

import zapros
from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class InvalidOutputLocation_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidOutputLocation_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidOutputLocation_:
    out: InvalidOutputLocation_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidOutputLocation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidOutputLocation``."""

    code: str | None = "InvalidOutputLocation"

    def __init__(
        self,
        data: InvalidOutputLocation_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidOutputLocation",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidOutputLocation":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
