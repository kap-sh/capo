"""Generated from Smithy shape ``com.amazonaws.devicefarm#Job``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.counters
    import capo_device_farm.types.date_time
    import capo_device_farm.types.device
    import capo_device_farm.types.device_minutes
    import capo_device_farm.types.execution_result
    import capo_device_farm.types.execution_status
    import capo_device_farm.types.job_insights
    import capo_device_farm.types.message
    import capo_device_farm.types.name
    import capo_device_farm.types.string
    import capo_device_farm.types.test_type
    import capo_device_farm.types.video_capture


class Job(TypedDict, closed=True):
    arn: NotRequired["capo_device_farm.types.amazon_resource_name.AmazonResourceName"]
    """<p>The job's ARN.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The job's name.</p>"""
    type: NotRequired["capo_device_farm.types.test_type.TestType"]
    """<p>The job's type.</p> <p>Allowed values include the following:</p> <ul> <li> <p>BUILTIN_FUZZ</p> </li> <li> <p>APPIUM_JAVA_JUNIT</p> </li> <li> <p>APPIUM_JAVA_TESTNG</p> </li> <li> <p>APPIUM_PYTHON</p> </li> <li> <p>APPIUM_NODE</p> </li> <li> <p>APPIUM_RUBY</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG</p> </li> <li> <p>APPIUM_WEB_PYTHON</p> </li> <li> <p>APPIUM_WEB_NODE</p> </li> <li> <p>APPIUM_WEB_RUBY</p> </li> <li> <p>INSTRUMENTATION</p> </li> <li> <p>XCTEST</p> </li> <li> <p>XCTEST_UI</p> </li> </ul>"""
    created: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>When the job was created.</p>"""
    status: NotRequired["capo_device_farm.types.execution_status.ExecutionStatus"]
    """<p>The job's status.</p> <p>Allowed values include:</p> <ul> <li> <p>PENDING</p> </li> <li> <p>PENDING_CONCURRENCY</p> </li> <li> <p>PENDING_DEVICE</p> </li> <li> <p>PROCESSING</p> </li> <li> <p>SCHEDULING</p> </li> <li> <p>PREPARING</p> </li> <li> <p>RUNNING</p> </li> <li> <p>COMPLETED</p> </li> <li> <p>STOPPING</p> </li> </ul>"""
    result: NotRequired["capo_device_farm.types.execution_result.ExecutionResult"]
    """<p>The job's result.</p> <p>Allowed values include:</p> <ul> <li> <p>PENDING</p> </li> <li> <p>PASSED</p> </li> <li> <p>WARNED</p> </li> <li> <p>FAILED</p> </li> <li> <p>SKIPPED</p> </li> <li> <p>ERRORED</p> </li> <li> <p>STOPPED</p> </li> </ul>"""
    started: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>The job's start time.</p>"""
    stopped: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>The job's stop time.</p>"""
    counters: NotRequired["capo_device_farm.types.counters.Counters"]
    """<p>The job's result counters.</p>"""
    message: NotRequired["capo_device_farm.types.message.Message"]
    """<p>A message about the job's result.</p>"""
    device: NotRequired["capo_device_farm.types.device.Device"]
    """<p>The device (phone or tablet).</p>"""
    instance_arn: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the instance.</p>"""
    device_minutes: NotRequired["capo_device_farm.types.device_minutes.DeviceMinutes"]
    """<p>Represents the total (metered or unmetered) minutes used by the job.</p>"""
    video_endpoint: NotRequired["capo_device_farm.types.string.String"]
    """<p>The endpoint for streaming device video.</p>"""
    video_capture: NotRequired["capo_device_farm.types.video_capture.VideoCapture"]
    """<p>This value is set to true if video capture is enabled. Otherwise, it is set to false.</p>"""
    insights: NotRequired["capo_device_farm.types.job_insights.JobInsights"]
    """<p>The insights for the job, including the report status and test-level metrics. This field contains data only if you specified <code>insightsTypes</code> when you scheduled the run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Job) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_device_farm.types.test_type

        out["type"] = capo_device_farm.types.test_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "created" in value:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["created"]
        )
    if "status" in value:
        import capo_device_farm.types.execution_status

        out["status"] = capo_device_farm.types.execution_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "result" in value:
        import capo_device_farm.types.execution_result

        out["result"] = capo_device_farm.types.execution_result.serialize_aws_json_1_1(
            value["result"]
        )
    if "started" in value:
        import capo_device_farm.types.date_time

        out["started"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["started"]
        )
    if "stopped" in value:
        import capo_device_farm.types.date_time

        out["stopped"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["stopped"]
        )
    if "counters" in value:
        import capo_device_farm.types.counters

        out["counters"] = capo_device_farm.types.counters.serialize_aws_json_1_1(
            value["counters"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "device" in value:
        import capo_device_farm.types.device

        out["device"] = capo_device_farm.types.device.serialize_aws_json_1_1(
            value["device"]
        )
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    if "device_minutes" in value:
        import capo_device_farm.types.device_minutes

        out["deviceMinutes"] = (
            capo_device_farm.types.device_minutes.serialize_aws_json_1_1(
                value["device_minutes"]
            )
        )
    if "video_endpoint" in value:
        out["videoEndpoint"] = value["video_endpoint"]
    if "video_capture" in value:
        out["videoCapture"] = value["video_capture"]
    if "insights" in value:
        import capo_device_farm.types.job_insights

        out["insights"] = capo_device_farm.types.job_insights.serialize_aws_json_1_1(
            value["insights"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        import capo_device_farm.types.test_type

        out["type"] = capo_device_farm.types.test_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("created") is not None:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["created"]
        )
    if data.get("status") is not None:
        import capo_device_farm.types.execution_status

        out["status"] = (
            capo_device_farm.types.execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("result") is not None:
        import capo_device_farm.types.execution_result

        out["result"] = (
            capo_device_farm.types.execution_result.deserialize_aws_json_1_1(
                data["result"]
            )
        )
    if data.get("started") is not None:
        import capo_device_farm.types.date_time

        out["started"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["started"]
        )
    if data.get("stopped") is not None:
        import capo_device_farm.types.date_time

        out["stopped"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["stopped"]
        )
    if data.get("counters") is not None:
        import capo_device_farm.types.counters

        out["counters"] = capo_device_farm.types.counters.deserialize_aws_json_1_1(
            data["counters"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("device") is not None:
        import capo_device_farm.types.device

        out["device"] = capo_device_farm.types.device.deserialize_aws_json_1_1(
            data["device"]
        )
    if data.get("instanceArn") is not None:
        out["instance_arn"] = data["instanceArn"]
    if data.get("deviceMinutes") is not None:
        import capo_device_farm.types.device_minutes

        out["device_minutes"] = (
            capo_device_farm.types.device_minutes.deserialize_aws_json_1_1(
                data["deviceMinutes"]
            )
        )
    if data.get("videoEndpoint") is not None:
        out["video_endpoint"] = data["videoEndpoint"]
    if data.get("videoCapture") is not None:
        out["video_capture"] = data["videoCapture"]
    if data.get("insights") is not None:
        import capo_device_farm.types.job_insights

        out["insights"] = capo_device_farm.types.job_insights.deserialize_aws_json_1_1(
            data["insights"]
        )
    return out


def redact_sensitive(value: Job) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "insights" in value:
        import capo_device_farm.types.job_insights

        out["insights"] = capo_device_farm.types.job_insights.redact_sensitive(
            value["insights"]
        )
    return out
