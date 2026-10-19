"""Generated from Smithy shape ``com.amazonaws.ssm#PatchRuleGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.patch_rule_list


class PatchRuleGroup(TypedDict, closed=True):
    patch_rules: "capo_ssm.types.patch_rule_list.PatchRuleList"
    """<p>The rules that make up the rule group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchRuleGroup) -> dict:
    out: dict = {}
    import capo_ssm.types.patch_rule_list

    out["PatchRules"] = capo_ssm.types.patch_rule_list.serialize_aws_json_1_1(
        value["patch_rules"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PatchRuleGroup:
    out: PatchRuleGroup = {}  # type: ignore[typeddict-item]
    if data.get("PatchRules") is not None:
        import capo_ssm.types.patch_rule_list

        out["patch_rules"] = capo_ssm.types.patch_rule_list.deserialize_aws_json_1_1(
            data["PatchRules"]
        )
    else:
        out["patch_rules"] = []
    return out
