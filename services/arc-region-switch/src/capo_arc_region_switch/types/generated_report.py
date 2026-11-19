"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GeneratedReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_arc_region_switch.types.report_output


class GeneratedReport(TypedDict, closed=True):
    report_generation_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when the report was generated.</p>"""
    report_output: NotRequired[
        "capo_arc_region_switch.types.report_output.ReportOutput"
    ]
    """<p>The output location or cause of a failure in report generation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GeneratedReport) -> dict:
    out: dict = {}
    if "report_generation_time" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["reportGenerationTime"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["report_generation_time"]
            )
        )
    if "report_output" in value:
        import capo_arc_region_switch.types.report_output

        out["reportOutput"] = (
            capo_arc_region_switch.types.report_output.serialize_aws_json_1_0(
                value["report_output"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GeneratedReport:
    out: GeneratedReport = {}  # type: ignore[typeddict-item]
    if data.get("reportGenerationTime") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["report_generation_time"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["reportGenerationTime"]
            )
        )
    if data.get("reportOutput") is not None:
        import capo_arc_region_switch.types.report_output

        out["report_output"] = (
            capo_arc_region_switch.types.report_output.deserialize_aws_json_1_0(
                data["reportOutput"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GeneratedReport) -> dict:
    out: dict = {}
    if "report_generation_time" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["reportGenerationTime"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_cbor(
                value["report_generation_time"]
            )
        )
    if "report_output" in value:
        import capo_arc_region_switch.types.report_output

        out["reportOutput"] = capo_arc_region_switch.types.report_output.serialize_cbor(
            value["report_output"]
        )
    return out


def deserialize_cbor(data: dict) -> GeneratedReport:
    out: GeneratedReport = {}  # type: ignore[typeddict-item]
    if data.get("reportGenerationTime") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["report_generation_time"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_cbor(
                data["reportGenerationTime"]
            )
        )
    if data.get("reportOutput") is not None:
        import capo_arc_region_switch.types.report_output

        out["report_output"] = (
            capo_arc_region_switch.types.report_output.deserialize_cbor(
                data["reportOutput"]
            )
        )
    return out
