"""Generated from Smithy shape ``com.amazonaws.cloudfront#TestFunctionFailed``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class TestFunctionFailed_(TypedDict, closed=True):
    message: NotRequired["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: TestFunctionFailed_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> TestFunctionFailed_:
    out: TestFunctionFailed_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TestFunctionFailed(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#TestFunctionFailed``."""

    code: str | None = "TestFunctionFailed"

    def __init__(
        self,
        data: TestFunctionFailed_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="TestFunctionFailed",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "TestFunctionFailed":
        return cls(deserialize_xml(el), message, response=response)
