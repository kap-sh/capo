"""Generated from Smithy shape ``com.amazonaws.inspector2#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.provider
    import capo_inspector2.types.provider_account_id
    import capo_inspector2.types.provider_org_id
    import capo_inspector2.types.resource_details
    import capo_inspector2.types.resource_type
    import capo_inspector2.types.tag_map


class Resource(TypedDict, closed=True):
    type: "capo_inspector2.types.resource_type.ResourceType"
    """<p>The type of resource.</p>"""
    id: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The ID of the resource.</p>"""
    partition: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The partition of the resource.</p>"""
    region: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services Region the impacted resource is located in.</p>"""
    tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags attached to the resource.</p>"""
    details: NotRequired["capo_inspector2.types.resource_details.ResourceDetails"]
    """<p>An object that contains details about the resource involved in a finding.</p>"""
    provider: NotRequired["capo_inspector2.types.provider.Provider"]
    """<p>The cloud provider of the resource.</p>"""
    provider_account_id: NotRequired[
        "capo_inspector2.types.provider_account_id.ProviderAccountId"
    ]
    """<p>The cloud provider account ID of the resource.</p>"""
    provider_org_id: NotRequired["capo_inspector2.types.provider_org_id.ProviderOrgId"]
    """<p>The cloud provider organization ID of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["id"] = value["id"]
    if "partition" in value:
        out["partition"] = value["partition"]
    if "region" in value:
        out["region"] = value["region"]
    if "tags" in value:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.serialize_json(value["tags"])
    if "details" in value:
        import capo_inspector2.types.resource_details

        out["details"] = capo_inspector2.types.resource_details.serialize_json(
            value["details"]
        )
    if "provider" in value:
        out["provider"] = value["provider"]
    if "provider_account_id" in value:
        out["providerAccountId"] = value["provider_account_id"]
    if "provider_org_id" in value:
        out["providerOrgId"] = value["provider_org_id"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("partition") is not None:
        out["partition"] = data["partition"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("tags") is not None:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.deserialize_json(data["tags"])
    if data.get("details") is not None:
        import capo_inspector2.types.resource_details

        out["details"] = capo_inspector2.types.resource_details.deserialize_json(
            data["details"]
        )
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    if data.get("providerAccountId") is not None:
        out["provider_account_id"] = data["providerAccountId"]
    if data.get("providerOrgId") is not None:
        out["provider_org_id"] = data["providerOrgId"]
    return out
