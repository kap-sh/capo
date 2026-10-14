"""Generated from Smithy shape ``com.amazonaws.sns#FilterPolicyLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import ServiceError

if TYPE_CHECKING:
    import capo_sns.types.string


class FilterPolicyLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_sns.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: FilterPolicyLimitExceededException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> FilterPolicyLimitExceededException_:
    out: FilterPolicyLimitExceededException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class FilterPolicyLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sns#FilterPolicyLimitExceededException``."""

    code: str | None = "FilterPolicyLimitExceededException"

    def __init__(
        self,
        data: FilterPolicyLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FilterPolicyLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "FilterPolicyLimitExceededException":
        return cls(deserialize_query(el), message, response=response)
