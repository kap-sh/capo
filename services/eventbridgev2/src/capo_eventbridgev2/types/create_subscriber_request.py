"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#CreateSubscriberRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.batch_configuration
    import capo_eventbridgev2.types.client_token
    import capo_eventbridgev2.types.description
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.filter_configuration
    import capo_eventbridgev2.types.invoke_configuration
    import capo_eventbridgev2.types.log_configuration
    import capo_eventbridgev2.types.on_failure_configuration
    import capo_eventbridgev2.types.ordering_type
    import capo_eventbridgev2.types.point_in_time_configuration
    import capo_eventbridgev2.types.retry_policy
    import capo_eventbridgev2.types.starting_position
    import capo_eventbridgev2.types.subscriber_name
    import capo_eventbridgev2.types.subscriber_state
    import capo_eventbridgev2.types.tag_map
    import capo_eventbridgev2.types.transformer


class CreateSubscriberRequest(TypedDict, closed=True):
    name: "capo_eventbridgev2.types.subscriber_name.SubscriberName"
    event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
    invoke_configuration: (
        "capo_eventbridgev2.types.invoke_configuration.InvokeConfiguration"
    )
    description: NotRequired["capo_eventbridgev2.types.description.Description"]
    filter_configuration: NotRequired[
        "capo_eventbridgev2.types.filter_configuration.FilterConfiguration"
    ]
    type: NotRequired["capo_eventbridgev2.types.ordering_type.OrderingType"]
    starting_position: NotRequired[
        "capo_eventbridgev2.types.starting_position.StartingPosition"
    ]
    point_in_time_configuration: NotRequired[
        "capo_eventbridgev2.types.point_in_time_configuration.PointInTimeConfiguration"
    ]
    batch_configuration: NotRequired[
        "capo_eventbridgev2.types.batch_configuration.BatchConfiguration"
    ]
    transformer: NotRequired["capo_eventbridgev2.types.transformer.Transformer"]
    """Not applicable to universal (aws-sdk) targets, whose input transformation is UniversalTargetParameters.Input; a Transformer on such a target is rejected."""
    retry_policy: NotRequired["capo_eventbridgev2.types.retry_policy.RetryPolicy"]
    on_failure_configuration: NotRequired[
        "capo_eventbridgev2.types.on_failure_configuration.OnFailureConfiguration"
    ]
    log_configuration: NotRequired[
        "capo_eventbridgev2.types.log_configuration.LogConfiguration"
    ]
    state: NotRequired["capo_eventbridgev2.types.subscriber_state.SubscriberState"]
    tags: NotRequired["capo_eventbridgev2.types.tag_map.TagMap"]
    client_token: NotRequired["capo_eventbridgev2.types.client_token.ClientToken"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateSubscriberRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["EventBusArn"] = value["event_bus_arn"]
    import capo_eventbridgev2.types.invoke_configuration

    out["InvokeConfiguration"] = (
        capo_eventbridgev2.types.invoke_configuration.serialize_cbor(
            value["invoke_configuration"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "filter_configuration" in value:
        import capo_eventbridgev2.types.filter_configuration

        out["FilterConfiguration"] = (
            capo_eventbridgev2.types.filter_configuration.serialize_cbor(
                value["filter_configuration"]
            )
        )
    if "type" in value:
        import capo_eventbridgev2.types.ordering_type

        out["Type"] = capo_eventbridgev2.types.ordering_type.serialize_cbor(
            value["type"]
        )
    if "starting_position" in value:
        import capo_eventbridgev2.types.starting_position

        out["StartingPosition"] = (
            capo_eventbridgev2.types.starting_position.serialize_cbor(
                value["starting_position"]
            )
        )
    if "point_in_time_configuration" in value:
        import capo_eventbridgev2.types.point_in_time_configuration

        out["PointInTimeConfiguration"] = (
            capo_eventbridgev2.types.point_in_time_configuration.serialize_cbor(
                value["point_in_time_configuration"]
            )
        )
    if "batch_configuration" in value:
        import capo_eventbridgev2.types.batch_configuration

        out["BatchConfiguration"] = (
            capo_eventbridgev2.types.batch_configuration.serialize_cbor(
                value["batch_configuration"]
            )
        )
    if "transformer" in value:
        import capo_eventbridgev2.types.transformer

        out["Transformer"] = capo_eventbridgev2.types.transformer.serialize_cbor(
            value["transformer"]
        )
    if "retry_policy" in value:
        import capo_eventbridgev2.types.retry_policy

        out["RetryPolicy"] = capo_eventbridgev2.types.retry_policy.serialize_cbor(
            value["retry_policy"]
        )
    if "on_failure_configuration" in value:
        import capo_eventbridgev2.types.on_failure_configuration

        out["OnFailureConfiguration"] = (
            capo_eventbridgev2.types.on_failure_configuration.serialize_cbor(
                value["on_failure_configuration"]
            )
        )
    if "log_configuration" in value:
        import capo_eventbridgev2.types.log_configuration

        out["LogConfiguration"] = (
            capo_eventbridgev2.types.log_configuration.serialize_cbor(
                value["log_configuration"]
            )
        )
    if "state" in value:
        import capo_eventbridgev2.types.subscriber_state

        out["State"] = capo_eventbridgev2.types.subscriber_state.serialize_cbor(
            value["state"]
        )
    if "tags" in value:
        import capo_eventbridgev2.types.tag_map

        out["Tags"] = capo_eventbridgev2.types.tag_map.serialize_cbor(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> CreateSubscriberRequest:
    out: CreateSubscriberRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateSubscriberRequest.name required")
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    else:
        raise DeserializationError("CreateSubscriberRequest.event_bus_arn required")
    if data.get("InvokeConfiguration") is not None:
        import capo_eventbridgev2.types.invoke_configuration

        out["invoke_configuration"] = (
            capo_eventbridgev2.types.invoke_configuration.deserialize_cbor(
                data["InvokeConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriberRequest.invoke_configuration required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FilterConfiguration") is not None:
        import capo_eventbridgev2.types.filter_configuration

        out["filter_configuration"] = (
            capo_eventbridgev2.types.filter_configuration.deserialize_cbor(
                data["FilterConfiguration"]
            )
        )
    if data.get("Type") is not None:
        import capo_eventbridgev2.types.ordering_type

        out["type"] = capo_eventbridgev2.types.ordering_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("StartingPosition") is not None:
        import capo_eventbridgev2.types.starting_position

        out["starting_position"] = (
            capo_eventbridgev2.types.starting_position.deserialize_cbor(
                data["StartingPosition"]
            )
        )
    if data.get("PointInTimeConfiguration") is not None:
        import capo_eventbridgev2.types.point_in_time_configuration

        out["point_in_time_configuration"] = (
            capo_eventbridgev2.types.point_in_time_configuration.deserialize_cbor(
                data["PointInTimeConfiguration"]
            )
        )
    if data.get("BatchConfiguration") is not None:
        import capo_eventbridgev2.types.batch_configuration

        out["batch_configuration"] = (
            capo_eventbridgev2.types.batch_configuration.deserialize_cbor(
                data["BatchConfiguration"]
            )
        )
    if data.get("Transformer") is not None:
        import capo_eventbridgev2.types.transformer

        out["transformer"] = capo_eventbridgev2.types.transformer.deserialize_cbor(
            data["Transformer"]
        )
    if data.get("RetryPolicy") is not None:
        import capo_eventbridgev2.types.retry_policy

        out["retry_policy"] = capo_eventbridgev2.types.retry_policy.deserialize_cbor(
            data["RetryPolicy"]
        )
    if data.get("OnFailureConfiguration") is not None:
        import capo_eventbridgev2.types.on_failure_configuration

        out["on_failure_configuration"] = (
            capo_eventbridgev2.types.on_failure_configuration.deserialize_cbor(
                data["OnFailureConfiguration"]
            )
        )
    if data.get("LogConfiguration") is not None:
        import capo_eventbridgev2.types.log_configuration

        out["log_configuration"] = (
            capo_eventbridgev2.types.log_configuration.deserialize_cbor(
                data["LogConfiguration"]
            )
        )
    if data.get("State") is not None:
        import capo_eventbridgev2.types.subscriber_state

        out["state"] = capo_eventbridgev2.types.subscriber_state.deserialize_cbor(
            data["State"]
        )
    if data.get("Tags") is not None:
        import capo_eventbridgev2.types.tag_map

        out["tags"] = capo_eventbridgev2.types.tag_map.deserialize_cbor(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: CreateSubscriberRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "invoke_configuration" in value:
        import capo_eventbridgev2.types.invoke_configuration

        out["invoke_configuration"] = (
            capo_eventbridgev2.types.invoke_configuration.redact_sensitive(
                value["invoke_configuration"]
            )
        )
    if "filter_configuration" in value:
        import capo_eventbridgev2.types.filter_configuration

        out["filter_configuration"] = (
            capo_eventbridgev2.types.filter_configuration.redact_sensitive(
                value["filter_configuration"]
            )
        )
    if "transformer" in value:
        import capo_eventbridgev2.types.transformer

        out["transformer"] = capo_eventbridgev2.types.transformer.redact_sensitive(
            value["transformer"]
        )
    return out
