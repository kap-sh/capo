"""Generated from Smithy shape ``com.amazonaws.sso#RoleCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso.types.access_key_type
    import capo_sso.types.expiration_timestamp_type
    import capo_sso.types.secret_access_key_type
    import capo_sso.types.session_token_type


class RoleCredentials(TypedDict, closed=True):
    access_key_id: NotRequired["capo_sso.types.access_key_type.AccessKeyType"]
    """<p>The identifier used for the temporary security credentials. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html">Using Temporary Security Credentials to Request Access to AWS Resources</a> in the <i>AWS IAM User Guide</i>.</p>"""
    secret_access_key: NotRequired[
        "capo_sso.types.secret_access_key_type.SecretAccessKeyType"
    ]
    """<p>The key that is used to sign the request. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html">Using Temporary Security Credentials to Request Access to AWS Resources</a> in the <i>AWS IAM User Guide</i>.</p>"""
    session_token: NotRequired["capo_sso.types.session_token_type.SessionTokenType"]
    """<p>The token used for temporary credentials. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html">Using Temporary Security Credentials to Request Access to AWS Resources</a> in the <i>AWS IAM User Guide</i>.</p>"""
    expiration: "capo_sso.types.expiration_timestamp_type.ExpirationTimestampType"
    """<p>The date on which temporary security credentials expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoleCredentials) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["accessKeyId"] = value["access_key_id"]
    if "secret_access_key" in value:
        out["secretAccessKey"] = value["secret_access_key"]
    if "session_token" in value:
        out["sessionToken"] = value["session_token"]
    out["expiration"] = value.get("expiration", 0)
    return out


def deserialize_json(data: dict) -> RoleCredentials:
    out: RoleCredentials = {}  # type: ignore[typeddict-item]
    if data.get("accessKeyId") is not None:
        out["access_key_id"] = data["accessKeyId"]
    if data.get("secretAccessKey") is not None:
        out["secret_access_key"] = data["secretAccessKey"]
    if data.get("sessionToken") is not None:
        out["session_token"] = data["sessionToken"]
    if data.get("expiration") is not None:
        out["expiration"] = data["expiration"]
    else:
        out["expiration"] = 0
    return out
