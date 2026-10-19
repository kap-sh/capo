"""Generated from Smithy shape ``com.amazonaws.quicksight#KeyPairCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.db_username
    import capo_quicksight.types.private_key
    import capo_quicksight.types.private_key_passphrase


class KeyPairCredentials(TypedDict, closed=True):
    key_pair_username: "capo_quicksight.types.db_username.DbUsername"
    """<p>Username</p>"""
    private_key: "capo_quicksight.types.private_key.PrivateKey"
    """<p>PrivateKey</p>"""
    private_key_passphrase: NotRequired[
        "capo_quicksight.types.private_key_passphrase.PrivateKeyPassphrase"
    ]
    """<p>PrivateKeyPassphrase</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyPairCredentials) -> dict:
    out: dict = {}
    out["KeyPairUsername"] = value["key_pair_username"]
    out["PrivateKey"] = value["private_key"]
    if "private_key_passphrase" in value:
        out["PrivateKeyPassphrase"] = value["private_key_passphrase"]
    return out


def deserialize_json(data: dict) -> KeyPairCredentials:
    out: KeyPairCredentials = {}  # type: ignore[typeddict-item]
    if data.get("KeyPairUsername") is not None:
        out["key_pair_username"] = data["KeyPairUsername"]
    else:
        out["key_pair_username"] = ""
    if data.get("PrivateKey") is not None:
        out["private_key"] = data["PrivateKey"]
    else:
        out["private_key"] = ""
    if data.get("PrivateKeyPassphrase") is not None:
        out["private_key_passphrase"] = data["PrivateKeyPassphrase"]
    return out


def redact_sensitive(value: KeyPairCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "private_key" in value:
        out["private_key"] = "*** Sensitive Data Redacted ***"
    if "private_key_passphrase" in value:
        out["private_key_passphrase"] = "*** Sensitive Data Redacted ***"
    return out
