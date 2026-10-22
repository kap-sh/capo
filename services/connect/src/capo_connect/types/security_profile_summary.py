"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.region_name
    import capo_connect.types.security_profile_id
    import capo_connect.types.security_profile_name
    import capo_connect.types.security_profile_type
    import capo_connect.types.timestamp


class SecurityProfileSummary(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.security_profile_id.SecurityProfileId"]
    """<p>The identifier of the security profile.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the security profile.</p>"""
    name: NotRequired["capo_connect.types.security_profile_name.SecurityProfileName"]
    """<p>The name of the security profile.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""
    type: NotRequired["capo_connect.types.security_profile_type.SecurityProfileType"]
    """<p>The type of the security profile: <code>AWS_MANAGED</code> or <code>CUSTOMER_MANAGED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "type" in value:
        import capo_connect.types.security_profile_type

        out["Type"] = capo_connect.types.security_profile_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> SecurityProfileSummary:
    out: SecurityProfileSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if data.get("Type") is not None:
        import capo_connect.types.security_profile_type

        out["type"] = capo_connect.types.security_profile_type.deserialize_json(
            data["Type"]
        )
    return out
