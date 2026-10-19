"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeApplicationProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_provider_arn


class DescribeApplicationProviderRequest(TypedDict, closed=True):
    application_provider_arn: (
        "capo_sso_admin.types.application_provider_arn.ApplicationProviderArn"
    )
    """<p>Specifies the ARN of the application provider for which you want details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationProviderRequest) -> dict:
    out: dict = {}
    out["ApplicationProviderArn"] = value["application_provider_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationProviderRequest:
    out: DescribeApplicationProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationProviderArn") is not None:
        out["application_provider_arn"] = data["ApplicationProviderArn"]
    else:
        out["application_provider_arn"] = ""
    return out
