"""Generated from Smithy shape ``com.amazonaws.wafv2#AWSManagedRulesBotControlRuleSet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.enable_machine_learning
    import capo_wafv2.types.inspection_level


class AWSManagedRulesBotControlRuleSet(TypedDict, closed=True):
    inspection_level: "capo_wafv2.types.inspection_level.InspectionLevel"
    """<p>The inspection level to use for the Bot Control rule group. The common level is the least expensive. The targeted level includes all common level rules and adds rules with more advanced inspection criteria. For details, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html">WAF Bot Control rule group</a> in the <i>WAF Developer Guide</i>.</p>"""
    enable_machine_learning: (
        "capo_wafv2.types.enable_machine_learning.EnableMachineLearning"
    )
    """<p>Applies only to the targeted inspection level. </p> <p>Determines whether to use machine learning (ML) to analyze your web traffic for bot-related activity. Machine learning is required for the Bot Control rules <code>TGT_ML_CoordinatedActivityLow</code> and <code>TGT_ML_CoordinatedActivityMedium</code>, which inspect for anomalous behavior that might indicate distributed, coordinated bot activity.</p> <p>For more information about this choice, see the listing for these rules in the table at <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html#aws-managed-rule-groups-bot-rules">Bot Control rules listing</a> in the <i>WAF Developer Guide</i>.</p> <p>Default: <code>TRUE</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AWSManagedRulesBotControlRuleSet) -> dict:
    out: dict = {}
    import capo_wafv2.types.inspection_level

    out["InspectionLevel"] = capo_wafv2.types.inspection_level.serialize_aws_json_1_1(
        value["inspection_level"]
    )
    out["EnableMachineLearning"] = value.get("enable_machine_learning", True)
    return out


def deserialize_aws_json_1_1(data: dict) -> AWSManagedRulesBotControlRuleSet:
    out: AWSManagedRulesBotControlRuleSet = {}  # type: ignore[typeddict-item]
    if data.get("InspectionLevel") is not None:
        import capo_wafv2.types.inspection_level

        out["inspection_level"] = (
            capo_wafv2.types.inspection_level.deserialize_aws_json_1_1(
                data["InspectionLevel"]
            )
        )
    else:
        raise DeserializationError(
            "AWSManagedRulesBotControlRuleSet.inspection_level required"
        )
    if data.get("EnableMachineLearning") is not None:
        out["enable_machine_learning"] = data["EnableMachineLearning"]
    else:
        out["enable_machine_learning"] = True
    return out
