"""Generated from Smithy shape ``com.amazonaws.amplify#Step``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.artifacts_url
    import capo_amplify.types.context
    import capo_amplify.types.end_time
    import capo_amplify.types.job_status
    import capo_amplify.types.log_url
    import capo_amplify.types.screenshots
    import capo_amplify.types.start_time
    import capo_amplify.types.status_reason
    import capo_amplify.types.step_name
    import capo_amplify.types.test_artifacts_url
    import capo_amplify.types.test_config_url


class Step(TypedDict, closed=True):
    step_name: "capo_amplify.types.step_name.StepName"
    """<p> The name of the execution step. </p>"""
    start_time: "capo_amplify.types.start_time.StartTime"
    """<p> The start date and time of the execution step. </p>"""
    status: "capo_amplify.types.job_status.JobStatus"
    """<p> The status of the execution step. </p>"""
    end_time: "capo_amplify.types.end_time.EndTime"
    """<p> The end date and time of the execution step. </p>"""
    log_url: NotRequired["capo_amplify.types.log_url.LogUrl"]
    """<p> The URL to the logs for the execution step. </p>"""
    artifacts_url: NotRequired["capo_amplify.types.artifacts_url.ArtifactsUrl"]
    """<p> The URL to the build artifact for the execution step. </p>"""
    test_artifacts_url: NotRequired[
        "capo_amplify.types.test_artifacts_url.TestArtifactsUrl"
    ]
    """<p> The URL to the test artifact for the execution step. </p>"""
    test_config_url: NotRequired["capo_amplify.types.test_config_url.TestConfigUrl"]
    """<p> The URL to the test configuration for the execution step. </p>"""
    screenshots: NotRequired["capo_amplify.types.screenshots.Screenshots"]
    """<p> The list of screenshot URLs for the execution step, if relevant. </p>"""
    status_reason: NotRequired["capo_amplify.types.status_reason.StatusReason"]
    """<p> The reason for the current step status. </p>"""
    context: NotRequired["capo_amplify.types.context.Context"]
    """<p> The context for the current step. Includes a build image if the step is build. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Step) -> dict:
    out: dict = {}
    out["stepName"] = value["step_name"]
    import capo_amplify.types.start_time

    out["startTime"] = capo_amplify.types.start_time.serialize_json(value["start_time"])
    import capo_amplify.types.job_status

    out["status"] = capo_amplify.types.job_status.serialize_json(value["status"])
    import capo_amplify.types.end_time

    out["endTime"] = capo_amplify.types.end_time.serialize_json(value["end_time"])
    if "log_url" in value:
        out["logUrl"] = value["log_url"]
    if "artifacts_url" in value:
        out["artifactsUrl"] = value["artifacts_url"]
    if "test_artifacts_url" in value:
        out["testArtifactsUrl"] = value["test_artifacts_url"]
    if "test_config_url" in value:
        out["testConfigUrl"] = value["test_config_url"]
    if "screenshots" in value:
        import capo_amplify.types.screenshots

        out["screenshots"] = capo_amplify.types.screenshots.serialize_json(
            value["screenshots"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "context" in value:
        out["context"] = value["context"]
    return out


def deserialize_json(data: dict) -> Step:
    out: Step = {}  # type: ignore[typeddict-item]
    if data.get("stepName") is not None:
        out["step_name"] = data["stepName"]
    else:
        out["step_name"] = ""
    if data.get("startTime") is not None:
        import capo_amplify.types.start_time

        out["start_time"] = capo_amplify.types.start_time.deserialize_json(
            data["startTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        import capo_amplify.types.job_status

        out["status"] = capo_amplify.types.job_status.deserialize_json(data["status"])
    else:
        import typing

        out["status"] = typing.cast("capo_amplify.types.job_status.JobStatus", "")
    if data.get("endTime") is not None:
        import capo_amplify.types.end_time

        out["end_time"] = capo_amplify.types.end_time.deserialize_json(data["endTime"])
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("logUrl") is not None:
        out["log_url"] = data["logUrl"]
    if data.get("artifactsUrl") is not None:
        out["artifacts_url"] = data["artifactsUrl"]
    if data.get("testArtifactsUrl") is not None:
        out["test_artifacts_url"] = data["testArtifactsUrl"]
    if data.get("testConfigUrl") is not None:
        out["test_config_url"] = data["testConfigUrl"]
    if data.get("screenshots") is not None:
        import capo_amplify.types.screenshots

        out["screenshots"] = capo_amplify.types.screenshots.deserialize_json(
            data["screenshots"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("context") is not None:
        out["context"] = data["context"]
    return out
