"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkInstanceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.get_sol_network_instance_metadata
    import capo_tnb.types.lcm_operation_info
    import capo_tnb.types.ns_instance_arn
    import capo_tnb.types.ns_instance_id
    import capo_tnb.types.ns_state
    import capo_tnb.types.nsd_id
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.tag_map


class GetSolNetworkInstanceOutput(TypedDict, closed=True):
    id: "capo_tnb.types.ns_instance_id.NsInstanceId"
    """<p>Network instance ID.</p>"""
    arn: "capo_tnb.types.ns_instance_arn.NsInstanceArn"
    """<p>Network instance ARN.</p>"""
    ns_instance_name: "str"
    """<p>Network instance name.</p>"""
    ns_instance_description: "str"
    """<p>Network instance description.</p>"""
    nsd_id: "capo_tnb.types.nsd_id.NsdId"
    """<p>Network service descriptor ID.</p>"""
    nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>Network service descriptor info ID.</p>"""
    ns_state: NotRequired["capo_tnb.types.ns_state.NsState"]
    """<p>Network instance state.</p>"""
    lcm_op_info: NotRequired["capo_tnb.types.lcm_operation_info.LcmOperationInfo"]
    metadata: (
        "capo_tnb.types.get_sol_network_instance_metadata.GetSolNetworkInstanceMetadata"
    )
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkInstanceOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsInstanceName"] = value["ns_instance_name"]
    out["nsInstanceDescription"] = value["ns_instance_description"]
    out["nsdId"] = value["nsd_id"]
    out["nsdInfoId"] = value["nsd_info_id"]
    if "ns_state" in value:
        import capo_tnb.types.ns_state

        out["nsState"] = capo_tnb.types.ns_state.serialize_json(value["ns_state"])
    if "lcm_op_info" in value:
        import capo_tnb.types.lcm_operation_info

        out["lcmOpInfo"] = capo_tnb.types.lcm_operation_info.serialize_json(
            value["lcm_op_info"]
        )
    import capo_tnb.types.get_sol_network_instance_metadata

    out["metadata"] = capo_tnb.types.get_sol_network_instance_metadata.serialize_json(
        value["metadata"]
    )
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSolNetworkInstanceOutput:
    out: GetSolNetworkInstanceOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("nsInstanceName") is not None:
        out["ns_instance_name"] = data["nsInstanceName"]
    else:
        out["ns_instance_name"] = ""
    if data.get("nsInstanceDescription") is not None:
        out["ns_instance_description"] = data["nsInstanceDescription"]
    else:
        out["ns_instance_description"] = ""
    if data.get("nsdId") is not None:
        out["nsd_id"] = data["nsdId"]
    else:
        out["nsd_id"] = ""
    if data.get("nsdInfoId") is not None:
        out["nsd_info_id"] = data["nsdInfoId"]
    else:
        out["nsd_info_id"] = ""
    if data.get("nsState") is not None:
        import capo_tnb.types.ns_state

        out["ns_state"] = capo_tnb.types.ns_state.deserialize_json(data["nsState"])
    if data.get("lcmOpInfo") is not None:
        import capo_tnb.types.lcm_operation_info

        out["lcm_op_info"] = capo_tnb.types.lcm_operation_info.deserialize_json(
            data["lcmOpInfo"]
        )
    if data.get("metadata") is not None:
        import capo_tnb.types.get_sol_network_instance_metadata

        out["metadata"] = (
            capo_tnb.types.get_sol_network_instance_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError("GetSolNetworkInstanceOutput.metadata required")
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: GetSolNetworkInstanceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
