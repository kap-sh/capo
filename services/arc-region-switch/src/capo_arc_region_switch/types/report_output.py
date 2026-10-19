"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ReportOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_arc_region_switch.errors import DeserializationError, SerializationError
from capo_arc_region_switch.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_arc_region_switch.types.failed_report_output
    import capo_arc_region_switch.types.s3_report_output


class _ReportOutput_s3ReportOutput(TypedDict, closed=True):
    s3ReportOutput: "capo_arc_region_switch.types.s3_report_output.S3ReportOutput"


class _ReportOutput_failedReportOutput(TypedDict, closed=True):
    failedReportOutput: (
        "capo_arc_region_switch.types.failed_report_output.FailedReportOutput"
    )


ReportOutput: TypeAlias = (
    _ReportOutput_s3ReportOutput | _ReportOutput_failedReportOutput | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReportOutput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ReportOutput: cannot serialize unknown variant {value.name!r}"
        )
    elif "s3ReportOutput" in value:
        import capo_arc_region_switch.types.s3_report_output

        return {
            "s3ReportOutput": capo_arc_region_switch.types.s3_report_output.serialize_aws_json_1_0(
                value["s3ReportOutput"]
            )
        }
    elif "failedReportOutput" in value:
        import capo_arc_region_switch.types.failed_report_output

        return {
            "failedReportOutput": capo_arc_region_switch.types.failed_report_output.serialize_aws_json_1_0(
                value["failedReportOutput"]
            )
        }
    else:
        raise SerializationError("ReportOutput: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ReportOutput:
    if data.get("s3ReportOutput") is not None:
        import capo_arc_region_switch.types.s3_report_output

        return {
            "s3ReportOutput": capo_arc_region_switch.types.s3_report_output.deserialize_aws_json_1_0(
                data["s3ReportOutput"]
            )
        }
    elif data.get("failedReportOutput") is not None:
        import capo_arc_region_switch.types.failed_report_output

        return {
            "failedReportOutput": capo_arc_region_switch.types.failed_report_output.deserialize_aws_json_1_0(
                data["failedReportOutput"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ReportOutput: no recognized variant key")
