"""Generated from Smithy shape ``com.amazonaws.redshift#EventSubscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean
    import capo_redshift.types.event_categories_list
    import capo_redshift.types.source_ids_list
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp
    import capo_redshift.types.tag_list


class EventSubscription(TypedDict, closed=True):
    customer_aws_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account associated with the Amazon Redshift event notification subscription.</p>"""
    cust_subscription_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the Amazon Redshift event notification subscription.</p>"""
    sns_topic_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic used by the event notification subscription.</p>"""
    status: NotRequired["capo_redshift.types.string.String"]
    """<p>The status of the Amazon Redshift event notification subscription.</p> <p>Constraints:</p> <ul> <li> <p>Can be one of the following: active | no-permission | topic-not-exist</p> </li> <li> <p>The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.</p> </li> </ul>"""
    subscription_creation_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The date and time the Amazon Redshift event notification subscription was created.</p>"""
    source_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The source type of the events returned by the Amazon Redshift event notification, such as cluster, cluster-snapshot, cluster-parameter-group, cluster-security-group, or scheduled-action. </p>"""
    source_ids_list: NotRequired["capo_redshift.types.source_ids_list.SourceIdsList"]
    """<p>A list of the sources that publish events to the Amazon Redshift event notification subscription.</p>"""
    event_categories_list: NotRequired[
        "capo_redshift.types.event_categories_list.EventCategoriesList"
    ]
    """<p>The list of Amazon Redshift event categories specified in the event notification subscription.</p> <p>Values: Configuration, Management, Monitoring, Security, Pending</p>"""
    severity: NotRequired["capo_redshift.types.string.String"]
    """<p>The event severity specified in the Amazon Redshift event notification subscription.</p> <p>Values: ERROR, INFO</p>"""
    enabled: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p>A boolean value indicating whether the subscription is enabled; <code>true</code> indicates that the subscription is enabled.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>The list of tags for the event subscription.</p>"""


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
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["subscription_creation_time"],
            pairs,
            f"{key_prefix}SubscriptionCreationTime",
        )
    if "source_type" in value:
        pairs.append((f"{key_prefix}SourceType", str(value["source_type"])))
    if "source_ids_list" in value:
        import capo_redshift.types.source_ids_list

        capo_redshift.types.source_ids_list.serialize_query(
            value["source_ids_list"], pairs, f"{key_prefix}SourceIdsList"
        )
    if "event_categories_list" in value:
        import capo_redshift.types.event_categories_list

        capo_redshift.types.event_categories_list.serialize_query(
            value["event_categories_list"], pairs, f"{key_prefix}EventCategoriesList"
        )
    if "severity" in value:
        pairs.append((f"{key_prefix}Severity", str(value["severity"])))
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
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
        import capo_redshift.types.t_stamp

        out["subscription_creation_time"] = (
            capo_redshift.types.t_stamp.deserialize_query(
                child_subscription_creation_time
            )
        )
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        out["source_type"] = str(child_source_type.text or "")
    child_source_ids_list = el.find("SourceIdsList")
    if child_source_ids_list is not None:
        import capo_redshift.types.source_ids_list

        out["source_ids_list"] = capo_redshift.types.source_ids_list.deserialize_query(
            child_source_ids_list
        )
    child_event_categories_list = el.find("EventCategoriesList")
    if child_event_categories_list is not None:
        import capo_redshift.types.event_categories_list

        out["event_categories_list"] = (
            capo_redshift.types.event_categories_list.deserialize_query(
                child_event_categories_list
            )
        )
    child_severity = el.find("Severity")
    if child_severity is not None:
        out["severity"] = str(child_severity.text or "")
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    return out
