"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackEvaluationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.annotation
    import capo_config_service.types.conformance_pack_compliance_type
    import capo_config_service.types.date
    import capo_config_service.types.evaluation_result_identifier


class ConformancePackEvaluationResult(TypedDict, closed=True):
    compliance_type: "capo_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType"
    """<p>The compliance type. The allowed values are <code>COMPLIANT</code> and <code>NON_COMPLIANT</code>. <code>INSUFFICIENT_DATA</code> is not supported.</p>"""
    evaluation_result_identifier: "capo_config_service.types.evaluation_result_identifier.EvaluationResultIdentifier"
    config_rule_invoked_time: "capo_config_service.types.date.Date"
    """<p>The time when Config rule evaluated Amazon Web Services resource.</p>"""
    result_recorded_time: "capo_config_service.types.date.Date"
    """<p>The time when Config recorded the evaluation result. </p>"""
    annotation: NotRequired["capo_config_service.types.annotation.Annotation"]
    """<p>Supplementary information about how the evaluation determined the compliance. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackEvaluationResult) -> dict:
    out: dict = {}
    import capo_config_service.types.conformance_pack_compliance_type

    out["ComplianceType"] = (
        capo_config_service.types.conformance_pack_compliance_type.serialize_aws_json_1_1(
            value["compliance_type"]
        )
    )
    import capo_config_service.types.evaluation_result_identifier

    out["EvaluationResultIdentifier"] = (
        capo_config_service.types.evaluation_result_identifier.serialize_aws_json_1_1(
            value["evaluation_result_identifier"]
        )
    )
    import capo_config_service.types.date

    out["ConfigRuleInvokedTime"] = (
        capo_config_service.types.date.serialize_aws_json_1_1(
            value["config_rule_invoked_time"]
        )
    )
    import capo_config_service.types.date

    out["ResultRecordedTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
        value["result_recorded_time"]
    )
    if "annotation" in value:
        out["Annotation"] = value["annotation"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackEvaluationResult:
    out: ConformancePackEvaluationResult = {}  # type: ignore[typeddict-item]
    if data.get("ComplianceType") is not None:
        import capo_config_service.types.conformance_pack_compliance_type

        out["compliance_type"] = (
            capo_config_service.types.conformance_pack_compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    else:
        import typing

        out["compliance_type"] = typing.cast(
            "capo_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType",
            "",
        )
    if data.get("EvaluationResultIdentifier") is not None:
        import capo_config_service.types.evaluation_result_identifier

        out["evaluation_result_identifier"] = (
            capo_config_service.types.evaluation_result_identifier.deserialize_aws_json_1_1(
                data["EvaluationResultIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "ConformancePackEvaluationResult.evaluation_result_identifier required"
        )
    if data.get("ConfigRuleInvokedTime") is not None:
        import capo_config_service.types.date

        out["config_rule_invoked_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["ConfigRuleInvokedTime"]
            )
        )
    else:
        import datetime

        out["config_rule_invoked_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ResultRecordedTime") is not None:
        import capo_config_service.types.date

        out["result_recorded_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["ResultRecordedTime"]
            )
        )
    else:
        import datetime

        out["result_recorded_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Annotation") is not None:
        out["annotation"] = data["Annotation"]
    return out
