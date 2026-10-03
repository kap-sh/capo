"""Generated from Smithy shape ``com.amazonaws.sagemaker#ScheduleConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.schedule_expression
    import capo_sagemaker.types.string


class ScheduleConfig(TypedDict, closed=True):
    schedule_expression: NotRequired[
        "capo_sagemaker.types.schedule_expression.ScheduleExpression"
    ]
    """<p>A cron expression that describes details about the monitoring schedule.</p> <p>The supported cron expressions are:</p> <ul> <li> <p>If you want to set the job to start every hour, use the following:</p> <p> <code>Hourly: cron(0 * ? * * *)</code> </p> </li> <li> <p>If you want to start the job daily:</p> <p> <code>cron(0 [00-23] ? * * *)</code> </p> </li> <li> <p>If you want to run the job one time, immediately, use the following keyword:</p> <p> <code>NOW</code> </p> </li> </ul> <p>For example, the following are valid cron expressions:</p> <ul> <li> <p>Daily at noon UTC: <code>cron(0 12 ? * * *)</code> </p> </li> <li> <p>Daily at midnight UTC: <code>cron(0 0 ? * * *)</code> </p> </li> </ul> <p>To support running every 6, 12 hours, the following are also supported:</p> <p> <code>cron(0 [00-23]/[01-24] ? * * *)</code> </p> <p>For example, the following are valid cron expressions:</p> <ul> <li> <p>Every 12 hours, starting at 5pm UTC: <code>cron(0 17/12 ? * * *)</code> </p> </li> <li> <p>Every two hours starting at midnight: <code>cron(0 0/2 ? * * *)</code> </p> </li> </ul> <note> <ul> <li> <p>Even though the cron expression is set to start at 5PM UTC, note that there could be a delay of 0-20 minutes from the actual requested time to run the execution. </p> </li> <li> <p>We recommend that if you would like a daily schedule, you do not provide this parameter. Amazon SageMaker AI will pick a time for running every day.</p> </li> </ul> </note> <p>You can also specify the keyword <code>NOW</code> to run the monitoring job immediately, one time, without recurring.</p>"""
    data_analysis_start_time: NotRequired["capo_sagemaker.types.string.String"]
    """<p>Sets the start time for a monitoring job window. Express this time as an offset to the times that you schedule your monitoring jobs to run. You schedule monitoring jobs with the <code>ScheduleExpression</code> parameter. Specify this offset in ISO 8601 duration format. For example, if you want to monitor the five hours of data in your dataset that precede the start of each monitoring job, you would specify: <code>"-PT5H"</code>.</p> <p>The start time that you specify must not precede the end time that you specify by more than 24 hours. You specify the end time with the <code>DataAnalysisEndTime</code> parameter.</p> <p>If you set <code>ScheduleExpression</code> to <code>NOW</code>, this parameter is required.</p>"""
    data_analysis_end_time: NotRequired["capo_sagemaker.types.string.String"]
    """<p>Sets the end time for a monitoring job window. Express this time as an offset to the times that you schedule your monitoring jobs to run. You schedule monitoring jobs with the <code>ScheduleExpression</code> parameter. Specify this offset in ISO 8601 duration format. For example, if you want to end the window one hour before the start of each monitoring job, you would specify: <code>"-PT1H"</code>.</p> <p>The end time that you specify must not follow the start time that you specify by more than 24 hours. You specify the start time with the <code>DataAnalysisStartTime</code> parameter.</p> <p>If you set <code>ScheduleExpression</code> to <code>NOW</code>, this parameter is required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleConfig) -> dict:
    out: dict = {}
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "data_analysis_start_time" in value:
        out["DataAnalysisStartTime"] = value["data_analysis_start_time"]
    if "data_analysis_end_time" in value:
        out["DataAnalysisEndTime"] = value["data_analysis_end_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduleConfig:
    out: ScheduleConfig = {}  # type: ignore[typeddict-item]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("DataAnalysisStartTime") is not None:
        out["data_analysis_start_time"] = data["DataAnalysisStartTime"]
    if data.get("DataAnalysisEndTime") is not None:
        out["data_analysis_end_time"] = data["DataAnalysisEndTime"]
    return out
