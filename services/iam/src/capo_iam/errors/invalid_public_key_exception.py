"""Generated from Smithy shape ``com.amazonaws.iam#InvalidPublicKeyException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import ServiceError

if TYPE_CHECKING:
    import capo_iam.types.invalid_public_key_message


class InvalidPublicKeyException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_iam.types.invalid_public_key_message.invalidPublicKeyMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidPublicKeyException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidPublicKeyException_:
    out: InvalidPublicKeyException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidPublicKeyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#InvalidPublicKeyException``."""

    code: str | None = "InvalidPublicKeyException"

    def __init__(
        self,
        data: InvalidPublicKeyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPublicKeyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidPublicKeyException":
        return cls(deserialize_query(el), message, response=response)
