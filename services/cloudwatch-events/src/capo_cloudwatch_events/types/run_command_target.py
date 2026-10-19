"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RunCommandTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.run_command_target_key
    import capo_cloudwatch_events.types.run_command_target_values


class RunCommandTarget(TypedDict, closed=True):
    key: "capo_cloudwatch_events.types.run_command_target_key.RunCommandTargetKey"
    """<p>Can be either <code>tag:</code> <i>tag-key</i> or <code>InstanceIds</code>.</p>"""
    values: (
        "capo_cloudwatch_events.types.run_command_target_values.RunCommandTargetValues"
    )
    """<p>If <code>Key</code> is <code>tag:</code> <i>tag-key</i>, <code>Values</code> is a list of tag values. If <code>Key</code> is <code>InstanceIds</code>, <code>Values</code> is a list of Amazon EC2 instance IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunCommandTarget) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_cloudwatch_events.types.run_command_target_values

    out["Values"] = (
        capo_cloudwatch_events.types.run_command_target_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RunCommandTarget:
    out: RunCommandTarget = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Values") is not None:
        import capo_cloudwatch_events.types.run_command_target_values

        out["values"] = (
            capo_cloudwatch_events.types.run_command_target_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
