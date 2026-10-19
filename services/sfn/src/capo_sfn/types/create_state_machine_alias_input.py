"""Generated from Smithy shape ``com.amazonaws.sfn#CreateStateMachineAliasInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.alias_description
    import capo_sfn.types.character_restricted_name
    import capo_sfn.types.routing_configuration_list


class CreateStateMachineAliasInput(TypedDict, closed=True):
    description: NotRequired["capo_sfn.types.alias_description.AliasDescription"]
    """<p>A description for the state machine alias.</p>"""
    name: "capo_sfn.types.character_restricted_name.CharacterRestrictedName"
    """<p>The name of the state machine alias.</p> <p>To avoid conflict with version ARNs, don't use an integer in the name of the alias.</p>"""
    routing_configuration: (
        "capo_sfn.types.routing_configuration_list.RoutingConfigurationList"
    )
    """<p>The routing configuration of a state machine alias. The routing configuration shifts execution traffic between two state machine versions. <code>routingConfiguration</code> contains an array of <code>RoutingConfig</code> objects that specify up to two state machine versions. Step Functions then randomly choses which version to run an execution with based on the weight assigned to each <code>RoutingConfig</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateStateMachineAliasInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    import capo_sfn.types.routing_configuration_list

    out["routingConfiguration"] = (
        capo_sfn.types.routing_configuration_list.serialize_aws_json_1_0(
            value["routing_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateStateMachineAliasInput:
    out: CreateStateMachineAliasInput = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("routingConfiguration") is not None:
        import capo_sfn.types.routing_configuration_list

        out["routing_configuration"] = (
            capo_sfn.types.routing_configuration_list.deserialize_aws_json_1_0(
                data["routingConfiguration"]
            )
        )
    else:
        out["routing_configuration"] = []
    return out


def redact_sensitive(value: CreateStateMachineAliasInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
