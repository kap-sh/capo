"""Generated from Smithy shape ``com.amazonaws.codebuild#CreateReportGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.report_export_config
    import capo_codebuild.types.report_group_name
    import capo_codebuild.types.report_type
    import capo_codebuild.types.tag_list


class CreateReportGroupInput(TypedDict, closed=True):
    name: "capo_codebuild.types.report_group_name.ReportGroupName"
    """<p> The name of the report group. </p>"""
    type: "capo_codebuild.types.report_type.ReportType"
    """<p> The type of report group. </p>"""
    export_config: "capo_codebuild.types.report_export_config.ReportExportConfig"
    """<p> A <code>ReportExportConfig</code> object that contains information about where the report group test results are exported. </p>"""
    tags: NotRequired["capo_codebuild.types.tag_list.TagList"]
    """<p> A list of tag key and value pairs associated with this report group. </p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild report group tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReportGroupInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_codebuild.types.report_type

    out["type"] = capo_codebuild.types.report_type.serialize_aws_json_1_1(value["type"])
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


def deserialize_aws_json_1_1(data: dict) -> CreateReportGroupInput:
    out: CreateReportGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_codebuild.types.report_type

        out["type"] = capo_codebuild.types.report_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_codebuild.types.report_type.ReportType", "")
    if data.get("exportConfig") is not None:
        import capo_codebuild.types.report_export_config

        out["export_config"] = (
            capo_codebuild.types.report_export_config.deserialize_aws_json_1_1(
                data["exportConfig"]
            )
        )
    else:
        raise DeserializationError("CreateReportGroupInput.export_config required")
    if data.get("tags") is not None:
        import capo_codebuild.types.tag_list

        out["tags"] = capo_codebuild.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
