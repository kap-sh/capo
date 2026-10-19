"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PartnerEventsSourceConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_pattern
    import capo_eventbridgev2.types.kms_key_identifier
    import capo_eventbridgev2.types.on_failure_configuration
    import capo_eventbridgev2.types.partner_event_source_arn


class PartnerEventsSourceConfiguration(TypedDict, closed=True):
    partner_event_source_arn: (
        "capo_eventbridgev2.types.partner_event_source_arn.PartnerEventSourceArn"
    )
    pattern: NotRequired["capo_eventbridgev2.types.event_pattern.EventPattern"]
    """A filter pattern, as a JSON string, that defines which of the partner event source's events are forwarded to the event bus. If no pattern is specified, all events from the partner event source are forwarded."""
    partner_bus_kms_key_identifier: NotRequired[
        "capo_eventbridgev2.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    on_failure_configuration: NotRequired[
        "capo_eventbridgev2.types.on_failure_configuration.OnFailureConfiguration"
    ]
    """The destination for events that could not be forwarded, covering both the forwarding target and the managed partner event bus."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PartnerEventsSourceConfiguration) -> dict:
    out: dict = {}
    out["PartnerEventSourceArn"] = value["partner_event_source_arn"]
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    if "partner_bus_kms_key_identifier" in value:
        out["PartnerBusKmsKeyIdentifier"] = value["partner_bus_kms_key_identifier"]
    if "on_failure_configuration" in value:
        import capo_eventbridgev2.types.on_failure_configuration

        out["OnFailureConfiguration"] = (
            capo_eventbridgev2.types.on_failure_configuration.serialize_cbor(
                value["on_failure_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PartnerEventsSourceConfiguration:
    out: PartnerEventsSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("PartnerEventSourceArn") is not None:
        out["partner_event_source_arn"] = data["PartnerEventSourceArn"]
    else:
        out["partner_event_source_arn"] = ""
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    if data.get("PartnerBusKmsKeyIdentifier") is not None:
        out["partner_bus_kms_key_identifier"] = data["PartnerBusKmsKeyIdentifier"]
    if data.get("OnFailureConfiguration") is not None:
        import capo_eventbridgev2.types.on_failure_configuration

        out["on_failure_configuration"] = (
            capo_eventbridgev2.types.on_failure_configuration.deserialize_cbor(
                data["OnFailureConfiguration"]
            )
        )
    return out


def redact_sensitive(value: PartnerEventsSourceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pattern" in value:
        out["pattern"] = "*** Sensitive Data Redacted ***"
    return out
