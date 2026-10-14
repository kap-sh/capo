"""Generated from Smithy shape ``com.amazonaws.cloudfront#TooManyPublicKeysInKeyGroup``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class TooManyPublicKeysInKeyGroup_(TypedDict, closed=True):
    message: NotRequired["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: TooManyPublicKeysInKeyGroup_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> TooManyPublicKeysInKeyGroup_:
    out: TooManyPublicKeysInKeyGroup_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyPublicKeysInKeyGroup(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#TooManyPublicKeysInKeyGroup``."""

    code: str | None = "TooManyPublicKeysInKeyGroup"

    def __init__(
        self,
        data: TooManyPublicKeysInKeyGroup_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyPublicKeysInKeyGroup",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyPublicKeysInKeyGroup":
        return cls(deserialize_xml(el), message, response=response)
