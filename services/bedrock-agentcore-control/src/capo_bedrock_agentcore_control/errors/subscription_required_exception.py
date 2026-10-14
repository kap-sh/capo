"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SubscriptionRequiredException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError, ServiceError


class SubscriptionRequiredException_(TypedDict, closed=True):
    message: "str"
    subscription_url: NotRequired["str"]
    """URL to the Marketplace listing for subscription"""
    product_name: NotRequired["str"]
    """The product requiring subscription"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionRequiredException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "subscription_url" in value:
        out["subscriptionUrl"] = value["subscription_url"]
    if "product_name" in value:
        out["productName"] = value["product_name"]
    return out


def deserialize_json(data: dict) -> SubscriptionRequiredException_:
    out: SubscriptionRequiredException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("SubscriptionRequiredException_.message required")
    if data.get("subscriptionUrl") is not None:
        out["subscription_url"] = data["subscriptionUrl"]
    if data.get("productName") is not None:
        out["product_name"] = data["productName"]
    return out


class SubscriptionRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SubscriptionRequiredException``."""

    code: str | None = "SubscriptionRequiredException"

    def __init__(
        self,
        data: SubscriptionRequiredException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SubscriptionRequiredException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SubscriptionRequiredException":
        return cls(deserialize_json(data), message, response=response)
