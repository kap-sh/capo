"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.application_name
    import capo_kinesis_analytics.types.application_status
    import capo_kinesis_analytics.types.resource_arn


class ApplicationSummary(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of the application.</p>"""
    application_arn: "capo_kinesis_analytics.types.resource_arn.ResourceARN"
    """<p>ARN of the application.</p>"""
    application_status: (
        "capo_kinesis_analytics.types.application_status.ApplicationStatus"
    )
    """<p>Status of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSummary) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["ApplicationARN"] = value["application_arn"]
    import capo_kinesis_analytics.types.application_status

    out["ApplicationStatus"] = (
        capo_kinesis_analytics.types.application_status.serialize_aws_json_1_1(
            value["application_status"]
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
        import capo_kinesis_analytics.types.application_status

        out["application_status"] = (
            capo_kinesis_analytics.types.application_status.deserialize_aws_json_1_1(
                data["ApplicationStatus"]
            )
        )
    else:
        import typing

        out["application_status"] = typing.cast(
            "capo_kinesis_analytics.types.application_status.ApplicationStatus", ""
        )
    return out
