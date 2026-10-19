"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyEventSubscriptionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.event_categories_list
    import capo_database_migration_service.types.string


class ModifyEventSubscriptionMessage(TypedDict, closed=True):
    subscription_name: "capo_database_migration_service.types.string.String"
    """<p>The name of the DMS event notification subscription to be modified.</p>"""
    sns_topic_arn: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.</p>"""
    source_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> The type of DMS resource that generates the events you want to subscribe to. </p> <p>Valid values: replication-instance | replication-task</p>"""
    event_categories: NotRequired[
        "capo_database_migration_service.types.event_categories_list.EventCategoriesList"
    ]
    """<p> A list of event categories for a source type that you want to subscribe to. Use the <code>DescribeEventCategories</code> action to see a list of event categories. </p>"""
    enabled: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p> A Boolean value; set to <b>true</b> to activate the subscription. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyEventSubscriptionMessage) -> dict:
    out: dict = {}
    out["SubscriptionName"] = value["subscription_name"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "event_categories" in value:
        import capo_database_migration_service.types.event_categories_list

        out["EventCategories"] = (
            capo_database_migration_service.types.event_categories_list.serialize_aws_json_1_1(
                value["event_categories"]
            )
        )
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyEventSubscriptionMessage:
    out: ModifyEventSubscriptionMessage = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionName") is not None:
        out["subscription_name"] = data["SubscriptionName"]
    else:
        out["subscription_name"] = ""
    if data.get("SnsTopicArn") is not None:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if data.get("SourceType") is not None:
        out["source_type"] = data["SourceType"]
    if data.get("EventCategories") is not None:
        import capo_database_migration_service.types.event_categories_list

        out["event_categories"] = (
            capo_database_migration_service.types.event_categories_list.deserialize_aws_json_1_1(
                data["EventCategories"]
            )
        )
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    return out
