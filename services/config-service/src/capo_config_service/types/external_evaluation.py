"""Generated from Smithy shape ``com.amazonaws.configservice#ExternalEvaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.base_resource_id
    import capo_config_service.types.compliance_type
    import capo_config_service.types.ordering_timestamp
    import capo_config_service.types.string_with_char_limit256


class ExternalEvaluation(TypedDict, closed=True):
    compliance_resource_type: (
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>The evaluated compliance resource type. Config accepts <code>AWS::::Account</code> resource type.</p>"""
    compliance_resource_id: "capo_config_service.types.base_resource_id.BaseResourceId"
    """<p>The evaluated compliance resource ID. Config accepts only Amazon Web Services account ID.</p>"""
    compliance_type: "capo_config_service.types.compliance_type.ComplianceType"
    """<p>The compliance of the Amazon Web Services resource. The valid values are <code>COMPLIANT, NON_COMPLIANT, </code> and <code>NOT_APPLICABLE</code>.</p>"""
    annotation: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Supplementary information about the reason of compliance. For example, this task was completed on a specific date.</p>"""
    ordering_timestamp: "capo_config_service.types.ordering_timestamp.OrderingTimestamp"
    """<p>The time when the compliance was recorded. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalEvaluation) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ExternalEvaluation:
    out: ExternalEvaluation = {}  # type: ignore[typeddict-item]
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
