"""Generated from Smithy shape ``com.amazonaws.ses#UpdateConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.configuration_set_name
    import capo_ses.types.event_destination


class UpdateConfigurationSetEventDestinationRequest(TypedDict, closed=True):
    configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName"
    """<p>The name of the configuration set that contains the event destination.</p>"""
    event_destination: "capo_ses.types.event_destination.EventDestination"
    """<p>The event destination object.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateConfigurationSetEventDestinationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}ConfigurationSetName", str(value["configuration_set_name"]))
    )
    import capo_ses.types.event_destination

    capo_ses.types.event_destination.serialize_query(
        value["event_destination"], pairs, f"{key_prefix}EventDestination"
    )


def deserialize_query(el: Element) -> UpdateConfigurationSetEventDestinationRequest:
    out: UpdateConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    else:
        out["configuration_set_name"] = ""
    child_event_destination = el.find("EventDestination")
    if child_event_destination is not None:
        import capo_ses.types.event_destination

        out["event_destination"] = capo_ses.types.event_destination.deserialize_query(
            child_event_destination
        )
    else:
        raise DeserializationError(
            "UpdateConfigurationSetEventDestinationRequest.event_destination required"
        )
    return out
