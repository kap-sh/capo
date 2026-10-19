"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionInstanceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.get_sol_function_instance_metadata
    import capo_tnb.types.get_sol_vnf_info
    import capo_tnb.types.ns_instance_id
    import capo_tnb.types.tag_map
    import capo_tnb.types.vnf_instance_arn
    import capo_tnb.types.vnf_instance_id
    import capo_tnb.types.vnf_instantiation_state
    import capo_tnb.types.vnf_pkg_id
    import capo_tnb.types.vnfd_id


class GetSolFunctionInstanceOutput(TypedDict, closed=True):
    id: "capo_tnb.types.vnf_instance_id.VnfInstanceId"
    """<p>Network function instance ID.</p>"""
    arn: "capo_tnb.types.vnf_instance_arn.VnfInstanceArn"
    """<p>Network function instance ARN.</p>"""
    ns_instance_id: "capo_tnb.types.ns_instance_id.NsInstanceId"
    """<p>Network instance ID.</p>"""
    vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>Function package ID.</p>"""
    vnfd_id: "capo_tnb.types.vnfd_id.VnfdId"
    """<p>Function package descriptor ID.</p>"""
    vnf_provider: NotRequired["str"]
    """<p>Network function provider.</p>"""
    vnf_product_name: NotRequired["str"]
    """<p>Network function product name.</p>"""
    vnfd_version: NotRequired["str"]
    """<p>Function package descriptor version.</p>"""
    instantiation_state: "capo_tnb.types.vnf_instantiation_state.VnfInstantiationState"
    """<p>Network function instantiation state.</p>"""
    instantiated_vnf_info: NotRequired["capo_tnb.types.get_sol_vnf_info.GetSolVnfInfo"]
    metadata: "capo_tnb.types.get_sol_function_instance_metadata.GetSolFunctionInstanceMetadata"
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionInstanceOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsInstanceId"] = value["ns_instance_id"]
    out["vnfPkgId"] = value["vnf_pkg_id"]
    out["vnfdId"] = value["vnfd_id"]
    if "vnf_provider" in value:
        out["vnfProvider"] = value["vnf_provider"]
    if "vnf_product_name" in value:
        out["vnfProductName"] = value["vnf_product_name"]
    if "vnfd_version" in value:
        out["vnfdVersion"] = value["vnfd_version"]
    import capo_tnb.types.vnf_instantiation_state

    out["instantiationState"] = capo_tnb.types.vnf_instantiation_state.serialize_json(
        value["instantiation_state"]
    )
    if "instantiated_vnf_info" in value:
        import capo_tnb.types.get_sol_vnf_info

        out["instantiatedVnfInfo"] = capo_tnb.types.get_sol_vnf_info.serialize_json(
            value["instantiated_vnf_info"]
        )
    import capo_tnb.types.get_sol_function_instance_metadata

    out["metadata"] = capo_tnb.types.get_sol_function_instance_metadata.serialize_json(
        value["metadata"]
    )
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSolFunctionInstanceOutput:
    out: GetSolFunctionInstanceOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("vnfdId") is not None:
        out["vnfd_id"] = data["vnfdId"]
    else:
        out["vnfd_id"] = ""
    if data.get("vnfProvider") is not None:
        out["vnf_provider"] = data["vnfProvider"]
    if data.get("vnfProductName") is not None:
        out["vnf_product_name"] = data["vnfProductName"]
    if data.get("vnfdVersion") is not None:
        out["vnfd_version"] = data["vnfdVersion"]
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
        import capo_tnb.types.get_sol_vnf_info

        out["instantiated_vnf_info"] = capo_tnb.types.get_sol_vnf_info.deserialize_json(
            data["instantiatedVnfInfo"]
        )
    if data.get("metadata") is not None:
        import capo_tnb.types.get_sol_function_instance_metadata

        out["metadata"] = (
            capo_tnb.types.get_sol_function_instance_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError("GetSolFunctionInstanceOutput.metadata required")
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: GetSolFunctionInstanceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
