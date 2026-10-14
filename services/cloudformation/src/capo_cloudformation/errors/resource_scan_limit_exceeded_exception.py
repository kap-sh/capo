"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceScanLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element
from capo_cloudformation.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudformation.types.error_message


class ResourceScanLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudformation.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceScanLimitExceededException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> ResourceScanLimitExceededException_:
    out: ResourceScanLimitExceededException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ResourceScanLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudformation#ResourceScanLimitExceededException``."""

    code: str | None = "ResourceScanLimitExceededException"

    def __init__(
        self,
        data: ResourceScanLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceScanLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceScanLimitExceededException":
        return cls(deserialize_query(el), message, response=response)
