"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#AwsServiceEventsSourceConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.aws_service_source
    import capo_eventbridgev2.types.event_pattern
    import capo_eventbridgev2.types.on_failure_configuration


class AwsServiceEventsSourceConfiguration(TypedDict, closed=True):
    aws_service: "capo_eventbridgev2.types.aws_service_source.AwsServiceSource"
    pattern: NotRequired["capo_eventbridgev2.types.event_pattern.EventPattern"]
    """A filter pattern, as a JSON string, that defines which of the service's events are forwarded to the event bus. Do not include source, account, or region as top-level fields. If no pattern is specified, all events from the service are forwarded."""
    on_failure_configuration: NotRequired[
        "capo_eventbridgev2.types.on_failure_configuration.OnFailureConfiguration"
    ]
    """The destination for events that could not be forwarded."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AwsServiceEventsSourceConfiguration) -> dict:
    out: dict = {}
    out["AwsService"] = value["aws_service"]
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    if "on_failure_configuration" in value:
        import capo_eventbridgev2.types.on_failure_configuration

        out["OnFailureConfiguration"] = (
            capo_eventbridgev2.types.on_failure_configuration.serialize_cbor(
                value["on_failure_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AwsServiceEventsSourceConfiguration:
    out: AwsServiceEventsSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AwsService") is not None:
        out["aws_service"] = data["AwsService"]
    else:
        out["aws_service"] = ""
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    if data.get("OnFailureConfiguration") is not None:
        import capo_eventbridgev2.types.on_failure_configuration

        out["on_failure_configuration"] = (
            capo_eventbridgev2.types.on_failure_configuration.deserialize_cbor(
                data["OnFailureConfiguration"]
            )
        )
    return out


def redact_sensitive(value: AwsServiceEventsSourceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pattern" in value:
        out["pattern"] = "*** Sensitive Data Redacted ***"
    return out
