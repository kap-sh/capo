"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobResultFileGroup``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.snapshot_file_list
    import capo_quicksight.types.snapshot_job_s3_result_list


class SnapshotJobResultFileGroup(TypedDict, closed=True):
    files: NotRequired["capo_quicksight.types.snapshot_file_list.SnapshotFileList"]
    """<p> A list of <code>SnapshotFile</code> objects.</p>"""
    s3_results: NotRequired[
        "capo_quicksight.types.snapshot_job_s3_result_list.SnapshotJobS3ResultList"
    ]
    """<p> A list of <code>SnapshotJobS3Result</code> objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobResultFileGroup) -> dict:
    out: dict = {}
    if "files" in value:
        import capo_quicksight.types.snapshot_file_list

        out["Files"] = capo_quicksight.types.snapshot_file_list.serialize_json(
            value["files"]
        )
    if "s3_results" in value:
        import capo_quicksight.types.snapshot_job_s3_result_list

        out["S3Results"] = (
            capo_quicksight.types.snapshot_job_s3_result_list.serialize_json(
                value["s3_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotJobResultFileGroup:
    out: SnapshotJobResultFileGroup = {}  # type: ignore[typeddict-item]
    if data.get("Files") is not None:
        import capo_quicksight.types.snapshot_file_list

        out["files"] = capo_quicksight.types.snapshot_file_list.deserialize_json(
            data["Files"]
        )
    if data.get("S3Results") is not None:
        import capo_quicksight.types.snapshot_job_s3_result_list

        out["s3_results"] = (
            capo_quicksight.types.snapshot_job_s3_result_list.deserialize_json(
                data["S3Results"]
            )
        )
    return out


def redact_sensitive(value: SnapshotJobResultFileGroup) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "s3_results" in value:
        import capo_quicksight.types.snapshot_job_s3_result_list

        out["s3_results"] = (
            capo_quicksight.types.snapshot_job_s3_result_list.redact_sensitive(
                value["s3_results"]
            )
        )
    return out
