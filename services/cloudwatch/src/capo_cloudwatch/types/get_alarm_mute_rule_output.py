"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetAlarmMuteRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_description
    import capo_cloudwatch.types.alarm_mute_rule_status
    import capo_cloudwatch.types.arn
    import capo_cloudwatch.types.mute_targets
    import capo_cloudwatch.types.mute_type
    import capo_cloudwatch.types.name
    import capo_cloudwatch.types.rule
    import capo_cloudwatch.types.timestamp


class GetAlarmMuteRuleOutput(TypedDict, closed=True):
    name: NotRequired["capo_cloudwatch.types.name.Name"]
    """<p>The name of the alarm mute rule.</p>"""
    alarm_mute_rule_arn: NotRequired["capo_cloudwatch.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the alarm mute rule.</p>"""
    description: NotRequired["capo_cloudwatch.types.alarm_description.AlarmDescription"]
    """<p>The description of the alarm mute rule.</p>"""
    rule: NotRequired["capo_cloudwatch.types.rule.Rule"]
    """<p>The configuration that defines when and how long alarms are muted.</p>"""
    mute_targets: NotRequired["capo_cloudwatch.types.mute_targets.MuteTargets"]
    """<p>Specifies which alarms this rule applies to.</p>"""
    start_date: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time when the mute rule becomes active. If not set, the rule is active immediately.</p>"""
    expire_date: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time when the mute rule expires and is no longer evaluated.</p>"""
    status: NotRequired[
        "capo_cloudwatch.types.alarm_mute_rule_status.AlarmMuteRuleStatus"
    ]
    """<p>The current status of the alarm mute rule. Valid values are <code>SCHEDULED</code>, <code>ACTIVE</code>, or <code>EXPIRED</code>.</p>"""
    last_updated_timestamp: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time when the mute rule was last updated.</p>"""
    mute_type: NotRequired["capo_cloudwatch.types.mute_type.MuteType"]
    """<p>Indicates whether the mute rule is one-time or recurring. Valid values are <code>ONE_TIME</code> or <code>RECURRING</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAlarmMuteRuleOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "alarm_mute_rule_arn" in value:
        out["AlarmMuteRuleArn"] = value["alarm_mute_rule_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "rule" in value:
        import capo_cloudwatch.types.rule

        out["Rule"] = capo_cloudwatch.types.rule.serialize_aws_json_1_0(value["rule"])
    if "mute_targets" in value:
        import capo_cloudwatch.types.mute_targets

        out["MuteTargets"] = capo_cloudwatch.types.mute_targets.serialize_aws_json_1_0(
            value["mute_targets"]
        )
    if "start_date" in value:
        import capo_cloudwatch.types.timestamp

        out["StartDate"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["start_date"]
        )
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
    if "last_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    if "mute_type" in value:
        out["MuteType"] = value["mute_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAlarmMuteRuleOutput:
    out: GetAlarmMuteRuleOutput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AlarmMuteRuleArn") is not None:
        out["alarm_mute_rule_arn"] = data["AlarmMuteRuleArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Rule") is not None:
        import capo_cloudwatch.types.rule

        out["rule"] = capo_cloudwatch.types.rule.deserialize_aws_json_1_0(data["Rule"])
    if data.get("MuteTargets") is not None:
        import capo_cloudwatch.types.mute_targets

        out["mute_targets"] = (
            capo_cloudwatch.types.mute_targets.deserialize_aws_json_1_0(
                data["MuteTargets"]
            )
        )
    if data.get("StartDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["start_date"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["StartDate"]
        )
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
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["last_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTimestamp"]
            )
        )
    if data.get("MuteType") is not None:
        out["mute_type"] = data["MuteType"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAlarmMuteRuleOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "alarm_mute_rule_arn" in value:
        pairs.append(
            (f"{key_prefix}AlarmMuteRuleArn", str(value["alarm_mute_rule_arn"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "rule" in value:
        import capo_cloudwatch.types.rule

        capo_cloudwatch.types.rule.serialize_query(
            value["rule"], pairs, f"{key_prefix}Rule"
        )
    if "mute_targets" in value:
        import capo_cloudwatch.types.mute_targets

        capo_cloudwatch.types.mute_targets.serialize_query(
            value["mute_targets"], pairs, f"{key_prefix}MuteTargets"
        )
    if "start_date" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["start_date"], pairs, f"{key_prefix}StartDate"
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
    if "last_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["last_updated_timestamp"], pairs, f"{key_prefix}LastUpdatedTimestamp"
        )
    if "mute_type" in value:
        pairs.append((f"{key_prefix}MuteType", str(value["mute_type"])))


def deserialize_query(el: Element) -> GetAlarmMuteRuleOutput:
    out: GetAlarmMuteRuleOutput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_alarm_mute_rule_arn = el.find("AlarmMuteRuleArn")
    if child_alarm_mute_rule_arn is not None:
        out["alarm_mute_rule_arn"] = str(child_alarm_mute_rule_arn.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_rule = el.find("Rule")
    if child_rule is not None:
        import capo_cloudwatch.types.rule

        out["rule"] = capo_cloudwatch.types.rule.deserialize_query(child_rule)
    child_mute_targets = el.find("MuteTargets")
    if child_mute_targets is not None:
        import capo_cloudwatch.types.mute_targets

        out["mute_targets"] = capo_cloudwatch.types.mute_targets.deserialize_query(
            child_mute_targets
        )
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import capo_cloudwatch.types.timestamp

        out["start_date"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_start_date
        )
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
    child_last_updated_timestamp = el.find("LastUpdatedTimestamp")
    if child_last_updated_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["last_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_query(
                child_last_updated_timestamp
            )
        )
    child_mute_type = el.find("MuteType")
    if child_mute_type is not None:
        out["mute_type"] = str(child_mute_type.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAlarmMuteRuleOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "alarm_mute_rule_arn" in value:
        out["AlarmMuteRuleArn"] = value["alarm_mute_rule_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "rule" in value:
        import capo_cloudwatch.types.rule

        out["Rule"] = capo_cloudwatch.types.rule.serialize_cbor(value["rule"])
    if "mute_targets" in value:
        import capo_cloudwatch.types.mute_targets

        out["MuteTargets"] = capo_cloudwatch.types.mute_targets.serialize_cbor(
            value["mute_targets"]
        )
    if "start_date" in value:
        import capo_cloudwatch.types.timestamp

        out["StartDate"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["start_date"]
        )
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
    if "last_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["LastUpdatedTimestamp"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["last_updated_timestamp"]
        )
    if "mute_type" in value:
        out["MuteType"] = value["mute_type"]
    return out


def deserialize_cbor(data: dict) -> GetAlarmMuteRuleOutput:
    out: GetAlarmMuteRuleOutput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AlarmMuteRuleArn") is not None:
        out["alarm_mute_rule_arn"] = data["AlarmMuteRuleArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Rule") is not None:
        import capo_cloudwatch.types.rule

        out["rule"] = capo_cloudwatch.types.rule.deserialize_cbor(data["Rule"])
    if data.get("MuteTargets") is not None:
        import capo_cloudwatch.types.mute_targets

        out["mute_targets"] = capo_cloudwatch.types.mute_targets.deserialize_cbor(
            data["MuteTargets"]
        )
    if data.get("StartDate") is not None:
        import capo_cloudwatch.types.timestamp

        out["start_date"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["StartDate"]
        )
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
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["last_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_cbor(
                data["LastUpdatedTimestamp"]
            )
        )
    if data.get("MuteType") is not None:
        out["mute_type"] = data["MuteType"]
    return out
