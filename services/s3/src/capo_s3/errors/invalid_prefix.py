"""Generated from Smithy shape ``com.amazonaws.s3#InvalidPrefix``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class InvalidPrefix_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: InvalidPrefix_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> InvalidPrefix_:
    out: InvalidPrefix_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidPrefix(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#InvalidPrefix``."""

    code: str | None = "InvalidPrefix"

    def __init__(
        self,
        data: InvalidPrefix_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPrefix",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidPrefix":
        return cls(deserialize_xml(el), message, response=response)
