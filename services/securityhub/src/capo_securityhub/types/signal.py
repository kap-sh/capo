"""Generated from Smithy shape ``com.amazonaws.securityhub#Signal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.double
    import capo_securityhub.types.indicators_list
    import capo_securityhub.types.integer
    import capo_securityhub.types.long
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class Signal(TypedDict, closed=True):
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The type of the signal used to identify an attack sequence. </p> <p>Signals can be GuardDuty findings or activities observed in data sources that GuardDuty monitors. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html">GuardDuty foundational data sources</a> in the <i>Amazon GuardDuty User Guide</i>.</p> <p>A signal type can be one of the following values. Here are the related descriptions:</p> <ul> <li> <p> <code>FINDING</code> - Individually generated GuardDuty finding.</p> </li> <li> <p> <code>CLOUD_TRAIL</code> - Activity observed from CloudTrail logs</p> </li> <li> <p> <code>S3_DATA_EVENTS</code> - Activity observed from CloudTrail data events for Amazon Simple Storage Service (S3). Activities associated with this type will show up only when you have enabled GuardDuty S3 Protection feature in your account. For more information about S3 Protection and the steps to enable it, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html">S3 Protection</a> in the <i>Amazon GuardDuty User Guide</i>.</p> </li> </ul>"""
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The identifier of the signal. </p>"""
    title: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The description of the GuardDuty finding. </p>"""
    product_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the product that generated the signal. </p>"""
    resource_ids: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> The ARN or ID of the Amazon Web Services resource associated with the signal. </p>"""
    signal_indicators: NotRequired[
        "capo_securityhub.types.indicators_list.IndicatorsList"
    ]
    """<p> Contains information about the indicators associated with the signals in this attack sequence finding. The values for <code>SignalIndicators</code> are a subset of the values for <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Sequence.html">SequenceIndicators</a>, but the values for these fields don't always match 1:1. </p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the GuardDuty signal. For example, when signal type is <code>FINDING</code>, the signal name is the name of the finding. </p>"""
    created_at: NotRequired["capo_securityhub.types.long.Long"]
    """<p> The timestamp when the first finding or activity related to this signal was observed. </p>"""
    updated_at: NotRequired["capo_securityhub.types.long.Long"]
    """<p> The timestamp when this signal was last observed. </p>"""
    first_seen_at: NotRequired["capo_securityhub.types.long.Long"]
    """<p> The timestamp when the first finding or activity related to this signal was observed. </p>"""
    last_seen_at: NotRequired["capo_securityhub.types.long.Long"]
    """<p> The timestamp when the last finding or activity related to this signal was observed. </p>"""
    severity: NotRequired["capo_securityhub.types.double.Double"]
    """<p>The severity associated with the signal. For more information about severity, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html">Severity levels for GuardDuty findings</a> in the <i>Amazon GuardDuty User Guide</i>.</p>"""
    count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The number of times this signal was observed. </p>"""
    actor_ids: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> The IDs of the threat actors involved in the signal. </p>"""
    endpoint_ids: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>Information about the endpoint IDs associated with this signal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Signal) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "id" in value:
        out["Id"] = value["id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "product_arn" in value:
        out["ProductArn"] = value["product_arn"]
    if "resource_ids" in value:
        import capo_securityhub.types.non_empty_string_list

        out["ResourceIds"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["resource_ids"]
            )
        )
    if "signal_indicators" in value:
        import capo_securityhub.types.indicators_list

        out["SignalIndicators"] = capo_securityhub.types.indicators_list.serialize_json(
            value["signal_indicators"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "created_at" in value:
        out["CreatedAt"] = value["created_at"]
    if "updated_at" in value:
        out["UpdatedAt"] = value["updated_at"]
    if "first_seen_at" in value:
        out["FirstSeenAt"] = value["first_seen_at"]
    if "last_seen_at" in value:
        out["LastSeenAt"] = value["last_seen_at"]
    if "severity" in value:
        out["Severity"] = (
            "NaN"
            if value["severity"] != value["severity"]
            else "Infinity"
            if value["severity"] == float("inf")
            else "-Infinity"
            if value["severity"] == float("-inf")
            else value["severity"]
        )
    if "count" in value:
        out["Count"] = value["count"]
    if "actor_ids" in value:
        import capo_securityhub.types.non_empty_string_list

        out["ActorIds"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["actor_ids"]
        )
    if "endpoint_ids" in value:
        import capo_securityhub.types.non_empty_string_list

        out["EndpointIds"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["endpoint_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> Signal:
    out: Signal = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("ProductArn") is not None:
        out["product_arn"] = data["ProductArn"]
    if data.get("ResourceIds") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["resource_ids"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["ResourceIds"]
            )
        )
    if data.get("SignalIndicators") is not None:
        import capo_securityhub.types.indicators_list

        out["signal_indicators"] = (
            capo_securityhub.types.indicators_list.deserialize_json(
                data["SignalIndicators"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreatedAt") is not None:
        out["created_at"] = data["CreatedAt"]
    if data.get("UpdatedAt") is not None:
        out["updated_at"] = data["UpdatedAt"]
    if data.get("FirstSeenAt") is not None:
        out["first_seen_at"] = data["FirstSeenAt"]
    if data.get("LastSeenAt") is not None:
        out["last_seen_at"] = data["LastSeenAt"]
    if data.get("Severity") is not None:
        out["severity"] = float(data["Severity"])
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    if data.get("ActorIds") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["actor_ids"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["ActorIds"]
            )
        )
    if data.get("EndpointIds") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["endpoint_ids"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["EndpointIds"]
            )
        )
    return out
