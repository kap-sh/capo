"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncInvalidConfigurationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class ResourceDataSyncInvalidConfigurationException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ResourceDataSyncInvalidConfigurationException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ResourceDataSyncInvalidConfigurationException_:
    out: ResourceDataSyncInvalidConfigurationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ResourceDataSyncInvalidConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ResourceDataSyncInvalidConfigurationException``."""

    code: str | None = "ResourceDataSyncInvalidConfigurationException"

    def __init__(
        self,
        data: ResourceDataSyncInvalidConfigurationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceDataSyncInvalidConfigurationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceDataSyncInvalidConfigurationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
