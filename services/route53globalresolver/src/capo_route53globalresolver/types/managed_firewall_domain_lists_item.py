"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ManagedFirewallDomainListsItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class ManagedFirewallDomainListsItem(TypedDict, closed=True):
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>A description of the managed firewall domain list.</p>"""
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the managed firewall domain list.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the managed firewall domain list.</p>"""
    managed_list_type: "str"
    """<p>The type of the managed firewall domain list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedFirewallDomainListsItem) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["managedListType"] = value["managed_list_type"]
    return out


def deserialize_json(data: dict) -> ManagedFirewallDomainListsItem:
    out: ManagedFirewallDomainListsItem = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("managedListType") is not None:
        out["managed_list_type"] = data["managedListType"]
    else:
        out["managed_list_type"] = ""
    return out
