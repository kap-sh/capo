"""Generated from Smithy shape ``com.amazonaws.mgn#ExportTask``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.arn
    import capo_mgn.types.export_id
    import capo_mgn.types.export_status
    import capo_mgn.types.export_task_summary
    import capo_mgn.types.iso8601_datetime_string
    import capo_mgn.types.s3_bucket_name
    import capo_mgn.types.s3_key
    import capo_mgn.types.tags_map


class ExportTask(TypedDict, closed=True):
    export_id: NotRequired["capo_mgn.types.export_id.ExportID"]
    """<p>Export task id.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>ExportTask arn.</p>"""
    s3_bucket: NotRequired["capo_mgn.types.s3_bucket_name.S3BucketName"]
    """<p>Export task s3 bucket.</p>"""
    s3_key: NotRequired["capo_mgn.types.s3_key.S3Key"]
    """<p>Export task s3 key.</p>"""
    s3_bucket_owner: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Export task s3 bucket owner.</p>"""
    creation_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Export task creation datetime.</p>"""
    end_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Export task end datetime.</p>"""
    status: NotRequired["capo_mgn.types.export_status.ExportStatus"]
    """<p>Export task status.</p>"""
    progress_percentage: NotRequired["float"]
    """<p>Export task progress percentage.</p>"""
    summary: NotRequired["capo_mgn.types.export_task_summary.ExportTaskSummary"]
    """<p>Export task summary.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Export task tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportTask) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["exportID"] = value["export_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["s3Key"] = value["s3_key"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    if "creation_date_time" in value:
        out["creationDateTime"] = value["creation_date_time"]
    if "end_date_time" in value:
        out["endDateTime"] = value["end_date_time"]
    if "status" in value:
        out["status"] = value["status"]
    if "progress_percentage" in value:
        out["progressPercentage"] = (
            "NaN"
            if value["progress_percentage"] != value["progress_percentage"]
            else "Infinity"
            if value["progress_percentage"] == float("inf")
            else "-Infinity"
            if value["progress_percentage"] == float("-inf")
            else value["progress_percentage"]
        )
    if "summary" in value:
        import capo_mgn.types.export_task_summary

        out["summary"] = capo_mgn.types.export_task_summary.serialize_json(
            value["summary"]
        )
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ExportTask:
    out: ExportTask = {}  # type: ignore[typeddict-item]
    if data.get("exportID") is not None:
        out["export_id"] = data["exportID"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("s3Bucket") is not None:
        out["s3_bucket"] = data["s3Bucket"]
    if data.get("s3Key") is not None:
        out["s3_key"] = data["s3Key"]
    if data.get("s3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    if data.get("creationDateTime") is not None:
        out["creation_date_time"] = data["creationDateTime"]
    if data.get("endDateTime") is not None:
        out["end_date_time"] = data["endDateTime"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("progressPercentage") is not None:
        out["progress_percentage"] = float(data["progressPercentage"])
    if data.get("summary") is not None:
        import capo_mgn.types.export_task_summary

        out["summary"] = capo_mgn.types.export_task_summary.deserialize_json(
            data["summary"]
        )
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: ExportTask) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
