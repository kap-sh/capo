"""Generated from Smithy shape ``com.amazonaws.s3#NoSuchAnnotation``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class NoSuchAnnotation_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: NoSuchAnnotation_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> NoSuchAnnotation_:
    out: NoSuchAnnotation_ = {}  # type: ignore[typeddict-item]
    return out


class NoSuchAnnotation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#NoSuchAnnotation``."""

    code: str | None = "NoSuchAnnotation"

    def __init__(
        self,
        data: NoSuchAnnotation_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchAnnotation",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "NoSuchAnnotation":
        return cls(deserialize_xml(el), message, response=response)
