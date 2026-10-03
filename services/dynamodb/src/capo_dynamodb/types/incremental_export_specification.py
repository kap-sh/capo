"""Generated from Smithy shape ``com.amazonaws.dynamodb#IncrementalExportSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.export_from_time
    import capo_dynamodb.types.export_to_time
    import capo_dynamodb.types.export_view_type


class IncrementalExportSpecification(TypedDict, closed=True):
    export_from_time: NotRequired["capo_dynamodb.types.export_from_time.ExportFromTime"]
    """<p>Time in the past which provides the inclusive start range for the export table's data, counted in seconds from the start of the Unix epoch. The incremental export will reflect the table's state including and after this point in time.</p>"""
    export_to_time: NotRequired["capo_dynamodb.types.export_to_time.ExportToTime"]
    """<p>Time in the past which provides the exclusive end range for the export table's data, counted in seconds from the start of the Unix epoch. The incremental export will reflect the table's state just prior to this point in time. If this is not provided, the latest time with data available will be used.</p>"""
    export_view_type: NotRequired["capo_dynamodb.types.export_view_type.ExportViewType"]
    """<p>The view type that was chosen for the export. Valid values are <code>NEW_AND_OLD_IMAGES</code> and <code>NEW_IMAGES</code>. The default value is <code>NEW_AND_OLD_IMAGES</code>.</p> <p> <code>NEW_AND_OLD_IMAGES</code> exports both the new and old images of each changed item, while <code>NEW_IMAGES</code> exports only the new (latest) image. The view type you choose determines the structure of each item in the output for <code>insert</code>, <code>update</code>, and <code>delete</code> operations. For details and examples of how each view type shapes the export output, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataExport.Output.html">DynamoDB table export output format</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IncrementalExportSpecification) -> dict:
    out: dict = {}
    if "export_from_time" in value:
        import capo_dynamodb.types.export_from_time

        out["ExportFromTime"] = (
            capo_dynamodb.types.export_from_time.serialize_aws_json_1_0(
                value["export_from_time"]
            )
        )
    if "export_to_time" in value:
        import capo_dynamodb.types.export_to_time

        out["ExportToTime"] = capo_dynamodb.types.export_to_time.serialize_aws_json_1_0(
            value["export_to_time"]
        )
    if "export_view_type" in value:
        import capo_dynamodb.types.export_view_type

        out["ExportViewType"] = (
            capo_dynamodb.types.export_view_type.serialize_aws_json_1_0(
                value["export_view_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IncrementalExportSpecification:
    out: IncrementalExportSpecification = {}  # type: ignore[typeddict-item]
    if data.get("ExportFromTime") is not None:
        import capo_dynamodb.types.export_from_time

        out["export_from_time"] = (
            capo_dynamodb.types.export_from_time.deserialize_aws_json_1_0(
                data["ExportFromTime"]
            )
        )
    if data.get("ExportToTime") is not None:
        import capo_dynamodb.types.export_to_time

        out["export_to_time"] = (
            capo_dynamodb.types.export_to_time.deserialize_aws_json_1_0(
                data["ExportToTime"]
            )
        )
    if data.get("ExportViewType") is not None:
        import capo_dynamodb.types.export_view_type

        out["export_view_type"] = (
            capo_dynamodb.types.export_view_type.deserialize_aws_json_1_0(
                data["ExportViewType"]
            )
        )
    return out
