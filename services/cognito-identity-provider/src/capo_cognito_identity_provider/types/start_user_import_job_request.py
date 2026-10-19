"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#StartUserImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_import_job_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class StartUserImportJobRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that you want to start importing users into.</p>"""
    job_id: "capo_cognito_identity_provider.types.user_import_job_id_type.UserImportJobIdType"
    """<p>The ID of a user import job that you previously created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartUserImportJobRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartUserImportJobRequest:
    out: StartUserImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
