"""Generated from Smithy shape ``com.amazonaws.s3#ObjectAlreadyInActiveTierError``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class ObjectAlreadyInActiveTierError_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: ObjectAlreadyInActiveTierError_, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ObjectAlreadyInActiveTierError_:
    out: ObjectAlreadyInActiveTierError_ = {}  # type: ignore[typeddict-item]
    return out


class ObjectAlreadyInActiveTierError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#ObjectAlreadyInActiveTierError``."""

    code: str | None = "ObjectAlreadyInActiveTierError"

    def __init__(
        self,
        data: ObjectAlreadyInActiveTierError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ObjectAlreadyInActiveTierError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ObjectAlreadyInActiveTierError":
        return cls(deserialize_xml(el), message, response=response)
