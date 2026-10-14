"""Generated from Smithy shape ``com.amazonaws.dlm#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dlm.errors import ServiceError

if TYPE_CHECKING:
    import capo_dlm.types.error_code
    import capo_dlm.types.error_message
    import capo_dlm.types.policy_id_list
    import capo_dlm.types.string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_dlm.types.error_message.ErrorMessage"]
    code: NotRequired["capo_dlm.types.error_code.ErrorCode"]
    resource_type: NotRequired["capo_dlm.types.string.String"]
    """<p>Value is the type of resource that was not found.</p>"""
    resource_ids: NotRequired["capo_dlm.types.policy_id_list.PolicyIdList"]
    """<p>Value is a list of resource IDs that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_ids" in value:
        import capo_dlm.types.policy_id_list

        out["ResourceIds"] = capo_dlm.types.policy_id_list.serialize_json(
            value["resource_ids"]
        )
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("ResourceIds") is not None:
        import capo_dlm.types.policy_id_list

        out["resource_ids"] = capo_dlm.types.policy_id_list.deserialize_json(
            data["ResourceIds"]
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dlm#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(
        self,
        data: ResourceNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceNotFoundException":
        return cls(deserialize_json(data), message, response=response)
