"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_mode
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.application_status
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.resource_arn
    import capo_kinesis_analytics_v2.types.runtime_environment


class ApplicationSummary(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of the application.</p>"""
    application_arn: "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The ARN of the application.</p>"""
    application_status: (
        "capo_kinesis_analytics_v2.types.application_status.ApplicationStatus"
    )
    """<p>The status of the application.</p>"""
    application_version_id: (
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>Provides the current application version.</p>"""
    runtime_environment: (
        "capo_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment"
    )
    """<p>The runtime environment for the application.</p>"""
    application_mode: NotRequired[
        "capo_kinesis_analytics_v2.types.application_mode.ApplicationMode"
    ]
    """<p>For a Managed Service for Apache Flink application, the mode is <code>STREAMING</code>. For a Managed Service for Apache Flink Studio notebook, it is <code>INTERACTIVE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSummary) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["ApplicationARN"] = value["application_arn"]
    import capo_kinesis_analytics_v2.types.application_status

    out["ApplicationStatus"] = (
        capo_kinesis_analytics_v2.types.application_status.serialize_aws_json_1_1(
            value["application_status"]
        )
    )
    out["ApplicationVersionId"] = value["application_version_id"]
    import capo_kinesis_analytics_v2.types.runtime_environment

    out["RuntimeEnvironment"] = (
        capo_kinesis_analytics_v2.types.runtime_environment.serialize_aws_json_1_1(
            value["runtime_environment"]
        )
    )
    if "application_mode" in value:
        import capo_kinesis_analytics_v2.types.application_mode

        out["ApplicationMode"] = (
            capo_kinesis_analytics_v2.types.application_mode.serialize_aws_json_1_1(
                value["application_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("ApplicationARN") is not None:
        out["application_arn"] = data["ApplicationARN"]
    else:
        out["application_arn"] = ""
    if data.get("ApplicationStatus") is not None:
        import capo_kinesis_analytics_v2.types.application_status

        out["application_status"] = (
            capo_kinesis_analytics_v2.types.application_status.deserialize_aws_json_1_1(
                data["ApplicationStatus"]
            )
        )
    else:
        import typing

        out["application_status"] = typing.cast(
            "capo_kinesis_analytics_v2.types.application_status.ApplicationStatus", ""
        )
    if data.get("ApplicationVersionId") is not None:
        out["application_version_id"] = data["ApplicationVersionId"]
    else:
        out["application_version_id"] = 0
    if data.get("RuntimeEnvironment") is not None:
        import capo_kinesis_analytics_v2.types.runtime_environment

        out["runtime_environment"] = (
            capo_kinesis_analytics_v2.types.runtime_environment.deserialize_aws_json_1_1(
                data["RuntimeEnvironment"]
            )
        )
    else:
        import typing

        out["runtime_environment"] = typing.cast(
            "capo_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment", ""
        )
    if data.get("ApplicationMode") is not None:
        import capo_kinesis_analytics_v2.types.application_mode

        out["application_mode"] = (
            capo_kinesis_analytics_v2.types.application_mode.deserialize_aws_json_1_1(
                data["ApplicationMode"]
            )
        )
    return out
