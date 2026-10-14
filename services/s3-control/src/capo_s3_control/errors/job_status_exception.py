"""Generated from Smithy shape ``com.amazonaws.s3control#JobStatusException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import ServiceError

if TYPE_CHECKING:
    import capo_s3_control.types.exception_message


class JobStatusException_(TypedDict, closed=True):
    message: NotRequired["capo_s3_control.types.exception_message.ExceptionMessage"]


# --- restXml ser/de ---
def serialize_xml(value: JobStatusException_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> JobStatusException_:
    out: JobStatusException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class JobStatusException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3control#JobStatusException``."""

    code: str | None = "JobStatusException"

    def __init__(
        self,
        data: JobStatusException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="JobStatusException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "JobStatusException":
        return cls(deserialize_xml(el), message, response=response)
