"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetTemporaryGlueFunctionCredentialsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.access_key_id_string
    import capo_lakeformation.types.expiration_timestamp
    import capo_lakeformation.types.secret_access_key_string
    import capo_lakeformation.types.session_token_string


class GetTemporaryGlueFunctionCredentialsResponse(TypedDict, closed=True):
    access_key_id: NotRequired[
        "capo_lakeformation.types.access_key_id_string.AccessKeyIdString"
    ]
    """<p>The access key ID for the temporary credentials.</p>"""
    secret_access_key: NotRequired[
        "capo_lakeformation.types.secret_access_key_string.SecretAccessKeyString"
    ]
    """<p>The secret key for the temporary credentials.</p>"""
    session_token: NotRequired[
        "capo_lakeformation.types.session_token_string.SessionTokenString"
    ]
    """<p>The session token for the temporary credentials.</p>"""
    expiration: NotRequired[
        "capo_lakeformation.types.expiration_timestamp.ExpirationTimestamp"
    ]
    """<p>The date and time when the temporary credentials expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemporaryGlueFunctionCredentialsResponse) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["AccessKeyId"] = value["access_key_id"]
    if "secret_access_key" in value:
        out["SecretAccessKey"] = value["secret_access_key"]
    if "session_token" in value:
        out["SessionToken"] = value["session_token"]
    if "expiration" in value:
        import capo_lakeformation.types.expiration_timestamp

        out["Expiration"] = (
            capo_lakeformation.types.expiration_timestamp.serialize_json(
                value["expiration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTemporaryGlueFunctionCredentialsResponse:
    out: GetTemporaryGlueFunctionCredentialsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AccessKeyId") is not None:
        out["access_key_id"] = data["AccessKeyId"]
    if data.get("SecretAccessKey") is not None:
        out["secret_access_key"] = data["SecretAccessKey"]
    if data.get("SessionToken") is not None:
        out["session_token"] = data["SessionToken"]
    if data.get("Expiration") is not None:
        import capo_lakeformation.types.expiration_timestamp

        out["expiration"] = (
            capo_lakeformation.types.expiration_timestamp.deserialize_json(
                data["Expiration"]
            )
        )
    return out
