"""Generated from Smithy shape ``com.amazonaws.opensearch#SlotNotAvailableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import ServiceError

if TYPE_CHECKING:
    import capo_opensearch.types.error_message
    import capo_opensearch.types.slot_list


class SlotNotAvailableException_(TypedDict, closed=True):
    slot_suggestions: NotRequired["capo_opensearch.types.slot_list.SlotList"]
    """<p>Alternate time slots during which OpenSearch Service has available capacity to schedule a domain action.</p>"""
    message: NotRequired["capo_opensearch.types.error_message.ErrorMessage"]
    """<p>A description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotNotAvailableException_) -> dict:
    out: dict = {}
    if "slot_suggestions" in value:
        import capo_opensearch.types.slot_list

        out["SlotSuggestions"] = capo_opensearch.types.slot_list.serialize_json(
            value["slot_suggestions"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SlotNotAvailableException_:
    out: SlotNotAvailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("SlotSuggestions") is not None:
        import capo_opensearch.types.slot_list

        out["slot_suggestions"] = capo_opensearch.types.slot_list.deserialize_json(
            data["SlotSuggestions"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class SlotNotAvailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.opensearch#SlotNotAvailableException``."""

    code: str | None = "SlotNotAvailableException"

    def __init__(
        self,
        data: SlotNotAvailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SlotNotAvailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SlotNotAvailableException":
        return cls(deserialize_json(data), message, response=response)
