"""Generated from Smithy shape ``com.amazonaws.s3#InvalidObjectState``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError

if TYPE_CHECKING:
    import capo_s3.types.intelligent_tiering_access_tier
    import capo_s3.types.storage_class


class InvalidObjectState_(TypedDict, closed=True):
    storage_class: NotRequired["capo_s3.types.storage_class.StorageClass"]
    access_tier: NotRequired[
        "capo_s3.types.intelligent_tiering_access_tier.IntelligentTieringAccessTier"
    ]


# --- restXml ser/de ---
def serialize_xml(value: InvalidObjectState_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "storage_class" in value:
        import capo_s3.types.storage_class

        capo_s3.types.storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )
    if "access_tier" in value:
        import capo_s3.types.intelligent_tiering_access_tier

        capo_s3.types.intelligent_tiering_access_tier.serialize_xml(
            value["access_tier"], el, "AccessTier"
        )


def deserialize_xml(el: Element) -> InvalidObjectState_:
    out: InvalidObjectState_ = {}  # type: ignore[typeddict-item]
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3.types.storage_class

        out["storage_class"] = capo_s3.types.storage_class.deserialize_xml(
            child_storage_class
        )
    child_access_tier = el.find("AccessTier")
    if child_access_tier is not None:
        import capo_s3.types.intelligent_tiering_access_tier

        out["access_tier"] = (
            capo_s3.types.intelligent_tiering_access_tier.deserialize_xml(
                child_access_tier
            )
        )
    return out


class InvalidObjectState(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#InvalidObjectState``."""

    code: str | None = "InvalidObjectState"

    def __init__(
        self,
        data: InvalidObjectState_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidObjectState",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidObjectState":
        return cls(deserialize_xml(el), message, response=response)
