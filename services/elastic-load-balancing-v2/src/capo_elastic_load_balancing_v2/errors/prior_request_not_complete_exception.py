"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#PriorRequestNotCompleteException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element
from capo_elastic_load_balancing_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.error_description


class PriorRequestNotCompleteException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_elastic_load_balancing_v2.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: PriorRequestNotCompleteException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> PriorRequestNotCompleteException_:
    out: PriorRequestNotCompleteException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class PriorRequestNotCompleteException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancingv2#PriorRequestNotCompleteException``."""

    code: str | None = "PriorRequestNotCompleteException"

    def __init__(
        self,
        data: PriorRequestNotCompleteException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PriorRequestNotCompleteException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "PriorRequestNotCompleteException":
        return cls(deserialize_query(el), message, response=response)
