"""Generated from Smithy shape ``com.amazonaws.codepipeline#AWSSessionCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.access_key_id
    import capo_codepipeline.types.secret_access_key
    import capo_codepipeline.types.session_token


class AWSSessionCredentials(TypedDict, closed=True):
    access_key_id: "capo_codepipeline.types.access_key_id.AccessKeyId"
    """<p>The access key for the session.</p>"""
    secret_access_key: "capo_codepipeline.types.secret_access_key.SecretAccessKey"
    """<p>The secret access key for the session.</p>"""
    session_token: "capo_codepipeline.types.session_token.SessionToken"
    """<p>The token for the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AWSSessionCredentials) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["sessionToken"] = value["session_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AWSSessionCredentials:
    out: AWSSessionCredentials = {}  # type: ignore[typeddict-item]
    if data.get("accessKeyId") is not None:
        out["access_key_id"] = data["accessKeyId"]
    else:
        out["access_key_id"] = ""
    if data.get("secretAccessKey") is not None:
        out["secret_access_key"] = data["secretAccessKey"]
    else:
        out["secret_access_key"] = ""
    if data.get("sessionToken") is not None:
        out["session_token"] = data["sessionToken"]
    else:
        out["session_token"] = ""
    return out
