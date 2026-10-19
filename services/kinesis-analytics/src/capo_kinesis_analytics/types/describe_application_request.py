"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#DescribeApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.application_name


class DescribeApplicationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationRequest:
    out: DescribeApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    return out
