"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeStateMachineAliasOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.alias_description
    import capo_sfn.types.arn
    import capo_sfn.types.name
    import capo_sfn.types.routing_configuration_list
    import capo_sfn.types.timestamp


class DescribeStateMachineAliasOutput(TypedDict, closed=True):
    state_machine_alias_arn: NotRequired["capo_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the state machine alias.</p>"""
    name: NotRequired["capo_sfn.types.name.Name"]
    """<p>The name of the state machine alias.</p>"""
    description: NotRequired["capo_sfn.types.alias_description.AliasDescription"]
    """<p>A description of the alias.</p>"""
    routing_configuration: NotRequired[
        "capo_sfn.types.routing_configuration_list.RoutingConfigurationList"
    ]
    """<p>The routing configuration of the alias.</p>"""
    creation_date: NotRequired["capo_sfn.types.timestamp.Timestamp"]
    """<p>The date the state machine alias was created.</p>"""
    update_date: NotRequired["capo_sfn.types.timestamp.Timestamp"]
    """<p>The date the state machine alias was last updated.</p> <p>For a newly created state machine, this is the same as the creation date.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeStateMachineAliasOutput) -> dict:
    out: dict = {}
    if "state_machine_alias_arn" in value:
        out["stateMachineAliasArn"] = value["state_machine_alias_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "routing_configuration" in value:
        import capo_sfn.types.routing_configuration_list

        out["routingConfiguration"] = (
            capo_sfn.types.routing_configuration_list.serialize_aws_json_1_0(
                value["routing_configuration"]
            )
        )
    if "creation_date" in value:
        import capo_sfn.types.timestamp

        out["creationDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
            value["creation_date"]
        )
    if "update_date" in value:
        import capo_sfn.types.timestamp

        out["updateDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
            value["update_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeStateMachineAliasOutput:
    out: DescribeStateMachineAliasOutput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineAliasArn") is not None:
        out["state_machine_alias_arn"] = data["stateMachineAliasArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("routingConfiguration") is not None:
        import capo_sfn.types.routing_configuration_list

        out["routing_configuration"] = (
            capo_sfn.types.routing_configuration_list.deserialize_aws_json_1_0(
                data["routingConfiguration"]
            )
        )
    if data.get("creationDate") is not None:
        import capo_sfn.types.timestamp

        out["creation_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    if data.get("updateDate") is not None:
        import capo_sfn.types.timestamp

        out["update_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["updateDate"]
        )
    return out


def redact_sensitive(value: DescribeStateMachineAliasOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
