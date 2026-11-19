"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmMuteRuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_mute_rule_status
    import capo_cloudwatch.types.arn
    import capo_cloudwatch.types.mute_type
    import capo_cloudwatch.types.timestamp


class AlarmMuteRuleSummary(TypedDict, closed=True):
    alarm_mute_rule_arn: NotRequired["capo_cloudwatch.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the alarm mute rule.</p>"""
    expire_date: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time when the mute rule expires and is no longer evaluated. This field is only present if an expiration date was configured.</p>"""
    status: NotRequired[
        "capo_cloudwatch.types.alarm_mute_rule_status.AlarmMuteRuleStatus"
    ]
    """<p>The current status of the alarm mute rule. Valid values are <code>SCHEDULED</code>, <code>ACTIVE</code>, or <code>EXPIRED</code>.</p>"""
    mute_type: NotRequired["capo_cloudwatch.types.mute_type.MuteType"]
    """<p>Indicates whether the mute rule is one-time or recurring. Valid values are <code>ONE_TIME</code> or <code>RECURRING</code>.</p>"""
    last_updated_timestamp: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time when the mute rule was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmMuteRuleSummary) -> dict:
    out: dict = {}
    if "alarm_mute_rule_arn" in value:
        out["AlarmMuteRuleArn"] = value["alarm_mute_rule_arn"]
    if "expire_date" in value:
        import capo_cloudwatch.types.timestamp

        out["ExpireDate"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["expire_date"]
        )
    if "status" in value:
        import capo_cloudwatch.types.alarm_mute_rule_status

        out["Status"] = (
            capo_cloudwatch.types.alarm_mute_rule_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "mute_type" in value:
        out["MuteType"] = value["mute_type"]
    if "last_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AlarmMuteRuleSummary:
    out: AlarmMuteRuleSummary = {}  # type: ignore[typeddict-item]
    if data.get("AlarmMuteRuleArn") is not None:
        out["alarm_mute_rule_arn"] = data["AlarmMuteRuleArn"]
    if data.get("ExpireDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["expire_date"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["ExpireDate"]
        )
    if data.get("Status") is not None:
        import capo_cloudwatch.types.alarm_mute_rule_status

        out["status"] = (
            capo_cloudwatch.types.alarm_mute_rule_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("MuteType") is not None:
        out["mute_type"] = data["MuteType"]
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["last_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTimestamp"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmMuteRuleSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_mute_rule_arn" in value:
        pairs.append(
            (f"{key_prefix}AlarmMuteRuleArn", str(value["alarm_mute_rule_arn"]))
        )
    if "expire_date" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["expire_date"], pairs, f"{key_prefix}ExpireDate"
        )
    if "status" in value:
        import capo_cloudwatch.types.alarm_mute_rule_status

        capo_cloudwatch.types.alarm_mute_rule_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "mute_type" in value:
        pairs.append((f"{key_prefix}MuteType", str(value["mute_type"])))
    if "last_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["last_updated_timestamp"], pairs, f"{key_prefix}LastUpdatedTimestamp"
        )


def deserialize_query(el: Element) -> AlarmMuteRuleSummary:
    out: AlarmMuteRuleSummary = {}  # type: ignore[typeddict-item]
    child_alarm_mute_rule_arn = el.find("AlarmMuteRuleArn")
    if child_alarm_mute_rule_arn is not None:
        out["alarm_mute_rule_arn"] = str(child_alarm_mute_rule_arn.text or "")
    child_expire_date = el.find("ExpireDate")
    if child_expire_date is not None:
        import capo_cloudwatch.types.timestamp

        out["expire_date"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_expire_date
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudwatch.types.alarm_mute_rule_status

        out["status"] = capo_cloudwatch.types.alarm_mute_rule_status.deserialize_query(
            child_status
        )
    child_mute_type = el.find("MuteType")
    if child_mute_type is not None:
        out["mute_type"] = str(child_mute_type.text or "")
    child_last_updated_timestamp = el.find("LastUpdatedTimestamp")
    if child_last_updated_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["last_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_query(
                child_last_updated_timestamp
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmMuteRuleSummary) -> dict:
    out: dict = {}
    if "alarm_mute_rule_arn" in value:
        out["AlarmMuteRuleArn"] = value["alarm_mute_rule_arn"]
    if "expire_date" in value:
        import capo_cloudwatch.types.timestamp

        out["ExpireDate"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["expire_date"]
        )
    if "status" in value:
        import capo_cloudwatch.types.alarm_mute_rule_status

        out["Status"] = capo_cloudwatch.types.alarm_mute_rule_status.serialize_cbor(
            value["status"]
        )
    if "mute_type" in value:
        out["MuteType"] = value["mute_type"]
    if "last_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["LastUpdatedTimestamp"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["last_updated_timestamp"]
        )
    return out


def deserialize_cbor(data: dict) -> AlarmMuteRuleSummary:
    out: AlarmMuteRuleSummary = {}  # type: ignore[typeddict-item]
    if data.get("AlarmMuteRuleArn") is not None:
        out["alarm_mute_rule_arn"] = data["AlarmMuteRuleArn"]
    if data.get("ExpireDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["expire_date"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["ExpireDate"]
        )
    if data.get("Status") is not None:
        import capo_cloudwatch.types.alarm_mute_rule_status

        out["status"] = capo_cloudwatch.types.alarm_mute_rule_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("MuteType") is not None:
        out["mute_type"] = data["MuteType"]
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["last_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_cbor(
                data["LastUpdatedTimestamp"]
            )
        )
    return out
