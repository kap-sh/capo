"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventSourceConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_eventbridgev2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.aws_service_events_source_configuration
    import capo_eventbridgev2.types.partner_events_source_configuration


class _EventSourceConfiguration_AwsServiceEventsConfiguration(TypedDict, closed=True):
    AwsServiceEventsConfiguration: "capo_eventbridgev2.types.aws_service_events_source_configuration.AwsServiceEventsSourceConfiguration"


class _EventSourceConfiguration_PartnerEventsConfiguration(TypedDict, closed=True):
    PartnerEventsConfiguration: "capo_eventbridgev2.types.partner_events_source_configuration.PartnerEventsSourceConfiguration"


EventSourceConfiguration: TypeAlias = (
    _EventSourceConfiguration_AwsServiceEventsConfiguration
    | _EventSourceConfiguration_PartnerEventsConfiguration
)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventSourceConfiguration) -> dict:
    if "AwsServiceEventsConfiguration" in value:
        import capo_eventbridgev2.types.aws_service_events_source_configuration

        return {
            "AwsServiceEventsConfiguration": capo_eventbridgev2.types.aws_service_events_source_configuration.serialize_cbor(
                value["AwsServiceEventsConfiguration"]
            )
        }
    elif "PartnerEventsConfiguration" in value:
        import capo_eventbridgev2.types.partner_events_source_configuration

        return {
            "PartnerEventsConfiguration": capo_eventbridgev2.types.partner_events_source_configuration.serialize_cbor(
                value["PartnerEventsConfiguration"]
            )
        }
    else:
        raise SerializationError("EventSourceConfiguration: no variant present")


def deserialize_cbor(data: dict) -> EventSourceConfiguration:
    if data.get("AwsServiceEventsConfiguration") is not None:
        import capo_eventbridgev2.types.aws_service_events_source_configuration

        return {
            "AwsServiceEventsConfiguration": capo_eventbridgev2.types.aws_service_events_source_configuration.deserialize_cbor(
                data["AwsServiceEventsConfiguration"]
            )
        }
    elif data.get("PartnerEventsConfiguration") is not None:
        import capo_eventbridgev2.types.partner_events_source_configuration

        return {
            "PartnerEventsConfiguration": capo_eventbridgev2.types.partner_events_source_configuration.deserialize_cbor(
                data["PartnerEventsConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "EventSourceConfiguration: no recognized variant key"
        )


def redact_sensitive(value: EventSourceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "AwsServiceEventsConfiguration" in value:
        import capo_eventbridgev2.types.aws_service_events_source_configuration

        out["AwsServiceEventsConfiguration"] = (
            capo_eventbridgev2.types.aws_service_events_source_configuration.redact_sensitive(
                value["AwsServiceEventsConfiguration"]
            )
        )
    if "PartnerEventsConfiguration" in value:
        import capo_eventbridgev2.types.partner_events_source_configuration

        out["PartnerEventsConfiguration"] = (
            capo_eventbridgev2.types.partner_events_source_configuration.redact_sensitive(
                value["PartnerEventsConfiguration"]
            )
        )
    return out
