"""Generated from Smithy shape ``com.amazonaws.cloudfront#TooManyDistributionsAssociatedToResponseHeadersPolicy``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class TooManyDistributionsAssociatedToResponseHeadersPolicy_(TypedDict, closed=True):
    message: NotRequired["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: TooManyDistributionsAssociatedToResponseHeadersPolicy_,
    parent: Element,
    tag: str,
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(
    el: Element,
) -> TooManyDistributionsAssociatedToResponseHeadersPolicy_:
    out: TooManyDistributionsAssociatedToResponseHeadersPolicy_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyDistributionsAssociatedToResponseHeadersPolicy(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#TooManyDistributionsAssociatedToResponseHeadersPolicy``."""

    code: str | None = "TooManyDistributionsAssociatedToResponseHeadersPolicy"

    def __init__(
        self,
        data: TooManyDistributionsAssociatedToResponseHeadersPolicy_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyDistributionsAssociatedToResponseHeadersPolicy",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyDistributionsAssociatedToResponseHeadersPolicy":
        return cls(deserialize_xml(el), message, response=response)
