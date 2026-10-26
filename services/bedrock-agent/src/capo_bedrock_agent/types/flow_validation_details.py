"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowValidationDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.cyclic_connection_flow_validation_details
    import capo_bedrock_agent.types.duplicate_condition_expression_flow_validation_details
    import capo_bedrock_agent.types.duplicate_connections_flow_validation_details
    import capo_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details
    import capo_bedrock_agent.types.invalid_loop_boundary_flow_validation_details
    import capo_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details
    import capo_bedrock_agent.types.malformed_condition_expression_flow_validation_details
    import capo_bedrock_agent.types.malformed_node_input_expression_flow_validation_details
    import capo_bedrock_agent.types.mismatched_node_input_type_flow_validation_details
    import capo_bedrock_agent.types.mismatched_node_output_type_flow_validation_details
    import capo_bedrock_agent.types.missing_connection_configuration_flow_validation_details
    import capo_bedrock_agent.types.missing_default_condition_flow_validation_details
    import capo_bedrock_agent.types.missing_ending_nodes_flow_validation_details
    import capo_bedrock_agent.types.missing_loop_controller_node_flow_validation_details
    import capo_bedrock_agent.types.missing_loop_input_node_flow_validation_details
    import capo_bedrock_agent.types.missing_node_configuration_flow_validation_details
    import capo_bedrock_agent.types.missing_node_input_flow_validation_details
    import capo_bedrock_agent.types.missing_node_output_flow_validation_details
    import capo_bedrock_agent.types.missing_starting_nodes_flow_validation_details
    import capo_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details
    import capo_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details
    import capo_bedrock_agent.types.multiple_node_input_connections_flow_validation_details
    import capo_bedrock_agent.types.unfulfilled_node_input_flow_validation_details
    import capo_bedrock_agent.types.unknown_connection_condition_flow_validation_details
    import capo_bedrock_agent.types.unknown_connection_source_flow_validation_details
    import capo_bedrock_agent.types.unknown_connection_source_output_flow_validation_details
    import capo_bedrock_agent.types.unknown_connection_target_flow_validation_details
    import capo_bedrock_agent.types.unknown_connection_target_input_flow_validation_details
    import capo_bedrock_agent.types.unknown_node_input_flow_validation_details
    import capo_bedrock_agent.types.unknown_node_output_flow_validation_details
    import capo_bedrock_agent.types.unreachable_node_flow_validation_details
    import capo_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details
    import capo_bedrock_agent.types.unspecified_flow_validation_details


class _FlowValidationDetails_cyclicConnection(TypedDict, closed=True):
    cyclicConnection: "capo_bedrock_agent.types.cyclic_connection_flow_validation_details.CyclicConnectionFlowValidationDetails"


class _FlowValidationDetails_duplicateConnections(TypedDict, closed=True):
    duplicateConnections: "capo_bedrock_agent.types.duplicate_connections_flow_validation_details.DuplicateConnectionsFlowValidationDetails"


class _FlowValidationDetails_duplicateConditionExpression(TypedDict, closed=True):
    duplicateConditionExpression: "capo_bedrock_agent.types.duplicate_condition_expression_flow_validation_details.DuplicateConditionExpressionFlowValidationDetails"


class _FlowValidationDetails_unreachableNode(TypedDict, closed=True):
    unreachableNode: "capo_bedrock_agent.types.unreachable_node_flow_validation_details.UnreachableNodeFlowValidationDetails"


class _FlowValidationDetails_unknownConnectionSource(TypedDict, closed=True):
    unknownConnectionSource: "capo_bedrock_agent.types.unknown_connection_source_flow_validation_details.UnknownConnectionSourceFlowValidationDetails"


class _FlowValidationDetails_unknownConnectionSourceOutput(TypedDict, closed=True):
    unknownConnectionSourceOutput: "capo_bedrock_agent.types.unknown_connection_source_output_flow_validation_details.UnknownConnectionSourceOutputFlowValidationDetails"


class _FlowValidationDetails_unknownConnectionTarget(TypedDict, closed=True):
    unknownConnectionTarget: "capo_bedrock_agent.types.unknown_connection_target_flow_validation_details.UnknownConnectionTargetFlowValidationDetails"


class _FlowValidationDetails_unknownConnectionTargetInput(TypedDict, closed=True):
    unknownConnectionTargetInput: "capo_bedrock_agent.types.unknown_connection_target_input_flow_validation_details.UnknownConnectionTargetInputFlowValidationDetails"


class _FlowValidationDetails_unknownConnectionCondition(TypedDict, closed=True):
    unknownConnectionCondition: "capo_bedrock_agent.types.unknown_connection_condition_flow_validation_details.UnknownConnectionConditionFlowValidationDetails"


class _FlowValidationDetails_malformedConditionExpression(TypedDict, closed=True):
    malformedConditionExpression: "capo_bedrock_agent.types.malformed_condition_expression_flow_validation_details.MalformedConditionExpressionFlowValidationDetails"


class _FlowValidationDetails_malformedNodeInputExpression(TypedDict, closed=True):
    malformedNodeInputExpression: "capo_bedrock_agent.types.malformed_node_input_expression_flow_validation_details.MalformedNodeInputExpressionFlowValidationDetails"


class _FlowValidationDetails_mismatchedNodeInputType(TypedDict, closed=True):
    mismatchedNodeInputType: "capo_bedrock_agent.types.mismatched_node_input_type_flow_validation_details.MismatchedNodeInputTypeFlowValidationDetails"


class _FlowValidationDetails_mismatchedNodeOutputType(TypedDict, closed=True):
    mismatchedNodeOutputType: "capo_bedrock_agent.types.mismatched_node_output_type_flow_validation_details.MismatchedNodeOutputTypeFlowValidationDetails"


class _FlowValidationDetails_incompatibleConnectionDataType(TypedDict, closed=True):
    incompatibleConnectionDataType: "capo_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details.IncompatibleConnectionDataTypeFlowValidationDetails"


class _FlowValidationDetails_missingConnectionConfiguration(TypedDict, closed=True):
    missingConnectionConfiguration: "capo_bedrock_agent.types.missing_connection_configuration_flow_validation_details.MissingConnectionConfigurationFlowValidationDetails"


class _FlowValidationDetails_missingDefaultCondition(TypedDict, closed=True):
    missingDefaultCondition: "capo_bedrock_agent.types.missing_default_condition_flow_validation_details.MissingDefaultConditionFlowValidationDetails"


class _FlowValidationDetails_missingEndingNodes(TypedDict, closed=True):
    missingEndingNodes: "capo_bedrock_agent.types.missing_ending_nodes_flow_validation_details.MissingEndingNodesFlowValidationDetails"


class _FlowValidationDetails_missingNodeConfiguration(TypedDict, closed=True):
    missingNodeConfiguration: "capo_bedrock_agent.types.missing_node_configuration_flow_validation_details.MissingNodeConfigurationFlowValidationDetails"


class _FlowValidationDetails_missingNodeInput(TypedDict, closed=True):
    missingNodeInput: "capo_bedrock_agent.types.missing_node_input_flow_validation_details.MissingNodeInputFlowValidationDetails"


class _FlowValidationDetails_missingNodeOutput(TypedDict, closed=True):
    missingNodeOutput: "capo_bedrock_agent.types.missing_node_output_flow_validation_details.MissingNodeOutputFlowValidationDetails"


class _FlowValidationDetails_missingStartingNodes(TypedDict, closed=True):
    missingStartingNodes: "capo_bedrock_agent.types.missing_starting_nodes_flow_validation_details.MissingStartingNodesFlowValidationDetails"


class _FlowValidationDetails_multipleNodeInputConnections(TypedDict, closed=True):
    multipleNodeInputConnections: "capo_bedrock_agent.types.multiple_node_input_connections_flow_validation_details.MultipleNodeInputConnectionsFlowValidationDetails"


class _FlowValidationDetails_unfulfilledNodeInput(TypedDict, closed=True):
    unfulfilledNodeInput: "capo_bedrock_agent.types.unfulfilled_node_input_flow_validation_details.UnfulfilledNodeInputFlowValidationDetails"


class _FlowValidationDetails_unsatisfiedConnectionConditions(TypedDict, closed=True):
    unsatisfiedConnectionConditions: "capo_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details.UnsatisfiedConnectionConditionsFlowValidationDetails"


class _FlowValidationDetails_unspecified(TypedDict, closed=True):
    unspecified: "capo_bedrock_agent.types.unspecified_flow_validation_details.UnspecifiedFlowValidationDetails"


class _FlowValidationDetails_unknownNodeInput(TypedDict, closed=True):
    unknownNodeInput: "capo_bedrock_agent.types.unknown_node_input_flow_validation_details.UnknownNodeInputFlowValidationDetails"


class _FlowValidationDetails_unknownNodeOutput(TypedDict, closed=True):
    unknownNodeOutput: "capo_bedrock_agent.types.unknown_node_output_flow_validation_details.UnknownNodeOutputFlowValidationDetails"


class _FlowValidationDetails_missingLoopInputNode(TypedDict, closed=True):
    missingLoopInputNode: "capo_bedrock_agent.types.missing_loop_input_node_flow_validation_details.MissingLoopInputNodeFlowValidationDetails"


class _FlowValidationDetails_missingLoopControllerNode(TypedDict, closed=True):
    missingLoopControllerNode: "capo_bedrock_agent.types.missing_loop_controller_node_flow_validation_details.MissingLoopControllerNodeFlowValidationDetails"


class _FlowValidationDetails_multipleLoopInputNodes(TypedDict, closed=True):
    multipleLoopInputNodes: "capo_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details.MultipleLoopInputNodesFlowValidationDetails"


class _FlowValidationDetails_multipleLoopControllerNodes(TypedDict, closed=True):
    multipleLoopControllerNodes: "capo_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details.MultipleLoopControllerNodesFlowValidationDetails"


class _FlowValidationDetails_loopIncompatibleNodeType(TypedDict, closed=True):
    loopIncompatibleNodeType: "capo_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details.LoopIncompatibleNodeTypeFlowValidationDetails"


class _FlowValidationDetails_invalidLoopBoundary(TypedDict, closed=True):
    invalidLoopBoundary: "capo_bedrock_agent.types.invalid_loop_boundary_flow_validation_details.InvalidLoopBoundaryFlowValidationDetails"


FlowValidationDetails: TypeAlias = (
    _FlowValidationDetails_cyclicConnection
    | _FlowValidationDetails_duplicateConnections
    | _FlowValidationDetails_duplicateConditionExpression
    | _FlowValidationDetails_unreachableNode
    | _FlowValidationDetails_unknownConnectionSource
    | _FlowValidationDetails_unknownConnectionSourceOutput
    | _FlowValidationDetails_unknownConnectionTarget
    | _FlowValidationDetails_unknownConnectionTargetInput
    | _FlowValidationDetails_unknownConnectionCondition
    | _FlowValidationDetails_malformedConditionExpression
    | _FlowValidationDetails_malformedNodeInputExpression
    | _FlowValidationDetails_mismatchedNodeInputType
    | _FlowValidationDetails_mismatchedNodeOutputType
    | _FlowValidationDetails_incompatibleConnectionDataType
    | _FlowValidationDetails_missingConnectionConfiguration
    | _FlowValidationDetails_missingDefaultCondition
    | _FlowValidationDetails_missingEndingNodes
    | _FlowValidationDetails_missingNodeConfiguration
    | _FlowValidationDetails_missingNodeInput
    | _FlowValidationDetails_missingNodeOutput
    | _FlowValidationDetails_missingStartingNodes
    | _FlowValidationDetails_multipleNodeInputConnections
    | _FlowValidationDetails_unfulfilledNodeInput
    | _FlowValidationDetails_unsatisfiedConnectionConditions
    | _FlowValidationDetails_unspecified
    | _FlowValidationDetails_unknownNodeInput
    | _FlowValidationDetails_unknownNodeOutput
    | _FlowValidationDetails_missingLoopInputNode
    | _FlowValidationDetails_missingLoopControllerNode
    | _FlowValidationDetails_multipleLoopInputNodes
    | _FlowValidationDetails_multipleLoopControllerNodes
    | _FlowValidationDetails_loopIncompatibleNodeType
    | _FlowValidationDetails_invalidLoopBoundary
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FlowValidationDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FlowValidationDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "cyclicConnection" in value:
        import capo_bedrock_agent.types.cyclic_connection_flow_validation_details

        return {
            "cyclicConnection": capo_bedrock_agent.types.cyclic_connection_flow_validation_details.serialize_json(
                value["cyclicConnection"]
            )
        }
    elif "duplicateConnections" in value:
        import capo_bedrock_agent.types.duplicate_connections_flow_validation_details

        return {
            "duplicateConnections": capo_bedrock_agent.types.duplicate_connections_flow_validation_details.serialize_json(
                value["duplicateConnections"]
            )
        }
    elif "duplicateConditionExpression" in value:
        import capo_bedrock_agent.types.duplicate_condition_expression_flow_validation_details

        return {
            "duplicateConditionExpression": capo_bedrock_agent.types.duplicate_condition_expression_flow_validation_details.serialize_json(
                value["duplicateConditionExpression"]
            )
        }
    elif "unreachableNode" in value:
        import capo_bedrock_agent.types.unreachable_node_flow_validation_details

        return {
            "unreachableNode": capo_bedrock_agent.types.unreachable_node_flow_validation_details.serialize_json(
                value["unreachableNode"]
            )
        }
    elif "unknownConnectionSource" in value:
        import capo_bedrock_agent.types.unknown_connection_source_flow_validation_details

        return {
            "unknownConnectionSource": capo_bedrock_agent.types.unknown_connection_source_flow_validation_details.serialize_json(
                value["unknownConnectionSource"]
            )
        }
    elif "unknownConnectionSourceOutput" in value:
        import capo_bedrock_agent.types.unknown_connection_source_output_flow_validation_details

        return {
            "unknownConnectionSourceOutput": capo_bedrock_agent.types.unknown_connection_source_output_flow_validation_details.serialize_json(
                value["unknownConnectionSourceOutput"]
            )
        }
    elif "unknownConnectionTarget" in value:
        import capo_bedrock_agent.types.unknown_connection_target_flow_validation_details

        return {
            "unknownConnectionTarget": capo_bedrock_agent.types.unknown_connection_target_flow_validation_details.serialize_json(
                value["unknownConnectionTarget"]
            )
        }
    elif "unknownConnectionTargetInput" in value:
        import capo_bedrock_agent.types.unknown_connection_target_input_flow_validation_details

        return {
            "unknownConnectionTargetInput": capo_bedrock_agent.types.unknown_connection_target_input_flow_validation_details.serialize_json(
                value["unknownConnectionTargetInput"]
            )
        }
    elif "unknownConnectionCondition" in value:
        import capo_bedrock_agent.types.unknown_connection_condition_flow_validation_details

        return {
            "unknownConnectionCondition": capo_bedrock_agent.types.unknown_connection_condition_flow_validation_details.serialize_json(
                value["unknownConnectionCondition"]
            )
        }
    elif "malformedConditionExpression" in value:
        import capo_bedrock_agent.types.malformed_condition_expression_flow_validation_details

        return {
            "malformedConditionExpression": capo_bedrock_agent.types.malformed_condition_expression_flow_validation_details.serialize_json(
                value["malformedConditionExpression"]
            )
        }
    elif "malformedNodeInputExpression" in value:
        import capo_bedrock_agent.types.malformed_node_input_expression_flow_validation_details

        return {
            "malformedNodeInputExpression": capo_bedrock_agent.types.malformed_node_input_expression_flow_validation_details.serialize_json(
                value["malformedNodeInputExpression"]
            )
        }
    elif "mismatchedNodeInputType" in value:
        import capo_bedrock_agent.types.mismatched_node_input_type_flow_validation_details

        return {
            "mismatchedNodeInputType": capo_bedrock_agent.types.mismatched_node_input_type_flow_validation_details.serialize_json(
                value["mismatchedNodeInputType"]
            )
        }
    elif "mismatchedNodeOutputType" in value:
        import capo_bedrock_agent.types.mismatched_node_output_type_flow_validation_details

        return {
            "mismatchedNodeOutputType": capo_bedrock_agent.types.mismatched_node_output_type_flow_validation_details.serialize_json(
                value["mismatchedNodeOutputType"]
            )
        }
    elif "incompatibleConnectionDataType" in value:
        import capo_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details

        return {
            "incompatibleConnectionDataType": capo_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details.serialize_json(
                value["incompatibleConnectionDataType"]
            )
        }
    elif "missingConnectionConfiguration" in value:
        import capo_bedrock_agent.types.missing_connection_configuration_flow_validation_details

        return {
            "missingConnectionConfiguration": capo_bedrock_agent.types.missing_connection_configuration_flow_validation_details.serialize_json(
                value["missingConnectionConfiguration"]
            )
        }
    elif "missingDefaultCondition" in value:
        import capo_bedrock_agent.types.missing_default_condition_flow_validation_details

        return {
            "missingDefaultCondition": capo_bedrock_agent.types.missing_default_condition_flow_validation_details.serialize_json(
                value["missingDefaultCondition"]
            )
        }
    elif "missingEndingNodes" in value:
        import capo_bedrock_agent.types.missing_ending_nodes_flow_validation_details

        return {
            "missingEndingNodes": capo_bedrock_agent.types.missing_ending_nodes_flow_validation_details.serialize_json(
                value["missingEndingNodes"]
            )
        }
    elif "missingNodeConfiguration" in value:
        import capo_bedrock_agent.types.missing_node_configuration_flow_validation_details

        return {
            "missingNodeConfiguration": capo_bedrock_agent.types.missing_node_configuration_flow_validation_details.serialize_json(
                value["missingNodeConfiguration"]
            )
        }
    elif "missingNodeInput" in value:
        import capo_bedrock_agent.types.missing_node_input_flow_validation_details

        return {
            "missingNodeInput": capo_bedrock_agent.types.missing_node_input_flow_validation_details.serialize_json(
                value["missingNodeInput"]
            )
        }
    elif "missingNodeOutput" in value:
        import capo_bedrock_agent.types.missing_node_output_flow_validation_details

        return {
            "missingNodeOutput": capo_bedrock_agent.types.missing_node_output_flow_validation_details.serialize_json(
                value["missingNodeOutput"]
            )
        }
    elif "missingStartingNodes" in value:
        import capo_bedrock_agent.types.missing_starting_nodes_flow_validation_details

        return {
            "missingStartingNodes": capo_bedrock_agent.types.missing_starting_nodes_flow_validation_details.serialize_json(
                value["missingStartingNodes"]
            )
        }
    elif "multipleNodeInputConnections" in value:
        import capo_bedrock_agent.types.multiple_node_input_connections_flow_validation_details

        return {
            "multipleNodeInputConnections": capo_bedrock_agent.types.multiple_node_input_connections_flow_validation_details.serialize_json(
                value["multipleNodeInputConnections"]
            )
        }
    elif "unfulfilledNodeInput" in value:
        import capo_bedrock_agent.types.unfulfilled_node_input_flow_validation_details

        return {
            "unfulfilledNodeInput": capo_bedrock_agent.types.unfulfilled_node_input_flow_validation_details.serialize_json(
                value["unfulfilledNodeInput"]
            )
        }
    elif "unsatisfiedConnectionConditions" in value:
        import capo_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details

        return {
            "unsatisfiedConnectionConditions": capo_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details.serialize_json(
                value["unsatisfiedConnectionConditions"]
            )
        }
    elif "unspecified" in value:
        import capo_bedrock_agent.types.unspecified_flow_validation_details

        return {
            "unspecified": capo_bedrock_agent.types.unspecified_flow_validation_details.serialize_json(
                value["unspecified"]
            )
        }
    elif "unknownNodeInput" in value:
        import capo_bedrock_agent.types.unknown_node_input_flow_validation_details

        return {
            "unknownNodeInput": capo_bedrock_agent.types.unknown_node_input_flow_validation_details.serialize_json(
                value["unknownNodeInput"]
            )
        }
    elif "unknownNodeOutput" in value:
        import capo_bedrock_agent.types.unknown_node_output_flow_validation_details

        return {
            "unknownNodeOutput": capo_bedrock_agent.types.unknown_node_output_flow_validation_details.serialize_json(
                value["unknownNodeOutput"]
            )
        }
    elif "missingLoopInputNode" in value:
        import capo_bedrock_agent.types.missing_loop_input_node_flow_validation_details

        return {
            "missingLoopInputNode": capo_bedrock_agent.types.missing_loop_input_node_flow_validation_details.serialize_json(
                value["missingLoopInputNode"]
            )
        }
    elif "missingLoopControllerNode" in value:
        import capo_bedrock_agent.types.missing_loop_controller_node_flow_validation_details

        return {
            "missingLoopControllerNode": capo_bedrock_agent.types.missing_loop_controller_node_flow_validation_details.serialize_json(
                value["missingLoopControllerNode"]
            )
        }
    elif "multipleLoopInputNodes" in value:
        import capo_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details

        return {
            "multipleLoopInputNodes": capo_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details.serialize_json(
                value["multipleLoopInputNodes"]
            )
        }
    elif "multipleLoopControllerNodes" in value:
        import capo_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details

        return {
            "multipleLoopControllerNodes": capo_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details.serialize_json(
                value["multipleLoopControllerNodes"]
            )
        }
    elif "loopIncompatibleNodeType" in value:
        import capo_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details

        return {
            "loopIncompatibleNodeType": capo_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details.serialize_json(
                value["loopIncompatibleNodeType"]
            )
        }
    elif "invalidLoopBoundary" in value:
        import capo_bedrock_agent.types.invalid_loop_boundary_flow_validation_details

        return {
            "invalidLoopBoundary": capo_bedrock_agent.types.invalid_loop_boundary_flow_validation_details.serialize_json(
                value["invalidLoopBoundary"]
            )
        }
    else:
        raise SerializationError("FlowValidationDetails: no variant present")


def deserialize_json(data: dict) -> FlowValidationDetails:
    if data.get("cyclicConnection") is not None:
        import capo_bedrock_agent.types.cyclic_connection_flow_validation_details

        return {
            "cyclicConnection": capo_bedrock_agent.types.cyclic_connection_flow_validation_details.deserialize_json(
                data["cyclicConnection"]
            )
        }
    elif data.get("duplicateConnections") is not None:
        import capo_bedrock_agent.types.duplicate_connections_flow_validation_details

        return {
            "duplicateConnections": capo_bedrock_agent.types.duplicate_connections_flow_validation_details.deserialize_json(
                data["duplicateConnections"]
            )
        }
    elif data.get("duplicateConditionExpression") is not None:
        import capo_bedrock_agent.types.duplicate_condition_expression_flow_validation_details

        return {
            "duplicateConditionExpression": capo_bedrock_agent.types.duplicate_condition_expression_flow_validation_details.deserialize_json(
                data["duplicateConditionExpression"]
            )
        }
    elif data.get("unreachableNode") is not None:
        import capo_bedrock_agent.types.unreachable_node_flow_validation_details

        return {
            "unreachableNode": capo_bedrock_agent.types.unreachable_node_flow_validation_details.deserialize_json(
                data["unreachableNode"]
            )
        }
    elif data.get("unknownConnectionSource") is not None:
        import capo_bedrock_agent.types.unknown_connection_source_flow_validation_details

        return {
            "unknownConnectionSource": capo_bedrock_agent.types.unknown_connection_source_flow_validation_details.deserialize_json(
                data["unknownConnectionSource"]
            )
        }
    elif data.get("unknownConnectionSourceOutput") is not None:
        import capo_bedrock_agent.types.unknown_connection_source_output_flow_validation_details

        return {
            "unknownConnectionSourceOutput": capo_bedrock_agent.types.unknown_connection_source_output_flow_validation_details.deserialize_json(
                data["unknownConnectionSourceOutput"]
            )
        }
    elif data.get("unknownConnectionTarget") is not None:
        import capo_bedrock_agent.types.unknown_connection_target_flow_validation_details

        return {
            "unknownConnectionTarget": capo_bedrock_agent.types.unknown_connection_target_flow_validation_details.deserialize_json(
                data["unknownConnectionTarget"]
            )
        }
    elif data.get("unknownConnectionTargetInput") is not None:
        import capo_bedrock_agent.types.unknown_connection_target_input_flow_validation_details

        return {
            "unknownConnectionTargetInput": capo_bedrock_agent.types.unknown_connection_target_input_flow_validation_details.deserialize_json(
                data["unknownConnectionTargetInput"]
            )
        }
    elif data.get("unknownConnectionCondition") is not None:
        import capo_bedrock_agent.types.unknown_connection_condition_flow_validation_details

        return {
            "unknownConnectionCondition": capo_bedrock_agent.types.unknown_connection_condition_flow_validation_details.deserialize_json(
                data["unknownConnectionCondition"]
            )
        }
    elif data.get("malformedConditionExpression") is not None:
        import capo_bedrock_agent.types.malformed_condition_expression_flow_validation_details

        return {
            "malformedConditionExpression": capo_bedrock_agent.types.malformed_condition_expression_flow_validation_details.deserialize_json(
                data["malformedConditionExpression"]
            )
        }
    elif data.get("malformedNodeInputExpression") is not None:
        import capo_bedrock_agent.types.malformed_node_input_expression_flow_validation_details

        return {
            "malformedNodeInputExpression": capo_bedrock_agent.types.malformed_node_input_expression_flow_validation_details.deserialize_json(
                data["malformedNodeInputExpression"]
            )
        }
    elif data.get("mismatchedNodeInputType") is not None:
        import capo_bedrock_agent.types.mismatched_node_input_type_flow_validation_details

        return {
            "mismatchedNodeInputType": capo_bedrock_agent.types.mismatched_node_input_type_flow_validation_details.deserialize_json(
                data["mismatchedNodeInputType"]
            )
        }
    elif data.get("mismatchedNodeOutputType") is not None:
        import capo_bedrock_agent.types.mismatched_node_output_type_flow_validation_details

        return {
            "mismatchedNodeOutputType": capo_bedrock_agent.types.mismatched_node_output_type_flow_validation_details.deserialize_json(
                data["mismatchedNodeOutputType"]
            )
        }
    elif data.get("incompatibleConnectionDataType") is not None:
        import capo_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details

        return {
            "incompatibleConnectionDataType": capo_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details.deserialize_json(
                data["incompatibleConnectionDataType"]
            )
        }
    elif data.get("missingConnectionConfiguration") is not None:
        import capo_bedrock_agent.types.missing_connection_configuration_flow_validation_details

        return {
            "missingConnectionConfiguration": capo_bedrock_agent.types.missing_connection_configuration_flow_validation_details.deserialize_json(
                data["missingConnectionConfiguration"]
            )
        }
    elif data.get("missingDefaultCondition") is not None:
        import capo_bedrock_agent.types.missing_default_condition_flow_validation_details

        return {
            "missingDefaultCondition": capo_bedrock_agent.types.missing_default_condition_flow_validation_details.deserialize_json(
                data["missingDefaultCondition"]
            )
        }
    elif data.get("missingEndingNodes") is not None:
        import capo_bedrock_agent.types.missing_ending_nodes_flow_validation_details

        return {
            "missingEndingNodes": capo_bedrock_agent.types.missing_ending_nodes_flow_validation_details.deserialize_json(
                data["missingEndingNodes"]
            )
        }
    elif data.get("missingNodeConfiguration") is not None:
        import capo_bedrock_agent.types.missing_node_configuration_flow_validation_details

        return {
            "missingNodeConfiguration": capo_bedrock_agent.types.missing_node_configuration_flow_validation_details.deserialize_json(
                data["missingNodeConfiguration"]
            )
        }
    elif data.get("missingNodeInput") is not None:
        import capo_bedrock_agent.types.missing_node_input_flow_validation_details

        return {
            "missingNodeInput": capo_bedrock_agent.types.missing_node_input_flow_validation_details.deserialize_json(
                data["missingNodeInput"]
            )
        }
    elif data.get("missingNodeOutput") is not None:
        import capo_bedrock_agent.types.missing_node_output_flow_validation_details

        return {
            "missingNodeOutput": capo_bedrock_agent.types.missing_node_output_flow_validation_details.deserialize_json(
                data["missingNodeOutput"]
            )
        }
    elif data.get("missingStartingNodes") is not None:
        import capo_bedrock_agent.types.missing_starting_nodes_flow_validation_details

        return {
            "missingStartingNodes": capo_bedrock_agent.types.missing_starting_nodes_flow_validation_details.deserialize_json(
                data["missingStartingNodes"]
            )
        }
    elif data.get("multipleNodeInputConnections") is not None:
        import capo_bedrock_agent.types.multiple_node_input_connections_flow_validation_details

        return {
            "multipleNodeInputConnections": capo_bedrock_agent.types.multiple_node_input_connections_flow_validation_details.deserialize_json(
                data["multipleNodeInputConnections"]
            )
        }
    elif data.get("unfulfilledNodeInput") is not None:
        import capo_bedrock_agent.types.unfulfilled_node_input_flow_validation_details

        return {
            "unfulfilledNodeInput": capo_bedrock_agent.types.unfulfilled_node_input_flow_validation_details.deserialize_json(
                data["unfulfilledNodeInput"]
            )
        }
    elif data.get("unsatisfiedConnectionConditions") is not None:
        import capo_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details

        return {
            "unsatisfiedConnectionConditions": capo_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details.deserialize_json(
                data["unsatisfiedConnectionConditions"]
            )
        }
    elif data.get("unspecified") is not None:
        import capo_bedrock_agent.types.unspecified_flow_validation_details

        return {
            "unspecified": capo_bedrock_agent.types.unspecified_flow_validation_details.deserialize_json(
                data["unspecified"]
            )
        }
    elif data.get("unknownNodeInput") is not None:
        import capo_bedrock_agent.types.unknown_node_input_flow_validation_details

        return {
            "unknownNodeInput": capo_bedrock_agent.types.unknown_node_input_flow_validation_details.deserialize_json(
                data["unknownNodeInput"]
            )
        }
    elif data.get("unknownNodeOutput") is not None:
        import capo_bedrock_agent.types.unknown_node_output_flow_validation_details

        return {
            "unknownNodeOutput": capo_bedrock_agent.types.unknown_node_output_flow_validation_details.deserialize_json(
                data["unknownNodeOutput"]
            )
        }
    elif data.get("missingLoopInputNode") is not None:
        import capo_bedrock_agent.types.missing_loop_input_node_flow_validation_details

        return {
            "missingLoopInputNode": capo_bedrock_agent.types.missing_loop_input_node_flow_validation_details.deserialize_json(
                data["missingLoopInputNode"]
            )
        }
    elif data.get("missingLoopControllerNode") is not None:
        import capo_bedrock_agent.types.missing_loop_controller_node_flow_validation_details

        return {
            "missingLoopControllerNode": capo_bedrock_agent.types.missing_loop_controller_node_flow_validation_details.deserialize_json(
                data["missingLoopControllerNode"]
            )
        }
    elif data.get("multipleLoopInputNodes") is not None:
        import capo_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details

        return {
            "multipleLoopInputNodes": capo_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details.deserialize_json(
                data["multipleLoopInputNodes"]
            )
        }
    elif data.get("multipleLoopControllerNodes") is not None:
        import capo_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details

        return {
            "multipleLoopControllerNodes": capo_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details.deserialize_json(
                data["multipleLoopControllerNodes"]
            )
        }
    elif data.get("loopIncompatibleNodeType") is not None:
        import capo_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details

        return {
            "loopIncompatibleNodeType": capo_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details.deserialize_json(
                data["loopIncompatibleNodeType"]
            )
        }
    elif data.get("invalidLoopBoundary") is not None:
        import capo_bedrock_agent.types.invalid_loop_boundary_flow_validation_details

        return {
            "invalidLoopBoundary": capo_bedrock_agent.types.invalid_loop_boundary_flow_validation_details.deserialize_json(
                data["invalidLoopBoundary"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FlowValidationDetails: no recognized variant key")


def redact_sensitive(value: FlowValidationDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "duplicateConditionExpression" in value:
        import capo_bedrock_agent.types.duplicate_condition_expression_flow_validation_details

        out["duplicateConditionExpression"] = (
            capo_bedrock_agent.types.duplicate_condition_expression_flow_validation_details.redact_sensitive(
                value["duplicateConditionExpression"]
            )
        )
    return out
