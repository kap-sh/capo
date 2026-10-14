"""Generated from Smithy shape ``com.amazonaws.autoscaling#IdempotentCallInProgressFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element
from capo_auto_scaling.errors import ServiceError

if TYPE_CHECKING:
    import capo_auto_scaling.types.xml_string_max_len255


class IdempotentCallInProgressFault_(TypedDict, closed=True):
    message: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: IdempotentCallInProgressFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> IdempotentCallInProgressFault_:
    out: IdempotentCallInProgressFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class IdempotentCallInProgressFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.autoscaling#IdempotentCallInProgressFault``."""

    code: str | None = "IdempotentCallInProgressFault"

    def __init__(
        self,
        data: IdempotentCallInProgressFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotentCallInProgressFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "IdempotentCallInProgressFault":
        return cls(deserialize_query(el), message, response=response)
