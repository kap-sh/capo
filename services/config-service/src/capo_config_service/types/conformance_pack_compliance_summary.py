"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackComplianceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_compliance_type
    import capo_config_service.types.conformance_pack_name


class ConformancePackComplianceSummary(TypedDict, closed=True):
    conformance_pack_name: (
        "capo_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>The name of the conformance pack name.</p>"""
    conformance_pack_compliance_status: "capo_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType"
    """<p>The status of the conformance pack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackComplianceSummary) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    import capo_config_service.types.conformance_pack_compliance_type

    out["ConformancePackComplianceStatus"] = (
        capo_config_service.types.conformance_pack_compliance_type.serialize_aws_json_1_1(
            value["conformance_pack_compliance_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackComplianceSummary:
    out: ConformancePackComplianceSummary = {}  # type: ignore[typeddict-item]
    if data.get("ConformancePackName") is not None:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        out["conformance_pack_name"] = ""
    if data.get("ConformancePackComplianceStatus") is not None:
        import capo_config_service.types.conformance_pack_compliance_type

        out["conformance_pack_compliance_status"] = (
            capo_config_service.types.conformance_pack_compliance_type.deserialize_aws_json_1_1(
                data["ConformancePackComplianceStatus"]
            )
        )
    else:
        import typing

        out["conformance_pack_compliance_status"] = typing.cast(
            "capo_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType",
            "",
        )
    return out
