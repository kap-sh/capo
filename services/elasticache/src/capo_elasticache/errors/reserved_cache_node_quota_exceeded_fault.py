"""Generated from Smithy shape ``com.amazonaws.elasticache#ReservedCacheNodeQuotaExceededFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element
from capo_elasticache.errors import ServiceError

if TYPE_CHECKING:
    import capo_elasticache.types.exception_message


class ReservedCacheNodeQuotaExceededFault_(TypedDict, closed=True):
    message: NotRequired["capo_elasticache.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedCacheNodeQuotaExceededFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> ReservedCacheNodeQuotaExceededFault_:
    out: ReservedCacheNodeQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ReservedCacheNodeQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticache#ReservedCacheNodeQuotaExceededFault``."""

    code: str | None = "ReservedCacheNodeQuotaExceededFault"

    def __init__(
        self,
        data: ReservedCacheNodeQuotaExceededFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReservedCacheNodeQuotaExceededFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ReservedCacheNodeQuotaExceededFault":
        return cls(deserialize_query(el), message, response=response)
