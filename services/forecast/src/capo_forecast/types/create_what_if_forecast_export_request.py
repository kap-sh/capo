"""Generated from Smithy shape ``com.amazonaws.forecast#CreateWhatIfForecastExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.data_destination
    import capo_forecast.types.format
    import capo_forecast.types.name
    import capo_forecast.types.tags
    import capo_forecast.types.what_if_forecast_arn_list_for_export


class CreateWhatIfForecastExportRequest(TypedDict, closed=True):
    what_if_forecast_export_name: "capo_forecast.types.name.Name"
    """<p>The name of the what-if forecast to export.</p>"""
    what_if_forecast_arns: "capo_forecast.types.what_if_forecast_arn_list_for_export.WhatIfForecastArnListForExport"
    """<p>The list of what-if forecast Amazon Resource Names (ARNs) to export.</p>"""
    destination: "capo_forecast.types.data_destination.DataDestination"
    """<p>The location where you want to save the forecast and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the location. The forecast must be exported to an Amazon S3 bucket.</p> <p>If encryption is used, <code>Destination</code> must include an Key Management Service (KMS) key. The IAM role must allow Amazon Forecast permission to access the key.</p>"""
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html">tags</a> to apply to the what if forecast.</p>"""
    format: NotRequired["capo_forecast.types.format.Format"]
    """<p>The format of the exported data, CSV or PARQUET.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWhatIfForecastExportRequest) -> dict:
    out: dict = {}
    out["WhatIfForecastExportName"] = value["what_if_forecast_export_name"]
    import capo_forecast.types.what_if_forecast_arn_list_for_export

    out["WhatIfForecastArns"] = (
        capo_forecast.types.what_if_forecast_arn_list_for_export.serialize_aws_json_1_1(
            value["what_if_forecast_arns"]
        )
    )
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


def deserialize_aws_json_1_1(data: dict) -> CreateWhatIfForecastExportRequest:
    out: CreateWhatIfForecastExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("WhatIfForecastExportName") is not None:
        out["what_if_forecast_export_name"] = data["WhatIfForecastExportName"]
    else:
        raise DeserializationError(
            "CreateWhatIfForecastExportRequest.what_if_forecast_export_name required"
        )
    if data.get("WhatIfForecastArns") is not None:
        import capo_forecast.types.what_if_forecast_arn_list_for_export

        out["what_if_forecast_arns"] = (
            capo_forecast.types.what_if_forecast_arn_list_for_export.deserialize_aws_json_1_1(
                data["WhatIfForecastArns"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWhatIfForecastExportRequest.what_if_forecast_arns required"
        )
    if data.get("Destination") is not None:
        import capo_forecast.types.data_destination

        out["destination"] = (
            capo_forecast.types.data_destination.deserialize_aws_json_1_1(
                data["Destination"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWhatIfForecastExportRequest.destination required"
        )
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("Format") is not None:
        out["format"] = data["Format"]
    return out
