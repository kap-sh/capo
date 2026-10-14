"""Generated from Smithy shape ``com.amazonaws.docdb#InvalidVPCNetworkStateFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element
from capo_docdb.errors import ServiceError

if TYPE_CHECKING:
    import capo_docdb.types.exception_message


class InvalidVPCNetworkStateFault_(TypedDict, closed=True):
    message: NotRequired["capo_docdb.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidVPCNetworkStateFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidVPCNetworkStateFault_:
    out: InvalidVPCNetworkStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidVPCNetworkStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.docdb#InvalidVPCNetworkStateFault``."""

    code: str | None = "InvalidVPCNetworkStateFault"

    def __init__(
        self,
        data: InvalidVPCNetworkStateFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidVPCNetworkStateFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidVPCNetworkStateFault":
        return cls(deserialize_query(el), message, response=response)
