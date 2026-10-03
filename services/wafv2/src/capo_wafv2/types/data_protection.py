"""Generated from Smithy shape ``com.amazonaws.wafv2#DataProtection``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.boolean
    import capo_wafv2.types.data_protection_action
    import capo_wafv2.types.field_to_protect


class DataProtection(TypedDict, closed=True):
    field: "capo_wafv2.types.field_to_protect.FieldToProtect"
    """<p>Specifies the field type and optional keys to apply the protection behavior to. </p>"""
    action: "capo_wafv2.types.data_protection_action.DataProtectionAction"
    """<p>Specifies how to protect the field. WAF can apply a one-way hash to the field or hard code a string substitution. </p> <ul> <li> <p>One-way hash example: <code>ade099751dEXAMPLEHASH2ea9f3393f80dd5d3bEXAMPLEHASH966ae0d3cd5a1e</code> </p> </li> <li> <p>Substitution example: <code>REDACTED</code> </p> </li> </ul>"""
    exclude_rule_match_details: "capo_wafv2.types.boolean.Boolean"
    """<p>Specifies whether to also exclude any rule match details from the data protection you have enabled for a given field. WAF logs these details for non-terminating matching rules and for the terminating matching rule. For additional information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html">Log fields for web ACL traffic</a> in the <i>WAF Developer Guide</i>.</p> <p>Default: <code>FALSE</code> </p>"""
    exclude_rate_based_details: "capo_wafv2.types.boolean.Boolean"
    """<p>Specifies whether to also exclude any rate-based rule details from the data protection you have enabled for a given field. If you specify this exception, RateBasedDetails will show the value of the field. For additional information, see the log field <code>rateBasedRuleList</code> at <a href="https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html">Log fields for web ACL traffic</a> in the <i>WAF Developer Guide</i>.</p> <p>Default: <code>FALSE</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProtection) -> dict:
    out: dict = {}
    import capo_wafv2.types.field_to_protect

    out["Field"] = capo_wafv2.types.field_to_protect.serialize_aws_json_1_1(
        value["field"]
    )
    import capo_wafv2.types.data_protection_action

    out["Action"] = capo_wafv2.types.data_protection_action.serialize_aws_json_1_1(
        value["action"]
    )
    out["ExcludeRuleMatchDetails"] = value.get("exclude_rule_match_details", False)
    out["ExcludeRateBasedDetails"] = value.get("exclude_rate_based_details", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DataProtection:
    out: DataProtection = {}  # type: ignore[typeddict-item]
    if data.get("Field") is not None:
        import capo_wafv2.types.field_to_protect

        out["field"] = capo_wafv2.types.field_to_protect.deserialize_aws_json_1_1(
            data["Field"]
        )
    else:
        raise DeserializationError("DataProtection.field required")
    if data.get("Action") is not None:
        import capo_wafv2.types.data_protection_action

        out["action"] = (
            capo_wafv2.types.data_protection_action.deserialize_aws_json_1_1(
                data["Action"]
            )
        )
    else:
        raise DeserializationError("DataProtection.action required")
    if data.get("ExcludeRuleMatchDetails") is not None:
        out["exclude_rule_match_details"] = data["ExcludeRuleMatchDetails"]
    else:
        out["exclude_rule_match_details"] = False
    if data.get("ExcludeRateBasedDetails") is not None:
        out["exclude_rate_based_details"] = data["ExcludeRateBasedDetails"]
    else:
        out["exclude_rate_based_details"] = False
    return out
