"""Generated from Smithy shape ``com.amazonaws.s3#ObjectNotInActiveTierError``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class ObjectNotInActiveTierError_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: ObjectNotInActiveTierError_, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ObjectNotInActiveTierError_:
    out: ObjectNotInActiveTierError_ = {}  # type: ignore[typeddict-item]
    return out


class ObjectNotInActiveTierError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#ObjectNotInActiveTierError``."""

    code: str | None = "ObjectNotInActiveTierError"

    def __init__(
        self,
        data: ObjectNotInActiveTierError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ObjectNotInActiveTierError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ObjectNotInActiveTierError":
        return cls(deserialize_xml(el), message, response=response)
