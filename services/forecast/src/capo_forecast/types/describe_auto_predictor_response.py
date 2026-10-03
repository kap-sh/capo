"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeAutoPredictorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.arn_list
    import capo_forecast.types.data_config
    import capo_forecast.types.encryption_config
    import capo_forecast.types.explainability_info
    import capo_forecast.types.forecast_dimensions
    import capo_forecast.types.forecast_types
    import capo_forecast.types.frequency
    import capo_forecast.types.integer
    import capo_forecast.types.long
    import capo_forecast.types.message
    import capo_forecast.types.monitor_info
    import capo_forecast.types.name
    import capo_forecast.types.optimization_metric
    import capo_forecast.types.reference_predictor_summary
    import capo_forecast.types.status
    import capo_forecast.types.time_alignment_boundary
    import capo_forecast.types.timestamp


class DescribeAutoPredictorResponse(TypedDict, closed=True):
    predictor_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the predictor</p>"""
    predictor_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the predictor.</p>"""
    forecast_horizon: NotRequired["capo_forecast.types.integer.Integer"]
    """<p>The number of time-steps that the model predicts. The forecast horizon is also called the prediction length.</p>"""
    forecast_types: NotRequired["capo_forecast.types.forecast_types.ForecastTypes"]
    """<p>The forecast types used during predictor training. Default value is ["0.1","0.5","0.9"].</p>"""
    forecast_frequency: NotRequired["capo_forecast.types.frequency.Frequency"]
    """<p>The frequency of predictions in a forecast.</p> <p>Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute). For example, "Y" indicates every year and "5min" indicates every five minutes.</p>"""
    forecast_dimensions: NotRequired[
        "capo_forecast.types.forecast_dimensions.ForecastDimensions"
    ]
    """<p>An array of dimension (field) names that specify the attributes used to group your time series.</p>"""
    dataset_import_job_arns: NotRequired["capo_forecast.types.arn_list.ArnList"]
    """<p>An array of the ARNs of the dataset import jobs used to import training data for the predictor.</p>"""
    data_config: NotRequired["capo_forecast.types.data_config.DataConfig"]
    """<p>The data configuration for your dataset group and any additional datasets.</p>"""
    encryption_config: NotRequired[
        "capo_forecast.types.encryption_config.EncryptionConfig"
    ]
    reference_predictor_summary: NotRequired[
        "capo_forecast.types.reference_predictor_summary.ReferencePredictorSummary"
    ]
    """<p>The ARN and state of the reference predictor. This parameter is only valid for retrained or upgraded predictors.</p>"""
    estimated_time_remaining_in_minutes: NotRequired["capo_forecast.types.long.Long"]
    """<p>The estimated time remaining in minutes for the predictor training job to complete.</p>"""
    status: NotRequired["capo_forecast.types.status.Status"]
    """<p>The status of the predictor. States include: </p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul>"""
    message: NotRequired["capo_forecast.types.message.Message"]
    """<p>In the event of an error, a message detailing the cause of the error.</p>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp of the CreateAutoPredictor request.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    optimization_metric: NotRequired[
        "capo_forecast.types.optimization_metric.OptimizationMetric"
    ]
    """<p>The accuracy metric used to optimize the predictor.</p>"""
    explainability_info: NotRequired[
        "capo_forecast.types.explainability_info.ExplainabilityInfo"
    ]
    """<p>Provides the status and ARN of the Predictor Explainability.</p>"""
    monitor_info: NotRequired["capo_forecast.types.monitor_info.MonitorInfo"]
    """<p>A object with the Amazon Resource Name (ARN) and status of the monitor resource.</p>"""
    time_alignment_boundary: NotRequired[
        "capo_forecast.types.time_alignment_boundary.TimeAlignmentBoundary"
    ]
    """<p>The time boundary Forecast uses when aggregating data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAutoPredictorResponse) -> dict:
    out: dict = {}
    if "predictor_arn" in value:
        out["PredictorArn"] = value["predictor_arn"]
    if "predictor_name" in value:
        out["PredictorName"] = value["predictor_name"]
    if "forecast_horizon" in value:
        out["ForecastHorizon"] = value["forecast_horizon"]
    if "forecast_types" in value:
        import capo_forecast.types.forecast_types

        out["ForecastTypes"] = (
            capo_forecast.types.forecast_types.serialize_aws_json_1_1(
                value["forecast_types"]
            )
        )
    if "forecast_frequency" in value:
        out["ForecastFrequency"] = value["forecast_frequency"]
    if "forecast_dimensions" in value:
        import capo_forecast.types.forecast_dimensions

        out["ForecastDimensions"] = (
            capo_forecast.types.forecast_dimensions.serialize_aws_json_1_1(
                value["forecast_dimensions"]
            )
        )
    if "dataset_import_job_arns" in value:
        import capo_forecast.types.arn_list

        out["DatasetImportJobArns"] = (
            capo_forecast.types.arn_list.serialize_aws_json_1_1(
                value["dataset_import_job_arns"]
            )
        )
    if "data_config" in value:
        import capo_forecast.types.data_config

        out["DataConfig"] = capo_forecast.types.data_config.serialize_aws_json_1_1(
            value["data_config"]
        )
    if "encryption_config" in value:
        import capo_forecast.types.encryption_config

        out["EncryptionConfig"] = (
            capo_forecast.types.encryption_config.serialize_aws_json_1_1(
                value["encryption_config"]
            )
        )
    if "reference_predictor_summary" in value:
        import capo_forecast.types.reference_predictor_summary

        out["ReferencePredictorSummary"] = (
            capo_forecast.types.reference_predictor_summary.serialize_aws_json_1_1(
                value["reference_predictor_summary"]
            )
        )
    if "estimated_time_remaining_in_minutes" in value:
        out["EstimatedTimeRemainingInMinutes"] = value[
            "estimated_time_remaining_in_minutes"
        ]
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
    if "optimization_metric" in value:
        import capo_forecast.types.optimization_metric

        out["OptimizationMetric"] = (
            capo_forecast.types.optimization_metric.serialize_aws_json_1_1(
                value["optimization_metric"]
            )
        )
    if "explainability_info" in value:
        import capo_forecast.types.explainability_info

        out["ExplainabilityInfo"] = (
            capo_forecast.types.explainability_info.serialize_aws_json_1_1(
                value["explainability_info"]
            )
        )
    if "monitor_info" in value:
        import capo_forecast.types.monitor_info

        out["MonitorInfo"] = capo_forecast.types.monitor_info.serialize_aws_json_1_1(
            value["monitor_info"]
        )
    if "time_alignment_boundary" in value:
        import capo_forecast.types.time_alignment_boundary

        out["TimeAlignmentBoundary"] = (
            capo_forecast.types.time_alignment_boundary.serialize_aws_json_1_1(
                value["time_alignment_boundary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAutoPredictorResponse:
    out: DescribeAutoPredictorResponse = {}  # type: ignore[typeddict-item]
    if data.get("PredictorArn") is not None:
        out["predictor_arn"] = data["PredictorArn"]
    if data.get("PredictorName") is not None:
        out["predictor_name"] = data["PredictorName"]
    if data.get("ForecastHorizon") is not None:
        out["forecast_horizon"] = data["ForecastHorizon"]
    if data.get("ForecastTypes") is not None:
        import capo_forecast.types.forecast_types

        out["forecast_types"] = (
            capo_forecast.types.forecast_types.deserialize_aws_json_1_1(
                data["ForecastTypes"]
            )
        )
    if data.get("ForecastFrequency") is not None:
        out["forecast_frequency"] = data["ForecastFrequency"]
    if data.get("ForecastDimensions") is not None:
        import capo_forecast.types.forecast_dimensions

        out["forecast_dimensions"] = (
            capo_forecast.types.forecast_dimensions.deserialize_aws_json_1_1(
                data["ForecastDimensions"]
            )
        )
    if data.get("DatasetImportJobArns") is not None:
        import capo_forecast.types.arn_list

        out["dataset_import_job_arns"] = (
            capo_forecast.types.arn_list.deserialize_aws_json_1_1(
                data["DatasetImportJobArns"]
            )
        )
    if data.get("DataConfig") is not None:
        import capo_forecast.types.data_config

        out["data_config"] = capo_forecast.types.data_config.deserialize_aws_json_1_1(
            data["DataConfig"]
        )
    if data.get("EncryptionConfig") is not None:
        import capo_forecast.types.encryption_config

        out["encryption_config"] = (
            capo_forecast.types.encryption_config.deserialize_aws_json_1_1(
                data["EncryptionConfig"]
            )
        )
    if data.get("ReferencePredictorSummary") is not None:
        import capo_forecast.types.reference_predictor_summary

        out["reference_predictor_summary"] = (
            capo_forecast.types.reference_predictor_summary.deserialize_aws_json_1_1(
                data["ReferencePredictorSummary"]
            )
        )
    if data.get("EstimatedTimeRemainingInMinutes") is not None:
        out["estimated_time_remaining_in_minutes"] = data[
            "EstimatedTimeRemainingInMinutes"
        ]
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
    if data.get("OptimizationMetric") is not None:
        import capo_forecast.types.optimization_metric

        out["optimization_metric"] = (
            capo_forecast.types.optimization_metric.deserialize_aws_json_1_1(
                data["OptimizationMetric"]
            )
        )
    if data.get("ExplainabilityInfo") is not None:
        import capo_forecast.types.explainability_info

        out["explainability_info"] = (
            capo_forecast.types.explainability_info.deserialize_aws_json_1_1(
                data["ExplainabilityInfo"]
            )
        )
    if data.get("MonitorInfo") is not None:
        import capo_forecast.types.monitor_info

        out["monitor_info"] = capo_forecast.types.monitor_info.deserialize_aws_json_1_1(
            data["MonitorInfo"]
        )
    if data.get("TimeAlignmentBoundary") is not None:
        import capo_forecast.types.time_alignment_boundary

        out["time_alignment_boundary"] = (
            capo_forecast.types.time_alignment_boundary.deserialize_aws_json_1_1(
                data["TimeAlignmentBoundary"]
            )
        )
    return out
