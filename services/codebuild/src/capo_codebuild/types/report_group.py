"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.report_export_config
    import capo_codebuild.types.report_group_name
    import capo_codebuild.types.report_group_status_type
    import capo_codebuild.types.report_type
    import capo_codebuild.types.tag_list
    import capo_codebuild.types.timestamp


class ReportGroup(TypedDict, closed=True):
    arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the <code>ReportGroup</code>. </p>"""
    name: NotRequired["capo_codebuild.types.report_group_name.ReportGroupName"]
    """<p>The name of the <code>ReportGroup</code>. </p>"""
    type: NotRequired["capo_codebuild.types.report_type.ReportType"]
    """<p>The type of the <code>ReportGroup</code>. This can be one of the following values:</p> <dl> <dt>CODE_COVERAGE</dt> <dd> <p>The report group contains code coverage reports.</p> </dd> <dt>TEST</dt> <dd> <p>The report group contains test reports.</p> </dd> </dl>"""
    export_config: NotRequired[
        "capo_codebuild.types.report_export_config.ReportExportConfig"
    ]
    """<p>Information about the destination where the raw data of this <code>ReportGroup</code> is exported. </p>"""
    created: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>The date and time this <code>ReportGroup</code> was created. </p>"""
    last_modified: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>The date and time this <code>ReportGroup</code> was last modified. </p>"""
    tags: NotRequired["capo_codebuild.types.tag_list.TagList"]
    """<p>A list of tag key and value pairs associated with this report group. </p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild report group tags.</p>"""
    status: NotRequired[
        "capo_codebuild.types.report_group_status_type.ReportGroupStatusType"
    ]
    """<p>The status of the report group. This property is read-only.</p> <p>This can be one of the following values:</p> <dl> <dt>ACTIVE</dt> <dd> <p>The report group is active.</p> </dd> <dt>DELETING</dt> <dd> <p>The report group is in the process of being deleted.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGroup) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_codebuild.types.report_type

        out["type"] = capo_codebuild.types.report_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "export_config" in value:
        import capo_codebuild.types.report_export_config

        out["exportConfig"] = (
            capo_codebuild.types.report_export_config.serialize_aws_json_1_1(
                value["export_config"]
            )
        )
    if "created" in value:
        import capo_codebuild.types.timestamp

        out["created"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "last_modified" in value:
        import capo_codebuild.types.timestamp

        out["lastModified"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["last_modified"]
        )
    if "tags" in value:
        import capo_codebuild.types.tag_list

        out["tags"] = capo_codebuild.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "status" in value:
        import capo_codebuild.types.report_group_status_type

        out["status"] = (
            capo_codebuild.types.report_group_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportGroup:
    out: ReportGroup = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        import capo_codebuild.types.report_type

        out["type"] = capo_codebuild.types.report_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("exportConfig") is not None:
        import capo_codebuild.types.report_export_config

        out["export_config"] = (
            capo_codebuild.types.report_export_config.deserialize_aws_json_1_1(
                data["exportConfig"]
            )
        )
    if data.get("created") is not None:
        import capo_codebuild.types.timestamp

        out["created"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    if data.get("lastModified") is not None:
        import capo_codebuild.types.timestamp

        out["last_modified"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["lastModified"]
        )
    if data.get("tags") is not None:
        import capo_codebuild.types.tag_list

        out["tags"] = capo_codebuild.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("status") is not None:
        import capo_codebuild.types.report_group_status_type

        out["status"] = (
            capo_codebuild.types.report_group_status_type.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportGroup) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_codebuild.types.report_type

        out["type"] = capo_codebuild.types.report_type.serialize_cbor(value["type"])
    if "export_config" in value:
        import capo_codebuild.types.report_export_config

        out["exportConfig"] = capo_codebuild.types.report_export_config.serialize_cbor(
            value["export_config"]
        )
    if "created" in value:
        import capo_codebuild.types.timestamp

        out["created"] = capo_codebuild.types.timestamp.serialize_cbor(value["created"])
    if "last_modified" in value:
        import capo_codebuild.types.timestamp

        out["lastModified"] = capo_codebuild.types.timestamp.serialize_cbor(
            value["last_modified"]
        )
    if "tags" in value:
        import capo_codebuild.types.tag_list

        out["tags"] = capo_codebuild.types.tag_list.serialize_cbor(value["tags"])
    if "status" in value:
        import capo_codebuild.types.report_group_status_type

        out["status"] = capo_codebuild.types.report_group_status_type.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> ReportGroup:
    out: ReportGroup = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        import capo_codebuild.types.report_type

        out["type"] = capo_codebuild.types.report_type.deserialize_cbor(data["type"])
    if data.get("exportConfig") is not None:
        import capo_codebuild.types.report_export_config

        out["export_config"] = (
            capo_codebuild.types.report_export_config.deserialize_cbor(
                data["exportConfig"]
            )
        )
    if data.get("created") is not None:
        import capo_codebuild.types.timestamp

        out["created"] = capo_codebuild.types.timestamp.deserialize_cbor(
            data["created"]
        )
    if data.get("lastModified") is not None:
        import capo_codebuild.types.timestamp

        out["last_modified"] = capo_codebuild.types.timestamp.deserialize_cbor(
            data["lastModified"]
        )
    if data.get("tags") is not None:
        import capo_codebuild.types.tag_list

        out["tags"] = capo_codebuild.types.tag_list.deserialize_cbor(data["tags"])
    if data.get("status") is not None:
        import capo_codebuild.types.report_group_status_type

        out["status"] = capo_codebuild.types.report_group_status_type.deserialize_cbor(
            data["status"]
        )
    return out
