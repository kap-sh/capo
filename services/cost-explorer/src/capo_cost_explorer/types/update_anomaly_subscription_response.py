"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateAnomalySubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class UpdateAnomalySubscriptionResponse(TypedDict, closed=True):
    subscription_arn: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>A cost anomaly subscription ARN. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAnomalySubscriptionResponse) -> dict:
    out: dict = {}
    out["SubscriptionArn"] = value["subscription_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAnomalySubscriptionResponse:
    out: UpdateAnomalySubscriptionResponse = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionArn") is not None:
        out["subscription_arn"] = data["SubscriptionArn"]
    else:
        out["subscription_arn"] = ""
    return out
