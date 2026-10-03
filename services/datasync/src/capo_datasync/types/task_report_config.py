"""Generated from Smithy shape ``com.amazonaws.datasync#TaskReportConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.object_version_ids
    import capo_datasync.types.report_destination
    import capo_datasync.types.report_level
    import capo_datasync.types.report_output_type
    import capo_datasync.types.report_overrides


class TaskReportConfig(TypedDict, closed=True):
    destination: NotRequired["capo_datasync.types.report_destination.ReportDestination"]
    """<p>Specifies the Amazon S3 bucket where DataSync uploads your task report. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html#task-report-access">Task reports</a>.</p>"""
    output_type: NotRequired["capo_datasync.types.report_output_type.ReportOutputType"]
    """<p>Specifies the type of task report that you want:</p> <ul> <li> <p> <code>SUMMARY_ONLY</code>: Provides necessary details about your task, including the number of files, objects, and directories transferred and transfer duration.</p> </li> <li> <p> <code>STANDARD</code>: Provides complete details about your task, including a full list of files, objects, and directories that were transferred, skipped, verified, and more.</p> </li> </ul>"""
    report_level: NotRequired["capo_datasync.types.report_level.ReportLevel"]
    """<p>Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't.</p> <ul> <li> <p> <code>ERRORS_ONLY</code>: A report shows what DataSync was unable to transfer, skip, verify, and delete.</p> </li> <li> <p> <code>SUCCESSES_AND_ERRORS</code>: A report shows what DataSync was able and unable to transfer, skip, verify, and delete.</p> </li> </ul>"""
    object_version_ids: NotRequired[
        "capo_datasync.types.object_version_ids.ObjectVersionIds"
    ]
    """<p>Specifies whether your task report includes the new version of each object transferred into an S3 bucket. This only applies if you <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html">enable versioning on your bucket</a>. Keep in mind that setting this to <code>INCLUDE</code> can increase the duration of your task execution.</p>"""
    overrides: NotRequired["capo_datasync.types.report_overrides.ReportOverrides"]
    """<p>Customizes the reporting level for aspects of your task report. For example, your report might generally only include errors, but you could specify that you want a list of successes and errors just for the files that DataSync attempted to delete in your destination location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskReportConfig) -> dict:
    out: dict = {}
    if "destination" in value:
        import capo_datasync.types.report_destination

        out["Destination"] = (
            capo_datasync.types.report_destination.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    if "output_type" in value:
        import capo_datasync.types.report_output_type

        out["OutputType"] = (
            capo_datasync.types.report_output_type.serialize_aws_json_1_1(
                value["output_type"]
            )
        )
    if "report_level" in value:
        import capo_datasync.types.report_level

        out["ReportLevel"] = capo_datasync.types.report_level.serialize_aws_json_1_1(
            value["report_level"]
        )
    if "object_version_ids" in value:
        import capo_datasync.types.object_version_ids

        out["ObjectVersionIds"] = (
            capo_datasync.types.object_version_ids.serialize_aws_json_1_1(
                value["object_version_ids"]
            )
        )
    if "overrides" in value:
        import capo_datasync.types.report_overrides

        out["Overrides"] = capo_datasync.types.report_overrides.serialize_aws_json_1_1(
            value["overrides"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskReportConfig:
    out: TaskReportConfig = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        import capo_datasync.types.report_destination

        out["destination"] = (
            capo_datasync.types.report_destination.deserialize_aws_json_1_1(
                data["Destination"]
            )
        )
    if data.get("OutputType") is not None:
        import capo_datasync.types.report_output_type

        out["output_type"] = (
            capo_datasync.types.report_output_type.deserialize_aws_json_1_1(
                data["OutputType"]
            )
        )
    if data.get("ReportLevel") is not None:
        import capo_datasync.types.report_level

        out["report_level"] = capo_datasync.types.report_level.deserialize_aws_json_1_1(
            data["ReportLevel"]
        )
    if data.get("ObjectVersionIds") is not None:
        import capo_datasync.types.object_version_ids

        out["object_version_ids"] = (
            capo_datasync.types.object_version_ids.deserialize_aws_json_1_1(
                data["ObjectVersionIds"]
            )
        )
    if data.get("Overrides") is not None:
        import capo_datasync.types.report_overrides

        out["overrides"] = (
            capo_datasync.types.report_overrides.deserialize_aws_json_1_1(
                data["Overrides"]
            )
        )
    return out
