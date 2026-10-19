"""Generated from Smithy shape ``com.amazonaws.waf#WafOverrideAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.waf_override_action_type


class WafOverrideAction(TypedDict, closed=True):
    type: "capo_waf.types.waf_override_action_type.WafOverrideActionType"
    """<p> <code>COUNT</code> overrides the action specified by the individual rule within a <code>RuleGroup</code> . If set to <code>NONE</code>, the rule's action will take place.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafOverrideAction) -> dict:
    out: dict = {}
    import capo_waf.types.waf_override_action_type

    out["Type"] = capo_waf.types.waf_override_action_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> WafOverrideAction:
    out: WafOverrideAction = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_waf.types.waf_override_action_type

        out["type"] = capo_waf.types.waf_override_action_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_waf.types.waf_override_action_type.WafOverrideActionType", ""
        )
    return out
