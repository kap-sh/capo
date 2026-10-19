"""Generated from Smithy shape ``com.amazonaws.fms#GetAppsListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.list_id


class GetAppsListRequest(TypedDict, closed=True):
    list_id: "capo_fms.types.list_id.ListId"
    """<p>The ID of the Firewall Manager applications list that you want the details for.</p>"""
    default_list: NotRequired["capo_fms.types.boolean.Boolean"]
    """<p>Specifies whether the list to retrieve is a default list owned by Firewall Manager.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAppsListRequest) -> dict:
    out: dict = {}
    out["ListId"] = value["list_id"]
    if "default_list" in value:
        out["DefaultList"] = value["default_list"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAppsListRequest:
    out: GetAppsListRequest = {}  # type: ignore[typeddict-item]
    if data.get("ListId") is not None:
        out["list_id"] = data["ListId"]
    else:
        raise DeserializationError("GetAppsListRequest.list_id required")
    if data.get("DefaultList") is not None:
        out["default_list"] = data["DefaultList"]
    return out
