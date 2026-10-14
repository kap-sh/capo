"""Generated from Smithy shape ``com.amazonaws.s3#BucketAlreadyExists``."""

import zapros
from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class BucketAlreadyExists_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: BucketAlreadyExists_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> BucketAlreadyExists_:
    out: BucketAlreadyExists_ = {}  # type: ignore[typeddict-item]
    return out


class BucketAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#BucketAlreadyExists``."""

    code: str | None = "BucketAlreadyExists"

    def __init__(
        self,
        data: BucketAlreadyExists_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BucketAlreadyExists",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "BucketAlreadyExists":
        return cls(deserialize_xml(el), message, response=response)
