"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmHistoryItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_name
    import capo_cloudwatch.types.alarm_type
    import capo_cloudwatch.types.contributor_attributes
    import capo_cloudwatch.types.contributor_id
    import capo_cloudwatch.types.history_data
    import capo_cloudwatch.types.history_item_type
    import capo_cloudwatch.types.history_summary
    import capo_cloudwatch.types.timestamp


class AlarmHistoryItem(TypedDict, closed=True):
    alarm_name: NotRequired["capo_cloudwatch.types.alarm_name.AlarmName"]
    """<p>The descriptive name for the alarm.</p>"""
    alarm_contributor_id: NotRequired[
        "capo_cloudwatch.types.contributor_id.ContributorId"
    ]
    """<p>The unique identifier of the alarm contributor associated with this history item, if applicable.</p>"""
    alarm_type: NotRequired["capo_cloudwatch.types.alarm_type.AlarmType"]
    """<p>The type of alarm, either metric alarm or composite alarm.</p>"""
    timestamp: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The time stamp for the alarm history item.</p>"""
    history_item_type: NotRequired[
        "capo_cloudwatch.types.history_item_type.HistoryItemType"
    ]
    """<p>The type of alarm history item.</p>"""
    history_summary: NotRequired["capo_cloudwatch.types.history_summary.HistorySummary"]
    """<p>A summary of the alarm history, in text format.</p>"""
    history_data: NotRequired["capo_cloudwatch.types.history_data.HistoryData"]
    """<p>Data about the alarm, in JSON format.</p>"""
    alarm_contributor_attributes: NotRequired[
        "capo_cloudwatch.types.contributor_attributes.ContributorAttributes"
    ]
    """<p>A map of attributes that describe the alarm contributor associated with this history item, providing context about the contributor's characteristics at the time of the event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmHistoryItem) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "alarm_contributor_id" in value:
        out["AlarmContributorId"] = value["alarm_contributor_id"]
    if "alarm_type" in value:
        import capo_cloudwatch.types.alarm_type

        out["AlarmType"] = capo_cloudwatch.types.alarm_type.serialize_aws_json_1_0(
            value["alarm_type"]
        )
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["Timestamp"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["timestamp"]
        )
    if "history_item_type" in value:
        import capo_cloudwatch.types.history_item_type

        out["HistoryItemType"] = (
            capo_cloudwatch.types.history_item_type.serialize_aws_json_1_0(
                value["history_item_type"]
            )
        )
    if "history_summary" in value:
        out["HistorySummary"] = value["history_summary"]
    if "history_data" in value:
        out["HistoryData"] = value["history_data"]
    if "alarm_contributor_attributes" in value:
        import capo_cloudwatch.types.contributor_attributes

        out["AlarmContributorAttributes"] = (
            capo_cloudwatch.types.contributor_attributes.serialize_aws_json_1_0(
                value["alarm_contributor_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AlarmHistoryItem:
    out: AlarmHistoryItem = {}  # type: ignore[typeddict-item]
    if data.get("AlarmName") is not None:
        out["alarm_name"] = data["AlarmName"]
    if data.get("AlarmContributorId") is not None:
        out["alarm_contributor_id"] = data["AlarmContributorId"]
    if data.get("AlarmType") is not None:
        import capo_cloudwatch.types.alarm_type

        out["alarm_type"] = capo_cloudwatch.types.alarm_type.deserialize_aws_json_1_0(
            data["AlarmType"]
        )
    if data.get("Timestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["Timestamp"]
        )
    if data.get("HistoryItemType") is not None:
        import capo_cloudwatch.types.history_item_type

        out["history_item_type"] = (
            capo_cloudwatch.types.history_item_type.deserialize_aws_json_1_0(
                data["HistoryItemType"]
            )
        )
    if data.get("HistorySummary") is not None:
        out["history_summary"] = data["HistorySummary"]
    if data.get("HistoryData") is not None:
        out["history_data"] = data["HistoryData"]
    if data.get("AlarmContributorAttributes") is not None:
        import capo_cloudwatch.types.contributor_attributes

        out["alarm_contributor_attributes"] = (
            capo_cloudwatch.types.contributor_attributes.deserialize_aws_json_1_0(
                data["AlarmContributorAttributes"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmHistoryItem, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_name" in value:
        pairs.append((f"{key_prefix}AlarmName", str(value["alarm_name"])))
    if "alarm_contributor_id" in value:
        pairs.append(
            (f"{key_prefix}AlarmContributorId", str(value["alarm_contributor_id"]))
        )
    if "alarm_type" in value:
        import capo_cloudwatch.types.alarm_type

        capo_cloudwatch.types.alarm_type.serialize_query(
            value["alarm_type"], pairs, f"{key_prefix}AlarmType"
        )
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )
    if "history_item_type" in value:
        import capo_cloudwatch.types.history_item_type

        capo_cloudwatch.types.history_item_type.serialize_query(
            value["history_item_type"], pairs, f"{key_prefix}HistoryItemType"
        )
    if "history_summary" in value:
        pairs.append((f"{key_prefix}HistorySummary", str(value["history_summary"])))
    if "history_data" in value:
        pairs.append((f"{key_prefix}HistoryData", str(value["history_data"])))
    if "alarm_contributor_attributes" in value:
        import capo_cloudwatch.types.contributor_attributes

        capo_cloudwatch.types.contributor_attributes.serialize_query(
            value["alarm_contributor_attributes"],
            pairs,
            f"{key_prefix}AlarmContributorAttributes",
        )


def deserialize_query(el: Element) -> AlarmHistoryItem:
    out: AlarmHistoryItem = {}  # type: ignore[typeddict-item]
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_alarm_contributor_id = el.find("AlarmContributorId")
    if child_alarm_contributor_id is not None:
        out["alarm_contributor_id"] = str(child_alarm_contributor_id.text or "")
    child_alarm_type = el.find("AlarmType")
    if child_alarm_type is not None:
        import capo_cloudwatch.types.alarm_type

        out["alarm_type"] = capo_cloudwatch.types.alarm_type.deserialize_query(
            child_alarm_type
        )
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_timestamp
        )
    child_history_item_type = el.find("HistoryItemType")
    if child_history_item_type is not None:
        import capo_cloudwatch.types.history_item_type

        out["history_item_type"] = (
            capo_cloudwatch.types.history_item_type.deserialize_query(
                child_history_item_type
            )
        )
    child_history_summary = el.find("HistorySummary")
    if child_history_summary is not None:
        out["history_summary"] = str(child_history_summary.text or "")
    child_history_data = el.find("HistoryData")
    if child_history_data is not None:
        out["history_data"] = str(child_history_data.text or "")
    child_alarm_contributor_attributes = el.find("AlarmContributorAttributes")
    if child_alarm_contributor_attributes is not None:
        import capo_cloudwatch.types.contributor_attributes

        out["alarm_contributor_attributes"] = (
            capo_cloudwatch.types.contributor_attributes.deserialize_query(
                child_alarm_contributor_attributes
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmHistoryItem) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "alarm_contributor_id" in value:
        out["AlarmContributorId"] = value["alarm_contributor_id"]
    if "alarm_type" in value:
        import capo_cloudwatch.types.alarm_type

        out["AlarmType"] = capo_cloudwatch.types.alarm_type.serialize_cbor(
            value["alarm_type"]
        )
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["Timestamp"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["timestamp"]
        )
    if "history_item_type" in value:
        import capo_cloudwatch.types.history_item_type

        out["HistoryItemType"] = capo_cloudwatch.types.history_item_type.serialize_cbor(
            value["history_item_type"]
        )
    if "history_summary" in value:
        out["HistorySummary"] = value["history_summary"]
    if "history_data" in value:
        out["HistoryData"] = value["history_data"]
    if "alarm_contributor_attributes" in value:
        import capo_cloudwatch.types.contributor_attributes

        out["AlarmContributorAttributes"] = (
            capo_cloudwatch.types.contributor_attributes.serialize_cbor(
                value["alarm_contributor_attributes"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AlarmHistoryItem:
    out: AlarmHistoryItem = {}  # type: ignore[typeddict-item]
    if data.get("AlarmName") is not None:
        out["alarm_name"] = data["AlarmName"]
    if data.get("AlarmContributorId") is not None:
        out["alarm_contributor_id"] = data["AlarmContributorId"]
    if data.get("AlarmType") is not None:
        import capo_cloudwatch.types.alarm_type

        out["alarm_type"] = capo_cloudwatch.types.alarm_type.deserialize_cbor(
            data["AlarmType"]
        )
    if data.get("Timestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["Timestamp"]
        )
    if data.get("HistoryItemType") is not None:
        import capo_cloudwatch.types.history_item_type

        out["history_item_type"] = (
            capo_cloudwatch.types.history_item_type.deserialize_cbor(
                data["HistoryItemType"]
            )
        )
    if data.get("HistorySummary") is not None:
        out["history_summary"] = data["HistorySummary"]
    if data.get("HistoryData") is not None:
        out["history_data"] = data["HistoryData"]
    if data.get("AlarmContributorAttributes") is not None:
        import capo_cloudwatch.types.contributor_attributes

        out["alarm_contributor_attributes"] = (
            capo_cloudwatch.types.contributor_attributes.deserialize_cbor(
                data["AlarmContributorAttributes"]
            )
        )
    return out
