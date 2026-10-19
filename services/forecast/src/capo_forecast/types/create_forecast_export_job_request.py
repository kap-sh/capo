"""Generated from Smithy shape ``com.amazonaws.forecast#CreateForecastExportJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.data_destination
    import capo_forecast.types.format
    import capo_forecast.types.name
    import capo_forecast.types.tags


class CreateForecastExportJobRequest(TypedDict, closed=True):
    forecast_export_job_name: "capo_forecast.types.name.Name"
    """<p>The name for the forecast export job.</p>"""
    forecast_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the forecast that you want to export.</p>"""
    destination: "capo_forecast.types.data_destination.DataDestination"
    """<p>The location where you want to save the forecast and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the location. The forecast must be exported to an Amazon S3 bucket.</p> <p>If encryption is used, <code>Destination</code> must include an Key Management Service (KMS) key. The IAM role must allow Amazon Forecast permission to access the key.</p>"""
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>The optional metadata that you apply to the forecast export job to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>"""
    format: NotRequired["capo_forecast.types.format.Format"]
    """<p>The format of the exported data, CSV or PARQUET. The default value is CSV.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateForecastExportJobRequest) -> dict:
    out: dict = {}
    out["ForecastExportJobName"] = value["forecast_export_job_name"]
    out["ForecastArn"] = value["forecast_arn"]
    import capo_forecast.types.data_destination

    out["Destination"] = capo_forecast.types.data_destination.serialize_aws_json_1_1(
        value["destination"]
    )
    if "tags" in value:
        import capo_forecast.types.tags

        out["Tags"] = capo_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    if "format" in value:
        out["Format"] = value["format"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateForecastExportJobRequest:
    out: CreateForecastExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("ForecastExportJobName") is not None:
        out["forecast_export_job_name"] = data["ForecastExportJobName"]
    else:
        out["forecast_export_job_name"] = ""
    if data.get("ForecastArn") is not None:
        out["forecast_arn"] = data["ForecastArn"]
    else:
        out["forecast_arn"] = ""
    if data.get("Destination") is not None:
        import capo_forecast.types.data_destination

        out["destination"] = (
            capo_forecast.types.data_destination.deserialize_aws_json_1_1(
                data["Destination"]
            )
        )
    else:
        raise DeserializationError(
            "CreateForecastExportJobRequest.destination required"
        )
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("Format") is not None:
        out["format"] = data["Format"]
    return out


def redact_sensitive(value: CreateForecastExportJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.redact_sensitive(value["tags"])
    return out
