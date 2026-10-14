"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#SerialConsoleSessionLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ec2_instance_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_ec2_instance_connect.types.string


class SerialConsoleSessionLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_ec2_instance_connect.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SerialConsoleSessionLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SerialConsoleSessionLimitExceededException_:
    out: SerialConsoleSessionLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class SerialConsoleSessionLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ec2instanceconnect#SerialConsoleSessionLimitExceededException``."""

    code: str | None = "SerialConsoleSessionLimitExceededException"

    def __init__(
        self,
        data: SerialConsoleSessionLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SerialConsoleSessionLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SerialConsoleSessionLimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
