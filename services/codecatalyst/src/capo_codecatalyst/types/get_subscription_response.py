"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.timestamp


class GetSubscriptionResponse(TypedDict, closed=True):
    subscription_type: NotRequired["str"]
    """<p>The type of the billing plan for the space.</p>"""
    aws_account_name: NotRequired["capo_codecatalyst.types.name_string.NameString"]
    """<p>The display name of the Amazon Web Services account used for billing for the space.</p>"""
    pending_subscription_type: NotRequired["str"]
    """<p>The type of the billing plan that the space will be changed to at the start of the next billing cycle. This applies only to changes that reduce the functionality available for the space. Billing plan changes that increase functionality are applied immediately. For more information, see <a href="https://codecatalyst.aws/explore/pricing">Pricing</a>.</p>"""
    pending_subscription_start_time: NotRequired[
        "capo_codecatalyst.types.timestamp.Timestamp"
    ]
    """<p>The day and time the pending change will be applied to the space, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionResponse) -> dict:
    out: dict = {}
    if "subscription_type" in value:
        out["subscriptionType"] = value["subscription_type"]
    if "aws_account_name" in value:
        out["awsAccountName"] = value["aws_account_name"]
    if "pending_subscription_type" in value:
        out["pendingSubscriptionType"] = value["pending_subscription_type"]
    if "pending_subscription_start_time" in value:
        import capo_codecatalyst._protocol.serialize

        out["pendingSubscriptionStartTime"] = (
            capo_codecatalyst._protocol.serialize.fmt_date_time(
                value["pending_subscription_start_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSubscriptionResponse:
    out: GetSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if data.get("subscriptionType") is not None:
        out["subscription_type"] = data["subscriptionType"]
    if data.get("awsAccountName") is not None:
        out["aws_account_name"] = data["awsAccountName"]
    if data.get("pendingSubscriptionType") is not None:
        out["pending_subscription_type"] = data["pendingSubscriptionType"]
    if data.get("pendingSubscriptionStartTime") is not None:
        import datetime

        out["pending_subscription_start_time"] = datetime.datetime.fromisoformat(
            data["pendingSubscriptionStartTime"].replace("Z", "+00:00")
        )
    return out
