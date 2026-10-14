"""Generated from Smithy shape ``com.amazonaws.ses#InvalidTrackingOptionsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.error_message


class InvalidTrackingOptionsException_(TypedDict, closed=True):
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidTrackingOptionsException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidTrackingOptionsException_:
    out: InvalidTrackingOptionsException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidTrackingOptionsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#InvalidTrackingOptionsException``."""

    code: str | None = "InvalidTrackingOptionsException"

    def __init__(
        self,
        data: InvalidTrackingOptionsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidTrackingOptionsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidTrackingOptionsException":
        return cls(deserialize_query(el), message, response=response)
