"""Generated from Smithy shape ``com.amazonaws.ssm#InvocationDoesNotExist``."""

import zapros
from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class InvocationDoesNotExist_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvocationDoesNotExist_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> InvocationDoesNotExist_:
    out: InvocationDoesNotExist_ = {}  # type: ignore[typeddict-item]
    return out


class InvocationDoesNotExist(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvocationDoesNotExist``."""

    code: str | None = "InvocationDoesNotExist"

    def __init__(
        self,
        data: InvocationDoesNotExist_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvocationDoesNotExist",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvocationDoesNotExist":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
