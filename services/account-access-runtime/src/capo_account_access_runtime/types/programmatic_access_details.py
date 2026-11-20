"""Generated from Smithy shape ``com.amazonaws.accountaccessruntime#ProgrammaticAccessDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class ProgrammaticAccessDetails(TypedDict, closed=True):
    access_key_id: "str"
    """<p>The access key ID for the temporary credentials.</p>"""
    secret_access_key: "str"
    """<p>The secret access key for the temporary credentials. Treat this value as a secret.</p>"""
    session_token: "str"
    """<p>The session token that you must include along with the access key ID and secret access key when you make requests with the temporary credentials.</p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the temporary credentials expire, after which they can no longer be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProgrammaticAccessDetails) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["sessionToken"] = value["session_token"]
    if "expires_at" in value:
        import capo_account_access_runtime.types._prelude.timestamp

        out["expiresAt"] = (
            capo_account_access_runtime.types._prelude.timestamp.serialize_json(
                value["expires_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProgrammaticAccessDetails:
    out: ProgrammaticAccessDetails = {}  # type: ignore[typeddict-item]
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
    if data.get("expiresAt") is not None:
        import capo_account_access_runtime.types._prelude.timestamp

        out["expires_at"] = (
            capo_account_access_runtime.types._prelude.timestamp.deserialize_json(
                data["expiresAt"]
            )
        )
    return out
