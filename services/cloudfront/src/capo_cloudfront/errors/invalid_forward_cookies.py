"""Generated from Smithy shape ``com.amazonaws.cloudfront#InvalidForwardCookies``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class InvalidForwardCookies_(TypedDict, closed=True):
    message: NotRequired["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: InvalidForwardCookies_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> InvalidForwardCookies_:
    out: InvalidForwardCookies_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidForwardCookies(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#InvalidForwardCookies``."""

    code: str | None = "InvalidForwardCookies"

    def __init__(
        self,
        data: InvalidForwardCookies_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidForwardCookies",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidForwardCookies":
        return cls(deserialize_xml(el), message, response=response)
