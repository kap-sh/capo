"""Generated from Smithy shape ``com.amazonaws.eksauth#Credentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class Credentials(TypedDict, closed=True):
    session_token: "str"
    """<p>The token that applications inside the pods must pass to any service API to use the temporary credentials.</p>"""
    secret_access_key: "str"
    """<p>The secret access key that applications inside the pods use to sign requests.</p>"""
    access_key_id: "str"
    """<p>The access key ID that identifies the temporary security credentials.</p>"""
    expiration: "datetime.datetime"
    """<p>The Unix epoch timestamp in seconds when the current credentials expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Credentials) -> dict:
    out: dict = {}
    out["sessionToken"] = value["session_token"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["accessKeyId"] = value["access_key_id"]
    import capo_eks_auth.types._prelude.timestamp

    out["expiration"] = capo_eks_auth.types._prelude.timestamp.serialize_json(
        value["expiration"]
    )
    return out


def deserialize_json(data: dict) -> Credentials:
    out: Credentials = {}  # type: ignore[typeddict-item]
    if data.get("sessionToken") is not None:
        out["session_token"] = data["sessionToken"]
    else:
        out["session_token"] = ""
    if data.get("secretAccessKey") is not None:
        out["secret_access_key"] = data["secretAccessKey"]
    else:
        out["secret_access_key"] = ""
    if data.get("accessKeyId") is not None:
        out["access_key_id"] = data["accessKeyId"]
    else:
        out["access_key_id"] = ""
    if data.get("expiration") is not None:
        import capo_eks_auth.types._prelude.timestamp

        out["expiration"] = capo_eks_auth.types._prelude.timestamp.deserialize_json(
            data["expiration"]
        )
    else:
        import datetime

        out["expiration"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
