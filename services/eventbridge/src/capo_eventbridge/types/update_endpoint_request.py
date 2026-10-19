"""Generated from Smithy shape ``com.amazonaws.eventbridge#UpdateEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.endpoint_description
    import capo_eventbridge.types.endpoint_event_bus_list
    import capo_eventbridge.types.endpoint_name
    import capo_eventbridge.types.iam_role_arn
    import capo_eventbridge.types.replication_config
    import capo_eventbridge.types.routing_config


class UpdateEndpointRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.endpoint_name.EndpointName"
    """<p>The name of the endpoint you want to update.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.endpoint_description.EndpointDescription"
    ]
    """<p>A description for the endpoint.</p>"""
    routing_config: NotRequired["capo_eventbridge.types.routing_config.RoutingConfig"]
    """<p>Configure the routing policy, including the health check and secondary Region.</p>"""
    replication_config: NotRequired[
        "capo_eventbridge.types.replication_config.ReplicationConfig"
    ]
    """<p>Whether event replication was enabled or disabled by this request.</p>"""
    event_buses: NotRequired[
        "capo_eventbridge.types.endpoint_event_bus_list.EndpointEventBusList"
    ]
    """<p>Define event buses used for replication.</p>"""
    role_arn: NotRequired["capo_eventbridge.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the role used by event replication for this request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "routing_config" in value:
        import capo_eventbridge.types.routing_config

        out["RoutingConfig"] = (
            capo_eventbridge.types.routing_config.serialize_aws_json_1_1(
                value["routing_config"]
            )
        )
    if "replication_config" in value:
        import capo_eventbridge.types.replication_config

        out["ReplicationConfig"] = (
            capo_eventbridge.types.replication_config.serialize_aws_json_1_1(
                value["replication_config"]
            )
        )
    if "event_buses" in value:
        import capo_eventbridge.types.endpoint_event_bus_list

        out["EventBuses"] = (
            capo_eventbridge.types.endpoint_event_bus_list.serialize_aws_json_1_1(
                value["event_buses"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointRequest:
    out: UpdateEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoutingConfig") is not None:
        import capo_eventbridge.types.routing_config

        out["routing_config"] = (
            capo_eventbridge.types.routing_config.deserialize_aws_json_1_1(
                data["RoutingConfig"]
            )
        )
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
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
