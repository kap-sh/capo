"""Generated from Smithy shape ``com.amazonaws.s3#NotFound``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class NotFound_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: NotFound_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> NotFound_:
    out: NotFound_ = {}  # type: ignore[typeddict-item]
    return out


class NotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#NotFound``."""

    code: str | None = "NotFound"

    def __init__(
        self, data: NotFound_, message: str | None = None, *, response: zapros.Response
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotFound",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "NotFound":
        return cls(deserialize_xml(el), message, response=response)
