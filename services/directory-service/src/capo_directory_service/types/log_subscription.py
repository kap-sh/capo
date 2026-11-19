"""Generated from Smithy shape ``com.amazonaws.directoryservice#LogSubscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.log_group_name
    import capo_directory_service.types.subscription_created_date_time


class LogSubscription(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>Identifier (ID) of the directory that you want to associate with the log subscription.</p>"""
    log_group_name: NotRequired[
        "capo_directory_service.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p>"""
    subscription_created_date_time: NotRequired[
        "capo_directory_service.types.subscription_created_date_time.SubscriptionCreatedDateTime"
    ]
    """<p>The date and time that the log subscription was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogSubscription) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "log_group_name" in value:
        out["LogGroupName"] = value["log_group_name"]
    if "subscription_created_date_time" in value:
        import capo_directory_service.types.subscription_created_date_time

        out["SubscriptionCreatedDateTime"] = (
            capo_directory_service.types.subscription_created_date_time.serialize_aws_json_1_1(
                value["subscription_created_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogSubscription:
    out: LogSubscription = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("LogGroupName") is not None:
        out["log_group_name"] = data["LogGroupName"]
    if data.get("SubscriptionCreatedDateTime") is not None:
        import capo_directory_service.types.subscription_created_date_time

        out["subscription_created_date_time"] = (
            capo_directory_service.types.subscription_created_date_time.deserialize_aws_json_1_1(
                data["SubscriptionCreatedDateTime"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogSubscription) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "log_group_name" in value:
        out["LogGroupName"] = value["log_group_name"]
    if "subscription_created_date_time" in value:
        import capo_directory_service.types.subscription_created_date_time

        out["SubscriptionCreatedDateTime"] = (
            capo_directory_service.types.subscription_created_date_time.serialize_cbor(
                value["subscription_created_date_time"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LogSubscription:
    out: LogSubscription = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("LogGroupName") is not None:
        out["log_group_name"] = data["LogGroupName"]
    if data.get("SubscriptionCreatedDateTime") is not None:
        import capo_directory_service.types.subscription_created_date_time

        out["subscription_created_date_time"] = (
            capo_directory_service.types.subscription_created_date_time.deserialize_cbor(
                data["SubscriptionCreatedDateTime"]
            )
        )
    return out
