"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkInstanceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.list_sol_network_instance_metadata
    import capo_tnb.types.ns_instance_arn
    import capo_tnb.types.ns_instance_id
    import capo_tnb.types.ns_state
    import capo_tnb.types.nsd_id
    import capo_tnb.types.nsd_info_id


class ListSolNetworkInstanceInfo(TypedDict, closed=True):
    id: "capo_tnb.types.ns_instance_id.NsInstanceId"
    """<p>ID of the network instance.</p>"""
    arn: "capo_tnb.types.ns_instance_arn.NsInstanceArn"
    """<p>Network instance ARN.</p>"""
    ns_instance_name: "str"
    """<p>Human-readable name of the network instance.</p>"""
    ns_instance_description: "str"
    """<p>Human-readable description of the network instance.</p>"""
    nsd_id: "capo_tnb.types.nsd_id.NsdId"
    """<p>ID of the network service descriptor in the network package.</p>"""
    nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network service descriptor in the network package.</p>"""
    ns_state: "capo_tnb.types.ns_state.NsState"
    """<p>The state of the network instance.</p>"""
    metadata: "capo_tnb.types.list_sol_network_instance_metadata.ListSolNetworkInstanceMetadata"
    """<p>The metadata of the network instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkInstanceInfo) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsInstanceName"] = value["ns_instance_name"]
    out["nsInstanceDescription"] = value["ns_instance_description"]
    out["nsdId"] = value["nsd_id"]
    out["nsdInfoId"] = value["nsd_info_id"]
    import capo_tnb.types.ns_state

    out["nsState"] = capo_tnb.types.ns_state.serialize_json(value["ns_state"])
    import capo_tnb.types.list_sol_network_instance_metadata

    out["metadata"] = capo_tnb.types.list_sol_network_instance_metadata.serialize_json(
        value["metadata"]
    )
    return out


def deserialize_json(data: dict) -> ListSolNetworkInstanceInfo:
    out: ListSolNetworkInstanceInfo = {}  # type: ignore[typeddict-item]
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
    else:
        import typing

        out["ns_state"] = typing.cast("capo_tnb.types.ns_state.NsState", "")
    if data.get("metadata") is not None:
        import capo_tnb.types.list_sol_network_instance_metadata

        out["metadata"] = (
            capo_tnb.types.list_sol_network_instance_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError("ListSolNetworkInstanceInfo.metadata required")
    return out
