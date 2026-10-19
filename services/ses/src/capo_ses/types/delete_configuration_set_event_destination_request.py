"""Generated from Smithy shape ``com.amazonaws.ses#DeleteConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.configuration_set_name
    import capo_ses.types.event_destination_name


class DeleteConfigurationSetEventDestinationRequest(TypedDict, closed=True):
    configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName"
    """<p>The name of the configuration set from which to delete the event destination.</p>"""
    event_destination_name: "capo_ses.types.event_destination_name.EventDestinationName"
    """<p>The name of the event destination to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteConfigurationSetEventDestinationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}ConfigurationSetName", str(value["configuration_set_name"]))
    )
    pairs.append(
        (f"{key_prefix}EventDestinationName", str(value["event_destination_name"]))
    )


def deserialize_query(el: Element) -> DeleteConfigurationSetEventDestinationRequest:
    out: DeleteConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    else:
        out["configuration_set_name"] = ""
    child_event_destination_name = el.find("EventDestinationName")
    if child_event_destination_name is not None:
        out["event_destination_name"] = str(child_event_destination_name.text or "")
    else:
        out["event_destination_name"] = ""
    return out
