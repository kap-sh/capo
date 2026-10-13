"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkOperationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.get_sol_network_operation_metadata
    import capo_tnb.types.get_sol_network_operation_tasks_list
    import capo_tnb.types.lcm_operation_type
    import capo_tnb.types.ns_instance_id
    import capo_tnb.types.ns_lcm_op_occ_arn
    import capo_tnb.types.ns_lcm_op_occ_id
    import capo_tnb.types.ns_lcm_operation_state
    import capo_tnb.types.problem_details
    import capo_tnb.types.tag_map
    import capo_tnb.types.update_sol_network_type


class GetSolNetworkOperationOutput(TypedDict, closed=True):
    id: NotRequired["capo_tnb.types.ns_lcm_op_occ_id.NsLcmOpOccId"]
    """<p>ID of this network operation occurrence.</p>"""
    arn: "capo_tnb.types.ns_lcm_op_occ_arn.NsLcmOpOccArn"
    """<p>Network operation ARN.</p>"""
    operation_state: NotRequired[
        "capo_tnb.types.ns_lcm_operation_state.NsLcmOperationState"
    ]
    """<p>The state of the network operation.</p>"""
    ns_instance_id: NotRequired["capo_tnb.types.ns_instance_id.NsInstanceId"]
    """<p>ID of the network operation instance.</p>"""
    lcm_operation_type: NotRequired[
        "capo_tnb.types.lcm_operation_type.LcmOperationType"
    ]
    """<p>Type of the operation represented by this occurrence.</p>"""
    update_type: NotRequired[
        "capo_tnb.types.update_sol_network_type.UpdateSolNetworkType"
    ]
    """<p>Type of the update. Only present if the network operation lcmOperationType is <code>UPDATE</code>.</p>"""
    error: NotRequired["capo_tnb.types.problem_details.ProblemDetails"]
    """<p>Error related to this specific network operation occurrence.</p>"""
    metadata: NotRequired[
        "capo_tnb.types.get_sol_network_operation_metadata.GetSolNetworkOperationMetadata"
    ]
    """<p>Metadata of this network operation occurrence.</p>"""
    tasks: NotRequired[
        "capo_tnb.types.get_sol_network_operation_tasks_list.GetSolNetworkOperationTasksList"
    ]
    """<p>All tasks associated with this operation occurrence.</p>"""
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkOperationOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "operation_state" in value:
        import capo_tnb.types.ns_lcm_operation_state

        out["operationState"] = capo_tnb.types.ns_lcm_operation_state.serialize_json(
            value["operation_state"]
        )
    if "ns_instance_id" in value:
        out["nsInstanceId"] = value["ns_instance_id"]
    if "lcm_operation_type" in value:
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
        import capo_tnb.types.get_sol_network_operation_metadata

        out["metadata"] = (
            capo_tnb.types.get_sol_network_operation_metadata.serialize_json(
                value["metadata"]
            )
        )
    if "tasks" in value:
        import capo_tnb.types.get_sol_network_operation_tasks_list

        out["tasks"] = (
            capo_tnb.types.get_sol_network_operation_tasks_list.serialize_json(
                value["tasks"]
            )
        )
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSolNetworkOperationOutput:
    out: GetSolNetworkOperationOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetSolNetworkOperationOutput.arn required")
    if data.get("operationState") is not None:
        import capo_tnb.types.ns_lcm_operation_state

        out["operation_state"] = capo_tnb.types.ns_lcm_operation_state.deserialize_json(
            data["operationState"]
        )
    if data.get("nsInstanceId") is not None:
        out["ns_instance_id"] = data["nsInstanceId"]
    if data.get("lcmOperationType") is not None:
        import capo_tnb.types.lcm_operation_type

        out["lcm_operation_type"] = capo_tnb.types.lcm_operation_type.deserialize_json(
            data["lcmOperationType"]
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
        import capo_tnb.types.get_sol_network_operation_metadata

        out["metadata"] = (
            capo_tnb.types.get_sol_network_operation_metadata.deserialize_json(
                data["metadata"]
            )
        )
    if data.get("tasks") is not None:
        import capo_tnb.types.get_sol_network_operation_tasks_list

        out["tasks"] = (
            capo_tnb.types.get_sol_network_operation_tasks_list.deserialize_json(
                data["tasks"]
            )
        )
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: GetSolNetworkOperationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
