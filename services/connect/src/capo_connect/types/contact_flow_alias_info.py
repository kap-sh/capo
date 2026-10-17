"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowAliasInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.contact_flow_description
    import capo_connect.types.contact_flow_name
    import capo_connect.types.region_name
    import capo_connect.types.resource_id
    import capo_connect.types.resource_version
    import capo_connect.types.timestamp


class ContactFlowAliasInfo(TypedDict, closed=True):
    contact_flow_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The identifier of the flow.</p>"""
    contact_flow_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    alias_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The identifier of the alias.</p>"""
    version: NotRequired["capo_connect.types.resource_version.ResourceVersion"]
    """<p>The version of the flow.</p>"""
    name: NotRequired["capo_connect.types.contact_flow_name.ContactFlowName"]
    """<p>The name of the alias.</p>"""
    description: NotRequired[
        "capo_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the alias.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowAliasInfo) -> dict:
    out: dict = {}
    if "contact_flow_id" in value:
        out["ContactFlowId"] = value["contact_flow_id"]
    if "contact_flow_arn" in value:
        out["ContactFlowArn"] = value["contact_flow_arn"]
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "version" in value:
        out["Version"] = value["version"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> ContactFlowAliasInfo:
    out: ContactFlowAliasInfo = {}  # type: ignore[typeddict-item]
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    if data.get("ContactFlowArn") is not None:
        out["contact_flow_arn"] = data["ContactFlowArn"]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    return out
