"""Generated from Smithy shape ``com.amazonaws.tnb#CreateSolNetworkInstanceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.ns_instance_arn
    import capo_tnb.types.ns_instance_id
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.tag_map


class CreateSolNetworkInstanceOutput(TypedDict, closed=True):
    id: "capo_tnb.types.ns_instance_id.NsInstanceId"
    """<p>Network instance ID.</p>"""
    arn: "capo_tnb.types.ns_instance_arn.NsInstanceArn"
    """<p>Network instance ARN.</p>"""
    nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>Network service descriptor ID.</p>"""
    ns_instance_name: "str"
    """<p>Network instance name.</p>"""
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSolNetworkInstanceOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsdInfoId"] = value["nsd_info_id"]
    out["nsInstanceName"] = value["ns_instance_name"]
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSolNetworkInstanceOutput:
    out: CreateSolNetworkInstanceOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("nsdInfoId") is not None:
        out["nsd_info_id"] = data["nsdInfoId"]
    else:
        out["nsd_info_id"] = ""
    if data.get("nsInstanceName") is not None:
        out["ns_instance_name"] = data["nsInstanceName"]
    else:
        out["ns_instance_name"] = ""
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateSolNetworkInstanceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
