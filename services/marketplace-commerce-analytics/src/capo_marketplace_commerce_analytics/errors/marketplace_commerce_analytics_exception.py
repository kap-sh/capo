"""Generated from Smithy shape ``com.amazonaws.marketplacecommerceanalytics#MarketplaceCommerceAnalyticsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_marketplace_commerce_analytics.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_commerce_analytics.types.exception_message


class MarketplaceCommerceAnalyticsException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_marketplace_commerce_analytics.types.exception_message.ExceptionMessage"
    ]
    """This message describes details of the error."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MarketplaceCommerceAnalyticsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MarketplaceCommerceAnalyticsException_:
    out: MarketplaceCommerceAnalyticsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class MarketplaceCommerceAnalyticsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacecommerceanalytics#MarketplaceCommerceAnalyticsException``."""

    code: str | None = "MarketplaceCommerceAnalyticsException"

    def __init__(
        self,
        data: MarketplaceCommerceAnalyticsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="MarketplaceCommerceAnalyticsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MarketplaceCommerceAnalyticsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
