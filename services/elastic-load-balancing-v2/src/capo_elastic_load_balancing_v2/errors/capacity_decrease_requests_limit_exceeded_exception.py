"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CapacityDecreaseRequestsLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element
from capo_elastic_load_balancing_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.error_description


class CapacityDecreaseRequestsLimitExceededException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_elastic_load_balancing_v2.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CapacityDecreaseRequestsLimitExceededException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> CapacityDecreaseRequestsLimitExceededException_:
    out: CapacityDecreaseRequestsLimitExceededException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CapacityDecreaseRequestsLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancingv2#CapacityDecreaseRequestsLimitExceededException``."""

    code: str | None = "CapacityDecreaseRequestsLimitExceededException"

    def __init__(
        self,
        data: CapacityDecreaseRequestsLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CapacityDecreaseRequestsLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "CapacityDecreaseRequestsLimitExceededException":
        return cls(deserialize_query(el), message, response=response)
