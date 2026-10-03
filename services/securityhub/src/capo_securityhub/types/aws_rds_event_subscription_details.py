"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsEventSubscriptionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsRdsEventSubscriptionDetails(TypedDict, closed=True):
    cust_subscription_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the account that is associated with the event notification subscription.</p>"""
    customer_aws_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the event notification subscription.</p>"""
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the event notification subscription is enabled.</p>"""
    event_categories_list: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The list of event categories for the event notification subscription.</p>"""
    event_subscription_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the event notification subscription.</p>"""
    sns_topic_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the SNS topic to post the event notifications to.</p>"""
    source_ids_list: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of source identifiers for the event notification subscription.</p>"""
    source_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The source type for the event notification subscription.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the event notification subscription.</p> <p>Valid values: <code>creating</code> | <code>modifying</code> | <code>deleting</code> | <code>active</code> | <code>no-permission</code> | <code>topic-not-exist</code> </p>"""
    subscription_creation_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The datetime when the event notification subscription was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsEventSubscriptionDetails) -> dict:
    out: dict = {}
    if "cust_subscription_id" in value:
        out["CustSubscriptionId"] = value["cust_subscription_id"]
    if "customer_aws_id" in value:
        out["CustomerAwsId"] = value["customer_aws_id"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "event_categories_list" in value:
        import capo_securityhub.types.non_empty_string_list

        out["EventCategoriesList"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["event_categories_list"]
            )
        )
    if "event_subscription_arn" in value:
        out["EventSubscriptionArn"] = value["event_subscription_arn"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "source_ids_list" in value:
        import capo_securityhub.types.non_empty_string_list

        out["SourceIdsList"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["source_ids_list"]
            )
        )
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "status" in value:
        out["Status"] = value["status"]
    if "subscription_creation_time" in value:
        out["SubscriptionCreationTime"] = value["subscription_creation_time"]
    return out


def deserialize_json(data: dict) -> AwsRdsEventSubscriptionDetails:
    out: AwsRdsEventSubscriptionDetails = {}  # type: ignore[typeddict-item]
    if data.get("CustSubscriptionId") is not None:
        out["cust_subscription_id"] = data["CustSubscriptionId"]
    if data.get("CustomerAwsId") is not None:
        out["customer_aws_id"] = data["CustomerAwsId"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("EventCategoriesList") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["event_categories_list"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["EventCategoriesList"]
            )
        )
    if data.get("EventSubscriptionArn") is not None:
        out["event_subscription_arn"] = data["EventSubscriptionArn"]
    if data.get("SnsTopicArn") is not None:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if data.get("SourceIdsList") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["source_ids_list"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["SourceIdsList"]
            )
        )
    if data.get("SourceType") is not None:
        out["source_type"] = data["SourceType"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("SubscriptionCreationTime") is not None:
        out["subscription_creation_time"] = data["SubscriptionCreationTime"]
    return out
