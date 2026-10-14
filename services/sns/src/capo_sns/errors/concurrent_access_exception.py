"""Generated from Smithy shape ``com.amazonaws.sns#ConcurrentAccessException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import ServiceError

if TYPE_CHECKING:
    import capo_sns.types.string


class ConcurrentAccessException_(TypedDict, closed=True):
    message: NotRequired["capo_sns.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ConcurrentAccessException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> ConcurrentAccessException_:
    out: ConcurrentAccessException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ConcurrentAccessException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sns#ConcurrentAccessException``."""

    code: str | None = "ConcurrentAccessException"

    def __init__(
        self,
        data: ConcurrentAccessException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentAccessException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ConcurrentAccessException":
        return cls(deserialize_query(el), message, response=response)
