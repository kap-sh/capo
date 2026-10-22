"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ActionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_tags_propagation


class ActionConfiguration(TypedDict, closed=True):
    alarm_tags_propagation: NotRequired[
        "capo_cloudwatch.types.alarm_tags_propagation.AlarmTagsPropagation"
    ]
    """<p>Settings for including the alarm's tags in its action notifications and state-change events.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionConfiguration) -> dict:
    out: dict = {}
    if "alarm_tags_propagation" in value:
        import capo_cloudwatch.types.alarm_tags_propagation

        out["AlarmTagsPropagation"] = (
            capo_cloudwatch.types.alarm_tags_propagation.serialize_aws_json_1_0(
                value["alarm_tags_propagation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ActionConfiguration:
    out: ActionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AlarmTagsPropagation") is not None:
        import capo_cloudwatch.types.alarm_tags_propagation

        out["alarm_tags_propagation"] = (
            capo_cloudwatch.types.alarm_tags_propagation.deserialize_aws_json_1_0(
                data["AlarmTagsPropagation"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ActionConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_tags_propagation" in value:
        import capo_cloudwatch.types.alarm_tags_propagation

        capo_cloudwatch.types.alarm_tags_propagation.serialize_query(
            value["alarm_tags_propagation"], pairs, f"{key_prefix}AlarmTagsPropagation"
        )


def deserialize_query(el: Element) -> ActionConfiguration:
    out: ActionConfiguration = {}  # type: ignore[typeddict-item]
    child_alarm_tags_propagation = el.find("AlarmTagsPropagation")
    if child_alarm_tags_propagation is not None:
        import capo_cloudwatch.types.alarm_tags_propagation

        out["alarm_tags_propagation"] = (
            capo_cloudwatch.types.alarm_tags_propagation.deserialize_query(
                child_alarm_tags_propagation
            )
        )
    return out
