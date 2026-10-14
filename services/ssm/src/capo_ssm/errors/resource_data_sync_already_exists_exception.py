"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.resource_data_sync_name


class ResourceDataSyncAlreadyExistsException_(TypedDict, closed=True):
    sync_name: NotRequired[
        "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncAlreadyExistsException_) -> dict:
    out: dict = {}
    if "sync_name" in value:
        out["SyncName"] = value["sync_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncAlreadyExistsException_:
    out: ResourceDataSyncAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("SyncName") is not None:
        out["sync_name"] = data["SyncName"]
    return out


class ResourceDataSyncAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ResourceDataSyncAlreadyExistsException``."""

    code: str | None = "ResourceDataSyncAlreadyExistsException"

    def __init__(
        self,
        data: ResourceDataSyncAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceDataSyncAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceDataSyncAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
