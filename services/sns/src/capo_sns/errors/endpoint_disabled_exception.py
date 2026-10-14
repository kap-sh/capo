"""Generated from Smithy shape ``com.amazonaws.sns#EndpointDisabledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import ServiceError

if TYPE_CHECKING:
    import capo_sns.types.string


class EndpointDisabledException_(TypedDict, closed=True):
    message: NotRequired["capo_sns.types.string.String"]
    """<p>Message for endpoint disabled.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EndpointDisabledException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> EndpointDisabledException_:
    out: EndpointDisabledException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class EndpointDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sns#EndpointDisabledException``."""

    code: str | None = "EndpointDisabledException"

    def __init__(
        self,
        data: EndpointDisabledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EndpointDisabledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "EndpointDisabledException":
        return cls(deserialize_query(el), message, response=response)
