"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EventSubscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean
    import capo_database_migration_service.types.event_categories_list
    import capo_database_migration_service.types.source_ids_list
    import capo_database_migration_service.types.string


class EventSubscription(TypedDict, closed=True):
    customer_aws_id: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The Amazon Web Services customer account associated with the DMS event notification subscription.</p>"""
    cust_subscription_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The DMS event notification subscription Id.</p>"""
    sns_topic_arn: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The topic ARN of the DMS event notification subscription.</p>"""
    status: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The status of the DMS event notification subscription.</p> <p>Constraints:</p> <p>Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist</p> <p>The status "no-permission" indicates that DMS no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.</p>"""
    subscription_creation_time: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The time the DMS event notification subscription was created.</p>"""
    source_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> The type of DMS resource that generates events. </p> <p>Valid values: replication-instance | replication-server | security-group | replication-task</p>"""
    source_ids_list: NotRequired[
        "capo_database_migration_service.types.source_ids_list.SourceIdsList"
    ]
    """<p>A list of source Ids for the event subscription.</p>"""
    event_categories_list: NotRequired[
        "capo_database_migration_service.types.event_categories_list.EventCategoriesList"
    ]
    """<p>A lists of event categories.</p>"""
    enabled: "capo_database_migration_service.types.boolean.Boolean"
    """<p>Boolean value that indicates if the event subscription is enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSubscription) -> dict:
    out: dict = {}
    if "customer_aws_id" in value:
        out["CustomerAwsId"] = value["customer_aws_id"]
    if "cust_subscription_id" in value:
        out["CustSubscriptionId"] = value["cust_subscription_id"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "status" in value:
        out["Status"] = value["status"]
    if "subscription_creation_time" in value:
        out["SubscriptionCreationTime"] = value["subscription_creation_time"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "source_ids_list" in value:
        import capo_database_migration_service.types.source_ids_list

        out["SourceIdsList"] = (
            capo_database_migration_service.types.source_ids_list.serialize_aws_json_1_1(
                value["source_ids_list"]
            )
        )
    if "event_categories_list" in value:
        import capo_database_migration_service.types.event_categories_list

        out["EventCategoriesList"] = (
            capo_database_migration_service.types.event_categories_list.serialize_aws_json_1_1(
                value["event_categories_list"]
            )
        )
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> EventSubscription:
    out: EventSubscription = {}  # type: ignore[typeddict-item]
    if data.get("CustomerAwsId") is not None:
        out["customer_aws_id"] = data["CustomerAwsId"]
    if data.get("CustSubscriptionId") is not None:
        out["cust_subscription_id"] = data["CustSubscriptionId"]
    if data.get("SnsTopicArn") is not None:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("SubscriptionCreationTime") is not None:
        out["subscription_creation_time"] = data["SubscriptionCreationTime"]
    if data.get("SourceType") is not None:
        out["source_type"] = data["SourceType"]
    if data.get("SourceIdsList") is not None:
        import capo_database_migration_service.types.source_ids_list

        out["source_ids_list"] = (
            capo_database_migration_service.types.source_ids_list.deserialize_aws_json_1_1(
                data["SourceIdsList"]
            )
        )
    if data.get("EventCategoriesList") is not None:
        import capo_database_migration_service.types.event_categories_list

        out["event_categories_list"] = (
            capo_database_migration_service.types.event_categories_list.deserialize_aws_json_1_1(
                data["EventCategoriesList"]
            )
        )
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
