"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#SerialConsoleSessionUnsupportedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ec2_instance_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_ec2_instance_connect.types.string


class SerialConsoleSessionUnsupportedException_(TypedDict, closed=True):
    message: NotRequired["capo_ec2_instance_connect.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SerialConsoleSessionUnsupportedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SerialConsoleSessionUnsupportedException_:
    out: SerialConsoleSessionUnsupportedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class SerialConsoleSessionUnsupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ec2instanceconnect#SerialConsoleSessionUnsupportedException``."""

    code: str | None = "SerialConsoleSessionUnsupportedException"

    def __init__(
        self,
        data: SerialConsoleSessionUnsupportedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SerialConsoleSessionUnsupportedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SerialConsoleSessionUnsupportedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
