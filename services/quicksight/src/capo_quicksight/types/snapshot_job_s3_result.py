"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobS3Result``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_s3_uri
    import capo_quicksight.types.snapshot_job_result_error_info_list
    import capo_quicksight.types.snapshot_s3_destination_configuration


class SnapshotJobS3Result(TypedDict, closed=True):
    s3_destination_configuration: NotRequired[
        "capo_quicksight.types.snapshot_s3_destination_configuration.SnapshotS3DestinationConfiguration"
    ]
    """<p>A list of Amazon S3 bucket configurations that are provided when you make a <code>StartDashboardSnapshotJob</code> API call. </p>"""
    s3_uri: NotRequired["capo_quicksight.types.sensitive_s3_uri.SensitiveS3Uri"]
    """<p>The Amazon S3 Uri.</p>"""
    error_info: NotRequired[
        "capo_quicksight.types.snapshot_job_result_error_info_list.SnapshotJobResultErrorInfoList"
    ]
    """<p>An array of error records that describe any failures that occur while the dashboard snapshot job runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobS3Result) -> dict:
    out: dict = {}
    if "s3_destination_configuration" in value:
        import capo_quicksight.types.snapshot_s3_destination_configuration

        out["S3DestinationConfiguration"] = (
            capo_quicksight.types.snapshot_s3_destination_configuration.serialize_json(
                value["s3_destination_configuration"]
            )
        )
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "error_info" in value:
        import capo_quicksight.types.snapshot_job_result_error_info_list

        out["ErrorInfo"] = (
            capo_quicksight.types.snapshot_job_result_error_info_list.serialize_json(
                value["error_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotJobS3Result:
    out: SnapshotJobS3Result = {}  # type: ignore[typeddict-item]
    if data.get("S3DestinationConfiguration") is not None:
        import capo_quicksight.types.snapshot_s3_destination_configuration

        out["s3_destination_configuration"] = (
            capo_quicksight.types.snapshot_s3_destination_configuration.deserialize_json(
                data["S3DestinationConfiguration"]
            )
        )
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    if data.get("ErrorInfo") is not None:
        import capo_quicksight.types.snapshot_job_result_error_info_list

        out["error_info"] = (
            capo_quicksight.types.snapshot_job_result_error_info_list.deserialize_json(
                data["ErrorInfo"]
            )
        )
    return out


def redact_sensitive(value: SnapshotJobS3Result) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "s3_uri" in value:
        out["s3_uri"] = "*** Sensitive Data Redacted ***"
    return out
