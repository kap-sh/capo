"""Generated from Smithy shape ``com.amazonaws.wickr#SecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.security_group_settings


class SecurityGroup(TypedDict, closed=True):
    active_members: "int"
    """<p>The number of active user members currently in the security group.</p>"""
    bot_members: "int"
    """<p>The number of bot members currently in the security group.</p>"""
    active_directory_guid: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The GUID of the Active Directory group associated with this security group, if synchronized with LDAP.</p>"""
    id: "capo_wickr.types.generic_string.GenericString"
    """<p>The unique identifier of the security group.</p>"""
    is_default: "bool"
    """<p>Indicates whether this is the default security group for the network. Each network has only one default group.</p>"""
    name: "capo_wickr.types.generic_string.GenericString"
    """<p>The human-readable name of the security group.</p>"""
    modified: "int"
    """<p>The timestamp when the security group was last modified, specified in epoch seconds.</p>"""
    security_group_settings: (
        "capo_wickr.types.security_group_settings.SecurityGroupSettings"
    )
    """<p>The comprehensive configuration settings that define capabilities and restrictions for members of this security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroup) -> dict:
    out: dict = {}
    out["activeMembers"] = value["active_members"]
    out["botMembers"] = value["bot_members"]
    if "active_directory_guid" in value:
        out["activeDirectoryGuid"] = value["active_directory_guid"]
    out["id"] = value["id"]
    out["isDefault"] = value["is_default"]
    out["name"] = value["name"]
    out["modified"] = value["modified"]
    import capo_wickr.types.security_group_settings

    out["securityGroupSettings"] = (
        capo_wickr.types.security_group_settings.serialize_json(
            value["security_group_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> SecurityGroup:
    out: SecurityGroup = {}  # type: ignore[typeddict-item]
    if data.get("activeMembers") is not None:
        out["active_members"] = data["activeMembers"]
    else:
        out["active_members"] = 0
    if data.get("botMembers") is not None:
        out["bot_members"] = data["botMembers"]
    else:
        out["bot_members"] = 0
    if data.get("activeDirectoryGuid") is not None:
        out["active_directory_guid"] = data["activeDirectoryGuid"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("isDefault") is not None:
        out["is_default"] = data["isDefault"]
    else:
        out["is_default"] = False
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("modified") is not None:
        out["modified"] = data["modified"]
    else:
        out["modified"] = 0
    if data.get("securityGroupSettings") is not None:
        import capo_wickr.types.security_group_settings

        out["security_group_settings"] = (
            capo_wickr.types.security_group_settings.deserialize_json(
                data["securityGroupSettings"]
            )
        )
    else:
        raise DeserializationError("SecurityGroup.security_group_settings required")
    return out
