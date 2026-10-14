"""Generated from Smithy shape ``com.amazonaws.s3#IdempotencyParameterMismatch``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class IdempotencyParameterMismatch_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: IdempotencyParameterMismatch_, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> IdempotencyParameterMismatch_:
    out: IdempotencyParameterMismatch_ = {}  # type: ignore[typeddict-item]
    return out


class IdempotencyParameterMismatch(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#IdempotencyParameterMismatch``."""

    code: str | None = "IdempotencyParameterMismatch"

    def __init__(
        self,
        data: IdempotencyParameterMismatch_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotencyParameterMismatch",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "IdempotencyParameterMismatch":
        return cls(deserialize_xml(el), message, response=response)
