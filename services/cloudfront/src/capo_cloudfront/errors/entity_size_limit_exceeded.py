"""Generated from Smithy shape ``com.amazonaws.cloudfront#EntitySizeLimitExceeded``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class EntitySizeLimitExceeded_(TypedDict, closed=True):
    message: NotRequired["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: EntitySizeLimitExceeded_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> EntitySizeLimitExceeded_:
    out: EntitySizeLimitExceeded_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class EntitySizeLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#EntitySizeLimitExceeded``."""

    code: str | None = "EntitySizeLimitExceeded"

    def __init__(
        self,
        data: EntitySizeLimitExceeded_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntitySizeLimitExceeded",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "EntitySizeLimitExceeded":
        return cls(deserialize_xml(el), message, response=response)
