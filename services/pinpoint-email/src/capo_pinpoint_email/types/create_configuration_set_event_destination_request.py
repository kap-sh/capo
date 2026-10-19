"""Generated from Smithy shape ``com.amazonaws.pinpointemail#CreateConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.configuration_set_name
    import capo_pinpoint_email.types.event_destination_definition
    import capo_pinpoint_email.types.event_destination_name


class CreateConfigurationSetEventDestinationRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that you want to add an event destination to.</p>"""
    event_destination_name: (
        "capo_pinpoint_email.types.event_destination_name.EventDestinationName"
    )
    """<p>A name that identifies the event destination within the configuration set.</p>"""
    event_destination: "capo_pinpoint_email.types.event_destination_definition.EventDestinationDefinition"
    """<p>An object that defines the event destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationSetEventDestinationRequest) -> dict:
    out: dict = {}
    out["EventDestinationName"] = value["event_destination_name"]
    import capo_pinpoint_email.types.event_destination_definition

    out["EventDestination"] = (
        capo_pinpoint_email.types.event_destination_definition.serialize_json(
            value["event_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateConfigurationSetEventDestinationRequest:
    out: CreateConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventDestinationName") is not None:
        out["event_destination_name"] = data["EventDestinationName"]
    else:
        out["event_destination_name"] = ""
    if data.get("EventDestination") is not None:
        import capo_pinpoint_email.types.event_destination_definition

        out["event_destination"] = (
            capo_pinpoint_email.types.event_destination_definition.deserialize_json(
                data["EventDestination"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConfigurationSetEventDestinationRequest.event_destination required"
        )
    return out
