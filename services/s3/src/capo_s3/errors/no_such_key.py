"""Generated from Smithy shape ``com.amazonaws.s3#NoSuchKey``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class NoSuchKey_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: NoSuchKey_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> NoSuchKey_:
    out: NoSuchKey_ = {}  # type: ignore[typeddict-item]
    return out


class NoSuchKey(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#NoSuchKey``."""

    code: str | None = "NoSuchKey"

    def __init__(
        self, data: NoSuchKey_, message: str | None = None, *, response: zapros.Response
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchKey",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "NoSuchKey":
        return cls(deserialize_xml(el), message, response=response)
