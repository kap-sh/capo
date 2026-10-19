"""Generated from Smithy shape ``com.amazonaws.wickr#CreateSecurityGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.client_token
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id
    import capo_wickr.types.security_group_settings_request


class CreateSecurityGroupRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network where the security group will be created.</p>"""
    name: "capo_wickr.types.generic_string.GenericString"
    """<p>The name for the new security group.</p>"""
    security_group_settings: (
        "capo_wickr.types.security_group_settings_request.SecurityGroupSettingsRequest"
    )
    """<p>The configuration settings for the security group, including permissions, federation settings, and feature controls.</p>"""
    client_token: NotRequired["capo_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityGroupRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_wickr.types.security_group_settings_request

    out["securityGroupSettings"] = (
        capo_wickr.types.security_group_settings_request.serialize_json(
            value["security_group_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateSecurityGroupRequest:
    out: CreateSecurityGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("securityGroupSettings") is not None:
        import capo_wickr.types.security_group_settings_request

        out["security_group_settings"] = (
            capo_wickr.types.security_group_settings_request.deserialize_json(
                data["securityGroupSettings"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSecurityGroupRequest.security_group_settings required"
        )
    return out
