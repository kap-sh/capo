"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolNetworkInstanceInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.ns_instance_id
    import capo_tnb.types.tag_map
    import capo_tnb.types.update_sol_network_modify
    import capo_tnb.types.update_sol_network_service_data
    import capo_tnb.types.update_sol_network_type


class UpdateSolNetworkInstanceInput(TypedDict, closed=True):
    ns_instance_id: "capo_tnb.types.ns_instance_id.NsInstanceId"
    """<p>ID of the network instance.</p>"""
    update_type: "capo_tnb.types.update_sol_network_type.UpdateSolNetworkType"
    """<p>The type of update.</p> <ul> <li> <p>Use the <code>MODIFY_VNF_INFORMATION</code> update type, to update a specific network function configuration, in the network instance.</p> </li> <li> <p>Use the <code>UPDATE_NS</code> update type, to update the network instance to a new network service descriptor.</p> </li> </ul>"""
    modify_vnf_info_data: NotRequired[
        "capo_tnb.types.update_sol_network_modify.UpdateSolNetworkModify"
    ]
    """<p>Identifies the network function information parameters and/or the configurable properties of the network function to be modified.</p> <p>Include this property only if the update type is <code>MODIFY_VNF_INFORMATION</code>.</p>"""
    update_ns: NotRequired[
        "capo_tnb.types.update_sol_network_service_data.UpdateSolNetworkServiceData"
    ]
    """<p>Identifies the network service descriptor and the configurable properties of the descriptor, to be used for the update.</p> <p>Include this property only if the update type is <code>UPDATE_NS</code>.</p>"""
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. When you use this API, the tags are only applied to the network operation that is created. These tags are not applied to the network instance. Use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolNetworkInstanceInput) -> dict:
    out: dict = {}
    import capo_tnb.types.update_sol_network_type

    out["updateType"] = capo_tnb.types.update_sol_network_type.serialize_json(
        value["update_type"]
    )
    if "modify_vnf_info_data" in value:
        import capo_tnb.types.update_sol_network_modify

        out["modifyVnfInfoData"] = (
            capo_tnb.types.update_sol_network_modify.serialize_json(
                value["modify_vnf_info_data"]
            )
        )
    if "update_ns" in value:
        import capo_tnb.types.update_sol_network_service_data

        out["updateNs"] = capo_tnb.types.update_sol_network_service_data.serialize_json(
            value["update_ns"]
        )
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateSolNetworkInstanceInput:
    out: UpdateSolNetworkInstanceInput = {}  # type: ignore[typeddict-item]
    if data.get("updateType") is not None:
        import capo_tnb.types.update_sol_network_type

        out["update_type"] = capo_tnb.types.update_sol_network_type.deserialize_json(
            data["updateType"]
        )
    else:
        import typing

        out["update_type"] = typing.cast(
            "capo_tnb.types.update_sol_network_type.UpdateSolNetworkType", ""
        )
    if data.get("modifyVnfInfoData") is not None:
        import capo_tnb.types.update_sol_network_modify

        out["modify_vnf_info_data"] = (
            capo_tnb.types.update_sol_network_modify.deserialize_json(
                data["modifyVnfInfoData"]
            )
        )
    if data.get("updateNs") is not None:
        import capo_tnb.types.update_sol_network_service_data

        out["update_ns"] = (
            capo_tnb.types.update_sol_network_service_data.deserialize_json(
                data["updateNs"]
            )
        )
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: UpdateSolNetworkInstanceInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
