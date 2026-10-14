"""Generated from Smithy shape ``com.amazonaws.s3#InvalidAnnotationName``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class InvalidAnnotationName_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: InvalidAnnotationName_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> InvalidAnnotationName_:
    out: InvalidAnnotationName_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidAnnotationName(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#InvalidAnnotationName``."""

    code: str | None = "InvalidAnnotationName"

    def __init__(
        self,
        data: InvalidAnnotationName_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAnnotationName",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidAnnotationName":
        return cls(deserialize_xml(el), message, response=response)
