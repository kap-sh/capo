"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateDataLakeExceptionSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.safe_string
    import capo_securitylake.types.subscription_protocol


class CreateDataLakeExceptionSubscriptionRequest(TypedDict, closed=True):
    subscription_protocol: (
        "capo_securitylake.types.subscription_protocol.SubscriptionProtocol"
    )
    """<p>The subscription protocol to which exception notifications are posted.</p>"""
    notification_endpoint: "capo_securitylake.types.safe_string.SafeString"
    """<p>The Amazon Web Services account where you want to receive exception notifications.</p>"""
    exception_time_to_live: NotRequired["int"]
    """<p>The expiration period and time-to-live (TTL). It is the duration of time until which the exception message remains.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataLakeExceptionSubscriptionRequest) -> dict:
    out: dict = {}
    out["subscriptionProtocol"] = value["subscription_protocol"]
    out["notificationEndpoint"] = value["notification_endpoint"]
    if "exception_time_to_live" in value:
        out["exceptionTimeToLive"] = value["exception_time_to_live"]
    return out


def deserialize_json(data: dict) -> CreateDataLakeExceptionSubscriptionRequest:
    out: CreateDataLakeExceptionSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("subscriptionProtocol") is not None:
        out["subscription_protocol"] = data["subscriptionProtocol"]
    else:
        out["subscription_protocol"] = ""
    if data.get("notificationEndpoint") is not None:
        out["notification_endpoint"] = data["notificationEndpoint"]
    else:
        out["notification_endpoint"] = ""
    if data.get("exceptionTimeToLive") is not None:
        out["exception_time_to_live"] = data["exceptionTimeToLive"]
    return out
