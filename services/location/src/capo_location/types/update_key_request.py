"""Generated from Smithy shape ``com.amazonaws.location#UpdateKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.api_key_restrictions
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class UpdateKeyRequest(TypedDict, closed=True):
    key_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the API key resource to update.</p>"""
    description: NotRequired[
        "capo_location.types.resource_description.ResourceDescription"
    ]
    """<p>Updates the description for the API key resource.</p>"""
    expire_time: NotRequired["capo_location.types.timestamp.Timestamp"]
    """<p>Updates the timestamp for when the API key resource will expire in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    no_expiry: NotRequired["bool"]
    """<p>Whether the API key should expire. Set to <code>true</code> to set the API key to have no expiration time.</p>"""
    force_update: NotRequired["bool"]
    """<p>The boolean flag to be included for updating <code>ExpireTime</code> or <code>Restrictions</code> details.</p> <p>Must be set to <code>true</code> to update an API key resource that has been used in the past 7 days.</p> <p> <code>False</code> if force update is not preferred</p> <p>Default value: <code>False</code> </p>"""
    restrictions: NotRequired[
        "capo_location.types.api_key_restrictions.ApiKeyRestrictions"
    ]
    """<p>Updates the API key restrictions for the API key resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKeyRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "expire_time" in value:
        import capo_location.types.timestamp

        out["ExpireTime"] = capo_location.types.timestamp.serialize_json(
            value["expire_time"]
        )
    if "no_expiry" in value:
        out["NoExpiry"] = value["no_expiry"]
    if "force_update" in value:
        out["ForceUpdate"] = value["force_update"]
    if "restrictions" in value:
        import capo_location.types.api_key_restrictions

        out["Restrictions"] = capo_location.types.api_key_restrictions.serialize_json(
            value["restrictions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateKeyRequest:
    out: UpdateKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ExpireTime") is not None:
        import capo_location.types.timestamp

        out["expire_time"] = capo_location.types.timestamp.deserialize_json(
            data["ExpireTime"]
        )
    if data.get("NoExpiry") is not None:
        out["no_expiry"] = data["NoExpiry"]
    if data.get("ForceUpdate") is not None:
        out["force_update"] = data["ForceUpdate"]
    if data.get("Restrictions") is not None:
        import capo_location.types.api_key_restrictions

        out["restrictions"] = capo_location.types.api_key_restrictions.deserialize_json(
            data["Restrictions"]
        )
    return out
