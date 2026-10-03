"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreateEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.endpoint_description
    import capo_eventbridge.types.endpoint_event_bus_list
    import capo_eventbridge.types.endpoint_name
    import capo_eventbridge.types.iam_role_arn
    import capo_eventbridge.types.replication_config
    import capo_eventbridge.types.routing_config


class CreateEndpointRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.endpoint_name.EndpointName"
    """<p>The name of the global endpoint. For example, <code>"Name":"us-east-2-custom_bus_A-endpoint"</code>.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.endpoint_description.EndpointDescription"
    ]
    """<p>A description of the global endpoint.</p>"""
    routing_config: "capo_eventbridge.types.routing_config.RoutingConfig"
    """<p>Configure the routing policy, including the health check and secondary Region..</p>"""
    replication_config: NotRequired[
        "capo_eventbridge.types.replication_config.ReplicationConfig"
    ]
    """<p>Enable or disable event replication. The default state is <code>ENABLED</code> which means you must supply a <code>RoleArn</code>. If you don't have a <code>RoleArn</code> or you don't want event replication enabled, set the state to <code>DISABLED</code>.</p>"""
    event_buses: "capo_eventbridge.types.endpoint_event_bus_list.EndpointEventBusList"
    """<p>Define the event buses used. </p> <important> <p>The names of the event buses must be identical in each Region.</p> </important>"""
    role_arn: NotRequired["capo_eventbridge.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the role used for replication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_eventbridge.types.routing_config

    out["RoutingConfig"] = capo_eventbridge.types.routing_config.serialize_aws_json_1_1(
        value["routing_config"]
    )
    if "replication_config" in value:
        import capo_eventbridge.types.replication_config

        out["ReplicationConfig"] = (
            capo_eventbridge.types.replication_config.serialize_aws_json_1_1(
                value["replication_config"]
            )
        )
    import capo_eventbridge.types.endpoint_event_bus_list

    out["EventBuses"] = (
        capo_eventbridge.types.endpoint_event_bus_list.serialize_aws_json_1_1(
            value["event_buses"]
        )
    )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointRequest:
    out: CreateEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateEndpointRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoutingConfig") is not None:
        import capo_eventbridge.types.routing_config

        out["routing_config"] = (
            capo_eventbridge.types.routing_config.deserialize_aws_json_1_1(
                data["RoutingConfig"]
            )
        )
    else:
        raise DeserializationError("CreateEndpointRequest.routing_config required")
    if data.get("ReplicationConfig") is not None:
        import capo_eventbridge.types.replication_config

        out["replication_config"] = (
            capo_eventbridge.types.replication_config.deserialize_aws_json_1_1(
                data["ReplicationConfig"]
            )
        )
    if data.get("EventBuses") is not None:
        import capo_eventbridge.types.endpoint_event_bus_list

        out["event_buses"] = (
            capo_eventbridge.types.endpoint_event_bus_list.deserialize_aws_json_1_1(
                data["EventBuses"]
            )
        )
    else:
        raise DeserializationError("CreateEndpointRequest.event_buses required")
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
