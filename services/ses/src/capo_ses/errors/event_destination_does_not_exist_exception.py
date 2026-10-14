"""Generated from Smithy shape ``com.amazonaws.ses#EventDestinationDoesNotExistException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.configuration_set_name
    import capo_ses.types.error_message
    import capo_ses.types.event_destination_name


class EventDestinationDoesNotExistException_(TypedDict, closed=True):
    configuration_set_name: NotRequired[
        "capo_ses.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>Indicates that the configuration set does not exist.</p>"""
    event_destination_name: NotRequired[
        "capo_ses.types.event_destination_name.EventDestinationName"
    ]
    """<p>Indicates that the event destination does not exist.</p>"""
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: EventDestinationDoesNotExistException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "configuration_set_name" in value:
        pairs.append(
            (f"{key_prefix}ConfigurationSetName", str(value["configuration_set_name"]))
        )
    if "event_destination_name" in value:
        pairs.append(
            (f"{key_prefix}EventDestinationName", str(value["event_destination_name"]))
        )
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> EventDestinationDoesNotExistException_:
    out: EventDestinationDoesNotExistException_ = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    child_event_destination_name = el.find("EventDestinationName")
    if child_event_destination_name is not None:
        out["event_destination_name"] = str(child_event_destination_name.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class EventDestinationDoesNotExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#EventDestinationDoesNotExistException``."""

    code: str | None = "EventDestinationDoesNotExistException"

    def __init__(
        self,
        data: EventDestinationDoesNotExistException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EventDestinationDoesNotExistException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "EventDestinationDoesNotExistException":
        return cls(deserialize_query(el), message, response=response)
