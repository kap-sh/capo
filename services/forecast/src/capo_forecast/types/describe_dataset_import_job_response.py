"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeDatasetImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.data_source
    import capo_forecast.types.double
    import capo_forecast.types.field_statistics
    import capo_forecast.types.format
    import capo_forecast.types.geolocation_format
    import capo_forecast.types.import_mode
    import capo_forecast.types.long
    import capo_forecast.types.message
    import capo_forecast.types.name
    import capo_forecast.types.status
    import capo_forecast.types.time_zone
    import capo_forecast.types.timestamp
    import capo_forecast.types.timestamp_format
    import capo_forecast.types.use_geolocation_for_time_zone


class DescribeDatasetImportJobResponse(TypedDict, closed=True):
    dataset_import_job_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the dataset import job.</p>"""
    dataset_import_job_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The ARN of the dataset import job.</p>"""
    dataset_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset that the training data was imported to.</p>"""
    timestamp_format: NotRequired[
        "capo_forecast.types.timestamp_format.TimestampFormat"
    ]
    """<p>The format of timestamps in the dataset. The format that you specify depends on the <code>DataFrequency</code> specified when the dataset was created. The following formats are supported</p> <ul> <li> <p>"yyyy-MM-dd"</p> <p>For the following data frequencies: Y, M, W, and D</p> </li> <li> <p>"yyyy-MM-dd HH:mm:ss"</p> <p>For the following data frequencies: H, 30min, 15min, and 1min; and optionally, for: Y, M, W, and D</p> </li> </ul>"""
    time_zone: NotRequired["capo_forecast.types.time_zone.TimeZone"]
    """<p>The single time zone applied to every item in the dataset</p>"""
    use_geolocation_for_time_zone: (
        "capo_forecast.types.use_geolocation_for_time_zone.UseGeolocationForTimeZone"
    )
    """<p>Whether <code>TimeZone</code> is automatically derived from the geolocation attribute.</p>"""
    geolocation_format: NotRequired[
        "capo_forecast.types.geolocation_format.GeolocationFormat"
    ]
    """<p>The format of the geolocation attribute. Valid Values:<code>"LAT_LONG"</code> and <code>"CC_POSTALCODE"</code>.</p>"""
    data_source: NotRequired["capo_forecast.types.data_source.DataSource"]
    """<p>The location of the training data to import and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the data.</p> <p>If encryption is used, <code>DataSource</code> includes an Key Management Service (KMS) key.</p>"""
    estimated_time_remaining_in_minutes: NotRequired["capo_forecast.types.long.Long"]
    """<p>The estimated time remaining in minutes for the dataset import job to complete.</p>"""
    field_statistics: NotRequired[
        "capo_forecast.types.field_statistics.FieldStatistics"
    ]
    """<p>Statistical information about each field in the input data.</p>"""
    data_size: NotRequired["capo_forecast.types.double.Double"]
    """<p>The size of the dataset in gigabytes (GB) after the import job has finished.</p>"""
    status: NotRequired["capo_forecast.types.status.Status"]
    """<p>The status of the dataset import job. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> </ul>"""
    message: NotRequired["capo_forecast.types.message.Message"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the dataset import job was created.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    format: NotRequired["capo_forecast.types.format.Format"]
    """<p>The format of the imported data, CSV or PARQUET.</p>"""
    import_mode: NotRequired["capo_forecast.types.import_mode.ImportMode"]
    """<p>The import mode of the dataset import job, FULL or INCREMENTAL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetImportJobResponse) -> dict:
    out: dict = {}
    if "dataset_import_job_name" in value:
        out["DatasetImportJobName"] = value["dataset_import_job_name"]
    if "dataset_import_job_arn" in value:
        out["DatasetImportJobArn"] = value["dataset_import_job_arn"]
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "timestamp_format" in value:
        out["TimestampFormat"] = value["timestamp_format"]
    if "time_zone" in value:
        out["TimeZone"] = value["time_zone"]
    out["UseGeolocationForTimeZone"] = value.get("use_geolocation_for_time_zone", False)
    if "geolocation_format" in value:
        out["GeolocationFormat"] = value["geolocation_format"]
    if "data_source" in value:
        import capo_forecast.types.data_source

        out["DataSource"] = capo_forecast.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "estimated_time_remaining_in_minutes" in value:
        out["EstimatedTimeRemainingInMinutes"] = value[
            "estimated_time_remaining_in_minutes"
        ]
    if "field_statistics" in value:
        import capo_forecast.types.field_statistics

        out["FieldStatistics"] = (
            capo_forecast.types.field_statistics.serialize_aws_json_1_1(
                value["field_statistics"]
            )
        )
    if "data_size" in value:
        out["DataSize"] = (
            "NaN"
            if value["data_size"] != value["data_size"]
            else "Infinity"
            if value["data_size"] == float("inf")
            else "-Infinity"
            if value["data_size"] == float("-inf")
            else value["data_size"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "message" in value:
        out["Message"] = value["message"]
    if "creation_time" in value:
        import capo_forecast.types.timestamp

        out["CreationTime"] = capo_forecast.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modification_time" in value:
        import capo_forecast.types.timestamp

        out["LastModificationTime"] = (
            capo_forecast.types.timestamp.serialize_aws_json_1_1(
                value["last_modification_time"]
            )
        )
    if "format" in value:
        out["Format"] = value["format"]
    if "import_mode" in value:
        import capo_forecast.types.import_mode

        out["ImportMode"] = capo_forecast.types.import_mode.serialize_aws_json_1_1(
            value["import_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetImportJobResponse:
    out: DescribeDatasetImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatasetImportJobName") is not None:
        out["dataset_import_job_name"] = data["DatasetImportJobName"]
    if data.get("DatasetImportJobArn") is not None:
        out["dataset_import_job_arn"] = data["DatasetImportJobArn"]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    if data.get("TimestampFormat") is not None:
        out["timestamp_format"] = data["TimestampFormat"]
    if data.get("TimeZone") is not None:
        out["time_zone"] = data["TimeZone"]
    if data.get("UseGeolocationForTimeZone") is not None:
        out["use_geolocation_for_time_zone"] = data["UseGeolocationForTimeZone"]
    else:
        out["use_geolocation_for_time_zone"] = False
    if data.get("GeolocationFormat") is not None:
        out["geolocation_format"] = data["GeolocationFormat"]
    if data.get("DataSource") is not None:
        import capo_forecast.types.data_source

        out["data_source"] = capo_forecast.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if data.get("EstimatedTimeRemainingInMinutes") is not None:
        out["estimated_time_remaining_in_minutes"] = data[
            "EstimatedTimeRemainingInMinutes"
        ]
    if data.get("FieldStatistics") is not None:
        import capo_forecast.types.field_statistics

        out["field_statistics"] = (
            capo_forecast.types.field_statistics.deserialize_aws_json_1_1(
                data["FieldStatistics"]
            )
        )
    if data.get("DataSize") is not None:
        out["data_size"] = float(data["DataSize"])
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("CreationTime") is not None:
        import capo_forecast.types.timestamp

        out["creation_time"] = capo_forecast.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModificationTime") is not None:
        import capo_forecast.types.timestamp

        out["last_modification_time"] = (
            capo_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["LastModificationTime"]
            )
        )
    if data.get("Format") is not None:
        out["format"] = data["Format"]
    if data.get("ImportMode") is not None:
        import capo_forecast.types.import_mode

        out["import_mode"] = capo_forecast.types.import_mode.deserialize_aws_json_1_1(
            data["ImportMode"]
        )
    return out
