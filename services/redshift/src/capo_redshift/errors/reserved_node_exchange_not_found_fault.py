"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeExchangeNotFoundFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import ServiceError

if TYPE_CHECKING:
    import capo_redshift.types.exception_message


class ReservedNodeExchangeNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNodeExchangeNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> ReservedNodeExchangeNotFoundFault_:
    out: ReservedNodeExchangeNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ReservedNodeExchangeNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#ReservedNodeExchangeNotFoundFault``."""

    code: str | None = "ReservedNodeExchangeNotFoundFault"

    def __init__(
        self,
        data: ReservedNodeExchangeNotFoundFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReservedNodeExchangeNotFoundFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ReservedNodeExchangeNotFoundFault":
        return cls(deserialize_query(el), message, response=response)
