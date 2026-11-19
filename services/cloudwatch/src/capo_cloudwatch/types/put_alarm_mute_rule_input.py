"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutAlarmMuteRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_description
    import capo_cloudwatch.types.mute_targets
    import capo_cloudwatch.types.name
    import capo_cloudwatch.types.rule
    import capo_cloudwatch.types.tag_list
    import capo_cloudwatch.types.timestamp


class PutAlarmMuteRuleInput(TypedDict, closed=True):
    name: NotRequired["capo_cloudwatch.types.name.Name"]
    """<p>The name of the alarm mute rule. This name must be unique within your Amazon Web Services account and region.</p>"""
    description: NotRequired["capo_cloudwatch.types.alarm_description.AlarmDescription"]
    """<p>A description of the alarm mute rule that helps you identify its purpose.</p>"""
    rule: NotRequired["capo_cloudwatch.types.rule.Rule"]
    """<p>The configuration that defines when and how long alarms should be muted.</p>"""
    mute_targets: NotRequired["capo_cloudwatch.types.mute_targets.MuteTargets"]
    """<p>Specifies which alarms this rule applies to.</p>"""
    tags: NotRequired["capo_cloudwatch.types.tag_list.TagList"]
    """<p>A list of key-value pairs to associate with the alarm mute rule. You can use tags to categorize and manage your mute rules.</p>"""
    start_date: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time after which the mute rule takes effect, specified as a timestamp in ISO 8601 format (for example, <code>2026-04-15T08:00:00Z</code>). If not specified, the mute rule takes effect immediately upon creation and the mutes are applied as per the schedule expression.</p>"""
    expire_date: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time when the mute rule expires and is no longer evaluated, specified as a timestamp in ISO 8601 format (for example, <code>2026-12-31T23:59:59Z</code>). After this time, the rule status becomes EXPIRED and will no longer mute the targeted alarms.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutAlarmMuteRuleInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
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
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        out["Tags"] = capo_cloudwatch.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> PutAlarmMuteRuleInput:
    out: PutAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
    if data.get("Tags") is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
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
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutAlarmMuteRuleInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
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
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        capo_cloudwatch.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
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


def deserialize_query(el: Element) -> PutAlarmMuteRuleInput:
    out: PutAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
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
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_query(child_tags)
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutAlarmMuteRuleInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
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
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        out["Tags"] = capo_cloudwatch.types.tag_list.serialize_cbor(value["tags"])
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
    return out


def deserialize_cbor(data: dict) -> PutAlarmMuteRuleInput:
    out: PutAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
    if data.get("Tags") is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_cbor(data["Tags"])
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
    return out
