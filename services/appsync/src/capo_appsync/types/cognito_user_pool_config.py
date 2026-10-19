"""Generated from Smithy shape ``com.amazonaws.appsync#CognitoUserPoolConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.string


class CognitoUserPoolConfig(TypedDict, closed=True):
    user_pool_id: "capo_appsync.types.string.String"
    """<p>The user pool ID.</p>"""
    aws_region: "capo_appsync.types.string.String"
    """<p>The Amazon Web Services Region in which the user pool was created.</p>"""
    app_id_client_regex: NotRequired["capo_appsync.types.string.String"]
    """<p>A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isn't set, no filtering is applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CognitoUserPoolConfig) -> dict:
    out: dict = {}
    out["userPoolId"] = value["user_pool_id"]
    out["awsRegion"] = value["aws_region"]
    if "app_id_client_regex" in value:
        out["appIdClientRegex"] = value["app_id_client_regex"]
    return out


def deserialize_json(data: dict) -> CognitoUserPoolConfig:
    out: CognitoUserPoolConfig = {}  # type: ignore[typeddict-item]
    if data.get("userPoolId") is not None:
        out["user_pool_id"] = data["userPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("awsRegion") is not None:
        out["aws_region"] = data["awsRegion"]
    else:
        out["aws_region"] = ""
    if data.get("appIdClientRegex") is not None:
        out["app_id_client_regex"] = data["appIdClientRegex"]
    return out
