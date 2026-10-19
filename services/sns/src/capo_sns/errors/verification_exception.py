"""Generated from Smithy shape ``com.amazonaws.sns#VerificationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import ServiceError

if TYPE_CHECKING:
    import capo_sns.types.string


class VerificationException_(TypedDict, closed=True):
    message: "capo_sns.types.string.String"
    status: "capo_sns.types.string.String"
    """<p>The status of the verification error.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VerificationException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Message", str(value["message"])))
    pairs.append((f"{key_prefix}Status", str(value["status"])))


def deserialize_query(el: Element) -> VerificationException_:
    out: VerificationException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    else:
        out["message"] = ""
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        out["status"] = ""
    return out


class VerificationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sns#VerificationException``."""

    code: str | None = "VerificationException"

    def __init__(
        self,
        data: VerificationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="VerificationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "VerificationException":
        return cls(deserialize_query(el), message, response=response)
