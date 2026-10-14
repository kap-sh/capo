"""Generated from Smithy shape ``com.amazonaws.redshift#Ipv6CidrBlockNotFoundFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import ServiceError

if TYPE_CHECKING:
    import capo_redshift.types.exception_message


class Ipv6CidrBlockNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Ipv6CidrBlockNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> Ipv6CidrBlockNotFoundFault_:
    out: Ipv6CidrBlockNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class Ipv6CidrBlockNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#Ipv6CidrBlockNotFoundFault``."""

    code: str | None = "Ipv6CidrBlockNotFoundFault"

    def __init__(
        self,
        data: Ipv6CidrBlockNotFoundFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="Ipv6CidrBlockNotFoundFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "Ipv6CidrBlockNotFoundFault":
        return cls(deserialize_query(el), message, response=response)
