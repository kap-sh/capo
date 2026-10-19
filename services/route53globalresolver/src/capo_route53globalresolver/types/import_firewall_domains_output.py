"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ImportFirewallDomainsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class ImportFirewallDomainsOutput(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the DNS Firewall domain list that you imported the domain list to.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>Name of the DNS Firewall domain list.</p>"""
    status: "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>Operational status of the DNS Firewall domain list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportFirewallDomainsOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_route53globalresolver.types.cr_resource_status

    out["status"] = capo_route53globalresolver.types.cr_resource_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> ImportFirewallDomainsOutput:
    out: ImportFirewallDomainsOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus", ""
        )
    return out
