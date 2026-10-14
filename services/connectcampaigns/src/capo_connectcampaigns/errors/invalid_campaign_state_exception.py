"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#InvalidCampaignStateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connectcampaigns.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_state
    import capo_connectcampaigns.types.x_amazon_error_type


class InvalidCampaignStateException_(TypedDict, closed=True):
    state: "capo_connectcampaigns.types.campaign_state.CampaignState"
    message: "str"
    x_amz_error_type: NotRequired[
        "capo_connectcampaigns.types.x_amazon_error_type.XAmazonErrorType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidCampaignStateException_) -> dict:
    out: dict = {}
    out["state"] = value["state"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidCampaignStateException_:
    out: InvalidCampaignStateException_ = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        raise DeserializationError("InvalidCampaignStateException_.state required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidCampaignStateException_.message required")
    return out


class InvalidCampaignStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connectcampaigns#InvalidCampaignStateException``."""

    code: str | None = "InvalidCampaignStateException"

    def __init__(
        self,
        data: InvalidCampaignStateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCampaignStateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidCampaignStateException":
        return cls(deserialize_json(data), message, response=response)
