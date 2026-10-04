"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.billed_size_bytes
    import capo_dynamodb.types.client_token
    import capo_dynamodb.types.export_arn
    import capo_dynamodb.types.export_end_time
    import capo_dynamodb.types.export_format
    import capo_dynamodb.types.export_manifest
    import capo_dynamodb.types.export_start_time
    import capo_dynamodb.types.export_status
    import capo_dynamodb.types.export_time
    import capo_dynamodb.types.export_type
    import capo_dynamodb.types.failure_code
    import capo_dynamodb.types.failure_message
    import capo_dynamodb.types.filter_specification
    import capo_dynamodb.types.incremental_export_specification
    import capo_dynamodb.types.item_count
    import capo_dynamodb.types.s3_bucket
    import capo_dynamodb.types.s3_bucket_owner
    import capo_dynamodb.types.s3_prefix
    import capo_dynamodb.types.s3_sse_algorithm
    import capo_dynamodb.types.s3_sse_kms_key_id
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.table_id


class ExportDescription(TypedDict, closed=True):
    export_arn: NotRequired["capo_dynamodb.types.export_arn.ExportArn"]
    """<p>The Amazon Resource Name (ARN) of the table export.</p>"""
    export_status: NotRequired["capo_dynamodb.types.export_status.ExportStatus"]
    """<p>Export can be in one of the following states: IN_PROGRESS, COMPLETED, or FAILED.</p>"""
    start_time: NotRequired["capo_dynamodb.types.export_start_time.ExportStartTime"]
    """<p>The time at which the export task began.</p>"""
    end_time: NotRequired["capo_dynamodb.types.export_end_time.ExportEndTime"]
    """<p>The time at which the export task completed.</p>"""
    export_manifest: NotRequired["capo_dynamodb.types.export_manifest.ExportManifest"]
    """<p>The name of the manifest file for the export task.</p>"""
    table_arn: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p>The Amazon Resource Name (ARN) of the table that was exported.</p>"""
    table_id: NotRequired["capo_dynamodb.types.table_id.TableId"]
    """<p>Unique ID of the table that was exported.</p>"""
    export_time: NotRequired["capo_dynamodb.types.export_time.ExportTime"]
    """<p>Point in time from which table data was exported.</p>"""
    client_token: NotRequired["capo_dynamodb.types.client_token.ClientToken"]
    """<p>The client token that was provided for the export task. A client token makes calls to <code>ExportTableToPointInTimeInput</code> idempotent, meaning that multiple identical calls have the same effect as one single call.</p>"""
    s3_bucket: NotRequired["capo_dynamodb.types.s3_bucket.S3Bucket"]
    """<p>The name of the Amazon S3 bucket containing the export.</p>"""
    s3_bucket_owner: NotRequired["capo_dynamodb.types.s3_bucket_owner.S3BucketOwner"]
    """<p>The ID of the Amazon Web Services account that owns the bucket containing the export.</p>"""
    s3_prefix: NotRequired["capo_dynamodb.types.s3_prefix.S3Prefix"]
    """<p>The Amazon S3 bucket prefix used as the file name and path of the exported snapshot.</p>"""
    s3_sse_algorithm: NotRequired["capo_dynamodb.types.s3_sse_algorithm.S3SseAlgorithm"]
    """<p>Type of encryption used on the bucket where export data is stored. Valid values for <code>S3SseAlgorithm</code> are:</p> <ul> <li> <p> <code>AES256</code> - server-side encryption with Amazon S3 managed keys</p> </li> <li> <p> <code>KMS</code> - server-side encryption with KMS managed keys</p> </li> </ul>"""
    s3_sse_kms_key_id: NotRequired[
        "capo_dynamodb.types.s3_sse_kms_key_id.S3SseKmsKeyId"
    ]
    """<p>The ID of the KMS managed key used to encrypt the S3 bucket where export data is stored (if applicable).</p>"""
    failure_code: NotRequired["capo_dynamodb.types.failure_code.FailureCode"]
    """<p>Status code for the result of the failed export.</p>"""
    failure_message: NotRequired["capo_dynamodb.types.failure_message.FailureMessage"]
    """<p>Export failure reason description.</p>"""
    export_format: NotRequired["capo_dynamodb.types.export_format.ExportFormat"]
    """<p>The format of the exported data. Valid values for <code>ExportFormat</code> are <code>DYNAMODB_JSON</code> or <code>ION</code>.</p>"""
    billed_size_bytes: NotRequired[
        "capo_dynamodb.types.billed_size_bytes.BilledSizeBytes"
    ]
    """<p>The billable size of the table export.</p>"""
    item_count: NotRequired["capo_dynamodb.types.item_count.ItemCount"]
    """<p>The number of items exported.</p>"""
    export_type: NotRequired["capo_dynamodb.types.export_type.ExportType"]
    """<p>The type of export that was performed. Valid values are <code>FULL_EXPORT</code> or <code>INCREMENTAL_EXPORT</code>.</p>"""
    incremental_export_specification: NotRequired[
        "capo_dynamodb.types.incremental_export_specification.IncrementalExportSpecification"
    ]
    """<p>Optional object containing the parameters specific to an incremental export.</p>"""
    filter_specification: NotRequired[
        "capo_dynamodb.types.filter_specification.FilterSpecification"
    ]
    """<p>The filter criteria applied to the export. When present, only items that match the specified key conditions and filter expressions are included in the export output.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportDescription) -> dict:
    out: dict = {}
    if "export_arn" in value:
        out["ExportArn"] = value["export_arn"]
    if "export_status" in value:
        import capo_dynamodb.types.export_status

        out["ExportStatus"] = capo_dynamodb.types.export_status.serialize_aws_json_1_0(
            value["export_status"]
        )
    if "start_time" in value:
        import capo_dynamodb.types.export_start_time

        out["StartTime"] = capo_dynamodb.types.export_start_time.serialize_aws_json_1_0(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_dynamodb.types.export_end_time

        out["EndTime"] = capo_dynamodb.types.export_end_time.serialize_aws_json_1_0(
            value["end_time"]
        )
    if "export_manifest" in value:
        out["ExportManifest"] = value["export_manifest"]
    if "table_arn" in value:
        out["TableArn"] = value["table_arn"]
    if "table_id" in value:
        out["TableId"] = value["table_id"]
    if "export_time" in value:
        import capo_dynamodb.types.export_time

        out["ExportTime"] = capo_dynamodb.types.export_time.serialize_aws_json_1_0(
            value["export_time"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_bucket_owner" in value:
        out["S3BucketOwner"] = value["s3_bucket_owner"]
    if "s3_prefix" in value:
        out["S3Prefix"] = value["s3_prefix"]
    if "s3_sse_algorithm" in value:
        import capo_dynamodb.types.s3_sse_algorithm

        out["S3SseAlgorithm"] = (
            capo_dynamodb.types.s3_sse_algorithm.serialize_aws_json_1_0(
                value["s3_sse_algorithm"]
            )
        )
    if "s3_sse_kms_key_id" in value:
        out["S3SseKmsKeyId"] = value["s3_sse_kms_key_id"]
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "export_format" in value:
        import capo_dynamodb.types.export_format

        out["ExportFormat"] = capo_dynamodb.types.export_format.serialize_aws_json_1_0(
            value["export_format"]
        )
    if "billed_size_bytes" in value:
        out["BilledSizeBytes"] = value["billed_size_bytes"]
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "export_type" in value:
        import capo_dynamodb.types.export_type

        out["ExportType"] = capo_dynamodb.types.export_type.serialize_aws_json_1_0(
            value["export_type"]
        )
    if "incremental_export_specification" in value:
        import capo_dynamodb.types.incremental_export_specification

        out["IncrementalExportSpecification"] = (
            capo_dynamodb.types.incremental_export_specification.serialize_aws_json_1_0(
                value["incremental_export_specification"]
            )
        )
    if "filter_specification" in value:
        import capo_dynamodb.types.filter_specification

        out["FilterSpecification"] = (
            capo_dynamodb.types.filter_specification.serialize_aws_json_1_0(
                value["filter_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportDescription:
    out: ExportDescription = {}  # type: ignore[typeddict-item]
    if data.get("ExportArn") is not None:
        out["export_arn"] = data["ExportArn"]
    if data.get("ExportStatus") is not None:
        import capo_dynamodb.types.export_status

        out["export_status"] = (
            capo_dynamodb.types.export_status.deserialize_aws_json_1_0(
                data["ExportStatus"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_dynamodb.types.export_start_time

        out["start_time"] = (
            capo_dynamodb.types.export_start_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_dynamodb.types.export_end_time

        out["end_time"] = capo_dynamodb.types.export_end_time.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    if data.get("ExportManifest") is not None:
        out["export_manifest"] = data["ExportManifest"]
    if data.get("TableArn") is not None:
        out["table_arn"] = data["TableArn"]
    if data.get("TableId") is not None:
        out["table_id"] = data["TableId"]
    if data.get("ExportTime") is not None:
        import capo_dynamodb.types.export_time

        out["export_time"] = capo_dynamodb.types.export_time.deserialize_aws_json_1_0(
            data["ExportTime"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    if data.get("S3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["S3BucketOwner"]
    if data.get("S3Prefix") is not None:
        out["s3_prefix"] = data["S3Prefix"]
    if data.get("S3SseAlgorithm") is not None:
        import capo_dynamodb.types.s3_sse_algorithm

        out["s3_sse_algorithm"] = (
            capo_dynamodb.types.s3_sse_algorithm.deserialize_aws_json_1_0(
                data["S3SseAlgorithm"]
            )
        )
    if data.get("S3SseKmsKeyId") is not None:
        out["s3_sse_kms_key_id"] = data["S3SseKmsKeyId"]
    if data.get("FailureCode") is not None:
        out["failure_code"] = data["FailureCode"]
    if data.get("FailureMessage") is not None:
        out["failure_message"] = data["FailureMessage"]
    if data.get("ExportFormat") is not None:
        import capo_dynamodb.types.export_format

        out["export_format"] = (
            capo_dynamodb.types.export_format.deserialize_aws_json_1_0(
                data["ExportFormat"]
            )
        )
    if data.get("BilledSizeBytes") is not None:
        out["billed_size_bytes"] = data["BilledSizeBytes"]
    if data.get("ItemCount") is not None:
        out["item_count"] = data["ItemCount"]
    if data.get("ExportType") is not None:
        import capo_dynamodb.types.export_type

        out["export_type"] = capo_dynamodb.types.export_type.deserialize_aws_json_1_0(
            data["ExportType"]
        )
    if data.get("IncrementalExportSpecification") is not None:
        import capo_dynamodb.types.incremental_export_specification

        out["incremental_export_specification"] = (
            capo_dynamodb.types.incremental_export_specification.deserialize_aws_json_1_0(
                data["IncrementalExportSpecification"]
            )
        )
    if data.get("FilterSpecification") is not None:
        import capo_dynamodb.types.filter_specification

        out["filter_specification"] = (
            capo_dynamodb.types.filter_specification.deserialize_aws_json_1_0(
                data["FilterSpecification"]
            )
        )
    return out
