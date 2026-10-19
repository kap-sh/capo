"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkOperationsInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.lcm_operation_type
    import capo_tnb.types.list_sol_network_operations_metadata
    import capo_tnb.types.ns_instance_id
    import capo_tnb.types.ns_lcm_op_occ_arn
    import capo_tnb.types.ns_lcm_op_occ_id
    import capo_tnb.types.ns_lcm_operation_state
    import capo_tnb.types.problem_details
    import capo_tnb.types.update_sol_network_type


class ListSolNetworkOperationsInfo(TypedDict, closed=True):
    id: "capo_tnb.types.ns_lcm_op_occ_id.NsLcmOpOccId"
    """<p>ID of this network operation.</p>"""
    arn: "capo_tnb.types.ns_lcm_op_occ_arn.NsLcmOpOccArn"
    """<p>Network operation ARN.</p>"""
    operation_state: "capo_tnb.types.ns_lcm_operation_state.NsLcmOperationState"
    """<p>The state of the network operation.</p>"""
    ns_instance_id: "capo_tnb.types.ns_instance_id.NsInstanceId"
    """<p>ID of the network instance related to this operation.</p>"""
    lcm_operation_type: "capo_tnb.types.lcm_operation_type.LcmOperationType"
    """<p>Type of lifecycle management network operation.</p>"""
    update_type: NotRequired[
        "capo_tnb.types.update_sol_network_type.UpdateSolNetworkType"
    ]
    """<p>Type of the update. Only present if the network operation lcmOperationType is <code>UPDATE</code>.</p>"""
    error: NotRequired["capo_tnb.types.problem_details.ProblemDetails"]
    """<p>Error related to this specific network operation.</p>"""
    metadata: NotRequired[
        "capo_tnb.types.list_sol_network_operations_metadata.ListSolNetworkOperationsMetadata"
    ]
    """<p>Metadata related to this network operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkOperationsInfo) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import capo_tnb.types.ns_lcm_operation_state

    out["operationState"] = capo_tnb.types.ns_lcm_operation_state.serialize_json(
        value["operation_state"]
    )
    out["nsInstanceId"] = value["ns_instance_id"]
    import capo_tnb.types.lcm_operation_type

    out["lcmOperationType"] = capo_tnb.types.lcm_operation_type.serialize_json(
        value["lcm_operation_type"]
    )
    if "update_type" in value:
        import capo_tnb.types.update_sol_network_type

        out["updateType"] = capo_tnb.types.update_sol_network_type.serialize_json(
            value["update_type"]
        )
    if "error" in value:
        import capo_tnb.types.problem_details

        out["error"] = capo_tnb.types.problem_details.serialize_json(value["error"])
    if "metadata" in value:
        import capo_tnb.types.list_sol_network_operations_metadata

        out["metadata"] = (
            capo_tnb.types.list_sol_network_operations_metadata.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSolNetworkOperationsInfo:
    out: ListSolNetworkOperationsInfo = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("operationState") is not None:
        import capo_tnb.types.ns_lcm_operation_state

        out["operation_state"] = capo_tnb.types.ns_lcm_operation_state.deserialize_json(
            data["operationState"]
        )
    else:
        import typing

        out["operation_state"] = typing.cast(
            "capo_tnb.types.ns_lcm_operation_state.NsLcmOperationState", ""
        )
    if data.get("nsInstanceId") is not None:
        out["ns_instance_id"] = data["nsInstanceId"]
    else:
        out["ns_instance_id"] = ""
    if data.get("lcmOperationType") is not None:
        import capo_tnb.types.lcm_operation_type

        out["lcm_operation_type"] = capo_tnb.types.lcm_operation_type.deserialize_json(
            data["lcmOperationType"]
        )
    else:
        import typing

        out["lcm_operation_type"] = typing.cast(
            "capo_tnb.types.lcm_operation_type.LcmOperationType", ""
        )
    if data.get("updateType") is not None:
        import capo_tnb.types.update_sol_network_type

        out["update_type"] = capo_tnb.types.update_sol_network_type.deserialize_json(
            data["updateType"]
        )
    if data.get("error") is not None:
        import capo_tnb.types.problem_details

        out["error"] = capo_tnb.types.problem_details.deserialize_json(data["error"])
    if data.get("metadata") is not None:
        import capo_tnb.types.list_sol_network_operations_metadata

        out["metadata"] = (
            capo_tnb.types.list_sol_network_operations_metadata.deserialize_json(
                data["metadata"]
            )
        )
    return out
