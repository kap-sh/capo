"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowAliasSummary``."""

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


class ContactFlowAliasSummary(TypedDict, closed=True):
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow alias.</p>"""
    alias_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The identifier of the alias.</p>"""
    version: NotRequired["capo_connect.types.resource_version.ResourceVersion"]
    """<p>The version of the flow.</p>"""
    alias_name: NotRequired["capo_connect.types.contact_flow_name.ContactFlowName"]
    """<p>The name of the alias.</p>"""
    alias_description: NotRequired[
        "capo_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the alias.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowAliasSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "version" in value:
        out["Version"] = value["version"]
    if "alias_name" in value:
        out["AliasName"] = value["alias_name"]
    if "alias_description" in value:
        out["AliasDescription"] = value["alias_description"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> ContactFlowAliasSummary:
    out: ContactFlowAliasSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("AliasName") is not None:
        out["alias_name"] = data["AliasName"]
    if data.get("AliasDescription") is not None:
        out["alias_description"] = data["AliasDescription"]
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
