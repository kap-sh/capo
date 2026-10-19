"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolFunctionInstanceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.get_sol_instantiated_vnf_info
    import capo_tnb.types.list_sol_function_instance_metadata
    import capo_tnb.types.ns_instance_id
    import capo_tnb.types.vnf_instance_arn
    import capo_tnb.types.vnf_instance_id
    import capo_tnb.types.vnf_instantiation_state
    import capo_tnb.types.vnf_pkg_id


class ListSolFunctionInstanceInfo(TypedDict, closed=True):
    id: "capo_tnb.types.vnf_instance_id.VnfInstanceId"
    """<p>Network function instance ID.</p>"""
    arn: "capo_tnb.types.vnf_instance_arn.VnfInstanceArn"
    """<p>Network function instance ARN.</p>"""
    ns_instance_id: "capo_tnb.types.ns_instance_id.NsInstanceId"
    """<p>Network instance ID.</p>"""
    vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>Function package ID.</p>"""
    vnf_pkg_name: NotRequired["str"]
    """<p>Function package name.</p>"""
    instantiation_state: "capo_tnb.types.vnf_instantiation_state.VnfInstantiationState"
    """<p>Network function instance instantiation state.</p>"""
    instantiated_vnf_info: NotRequired[
        "capo_tnb.types.get_sol_instantiated_vnf_info.GetSolInstantiatedVnfInfo"
    ]
    metadata: "capo_tnb.types.list_sol_function_instance_metadata.ListSolFunctionInstanceMetadata"
    """<p>Network function instance metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolFunctionInstanceInfo) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsInstanceId"] = value["ns_instance_id"]
    out["vnfPkgId"] = value["vnf_pkg_id"]
    if "vnf_pkg_name" in value:
        out["vnfPkgName"] = value["vnf_pkg_name"]
    import capo_tnb.types.vnf_instantiation_state

    out["instantiationState"] = capo_tnb.types.vnf_instantiation_state.serialize_json(
        value["instantiation_state"]
    )
    if "instantiated_vnf_info" in value:
        import capo_tnb.types.get_sol_instantiated_vnf_info

        out["instantiatedVnfInfo"] = (
            capo_tnb.types.get_sol_instantiated_vnf_info.serialize_json(
                value["instantiated_vnf_info"]
            )
        )
    import capo_tnb.types.list_sol_function_instance_metadata

    out["metadata"] = capo_tnb.types.list_sol_function_instance_metadata.serialize_json(
        value["metadata"]
    )
    return out


def deserialize_json(data: dict) -> ListSolFunctionInstanceInfo:
    out: ListSolFunctionInstanceInfo = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("nsInstanceId") is not None:
        out["ns_instance_id"] = data["nsInstanceId"]
    else:
        out["ns_instance_id"] = ""
    if data.get("vnfPkgId") is not None:
        out["vnf_pkg_id"] = data["vnfPkgId"]
    else:
        out["vnf_pkg_id"] = ""
    if data.get("vnfPkgName") is not None:
        out["vnf_pkg_name"] = data["vnfPkgName"]
    if data.get("instantiationState") is not None:
        import capo_tnb.types.vnf_instantiation_state

        out["instantiation_state"] = (
            capo_tnb.types.vnf_instantiation_state.deserialize_json(
                data["instantiationState"]
            )
        )
    else:
        import typing

        out["instantiation_state"] = typing.cast(
            "capo_tnb.types.vnf_instantiation_state.VnfInstantiationState", ""
        )
    if data.get("instantiatedVnfInfo") is not None:
        import capo_tnb.types.get_sol_instantiated_vnf_info

        out["instantiated_vnf_info"] = (
            capo_tnb.types.get_sol_instantiated_vnf_info.deserialize_json(
                data["instantiatedVnfInfo"]
            )
        )
    if data.get("metadata") is not None:
        import capo_tnb.types.list_sol_function_instance_metadata

        out["metadata"] = (
            capo_tnb.types.list_sol_function_instance_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError("ListSolFunctionInstanceInfo.metadata required")
    return out
