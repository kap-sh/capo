"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmTagsPropagation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_tags_propagation_enabled
    import capo_cloudwatch.types.alarm_tags_propagation_tag_keys


class AlarmTagsPropagation(TypedDict, closed=True):
    enabled: NotRequired[
        "capo_cloudwatch.types.alarm_tags_propagation_enabled.AlarmTagsPropagationEnabled"
    ]
    """<p>Set to <code>true</code> to include the alarm's tags. Set to <code>false</code> to stop including them.</p> <p>When this is <code>true</code>, you must have the <code>cloudwatch:ListTagsForResource</code> permission on the alarm to create or update it.</p>"""
    included_tag_keys: NotRequired[
        "capo_cloudwatch.types.alarm_tags_propagation_tag_keys.AlarmTagsPropagationTagKeys"
    ]
    """<p>The tag keys to include. Only the alarm's tags with these keys are included.</p> <p>You can specify 1 to 50 tag keys. Each tag key must be 1 to 128 characters long.</p> <p>You can't specify both <code>IncludedTagKeys</code> and <code>ExcludedTagKeys</code>.</p>"""
    excluded_tag_keys: NotRequired[
        "capo_cloudwatch.types.alarm_tags_propagation_tag_keys.AlarmTagsPropagationTagKeys"
    ]
    """<p>The tag keys to exclude. All of the alarm's tags except those with these keys are included.</p> <p>You can specify 1 to 50 tag keys. Each tag key must be 1 to 128 characters long.</p> <p>You can't specify both <code>IncludedTagKeys</code> and <code>ExcludedTagKeys</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmTagsPropagation) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "included_tag_keys" in value:
        import capo_cloudwatch.types.alarm_tags_propagation_tag_keys

        out["IncludedTagKeys"] = (
            capo_cloudwatch.types.alarm_tags_propagation_tag_keys.serialize_aws_json_1_0(
                value["included_tag_keys"]
            )
        )
    if "excluded_tag_keys" in value:
        import capo_cloudwatch.types.alarm_tags_propagation_tag_keys

        out["ExcludedTagKeys"] = (
            capo_cloudwatch.types.alarm_tags_propagation_tag_keys.serialize_aws_json_1_0(
                value["excluded_tag_keys"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AlarmTagsPropagation:
    out: AlarmTagsPropagation = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("IncludedTagKeys") is not None:
        import capo_cloudwatch.types.alarm_tags_propagation_tag_keys

        out["included_tag_keys"] = (
            capo_cloudwatch.types.alarm_tags_propagation_tag_keys.deserialize_aws_json_1_0(
                data["IncludedTagKeys"]
            )
        )
    if data.get("ExcludedTagKeys") is not None:
        import capo_cloudwatch.types.alarm_tags_propagation_tag_keys

        out["excluded_tag_keys"] = (
            capo_cloudwatch.types.alarm_tags_propagation_tag_keys.deserialize_aws_json_1_0(
                data["ExcludedTagKeys"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmTagsPropagation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))
    if "included_tag_keys" in value:
        import capo_cloudwatch.types.alarm_tags_propagation_tag_keys

        capo_cloudwatch.types.alarm_tags_propagation_tag_keys.serialize_query(
            value["included_tag_keys"], pairs, f"{key_prefix}IncludedTagKeys"
        )
    if "excluded_tag_keys" in value:
        import capo_cloudwatch.types.alarm_tags_propagation_tag_keys

        capo_cloudwatch.types.alarm_tags_propagation_tag_keys.serialize_query(
            value["excluded_tag_keys"], pairs, f"{key_prefix}ExcludedTagKeys"
        )


def deserialize_query(el: Element) -> AlarmTagsPropagation:
    out: AlarmTagsPropagation = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_included_tag_keys = el.find("IncludedTagKeys")
    if child_included_tag_keys is not None:
        import capo_cloudwatch.types.alarm_tags_propagation_tag_keys

        out["included_tag_keys"] = (
            capo_cloudwatch.types.alarm_tags_propagation_tag_keys.deserialize_query(
                child_included_tag_keys
            )
        )
    child_excluded_tag_keys = el.find("ExcludedTagKeys")
    if child_excluded_tag_keys is not None:
        import capo_cloudwatch.types.alarm_tags_propagation_tag_keys

        out["excluded_tag_keys"] = (
            capo_cloudwatch.types.alarm_tags_propagation_tag_keys.deserialize_query(
                child_excluded_tag_keys
            )
        )
    return out
