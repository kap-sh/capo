"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.resource_data_sync_name
    import capo_ssm.types.resource_data_sync_type
    import capo_ssm.types.string


class ResourceDataSyncNotFoundException_(TypedDict, closed=True):
    sync_name: NotRequired[
        "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    ]
    sync_type: NotRequired[
        "capo_ssm.types.resource_data_sync_type.ResourceDataSyncType"
    ]
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncNotFoundException_) -> dict:
    out: dict = {}
    if "sync_name" in value:
        out["SyncName"] = value["sync_name"]
    if "sync_type" in value:
        out["SyncType"] = value["sync_type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncNotFoundException_:
    out: ResourceDataSyncNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("SyncName") is not None:
        out["sync_name"] = data["SyncName"]
    if data.get("SyncType") is not None:
        out["sync_type"] = data["SyncType"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ResourceDataSyncNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ResourceDataSyncNotFoundException``."""

    code: str | None = "ResourceDataSyncNotFoundException"

    def __init__(
        self,
        data: ResourceDataSyncNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceDataSyncNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceDataSyncNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
