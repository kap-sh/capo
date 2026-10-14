"""Generated from Smithy shape ``com.amazonaws.s3#AccessDenied``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class AccessDenied_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: AccessDenied_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> AccessDenied_:
    out: AccessDenied_ = {}  # type: ignore[typeddict-item]
    return out


class AccessDenied(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#AccessDenied``."""

    code: str | None = "AccessDenied"

    def __init__(
        self,
        data: AccessDenied_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDenied",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "AccessDenied":
        return cls(deserialize_xml(el), message, response=response)
