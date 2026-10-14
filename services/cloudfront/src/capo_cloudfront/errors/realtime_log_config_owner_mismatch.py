"""Generated from Smithy shape ``com.amazonaws.cloudfront#RealtimeLogConfigOwnerMismatch``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class RealtimeLogConfigOwnerMismatch_(TypedDict, closed=True):
    message: NotRequired["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: RealtimeLogConfigOwnerMismatch_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> RealtimeLogConfigOwnerMismatch_:
    out: RealtimeLogConfigOwnerMismatch_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class RealtimeLogConfigOwnerMismatch(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#RealtimeLogConfigOwnerMismatch``."""

    code: str | None = "RealtimeLogConfigOwnerMismatch"

    def __init__(
        self,
        data: RealtimeLogConfigOwnerMismatch_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RealtimeLogConfigOwnerMismatch",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "RealtimeLogConfigOwnerMismatch":
        return cls(deserialize_xml(el), message, response=response)
