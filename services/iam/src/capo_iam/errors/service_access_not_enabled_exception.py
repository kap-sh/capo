"""Generated from Smithy shape ``com.amazonaws.iam#ServiceAccessNotEnabledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import ServiceError

if TYPE_CHECKING:
    import capo_iam.types.exception_message


class ServiceAccessNotEnabledException_(TypedDict, closed=True):
    message: NotRequired["capo_iam.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceAccessNotEnabledException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> ServiceAccessNotEnabledException_:
    out: ServiceAccessNotEnabledException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ServiceAccessNotEnabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#ServiceAccessNotEnabledException``."""

    code: str | None = "ServiceAccessNotEnabledException"

    def __init__(
        self,
        data: ServiceAccessNotEnabledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceAccessNotEnabledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceAccessNotEnabledException":
        return cls(deserialize_query(el), message, response=response)
