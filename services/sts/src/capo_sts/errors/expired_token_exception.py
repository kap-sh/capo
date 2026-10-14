"""Generated from Smithy shape ``com.amazonaws.sts#ExpiredTokenException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element
from capo_sts.errors import ServiceError

if TYPE_CHECKING:
    import capo_sts.types.expired_identity_token_message


class ExpiredTokenException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_sts.types.expired_identity_token_message.expiredIdentityTokenMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ExpiredTokenException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> ExpiredTokenException_:
    out: ExpiredTokenException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ExpiredTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sts#ExpiredTokenException``."""

    code: str | None = "ExpiredTokenException"

    def __init__(
        self,
        data: ExpiredTokenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExpiredTokenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ExpiredTokenException":
        return cls(deserialize_query(el), message, response=response)
