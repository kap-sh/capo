"""Generated from Smithy shape ``com.amazonaws.tnb#InstantiateSolNetworkInstanceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.ns_lcm_op_occ_id
    import capo_tnb.types.tag_map


class InstantiateSolNetworkInstanceOutput(TypedDict, closed=True):
    ns_lcm_op_occ_id: "capo_tnb.types.ns_lcm_op_occ_id.NsLcmOpOccId"
    """<p>The identifier of the network operation.</p>"""
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. When you use this API, the tags are only applied to the network operation that is created. These tags are not applied to the network instance. Use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstantiateSolNetworkInstanceOutput) -> dict:
    out: dict = {}
    out["nsLcmOpOccId"] = value["ns_lcm_op_occ_id"]
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> InstantiateSolNetworkInstanceOutput:
    out: InstantiateSolNetworkInstanceOutput = {}  # type: ignore[typeddict-item]
    if data.get("nsLcmOpOccId") is not None:
        out["ns_lcm_op_occ_id"] = data["nsLcmOpOccId"]
    else:
        out["ns_lcm_op_occ_id"] = ""
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: InstantiateSolNetworkInstanceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
