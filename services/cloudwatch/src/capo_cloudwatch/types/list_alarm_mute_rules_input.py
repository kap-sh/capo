"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListAlarmMuteRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_mute_rule_statuses
    import capo_cloudwatch.types.max_records
    import capo_cloudwatch.types.name
    import capo_cloudwatch.types.next_token


class ListAlarmMuteRulesInput(TypedDict, closed=True):
    alarm_name: NotRequired["capo_cloudwatch.types.name.Name"]
    """<p>Filter results to show only mute rules that target the specified alarm name.</p>"""
    statuses: NotRequired[
        "capo_cloudwatch.types.alarm_mute_rule_statuses.AlarmMuteRuleStatuses"
    ]
    """<p>Filter results to show only mute rules with the specified statuses. Valid values are <code>SCHEDULED</code>, <code>ACTIVE</code>, or <code>EXPIRED</code>.</p>"""
    max_records: NotRequired["capo_cloudwatch.types.max_records.MaxRecords"]
    """<p>The maximum number of mute rules to return in one call. The default is 50.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>The token returned from a previous call to indicate where to continue retrieving results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAlarmMuteRulesInput) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "statuses" in value:
        import capo_cloudwatch.types.alarm_mute_rule_statuses

        out["Statuses"] = (
            capo_cloudwatch.types.alarm_mute_rule_statuses.serialize_aws_json_1_0(
                value["statuses"]
            )
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAlarmMuteRulesInput:
    out: ListAlarmMuteRulesInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmName") is not None:
        out["alarm_name"] = data["AlarmName"]
    if data.get("Statuses") is not None:
        import capo_cloudwatch.types.alarm_mute_rule_statuses

        out["statuses"] = (
            capo_cloudwatch.types.alarm_mute_rule_statuses.deserialize_aws_json_1_0(
                data["Statuses"]
            )
        )
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListAlarmMuteRulesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_name" in value:
        pairs.append((f"{key_prefix}AlarmName", str(value["alarm_name"])))
    if "statuses" in value:
        import capo_cloudwatch.types.alarm_mute_rule_statuses

        capo_cloudwatch.types.alarm_mute_rule_statuses.serialize_query(
            value["statuses"], pairs, f"{key_prefix}Statuses"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListAlarmMuteRulesInput:
    out: ListAlarmMuteRulesInput = {}  # type: ignore[typeddict-item]
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_statuses = el.find("Statuses")
    if child_statuses is not None:
        import capo_cloudwatch.types.alarm_mute_rule_statuses

        out["statuses"] = (
            capo_cloudwatch.types.alarm_mute_rule_statuses.deserialize_query(
                child_statuses
            )
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAlarmMuteRulesInput) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "statuses" in value:
        import capo_cloudwatch.types.alarm_mute_rule_statuses

        out["Statuses"] = capo_cloudwatch.types.alarm_mute_rule_statuses.serialize_cbor(
            value["statuses"]
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAlarmMuteRulesInput:
    out: ListAlarmMuteRulesInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmName") is not None:
        out["alarm_name"] = data["AlarmName"]
    if data.get("Statuses") is not None:
        import capo_cloudwatch.types.alarm_mute_rule_statuses

        out["statuses"] = (
            capo_cloudwatch.types.alarm_mute_rule_statuses.deserialize_cbor(
                data["Statuses"]
            )
        )
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
