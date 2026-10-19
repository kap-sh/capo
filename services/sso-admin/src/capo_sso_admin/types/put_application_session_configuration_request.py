"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PutApplicationSessionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.user_background_session_application_status


class PutApplicationSessionConfigurationRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>The Amazon Resource Name (ARN) of the application for which to update the session configuration.</p>"""
    user_background_session_application_status: NotRequired[
        "capo_sso_admin.types.user_background_session_application_status.UserBackgroundSessionApplicationStatus"
    ]
    """<p>The status of user background sessions for the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutApplicationSessionConfigurationRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    if "user_background_session_application_status" in value:
        import capo_sso_admin.types.user_background_session_application_status

        out["UserBackgroundSessionApplicationStatus"] = (
            capo_sso_admin.types.user_background_session_application_status.serialize_aws_json_1_1(
                value["user_background_session_application_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutApplicationSessionConfigurationRequest:
    out: PutApplicationSessionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        out["application_arn"] = ""
    if data.get("UserBackgroundSessionApplicationStatus") is not None:
        import capo_sso_admin.types.user_background_session_application_status

        out["user_background_session_application_status"] = (
            capo_sso_admin.types.user_background_session_application_status.deserialize_aws_json_1_1(
                data["UserBackgroundSessionApplicationStatus"]
            )
        )
    return out
