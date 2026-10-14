"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#InsufficientCapacityException``."""

import zapros
from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError, ServiceError


class InsufficientCapacityException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsufficientCapacityException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InsufficientCapacityException_:
    out: InsufficientCapacityException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InsufficientCapacityException_.message required")
    return out


class InsufficientCapacityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftserverless#InsufficientCapacityException``."""

    code: str | None = "InsufficientCapacityException"

    def __init__(
        self,
        data: InsufficientCapacityException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="InsufficientCapacityException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InsufficientCapacityException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
