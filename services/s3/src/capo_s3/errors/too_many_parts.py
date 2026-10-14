"""Generated from Smithy shape ``com.amazonaws.s3#TooManyParts``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class TooManyParts_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: TooManyParts_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> TooManyParts_:
    out: TooManyParts_ = {}  # type: ignore[typeddict-item]
    return out


class TooManyParts(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#TooManyParts``."""

    code: str | None = "TooManyParts"

    def __init__(
        self,
        data: TooManyParts_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyParts",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyParts":
        return cls(deserialize_xml(el), message, response=response)
