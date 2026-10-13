"""Generated from Smithy shape ``com.amazonaws.mgn#ImportTask``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.arn
    import capo_mgn.types.import_id
    import capo_mgn.types.import_status
    import capo_mgn.types.import_task_summary
    import capo_mgn.types.iso8601_datetime_string
    import capo_mgn.types.s3_bucket_source
    import capo_mgn.types.tags_map


class ImportTask(TypedDict, closed=True):
    import_id: NotRequired["capo_mgn.types.import_id.ImportID"]
    """<p>Import task id.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>ImportTask arn.</p>"""
    s3_bucket_source: NotRequired["capo_mgn.types.s3_bucket_source.S3BucketSource"]
    """<p>Import task s3 bucket source.</p>"""
    creation_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Import task creation datetime.</p>"""
    end_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Import task end datetime.</p>"""
    status: NotRequired["capo_mgn.types.import_status.ImportStatus"]
    """<p>Import task status.</p>"""
    progress_percentage: NotRequired["float"]
    """<p>Import task progress percentage.</p>"""
    summary: NotRequired["capo_mgn.types.import_task_summary.ImportTaskSummary"]
    """<p>Import task summary.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Import task tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportTask) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["importID"] = value["import_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "s3_bucket_source" in value:
        import capo_mgn.types.s3_bucket_source

        out["s3BucketSource"] = capo_mgn.types.s3_bucket_source.serialize_json(
            value["s3_bucket_source"]
        )
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
        import capo_mgn.types.import_task_summary

        out["summary"] = capo_mgn.types.import_task_summary.serialize_json(
            value["summary"]
        )
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ImportTask:
    out: ImportTask = {}  # type: ignore[typeddict-item]
    if data.get("importID") is not None:
        out["import_id"] = data["importID"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("s3BucketSource") is not None:
        import capo_mgn.types.s3_bucket_source

        out["s3_bucket_source"] = capo_mgn.types.s3_bucket_source.deserialize_json(
            data["s3BucketSource"]
        )
    if data.get("creationDateTime") is not None:
        out["creation_date_time"] = data["creationDateTime"]
    if data.get("endDateTime") is not None:
        out["end_date_time"] = data["endDateTime"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("progressPercentage") is not None:
        out["progress_percentage"] = float(data["progressPercentage"])
    if data.get("summary") is not None:
        import capo_mgn.types.import_task_summary

        out["summary"] = capo_mgn.types.import_task_summary.deserialize_json(
            data["summary"]
        )
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: ImportTask) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
