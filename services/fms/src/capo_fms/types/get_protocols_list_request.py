"""Generated from Smithy shape ``com.amazonaws.fms#GetProtocolsListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.list_id


class GetProtocolsListRequest(TypedDict, closed=True):
    list_id: "capo_fms.types.list_id.ListId"
    """<p>The ID of the Firewall Manager protocols list that you want the details for.</p>"""
    default_list: NotRequired["capo_fms.types.boolean.Boolean"]
    """<p>Specifies whether the list to retrieve is a default list owned by Firewall Manager.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProtocolsListRequest) -> dict:
    out: dict = {}
    out["ListId"] = value["list_id"]
    if "default_list" in value:
        out["DefaultList"] = value["default_list"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProtocolsListRequest:
    out: GetProtocolsListRequest = {}  # type: ignore[typeddict-item]
    if data.get("ListId") is not None:
        out["list_id"] = data["ListId"]
    else:
        out["list_id"] = ""
    if data.get("DefaultList") is not None:
        out["default_list"] = data["DefaultList"]
    return out
