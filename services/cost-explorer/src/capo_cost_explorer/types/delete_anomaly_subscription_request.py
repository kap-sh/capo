"""Generated from Smithy shape ``com.amazonaws.costexplorer#DeleteAnomalySubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class DeleteAnomalySubscriptionRequest(TypedDict, closed=True):
    subscription_arn: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>The unique identifier of the cost anomaly subscription that you want to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAnomalySubscriptionRequest) -> dict:
    out: dict = {}
    out["SubscriptionArn"] = value["subscription_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAnomalySubscriptionRequest:
    out: DeleteAnomalySubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionArn") is not None:
        out["subscription_arn"] = data["SubscriptionArn"]
    else:
        out["subscription_arn"] = ""
    return out
