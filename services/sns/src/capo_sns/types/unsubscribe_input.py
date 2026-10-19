"""Generated from Smithy shape ``com.amazonaws.sns#UnsubscribeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.subscription_arn


class UnsubscribeInput(TypedDict, closed=True):
    subscription_arn: "capo_sns.types.subscription_arn.subscriptionARN"
    """<p>The ARN of the subscription to be deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UnsubscribeInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}SubscriptionArn", str(value["subscription_arn"])))


def deserialize_query(el: Element) -> UnsubscribeInput:
    out: UnsubscribeInput = {}  # type: ignore[typeddict-item]
    child_subscription_arn = el.find("SubscriptionArn")
    if child_subscription_arn is not None:
        out["subscription_arn"] = str(child_subscription_arn.text or "")
    else:
        out["subscription_arn"] = ""
    return out
