"""Generated from Smithy shape ``com.amazonaws.configservice#Evaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.base_resource_id
    import capo_config_service.types.compliance_type
    import capo_config_service.types.ordering_timestamp
    import capo_config_service.types.string_with_char_limit256


class Evaluation(TypedDict, closed=True):
    compliance_resource_type: (
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>The type of Amazon Web Services resource that was evaluated.</p>"""
    compliance_resource_id: "capo_config_service.types.base_resource_id.BaseResourceId"
    """<p>The ID of the Amazon Web Services resource that was evaluated.</p>"""
    compliance_type: "capo_config_service.types.compliance_type.ComplianceType"
    """<p>Indicates whether the Amazon Web Services resource complies with the Config rule that it was evaluated against.</p> <p>For the <code>Evaluation</code> data type, Config supports only the <code>COMPLIANT</code>, <code>NON_COMPLIANT</code>, and <code>NOT_APPLICABLE</code> values. Config does not support the <code>INSUFFICIENT_DATA</code> value for this data type.</p> <p>Similarly, Config does not accept <code>INSUFFICIENT_DATA</code> as the value for <code>ComplianceType</code> from a <code>PutEvaluations</code> request. For example, an Lambda function for a custom Config rule cannot pass an <code>INSUFFICIENT_DATA</code> value to Config.</p>"""
    annotation: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Supplementary information about how the evaluation determined the compliance.</p>"""
    ordering_timestamp: "capo_config_service.types.ordering_timestamp.OrderingTimestamp"
    """<p>The time of the event in Config that triggered the evaluation. For event-based evaluations, the time indicates when Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when Config triggered the evaluation at the frequency that you specified (for example, every 24 hours).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Evaluation) -> dict:
    out: dict = {}
    out["ComplianceResourceType"] = value["compliance_resource_type"]
    out["ComplianceResourceId"] = value["compliance_resource_id"]
    import capo_config_service.types.compliance_type

    out["ComplianceType"] = (
        capo_config_service.types.compliance_type.serialize_aws_json_1_1(
            value["compliance_type"]
        )
    )
    if "annotation" in value:
        out["Annotation"] = value["annotation"]
    import capo_config_service.types.ordering_timestamp

    out["OrderingTimestamp"] = (
        capo_config_service.types.ordering_timestamp.serialize_aws_json_1_1(
            value["ordering_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Evaluation:
    out: Evaluation = {}  # type: ignore[typeddict-item]
    if data.get("ComplianceResourceType") is not None:
        out["compliance_resource_type"] = data["ComplianceResourceType"]
    else:
        out["compliance_resource_type"] = ""
    if data.get("ComplianceResourceId") is not None:
        out["compliance_resource_id"] = data["ComplianceResourceId"]
    else:
        out["compliance_resource_id"] = ""
    if data.get("ComplianceType") is not None:
        import capo_config_service.types.compliance_type

        out["compliance_type"] = (
            capo_config_service.types.compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    else:
        import typing

        out["compliance_type"] = typing.cast(
            "capo_config_service.types.compliance_type.ComplianceType", ""
        )
    if data.get("Annotation") is not None:
        out["annotation"] = data["Annotation"]
    if data.get("OrderingTimestamp") is not None:
        import capo_config_service.types.ordering_timestamp

        out["ordering_timestamp"] = (
            capo_config_service.types.ordering_timestamp.deserialize_aws_json_1_1(
                data["OrderingTimestamp"]
            )
        )
    else:
        import datetime

        out["ordering_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
