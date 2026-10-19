"""Generated from Smithy shape ``com.amazonaws.forecast#CreatePredictorBacktestExportJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.data_destination
    import capo_forecast.types.format
    import capo_forecast.types.name
    import capo_forecast.types.tags


class CreatePredictorBacktestExportJobRequest(TypedDict, closed=True):
    predictor_backtest_export_job_name: "capo_forecast.types.name.Name"
    """<p>The name for the backtest export job.</p>"""
    predictor_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the predictor that you want to export.</p>"""
    destination: "capo_forecast.types.data_destination.DataDestination"
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>Optional metadata to help you categorize and organize your backtests. Each tag consists of a key and an optional value, both of which you define. Tag keys and values are case sensitive.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>For each resource, each tag key must be unique and each tag key must have one value.</p> </li> <li> <p>Maximum number of tags per resource: 50.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Accepted characters: all letters and numbers, spaces representable in UTF-8, and + - = . _ : / @. If your tagging schema is used across other services and resources, the character restrictions of those services also apply. </p> </li> <li> <p>Key prefixes cannot include any upper or lowercase combination of <code>aws:</code> or <code>AWS:</code>. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit. You cannot edit or delete tag keys with this prefix.</p> </li> </ul>"""
    format: NotRequired["capo_forecast.types.format.Format"]
    """<p>The format of the exported data, CSV or PARQUET. The default value is CSV.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePredictorBacktestExportJobRequest) -> dict:
    out: dict = {}
    out["PredictorBacktestExportJobName"] = value["predictor_backtest_export_job_name"]
    out["PredictorArn"] = value["predictor_arn"]
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


def deserialize_aws_json_1_1(data: dict) -> CreatePredictorBacktestExportJobRequest:
    out: CreatePredictorBacktestExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("PredictorBacktestExportJobName") is not None:
        out["predictor_backtest_export_job_name"] = data[
            "PredictorBacktestExportJobName"
        ]
    else:
        out["predictor_backtest_export_job_name"] = ""
    if data.get("PredictorArn") is not None:
        out["predictor_arn"] = data["PredictorArn"]
    else:
        out["predictor_arn"] = ""
    if data.get("Destination") is not None:
        import capo_forecast.types.data_destination

        out["destination"] = (
            capo_forecast.types.data_destination.deserialize_aws_json_1_1(
                data["Destination"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePredictorBacktestExportJobRequest.destination required"
        )
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("Format") is not None:
        out["format"] = data["Format"]
    return out


def redact_sensitive(value: CreatePredictorBacktestExportJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.redact_sensitive(value["tags"])
    return out
