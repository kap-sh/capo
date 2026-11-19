"""Generated from Smithy shape ``com.amazonaws.mwaa#IdentityCenterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.identity_center_identity_store_id
    import capo_mwaa.types.identity_center_start_url


class IdentityCenterConfiguration(TypedDict, closed=True):
    start_url: NotRequired[
        "capo_mwaa.types.identity_center_start_url.IdentityCenterStartUrl"
    ]
    """<p>The Amazon Web Services access portal URL of the IAM Identity Center instance associated with your environment. For example, <code>https://my-portal.awsapps.com/start</code>.</p>"""
    identity_store_id: NotRequired[
        "capo_mwaa.types.identity_center_identity_store_id.IdentityCenterIdentityStoreId"
    ]
    """<p>The identifier of the identity store associated with the IAM Identity Center instance for your environment. For example, <code>d-1234567890</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCenterConfiguration) -> dict:
    out: dict = {}
    if "start_url" in value:
        out["StartUrl"] = value["start_url"]
    if "identity_store_id" in value:
        out["IdentityStoreId"] = value["identity_store_id"]
    return out


def deserialize_json(data: dict) -> IdentityCenterConfiguration:
    out: IdentityCenterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StartUrl") is not None:
        out["start_url"] = data["StartUrl"]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    return out
