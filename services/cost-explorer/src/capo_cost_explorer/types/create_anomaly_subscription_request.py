"""Generated from Smithy shape ``com.amazonaws.costexplorer#CreateAnomalySubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.anomaly_subscription
    import capo_cost_explorer.types.resource_tag_list


class CreateAnomalySubscriptionRequest(TypedDict, closed=True):
    anomaly_subscription: (
        "capo_cost_explorer.types.anomaly_subscription.AnomalySubscription"
    )
    """<p>The cost anomaly subscription object that you want to create. </p>"""
    resource_tags: NotRequired[
        "capo_cost_explorer.types.resource_tag_list.ResourceTagList"
    ]
    """<p>An optional list of tags to associate with the specified <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html"> <code>AnomalySubscription</code> </a>. You can use resource tags to control access to your <code>subscription</code> using IAM policies.</p> <p>Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags:</p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services use</p> </li> <li> <p>The maximum length of a key is 128 characters</p> </li> <li> <p>The maximum length of a value is 256 characters</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code> </p> </li> <li> <p>Keys and values are case sensitive</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces</p> </li> <li> <p>Don’t use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services use</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAnomalySubscriptionRequest) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.anomaly_subscription

    out["AnomalySubscription"] = (
        capo_cost_explorer.types.anomaly_subscription.serialize_aws_json_1_1(
            value["anomaly_subscription"]
        )
    )
    if "resource_tags" in value:
        import capo_cost_explorer.types.resource_tag_list

        out["ResourceTags"] = (
            capo_cost_explorer.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAnomalySubscriptionRequest:
    out: CreateAnomalySubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AnomalySubscription") is not None:
        import capo_cost_explorer.types.anomaly_subscription

        out["anomaly_subscription"] = (
            capo_cost_explorer.types.anomaly_subscription.deserialize_aws_json_1_1(
                data["AnomalySubscription"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAnomalySubscriptionRequest.anomaly_subscription required"
        )
    if data.get("ResourceTags") is not None:
        import capo_cost_explorer.types.resource_tag_list

        out["resource_tags"] = (
            capo_cost_explorer.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    return out
