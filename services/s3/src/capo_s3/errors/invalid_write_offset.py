"""Generated from Smithy shape ``com.amazonaws.s3#InvalidWriteOffset``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class InvalidWriteOffset_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: InvalidWriteOffset_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> InvalidWriteOffset_:
    out: InvalidWriteOffset_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidWriteOffset(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#InvalidWriteOffset``."""

    code: str | None = "InvalidWriteOffset"

    def __init__(
        self,
        data: InvalidWriteOffset_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidWriteOffset",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidWriteOffset":
        return cls(deserialize_xml(el), message, response=response)
