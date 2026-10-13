"""Generated from Smithy shape ``com.amazonaws.sfn#UpdateStateMachineAliasInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.alias_description
    import capo_sfn.types.arn
    import capo_sfn.types.routing_configuration_list


class UpdateStateMachineAliasInput(TypedDict, closed=True):
    state_machine_alias_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine alias.</p>"""
    description: NotRequired["capo_sfn.types.alias_description.AliasDescription"]
    """<p>A description of the state machine alias.</p>"""
    routing_configuration: NotRequired[
        "capo_sfn.types.routing_configuration_list.RoutingConfigurationList"
    ]
    """<p>The routing configuration of the state machine alias.</p> <p>An array of <code>RoutingConfig</code> objects that specifies up to two state machine versions that the alias starts executions for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStateMachineAliasInput) -> dict:
    out: dict = {}
    out["stateMachineAliasArn"] = value["state_machine_alias_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "routing_configuration" in value:
        import capo_sfn.types.routing_configuration_list

        out["routingConfiguration"] = (
            capo_sfn.types.routing_configuration_list.serialize_aws_json_1_0(
                value["routing_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStateMachineAliasInput:
    out: UpdateStateMachineAliasInput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineAliasArn") is not None:
        out["state_machine_alias_arn"] = data["stateMachineAliasArn"]
    else:
        raise DeserializationError(
            "UpdateStateMachineAliasInput.state_machine_alias_arn required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("routingConfiguration") is not None:
        import capo_sfn.types.routing_configuration_list

        out["routing_configuration"] = (
            capo_sfn.types.routing_configuration_list.deserialize_aws_json_1_0(
                data["routingConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateStateMachineAliasInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
