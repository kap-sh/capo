"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#InvalidPaginationException``."""

import zapros
from typing_extensions import TypedDict

from capo_redshift_serverless.errors import ServiceError


class InvalidPaginationException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPaginationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPaginationException_:
    out: InvalidPaginationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class InvalidPaginationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftserverless#InvalidPaginationException``."""

    code: str | None = "InvalidPaginationException"

    def __init__(
        self,
        data: InvalidPaginationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPaginationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidPaginationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
