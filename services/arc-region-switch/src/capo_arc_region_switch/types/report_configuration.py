"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ReportConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.report_output_list


class ReportConfiguration(TypedDict, closed=True):
    report_output: NotRequired[
        "capo_arc_region_switch.types.report_output_list.ReportOutputList"
    ]
    """<p>The output configuration for the report.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReportConfiguration) -> dict:
    out: dict = {}
    if "report_output" in value:
        import capo_arc_region_switch.types.report_output_list

        out["reportOutput"] = (
            capo_arc_region_switch.types.report_output_list.serialize_aws_json_1_0(
                value["report_output"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReportConfiguration:
    out: ReportConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("reportOutput") is not None:
        import capo_arc_region_switch.types.report_output_list

        out["report_output"] = (
            capo_arc_region_switch.types.report_output_list.deserialize_aws_json_1_0(
                data["reportOutput"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportConfiguration) -> dict:
    out: dict = {}
    if "report_output" in value:
        import capo_arc_region_switch.types.report_output_list

        out["reportOutput"] = (
            capo_arc_region_switch.types.report_output_list.serialize_cbor(
                value["report_output"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ReportConfiguration:
    out: ReportConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("reportOutput") is not None:
        import capo_arc_region_switch.types.report_output_list

        out["report_output"] = (
            capo_arc_region_switch.types.report_output_list.deserialize_cbor(
                data["reportOutput"]
            )
        )
    return out
