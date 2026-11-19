"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmHistoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_name
    import capo_cloudwatch.types.alarm_types
    import capo_cloudwatch.types.contributor_id
    import capo_cloudwatch.types.history_item_type
    import capo_cloudwatch.types.max_records
    import capo_cloudwatch.types.next_token
    import capo_cloudwatch.types.scan_by
    import capo_cloudwatch.types.timestamp


class DescribeAlarmHistoryInput(TypedDict, closed=True):
    alarm_name: NotRequired["capo_cloudwatch.types.alarm_name.AlarmName"]
    """<p>The name of the alarm.</p>"""
    alarm_contributor_id: NotRequired[
        "capo_cloudwatch.types.contributor_id.ContributorId"
    ]
    """<p>The unique identifier of a specific alarm contributor to filter the alarm history results.</p>"""
    alarm_types: NotRequired["capo_cloudwatch.types.alarm_types.AlarmTypes"]
    """<p>Use this parameter to specify whether you want the operation to return metric alarms, composite alarms, or log alarms. If you omit this parameter, only metric alarms are returned.</p>"""
    history_item_type: NotRequired[
        "capo_cloudwatch.types.history_item_type.HistoryItemType"
    ]
    """<p>The type of alarm histories to retrieve.</p>"""
    start_date: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The starting date to retrieve alarm history.</p>"""
    end_date: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The ending date to retrieve alarm history.</p>"""
    max_records: NotRequired["capo_cloudwatch.types.max_records.MaxRecords"]
    """<p>The maximum number of alarm history records to retrieve.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>The token returned by a previous call to indicate that there is more data available.</p>"""
    scan_by: NotRequired["capo_cloudwatch.types.scan_by.ScanBy"]
    """<p>Specified whether to return the newest or oldest alarm history first. Specify <code>TimestampDescending</code> to have the newest event history returned first, and specify <code>TimestampAscending</code> to have the oldest history returned first.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmHistoryInput) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "alarm_contributor_id" in value:
        out["AlarmContributorId"] = value["alarm_contributor_id"]
    if "alarm_types" in value:
        import capo_cloudwatch.types.alarm_types

        out["AlarmTypes"] = capo_cloudwatch.types.alarm_types.serialize_aws_json_1_0(
            value["alarm_types"]
        )
    if "history_item_type" in value:
        import capo_cloudwatch.types.history_item_type

        out["HistoryItemType"] = (
            capo_cloudwatch.types.history_item_type.serialize_aws_json_1_0(
                value["history_item_type"]
            )
        )
    if "start_date" in value:
        import capo_cloudwatch.types.timestamp

        out["StartDate"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["start_date"]
        )
    if "end_date" in value:
        import capo_cloudwatch.types.timestamp

        out["EndDate"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["end_date"]
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "scan_by" in value:
        import capo_cloudwatch.types.scan_by

        out["ScanBy"] = capo_cloudwatch.types.scan_by.serialize_aws_json_1_0(
            value["scan_by"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmHistoryInput:
    out: DescribeAlarmHistoryInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmName") is not None:
        out["alarm_name"] = data["AlarmName"]
    if data.get("AlarmContributorId") is not None:
        out["alarm_contributor_id"] = data["AlarmContributorId"]
    if data.get("AlarmTypes") is not None:
        import capo_cloudwatch.types.alarm_types

        out["alarm_types"] = capo_cloudwatch.types.alarm_types.deserialize_aws_json_1_0(
            data["AlarmTypes"]
        )
    if data.get("HistoryItemType") is not None:
        import capo_cloudwatch.types.history_item_type

        out["history_item_type"] = (
            capo_cloudwatch.types.history_item_type.deserialize_aws_json_1_0(
                data["HistoryItemType"]
            )
        )
    if data.get("StartDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["start_date"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["StartDate"]
        )
    if data.get("EndDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["end_date"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["EndDate"]
        )
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ScanBy") is not None:
        import capo_cloudwatch.types.scan_by

        out["scan_by"] = capo_cloudwatch.types.scan_by.deserialize_aws_json_1_0(
            data["ScanBy"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmHistoryInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_name" in value:
        pairs.append((f"{key_prefix}AlarmName", str(value["alarm_name"])))
    if "alarm_contributor_id" in value:
        pairs.append(
            (f"{key_prefix}AlarmContributorId", str(value["alarm_contributor_id"]))
        )
    if "alarm_types" in value:
        import capo_cloudwatch.types.alarm_types

        capo_cloudwatch.types.alarm_types.serialize_query(
            value["alarm_types"], pairs, f"{key_prefix}AlarmTypes"
        )
    if "history_item_type" in value:
        import capo_cloudwatch.types.history_item_type

        capo_cloudwatch.types.history_item_type.serialize_query(
            value["history_item_type"], pairs, f"{key_prefix}HistoryItemType"
        )
    if "start_date" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["start_date"], pairs, f"{key_prefix}StartDate"
        )
    if "end_date" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["end_date"], pairs, f"{key_prefix}EndDate"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "scan_by" in value:
        import capo_cloudwatch.types.scan_by

        capo_cloudwatch.types.scan_by.serialize_query(
            value["scan_by"], pairs, f"{key_prefix}ScanBy"
        )


def deserialize_query(el: Element) -> DescribeAlarmHistoryInput:
    out: DescribeAlarmHistoryInput = {}  # type: ignore[typeddict-item]
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_alarm_contributor_id = el.find("AlarmContributorId")
    if child_alarm_contributor_id is not None:
        out["alarm_contributor_id"] = str(child_alarm_contributor_id.text or "")
    child_alarm_types = el.find("AlarmTypes")
    if child_alarm_types is not None:
        import capo_cloudwatch.types.alarm_types

        out["alarm_types"] = capo_cloudwatch.types.alarm_types.deserialize_query(
            child_alarm_types
        )
    child_history_item_type = el.find("HistoryItemType")
    if child_history_item_type is not None:
        import capo_cloudwatch.types.history_item_type

        out["history_item_type"] = (
            capo_cloudwatch.types.history_item_type.deserialize_query(
                child_history_item_type
            )
        )
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import capo_cloudwatch.types.timestamp

        out["start_date"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_start_date
        )
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import capo_cloudwatch.types.timestamp

        out["end_date"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_end_date
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_scan_by = el.find("ScanBy")
    if child_scan_by is not None:
        import capo_cloudwatch.types.scan_by

        out["scan_by"] = capo_cloudwatch.types.scan_by.deserialize_query(child_scan_by)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAlarmHistoryInput) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "alarm_contributor_id" in value:
        out["AlarmContributorId"] = value["alarm_contributor_id"]
    if "alarm_types" in value:
        import capo_cloudwatch.types.alarm_types

        out["AlarmTypes"] = capo_cloudwatch.types.alarm_types.serialize_cbor(
            value["alarm_types"]
        )
    if "history_item_type" in value:
        import capo_cloudwatch.types.history_item_type

        out["HistoryItemType"] = capo_cloudwatch.types.history_item_type.serialize_cbor(
            value["history_item_type"]
        )
    if "start_date" in value:
        import capo_cloudwatch.types.timestamp

        out["StartDate"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["start_date"]
        )
    if "end_date" in value:
        import capo_cloudwatch.types.timestamp

        out["EndDate"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["end_date"]
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "scan_by" in value:
        import capo_cloudwatch.types.scan_by

        out["ScanBy"] = capo_cloudwatch.types.scan_by.serialize_cbor(value["scan_by"])
    return out


def deserialize_cbor(data: dict) -> DescribeAlarmHistoryInput:
    out: DescribeAlarmHistoryInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmName") is not None:
        out["alarm_name"] = data["AlarmName"]
    if data.get("AlarmContributorId") is not None:
        out["alarm_contributor_id"] = data["AlarmContributorId"]
    if data.get("AlarmTypes") is not None:
        import capo_cloudwatch.types.alarm_types

        out["alarm_types"] = capo_cloudwatch.types.alarm_types.deserialize_cbor(
            data["AlarmTypes"]
        )
    if data.get("HistoryItemType") is not None:
        import capo_cloudwatch.types.history_item_type

        out["history_item_type"] = (
            capo_cloudwatch.types.history_item_type.deserialize_cbor(
                data["HistoryItemType"]
            )
        )
    if data.get("StartDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["start_date"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["StartDate"]
        )
    if data.get("EndDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["end_date"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["EndDate"]
        )
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ScanBy") is not None:
        import capo_cloudwatch.types.scan_by

        out["scan_by"] = capo_cloudwatch.types.scan_by.deserialize_cbor(data["ScanBy"])
    return out
