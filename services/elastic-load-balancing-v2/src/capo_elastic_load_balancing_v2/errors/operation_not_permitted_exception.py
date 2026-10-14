"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#OperationNotPermittedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element
from capo_elastic_load_balancing_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.error_description


class OperationNotPermittedException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_elastic_load_balancing_v2.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: OperationNotPermittedException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> OperationNotPermittedException_:
    out: OperationNotPermittedException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class OperationNotPermittedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancingv2#OperationNotPermittedException``."""

    code: str | None = "OperationNotPermittedException"

    def __init__(
        self,
        data: OperationNotPermittedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OperationNotPermittedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "OperationNotPermittedException":
        return cls(deserialize_query(el), message, response=response)
