"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateTenantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.tag_list
    import capo_sesv2.types.tenant_name
    import capo_sesv2.types.tenant_suppression_attributes


class CreateTenantRequest(TypedDict, closed=True):
    tenant_name: "capo_sesv2.types.tenant_name.TenantName"
    """<p>The name of the tenant to create. The name can contain up to 64 alphanumeric characters, including letters, numbers, hyphens (-) and underscores (_) only.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) to associate with the tenant</p>"""
    suppression_attributes: NotRequired[
        "capo_sesv2.types.tenant_suppression_attributes.TenantSuppressionAttributes"
    ]
    """<p>An object that contains information about the suppression list preferences for the tenant. Use this to configure tenant-level suppression at creation time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTenantRequest) -> dict:
    out: dict = {}
    out["TenantName"] = value["tenant_name"]
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    if "suppression_attributes" in value:
        import capo_sesv2.types.tenant_suppression_attributes

        out["SuppressionAttributes"] = (
            capo_sesv2.types.tenant_suppression_attributes.serialize_json(
                value["suppression_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTenantRequest:
    out: CreateTenantRequest = {}  # type: ignore[typeddict-item]
    if data.get("TenantName") is not None:
        out["tenant_name"] = data["TenantName"]
    else:
        out["tenant_name"] = ""
    if data.get("Tags") is not None:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if data.get("SuppressionAttributes") is not None:
        import capo_sesv2.types.tenant_suppression_attributes

        out["suppression_attributes"] = (
            capo_sesv2.types.tenant_suppression_attributes.deserialize_json(
                data["SuppressionAttributes"]
            )
        )
    return out
