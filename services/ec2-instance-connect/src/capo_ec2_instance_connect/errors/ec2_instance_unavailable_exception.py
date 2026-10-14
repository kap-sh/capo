"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#EC2InstanceUnavailableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ec2_instance_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_ec2_instance_connect.types.string


class EC2InstanceUnavailableException_(TypedDict, closed=True):
    message: NotRequired["capo_ec2_instance_connect.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2InstanceUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2InstanceUnavailableException_:
    out: EC2InstanceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class EC2InstanceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ec2instanceconnect#EC2InstanceUnavailableException``."""

    code: str | None = "EC2InstanceUnavailableException"

    def __init__(
        self,
        data: EC2InstanceUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="EC2InstanceUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "EC2InstanceUnavailableException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
