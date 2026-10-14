"""Generated from Smithy shape ``com.amazonaws.sts#OutboundWebIdentityFederationDisabledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element
from capo_sts.errors import ServiceError

if TYPE_CHECKING:
    import capo_sts.types.outbound_web_identity_federation_disabled_exception2


class OutboundWebIdentityFederationDisabledException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_sts.types.outbound_web_identity_federation_disabled_exception2.OutboundWebIdentityFederationDisabledException2"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: OutboundWebIdentityFederationDisabledException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> OutboundWebIdentityFederationDisabledException_:
    out: OutboundWebIdentityFederationDisabledException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class OutboundWebIdentityFederationDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sts#OutboundWebIdentityFederationDisabledException``."""

    code: str | None = "OutboundWebIdentityFederationDisabledException"

    def __init__(
        self,
        data: OutboundWebIdentityFederationDisabledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OutboundWebIdentityFederationDisabledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "OutboundWebIdentityFederationDisabledException":
        return cls(deserialize_query(el), message, response=response)
