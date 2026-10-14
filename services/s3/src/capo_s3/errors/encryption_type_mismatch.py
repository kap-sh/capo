"""Generated from Smithy shape ``com.amazonaws.s3#EncryptionTypeMismatch``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class EncryptionTypeMismatch_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: EncryptionTypeMismatch_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> EncryptionTypeMismatch_:
    out: EncryptionTypeMismatch_ = {}  # type: ignore[typeddict-item]
    return out


class EncryptionTypeMismatch(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#EncryptionTypeMismatch``."""

    code: str | None = "EncryptionTypeMismatch"

    def __init__(
        self,
        data: EncryptionTypeMismatch_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EncryptionTypeMismatch",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "EncryptionTypeMismatch":
        return cls(deserialize_xml(el), message, response=response)
