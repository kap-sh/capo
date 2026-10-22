"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#VolumeModificationRateExceededException``."""

import zapros
from typing_extensions import TypedDict

from capo_workspaces_instances.errors import ServiceError


class VolumeModificationRateExceededException_(TypedDict, closed=True):
    message: "str"
    """<p>Specifies the reason that the modification request was rejected.</p>"""
    resource_id: "str"
    """<p>Specifies the identifier of the volume for which the modification request was rejected.</p>"""
    resource_type: "str"
    """<p>Specifies the type of the resource for which the modification request was rejected.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VolumeModificationRateExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VolumeModificationRateExceededException_:
    out: VolumeModificationRateExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    return out


class VolumeModificationRateExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesinstances#VolumeModificationRateExceededException``."""

    code: str | None = "VolumeModificationRateExceededException"

    def __init__(
        self,
        data: VolumeModificationRateExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="VolumeModificationRateExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "VolumeModificationRateExceededException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
