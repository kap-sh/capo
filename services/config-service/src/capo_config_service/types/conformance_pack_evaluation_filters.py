"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackEvaluationFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_compliance_resource_ids
    import capo_config_service.types.conformance_pack_compliance_type
    import capo_config_service.types.conformance_pack_config_rule_names
    import capo_config_service.types.string_with_char_limit256


class ConformancePackEvaluationFilters(TypedDict, closed=True):
    config_rule_names: NotRequired[
        "capo_config_service.types.conformance_pack_config_rule_names.ConformancePackConfigRuleNames"
    ]
    """<p>Filters the results by Config rule names.</p>"""
    compliance_type: NotRequired[
        "capo_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType"
    ]
    """<p>Filters the results by compliance.</p> <p>The allowed values are <code>COMPLIANT</code> and <code>NON_COMPLIANT</code>. <code>INSUFFICIENT_DATA</code> is not supported.</p>"""
    resource_type: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Filters the results by the resource type (for example, <code>"AWS::EC2::Instance"</code>). </p>"""
    resource_ids: NotRequired[
        "capo_config_service.types.conformance_pack_compliance_resource_ids.ConformancePackComplianceResourceIds"
    ]
    """<p>Filters the results by resource IDs.</p> <note> <p>This is valid only when you provide resource type. If there is no resource type, you will see an error.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackEvaluationFilters) -> dict:
    out: dict = {}
    if "config_rule_names" in value:
        import capo_config_service.types.conformance_pack_config_rule_names

        out["ConfigRuleNames"] = (
            capo_config_service.types.conformance_pack_config_rule_names.serialize_aws_json_1_1(
                value["config_rule_names"]
            )
        )
    if "compliance_type" in value:
        import capo_config_service.types.conformance_pack_compliance_type

        out["ComplianceType"] = (
            capo_config_service.types.conformance_pack_compliance_type.serialize_aws_json_1_1(
                value["compliance_type"]
            )
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_ids" in value:
        import capo_config_service.types.conformance_pack_compliance_resource_ids

        out["ResourceIds"] = (
            capo_config_service.types.conformance_pack_compliance_resource_ids.serialize_aws_json_1_1(
                value["resource_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackEvaluationFilters:
    out: ConformancePackEvaluationFilters = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleNames") is not None:
        import capo_config_service.types.conformance_pack_config_rule_names

        out["config_rule_names"] = (
            capo_config_service.types.conformance_pack_config_rule_names.deserialize_aws_json_1_1(
                data["ConfigRuleNames"]
            )
        )
    if data.get("ComplianceType") is not None:
        import capo_config_service.types.conformance_pack_compliance_type

        out["compliance_type"] = (
            capo_config_service.types.conformance_pack_compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("ResourceIds") is not None:
        import capo_config_service.types.conformance_pack_compliance_resource_ids

        out["resource_ids"] = (
            capo_config_service.types.conformance_pack_compliance_resource_ids.deserialize_aws_json_1_1(
                data["ResourceIds"]
            )
        )
    return out
