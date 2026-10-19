"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#StartApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.run_configuration


class StartApplicationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of the application.</p>"""
    run_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.run_configuration.RunConfiguration"
    ]
    """<p>Identifies the run configuration (start parameters) of a Managed Service for Apache Flink application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "run_configuration" in value:
        import capo_kinesis_analytics_v2.types.run_configuration

        out["RunConfiguration"] = (
            capo_kinesis_analytics_v2.types.run_configuration.serialize_aws_json_1_1(
                value["run_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartApplicationRequest:
    out: StartApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("RunConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.run_configuration

        out["run_configuration"] = (
            capo_kinesis_analytics_v2.types.run_configuration.deserialize_aws_json_1_1(
                data["RunConfiguration"]
            )
        )
    return out
