"""Generated from Smithy shape ``com.amazonaws.sns#SubscribeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.subscription_arn


class SubscribeResponse(TypedDict, closed=True):
    subscription_arn: NotRequired["capo_sns.types.subscription_arn.subscriptionARN"]
    """<p>The ARN of the subscription if it is confirmed, or the string "pending confirmation" if the subscription requires confirmation. However, if the API request parameter <code>ReturnSubscriptionArn</code> is true, then the value is always the subscription ARN, even if the subscription requires confirmation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SubscribeResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subscription_arn" in value:
        pairs.append((f"{key_prefix}SubscriptionArn", str(value["subscription_arn"])))


def deserialize_query(el: Element) -> SubscribeResponse:
    out: SubscribeResponse = {}  # type: ignore[typeddict-item]
    child_subscription_arn = el.find("SubscriptionArn")
    if child_subscription_arn is not None:
        out["subscription_arn"] = str(child_subscription_arn.text or "")
    return out
