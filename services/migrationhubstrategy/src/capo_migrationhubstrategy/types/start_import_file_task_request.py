"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#StartImportFileTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.data_source_type
    import capo_migrationhubstrategy.types.group_ids
    import capo_migrationhubstrategy.types.import_s3_bucket
    import capo_migrationhubstrategy.types.string


class StartImportFileTaskRequest(TypedDict, closed=True):
    name: "capo_migrationhubstrategy.types.string.String"
    """<p> A descriptive name for the request. </p>"""
    s3_bucket: "capo_migrationhubstrategy.types.import_s3_bucket.importS3Bucket"
    """<p> The S3 bucket where the import file is located. The bucket name is required to begin with <code>migrationhub-strategy-</code>.</p>"""
    s3key: "capo_migrationhubstrategy.types.string.String"
    """<p> The Amazon S3 key name of the import file. </p>"""
    data_source_type: NotRequired[
        "capo_migrationhubstrategy.types.data_source_type.DataSourceType"
    ]
    """<p>Specifies the source that the servers are coming from. By default, Strategy Recommendations assumes that the servers specified in the import file are available in AWS Application Discovery Service. </p>"""
    group_id: NotRequired["capo_migrationhubstrategy.types.group_ids.GroupIds"]
    """<p>Groups the resources in the import file together with a unique name. This ID can be as filter in <code>ListApplicationComponents</code> and <code>ListServers</code>. </p>"""
    s3bucket_for_report_data: NotRequired[
        "capo_migrationhubstrategy.types.string.String"
    ]
    """<p> The S3 bucket where Strategy Recommendations uploads import results. The bucket name is required to begin with migrationhub-strategy-. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportFileTaskRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["S3Bucket"] = value["s3_bucket"]
    out["s3key"] = value["s3key"]
    if "data_source_type" in value:
        out["dataSourceType"] = value["data_source_type"]
    if "group_id" in value:
        import capo_migrationhubstrategy.types.group_ids

        out["groupId"] = capo_migrationhubstrategy.types.group_ids.serialize_json(
            value["group_id"]
        )
    if "s3bucket_for_report_data" in value:
        out["s3bucketForReportData"] = value["s3bucket_for_report_data"]
    return out


def deserialize_json(data: dict) -> StartImportFileTaskRequest:
    out: StartImportFileTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("s3key") is not None:
        out["s3key"] = data["s3key"]
    else:
        out["s3key"] = ""
    if data.get("dataSourceType") is not None:
        out["data_source_type"] = data["dataSourceType"]
    if data.get("groupId") is not None:
        import capo_migrationhubstrategy.types.group_ids

        out["group_id"] = capo_migrationhubstrategy.types.group_ids.deserialize_json(
            data["groupId"]
        )
    if data.get("s3bucketForReportData") is not None:
        out["s3bucket_for_report_data"] = data["s3bucketForReportData"]
    return out
