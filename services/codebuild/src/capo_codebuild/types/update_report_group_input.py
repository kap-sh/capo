"""Generated from Smithy shape ``com.amazonaws.codebuild#UpdateReportGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.report_export_config
    import capo_codebuild.types.tag_list


class UpdateReportGroupInput(TypedDict, closed=True):
    arn: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p> The ARN of the report group to update. </p>"""
    export_config: NotRequired[
        "capo_codebuild.types.report_export_config.ReportExportConfig"
    ]
    """<p> Used to specify an updated export type. Valid values are: </p> <ul> <li> <p> <code>S3</code>: The report results are exported to an S3 bucket. </p> </li> <li> <p> <code>NO_EXPORT</code>: The report results are not exported. </p> </li> </ul>"""
    tags: NotRequired["capo_codebuild.types.tag_list.TagList"]
    """<p> An updated list of tag key and value pairs associated with this report group. </p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild report group tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateReportGroupInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "export_config" in value:
        import capo_codebuild.types.report_export_config

        out["exportConfig"] = (
            capo_codebuild.types.report_export_config.serialize_aws_json_1_1(
                value["export_config"]
            )
        )
    if "tags" in value:
        import capo_codebuild.types.tag_list

        out["tags"] = capo_codebuild.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateReportGroupInput:
    out: UpdateReportGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("exportConfig") is not None:
        import capo_codebuild.types.report_export_config

        out["export_config"] = (
            capo_codebuild.types.report_export_config.deserialize_aws_json_1_1(
                data["exportConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_codebuild.types.tag_list

        out["tags"] = capo_codebuild.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
