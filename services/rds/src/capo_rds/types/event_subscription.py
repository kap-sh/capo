"""Generated from Smithy shape ``com.amazonaws.rds#EventSubscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.event_categories_list
    import capo_rds.types.source_ids_list
    import capo_rds.types.string


class EventSubscription(TypedDict, closed=True):
    customer_aws_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services customer account associated with the RDS event notification subscription.</p>"""
    cust_subscription_id: NotRequired["capo_rds.types.string.String"]
    """<p>The RDS event notification subscription Id.</p>"""
    sns_topic_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The topic ARN of the RDS event notification subscription.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the RDS event notification subscription.</p> <p>Constraints:</p> <p>Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist</p> <p>The status "no-permission" indicates that RDS no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.</p>"""
    subscription_creation_time: NotRequired["capo_rds.types.string.String"]
    """<p>The time the RDS event notification subscription was created.</p>"""
    source_type: NotRequired["capo_rds.types.string.String"]
    """<p>The source type for the RDS event notification subscription.</p>"""
    source_ids_list: NotRequired["capo_rds.types.source_ids_list.SourceIdsList"]
    """<p>A list of source IDs for the RDS event notification subscription.</p>"""
    event_categories_list: NotRequired[
        "capo_rds.types.event_categories_list.EventCategoriesList"
    ]
    """<p>A list of event categories for the RDS event notification subscription.</p>"""
    enabled: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether the subscription is enabled. True indicates the subscription is enabled.</p>"""
    event_subscription_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the event subscription.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventSubscription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "customer_aws_id" in value:
        pairs.append((f"{key_prefix}CustomerAwsId", str(value["customer_aws_id"])))
    if "cust_subscription_id" in value:
        pairs.append(
            (f"{key_prefix}CustSubscriptionId", str(value["cust_subscription_id"]))
        )
    if "sns_topic_arn" in value:
        pairs.append((f"{key_prefix}SnsTopicArn", str(value["sns_topic_arn"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "subscription_creation_time" in value:
        pairs.append(
            (
                f"{key_prefix}SubscriptionCreationTime",
                str(value["subscription_creation_time"]),
            )
        )
    if "source_type" in value:
        pairs.append((f"{key_prefix}SourceType", str(value["source_type"])))
    if "source_ids_list" in value:
        import capo_rds.types.source_ids_list

        capo_rds.types.source_ids_list.serialize_query(
            value["source_ids_list"], pairs, f"{key_prefix}SourceIdsList"
        )
    if "event_categories_list" in value:
        import capo_rds.types.event_categories_list

        capo_rds.types.event_categories_list.serialize_query(
            value["event_categories_list"], pairs, f"{key_prefix}EventCategoriesList"
        )
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))
    if "event_subscription_arn" in value:
        pairs.append(
            (f"{key_prefix}EventSubscriptionArn", str(value["event_subscription_arn"]))
        )


def deserialize_query(el: Element) -> EventSubscription:
    out: EventSubscription = {}  # type: ignore[typeddict-item]
    child_customer_aws_id = el.find("CustomerAwsId")
    if child_customer_aws_id is not None:
        out["customer_aws_id"] = str(child_customer_aws_id.text or "")
    child_cust_subscription_id = el.find("CustSubscriptionId")
    if child_cust_subscription_id is not None:
        out["cust_subscription_id"] = str(child_cust_subscription_id.text or "")
    child_sns_topic_arn = el.find("SnsTopicArn")
    if child_sns_topic_arn is not None:
        out["sns_topic_arn"] = str(child_sns_topic_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_subscription_creation_time = el.find("SubscriptionCreationTime")
    if child_subscription_creation_time is not None:
        out["subscription_creation_time"] = str(
            child_subscription_creation_time.text or ""
        )
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        out["source_type"] = str(child_source_type.text or "")
    child_source_ids_list = el.find("SourceIdsList")
    if child_source_ids_list is not None:
        import capo_rds.types.source_ids_list

        out["source_ids_list"] = capo_rds.types.source_ids_list.deserialize_query(
            child_source_ids_list
        )
    child_event_categories_list = el.find("EventCategoriesList")
    if child_event_categories_list is not None:
        import capo_rds.types.event_categories_list

        out["event_categories_list"] = (
            capo_rds.types.event_categories_list.deserialize_query(
                child_event_categories_list
            )
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_event_subscription_arn = el.find("EventSubscriptionArn")
    if child_event_subscription_arn is not None:
        out["event_subscription_arn"] = str(child_event_subscription_arn.text or "")
    return out
