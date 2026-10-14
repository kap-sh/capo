"""Generated from Smithy shape ``com.amazonaws.s3control#BucketAlreadyOwnedByYou``."""

import zapros
from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import ServiceError


class BucketAlreadyOwnedByYou_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: BucketAlreadyOwnedByYou_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> BucketAlreadyOwnedByYou_:
    out: BucketAlreadyOwnedByYou_ = {}  # type: ignore[typeddict-item]
    return out


class BucketAlreadyOwnedByYou(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3control#BucketAlreadyOwnedByYou``."""

    code: str | None = "BucketAlreadyOwnedByYou"

    def __init__(
        self,
        data: BucketAlreadyOwnedByYou_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BucketAlreadyOwnedByYou",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "BucketAlreadyOwnedByYou":
        return cls(deserialize_xml(el), message, response=response)
