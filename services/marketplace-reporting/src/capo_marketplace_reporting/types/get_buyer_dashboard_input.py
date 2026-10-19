"""Generated from Smithy shape ``com.amazonaws.marketplacereporting#GetBuyerDashboardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_reporting.types.dashboard_identifier
    import capo_marketplace_reporting.types.embedding_domains


class GetBuyerDashboardInput(TypedDict, closed=True):
    dashboard_identifier: (
        "capo_marketplace_reporting.types.dashboard_identifier.DashboardIdentifier"
    )
    """<p>The ARN of the requested dashboard.</p>"""
    embedding_domains: (
        "capo_marketplace_reporting.types.embedding_domains.EmbeddingDomains"
    )
    """<p>Fully qualified domains that you add to the allow list for access to the generated URL that is then embedded. You can list up to two domains or subdomains in each API call. To include all subdomains under a specific domain, use <code>*</code>. For example, <code>https://*.amazon.com</code> includes all subdomains under <code>https://aws.amazon.com</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBuyerDashboardInput) -> dict:
    out: dict = {}
    out["dashboardIdentifier"] = value["dashboard_identifier"]
    import capo_marketplace_reporting.types.embedding_domains

    out["embeddingDomains"] = (
        capo_marketplace_reporting.types.embedding_domains.serialize_json(
            value["embedding_domains"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetBuyerDashboardInput:
    out: GetBuyerDashboardInput = {}  # type: ignore[typeddict-item]
    if data.get("dashboardIdentifier") is not None:
        out["dashboard_identifier"] = data["dashboardIdentifier"]
    else:
        out["dashboard_identifier"] = ""
    if data.get("embeddingDomains") is not None:
        import capo_marketplace_reporting.types.embedding_domains

        out["embedding_domains"] = (
            capo_marketplace_reporting.types.embedding_domains.deserialize_json(
                data["embeddingDomains"]
            )
        )
    else:
        out["embedding_domains"] = []
    return out
