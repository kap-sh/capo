"""Generated from Smithy shape ``com.amazonaws.costexplorer#CreateAnomalySubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class CreateAnomalySubscriptionResponse(TypedDict, closed=True):
    subscription_arn: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>The unique identifier of your newly created cost anomaly subscription. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAnomalySubscriptionResponse) -> dict:
    out: dict = {}
    out["SubscriptionArn"] = value["subscription_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAnomalySubscriptionResponse:
    out: CreateAnomalySubscriptionResponse = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionArn") is not None:
        out["subscription_arn"] = data["SubscriptionArn"]
    else:
        out["subscription_arn"] = ""
    return out
