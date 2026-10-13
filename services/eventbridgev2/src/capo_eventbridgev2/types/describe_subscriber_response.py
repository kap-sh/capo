"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DescribeSubscriberResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.batch_configuration
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
    import capo_eventbridgev2.types.subscriber_arn
    import capo_eventbridgev2.types.subscriber_name
    import capo_eventbridgev2.types.subscriber_state
    import capo_eventbridgev2.types.timestamp
    import capo_eventbridgev2.types.transformer


class DescribeSubscriberResponse(TypedDict, closed=True):
    subscriber_arn: NotRequired["capo_eventbridgev2.types.subscriber_arn.SubscriberArn"]
    name: NotRequired["capo_eventbridgev2.types.subscriber_name.SubscriberName"]
    event_bus_arn: NotRequired["capo_eventbridgev2.types.event_bus_arn.EventBusArn"]
    invoke_configuration: NotRequired[
        "capo_eventbridgev2.types.invoke_configuration.InvokeConfiguration"
    ]
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
    """Absent for universal (aws-sdk) targets, whose input transformation is UniversalTargetParameters.Input."""
    retry_policy: NotRequired["capo_eventbridgev2.types.retry_policy.RetryPolicy"]
    on_failure_configuration: NotRequired[
        "capo_eventbridgev2.types.on_failure_configuration.OnFailureConfiguration"
    ]
    log_configuration: NotRequired[
        "capo_eventbridgev2.types.log_configuration.LogConfiguration"
    ]
    state: NotRequired["capo_eventbridgev2.types.subscriber_state.SubscriberState"]
    revoked: NotRequired["bool"]
    """True when the bus owner has revoked this subscriber. Present only when true, so an absent member means the subscriber is not revoked. Revocation is terminal: it never returns to false. Mutating operations on a revoked subscriber fail with InvalidStateException, except DeleteSubscriber, which stays available so a revoked subscriber can still be cleaned up."""
    creation_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the subscriber was created."""
    last_modified_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the subscriber was last modified."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSubscriberResponse) -> dict:
    out: dict = {}
    if "subscriber_arn" in value:
        out["SubscriberArn"] = value["subscriber_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    if "invoke_configuration" in value:
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
    if "revoked" in value:
        out["Revoked"] = value["revoked"]
    if "creation_time" in value:
        import capo_eventbridgev2.types.timestamp

        out["CreationTime"] = capo_eventbridgev2.types.timestamp.serialize_cbor(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_eventbridgev2.types.timestamp

        out["LastModifiedTime"] = capo_eventbridgev2.types.timestamp.serialize_cbor(
            value["last_modified_time"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeSubscriberResponse:
    out: DescribeSubscriberResponse = {}  # type: ignore[typeddict-item]
    if data.get("SubscriberArn") is not None:
        out["subscriber_arn"] = data["SubscriberArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    if data.get("InvokeConfiguration") is not None:
        import capo_eventbridgev2.types.invoke_configuration

        out["invoke_configuration"] = (
            capo_eventbridgev2.types.invoke_configuration.deserialize_cbor(
                data["InvokeConfiguration"]
            )
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
    if data.get("Revoked") is not None:
        out["revoked"] = data["Revoked"]
    if data.get("CreationTime") is not None:
        import capo_eventbridgev2.types.timestamp

        out["creation_time"] = capo_eventbridgev2.types.timestamp.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_eventbridgev2.types.timestamp

        out["last_modified_time"] = capo_eventbridgev2.types.timestamp.deserialize_cbor(
            data["LastModifiedTime"]
        )
    return out


def redact_sensitive(value: DescribeSubscriberResponse) -> dict[str, Any]:
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
