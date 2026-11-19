"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GeneratedReportDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.generated_report

GeneratedReportDetails: TypeAlias = list[
    "capo_arc_region_switch.types.generated_report.GeneratedReport"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GeneratedReportDetails) -> list:
    import capo_arc_region_switch.types.generated_report

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.generated_report.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> GeneratedReportDetails:
    import capo_arc_region_switch.types.generated_report

    out: GeneratedReportDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.generated_report.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GeneratedReportDetails) -> list:
    import capo_arc_region_switch.types.generated_report

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.generated_report.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> GeneratedReportDetails:
    import capo_arc_region_switch.types.generated_report

    out: GeneratedReportDetails = []
    for item in data:
        if item is None:
            continue
        out.append(capo_arc_region_switch.types.generated_report.deserialize_cbor(item))
    return out
