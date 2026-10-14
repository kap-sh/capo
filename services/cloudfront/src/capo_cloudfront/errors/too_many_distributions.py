"""Generated from Smithy shape ``com.amazonaws.cloudfront#TooManyDistributions``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class TooManyDistributions_(TypedDict, closed=True):
    message: NotRequired["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: TooManyDistributions_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> TooManyDistributions_:
    out: TooManyDistributions_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyDistributions(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#TooManyDistributions``."""

    code: str | None = "TooManyDistributions"

    def __init__(
        self,
        data: TooManyDistributions_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyDistributions",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyDistributions":
        return cls(deserialize_xml(el), message, response=response)
