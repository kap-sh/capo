"""Generated from Smithy shape ``com.amazonaws.s3#AnnotationLimitExceeded``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class AnnotationLimitExceeded_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: AnnotationLimitExceeded_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> AnnotationLimitExceeded_:
    out: AnnotationLimitExceeded_ = {}  # type: ignore[typeddict-item]
    return out


class AnnotationLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#AnnotationLimitExceeded``."""

    code: str | None = "AnnotationLimitExceeded"

    def __init__(
        self,
        data: AnnotationLimitExceeded_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AnnotationLimitExceeded",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "AnnotationLimitExceeded":
        return cls(deserialize_xml(el), message, response=response)
