"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchDeleteFirewallRuleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class BatchDeleteFirewallRuleResult(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>The unique string that identified the request and ensured idempotency.</p>"""
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the deleted firewall rule.</p>"""
    name: NotRequired["capo_route53globalresolver.types.resource_name.ResourceName"]
    """<p>The name of the deleted firewall rule.</p>"""
    status: NotRequired[
        "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    ]
    """<p>The final status of the deleted firewall rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteFirewallRuleResult) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteFirewallRuleResult:
    out: BatchDeleteFirewallRuleResult = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    return out
