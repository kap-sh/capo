"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#SerialConsoleSessionUnavailableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ec2_instance_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_ec2_instance_connect.types.string


class SerialConsoleSessionUnavailableException_(TypedDict, closed=True):
    message: NotRequired["capo_ec2_instance_connect.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SerialConsoleSessionUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SerialConsoleSessionUnavailableException_:
    out: SerialConsoleSessionUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class SerialConsoleSessionUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ec2instanceconnect#SerialConsoleSessionUnavailableException``."""

    code: str | None = "SerialConsoleSessionUnavailableException"

    def __init__(
        self,
        data: SerialConsoleSessionUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="SerialConsoleSessionUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SerialConsoleSessionUnavailableException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
