"""Generated from Smithy shape ``com.amazonaws.sts#PackedPolicyTooLargeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element
from capo_sts.errors import ServiceError

if TYPE_CHECKING:
    import capo_sts.types.packed_policy_too_large_message


class PackedPolicyTooLargeException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_sts.types.packed_policy_too_large_message.packedPolicyTooLargeMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: PackedPolicyTooLargeException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> PackedPolicyTooLargeException_:
    out: PackedPolicyTooLargeException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class PackedPolicyTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sts#PackedPolicyTooLargeException``."""

    code: str | None = "PackedPolicyTooLargeException"

    def __init__(
        self,
        data: PackedPolicyTooLargeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PackedPolicyTooLargeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "PackedPolicyTooLargeException":
        return cls(deserialize_query(el), message, response=response)
