"""Generated from Smithy shape ``com.amazonaws.connect#ListSecurityProfilePermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.permissions_list
    import capo_connect.types.region_name
    import capo_connect.types.timestamp


class ListSecurityProfilePermissionsResponse(TypedDict, closed=True):
    permissions: NotRequired["capo_connect.types.permissions_list.PermissionsList"]
    """<p>The permissions granted to the security profile. For a complete list of valid permissions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html">List of security profile permissions</a>.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfilePermissionsResponse) -> dict:
    out: dict = {}
    if "permissions" in value:
        import capo_connect.types.permissions_list

        out["Permissions"] = capo_connect.types.permissions_list.serialize_json(
            value["permissions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> ListSecurityProfilePermissionsResponse:
    out: ListSecurityProfilePermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Permissions") is not None:
        import capo_connect.types.permissions_list

        out["permissions"] = capo_connect.types.permissions_list.deserialize_json(
            data["Permissions"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
