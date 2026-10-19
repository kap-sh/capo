"""Generated from Smithy shape ``com.amazonaws.opensearch#KeyStoreAccessOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.role_arn


class KeyStoreAccessOption(TypedDict, closed=True):
    key_access_role_arn: NotRequired["capo_opensearch.types.role_arn.RoleArn"]
    """<p>Role ARN to access the KeyStore Key</p>"""
    key_store_access_enabled: "capo_opensearch.types.boolean.Boolean"
    """<p>This indicates whether Key Store access is enabled </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyStoreAccessOption) -> dict:
    out: dict = {}
    if "key_access_role_arn" in value:
        out["KeyAccessRoleArn"] = value["key_access_role_arn"]
    out["KeyStoreAccessEnabled"] = value["key_store_access_enabled"]
    return out


def deserialize_json(data: dict) -> KeyStoreAccessOption:
    out: KeyStoreAccessOption = {}  # type: ignore[typeddict-item]
    if data.get("KeyAccessRoleArn") is not None:
        out["key_access_role_arn"] = data["KeyAccessRoleArn"]
    if data.get("KeyStoreAccessEnabled") is not None:
        out["key_store_access_enabled"] = data["KeyStoreAccessEnabled"]
    else:
        out["key_store_access_enabled"] = False
    return out
