"""Generated from Smithy shape ``com.amazonaws.s3#NoSuchBucket``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class NoSuchBucket_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: NoSuchBucket_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> NoSuchBucket_:
    out: NoSuchBucket_ = {}  # type: ignore[typeddict-item]
    return out


class NoSuchBucket(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#NoSuchBucket``."""

    code: str | None = "NoSuchBucket"

    def __init__(
        self,
        data: NoSuchBucket_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchBucket",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "NoSuchBucket":
        return cls(deserialize_xml(el), message, response=response)
