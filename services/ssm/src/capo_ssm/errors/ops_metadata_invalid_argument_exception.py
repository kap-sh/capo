"""Generated from Smithy shape ``com.amazonaws.ssm#OpsMetadataInvalidArgumentException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class OpsMetadataInvalidArgumentException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsMetadataInvalidArgumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsMetadataInvalidArgumentException_:
    out: OpsMetadataInvalidArgumentException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class OpsMetadataInvalidArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsMetadataInvalidArgumentException``."""

    code: str | None = "OpsMetadataInvalidArgumentException"

    def __init__(
        self,
        data: OpsMetadataInvalidArgumentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsMetadataInvalidArgumentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OpsMetadataInvalidArgumentException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
