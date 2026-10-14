"""Generated from Smithy shape ``com.amazonaws.cloudformation#OperationIdAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element
from capo_cloudformation.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudformation.types.error_message


class OperationIdAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudformation.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: OperationIdAlreadyExistsException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> OperationIdAlreadyExistsException_:
    out: OperationIdAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class OperationIdAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudformation#OperationIdAlreadyExistsException``."""

    code: str | None = "OperationIdAlreadyExistsException"

    def __init__(
        self,
        data: OperationIdAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OperationIdAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "OperationIdAlreadyExistsException":
        return cls(deserialize_query(el), message, response=response)
