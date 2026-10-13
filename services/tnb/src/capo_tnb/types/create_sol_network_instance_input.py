"""Generated from Smithy shape ``com.amazonaws.tnb#CreateSolNetworkInstanceInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.tag_map


class CreateSolNetworkInstanceInput(TypedDict, closed=True):
    nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID for network service descriptor.</p>"""
    ns_name: "str"
    """<p>Network instance name.</p>"""
    ns_description: NotRequired["str"]
    """<p>Network instance description.</p>"""
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSolNetworkInstanceInput) -> dict:
    out: dict = {}
    out["nsdInfoId"] = value["nsd_info_id"]
    out["nsName"] = value["ns_name"]
    if "ns_description" in value:
        out["nsDescription"] = value["ns_description"]
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSolNetworkInstanceInput:
    out: CreateSolNetworkInstanceInput = {}  # type: ignore[typeddict-item]
    if data.get("nsdInfoId") is not None:
        out["nsd_info_id"] = data["nsdInfoId"]
    else:
        raise DeserializationError("CreateSolNetworkInstanceInput.nsd_info_id required")
    if data.get("nsName") is not None:
        out["ns_name"] = data["nsName"]
    else:
        raise DeserializationError("CreateSolNetworkInstanceInput.ns_name required")
    if data.get("nsDescription") is not None:
        out["ns_description"] = data["nsDescription"]
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateSolNetworkInstanceInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
