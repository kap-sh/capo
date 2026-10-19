"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetApplicationSessionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn


class GetApplicationSessionConfigurationRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>The Amazon Resource Name (ARN) of the application for which to retrieve the session configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationSessionConfigurationRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationSessionConfigurationRequest:
    out: GetApplicationSessionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        out["application_arn"] = ""
    return out
