"""Generated from Smithy shape ``com.amazonaws.iam#ServiceNotSupportedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import ServiceError

if TYPE_CHECKING:
    import capo_iam.types.service_not_supported_message


class ServiceNotSupportedException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_iam.types.service_not_supported_message.serviceNotSupportedMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceNotSupportedException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> ServiceNotSupportedException_:
    out: ServiceNotSupportedException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ServiceNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#ServiceNotSupportedException``."""

    code: str | None = "ServiceNotSupportedException"

    def __init__(
        self,
        data: ServiceNotSupportedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceNotSupportedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceNotSupportedException":
        return cls(deserialize_query(el), message, response=response)
