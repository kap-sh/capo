"""Generated from Smithy shape ``com.amazonaws.mediatailor#Alert``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.__timestamp_unix
    import capo_mediatailor.types.alert_category


class Alert(TypedDict, closed=True):
    alert_code: "capo_mediatailor.types.__string.__string"
    """<p>The code for the alert. For example, <code>NOT_PROCESSED</code>.</p>"""
    alert_message: "capo_mediatailor.types.__string.__string"
    """<p>If an alert is generated for a resource, an explanation of the reason for the alert.</p>"""
    last_modified_time: "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    """<p>The timestamp when the alert was last modified.</p>"""
    related_resource_arns: "capo_mediatailor.types.__list_of__string.__listOf__string"
    """<p>The Amazon Resource Names (ARNs) related to this alert.</p>"""
    resource_arn: "capo_mediatailor.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    category: NotRequired["capo_mediatailor.types.alert_category.AlertCategory"]
    """<p>The category that MediaTailor assigns to the alert.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Alert) -> dict:
    out: dict = {}
    out["AlertCode"] = value["alert_code"]
    out["AlertMessage"] = value["alert_message"]
    import capo_mediatailor.types.__timestamp_unix

    out["LastModifiedTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
        value["last_modified_time"]
    )
    import capo_mediatailor.types.__list_of__string

    out["RelatedResourceArns"] = (
        capo_mediatailor.types.__list_of__string.serialize_json(
            value["related_resource_arns"]
        )
    )
    out["ResourceArn"] = value["resource_arn"]
    if "category" in value:
        import capo_mediatailor.types.alert_category

        out["Category"] = capo_mediatailor.types.alert_category.serialize_json(
            value["category"]
        )
    return out


def deserialize_json(data: dict) -> Alert:
    out: Alert = {}  # type: ignore[typeddict-item]
    if data.get("AlertCode") is not None:
        out["alert_code"] = data["AlertCode"]
    else:
        out["alert_code"] = ""
    if data.get("AlertMessage") is not None:
        out["alert_message"] = data["AlertMessage"]
    else:
        out["alert_message"] = ""
    if data.get("LastModifiedTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["last_modified_time"] = (
            capo_mediatailor.types.__timestamp_unix.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("RelatedResourceArns") is not None:
        import capo_mediatailor.types.__list_of__string

        out["related_resource_arns"] = (
            capo_mediatailor.types.__list_of__string.deserialize_json(
                data["RelatedResourceArns"]
            )
        )
    else:
        out["related_resource_arns"] = []
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Category") is not None:
        import capo_mediatailor.types.alert_category

        out["category"] = capo_mediatailor.types.alert_category.deserialize_json(
            data["Category"]
        )
    return out
