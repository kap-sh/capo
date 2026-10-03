"""Generated from Smithy shape ``com.amazonaws.datasync#ReportOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.report_level


class ReportOverride(TypedDict, closed=True):
    report_level: NotRequired["capo_datasync.types.report_level.ReportLevel"]
    """<p>Specifies whether your task report includes errors only or successes and errors.</p> <p>For example, your report might mostly include only what didn't go well in your transfer (<code>ERRORS_ONLY</code>). At the same time, you want to verify that your <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">task filter</a> is working correctly. In this situation, you can get a list of what files DataSync successfully skipped and if something transferred that you didn't to transfer (<code>SUCCESSES_AND_ERRORS</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportOverride) -> dict:
    out: dict = {}
    if "report_level" in value:
        import capo_datasync.types.report_level

        out["ReportLevel"] = capo_datasync.types.report_level.serialize_aws_json_1_1(
            value["report_level"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportOverride:
    out: ReportOverride = {}  # type: ignore[typeddict-item]
    if data.get("ReportLevel") is not None:
        import capo_datasync.types.report_level

        out["report_level"] = capo_datasync.types.report_level.deserialize_aws_json_1_1(
            data["ReportLevel"]
        )
    return out
