"""Generated from Smithy shape ``com.amazonaws.iotevents#SSOIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.identity_store_id
    import capo_iot_events.types.sso_reference_id


class SSOIdentity(TypedDict, closed=True):
    identity_store_id: "capo_iot_events.types.identity_store_id.IdentityStoreId"
    """<p>The ID of the AWS SSO identity store.</p>"""
    user_id: NotRequired["capo_iot_events.types.sso_reference_id.SSOReferenceId"]
    """<p>The user ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SSOIdentity) -> dict:
    out: dict = {}
    out["identityStoreId"] = value["identity_store_id"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> SSOIdentity:
    out: SSOIdentity = {}  # type: ignore[typeddict-item]
    if data.get("identityStoreId") is not None:
        out["identity_store_id"] = data["identityStoreId"]
    else:
        out["identity_store_id"] = ""
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    return out
