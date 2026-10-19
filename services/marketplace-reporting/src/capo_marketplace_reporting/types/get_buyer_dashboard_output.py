"""Generated from Smithy shape ``com.amazonaws.marketplacereporting#GetBuyerDashboardOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_reporting.types.dashboard_identifier
    import capo_marketplace_reporting.types.embedding_domains


class GetBuyerDashboardOutput(TypedDict, closed=True):
    embed_url: "str"
    """<p>The dashboard's embedding URL.</p>"""
    dashboard_identifier: (
        "capo_marketplace_reporting.types.dashboard_identifier.DashboardIdentifier"
    )
    """<p>The ARN of the returned dashboard.</p>"""
    embedding_domains: (
        "capo_marketplace_reporting.types.embedding_domains.EmbeddingDomains"
    )
    """<p>The fully qualified domains specified in the request. The domains enable access to the generated URL that is then embedded. You can list up to two domains or subdomains in each API call. To include all subdomains under a specific domain, use <code>*</code>. For example, <code>https://*.amazon.com</code> includes all subdomains under <code>https://aws.amazon.com</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBuyerDashboardOutput) -> dict:
    out: dict = {}
    out["embedUrl"] = value["embed_url"]
    out["dashboardIdentifier"] = value["dashboard_identifier"]
    import capo_marketplace_reporting.types.embedding_domains

    out["embeddingDomains"] = (
        capo_marketplace_reporting.types.embedding_domains.serialize_json(
            value["embedding_domains"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetBuyerDashboardOutput:
    out: GetBuyerDashboardOutput = {}  # type: ignore[typeddict-item]
    if data.get("embedUrl") is not None:
        out["embed_url"] = data["embedUrl"]
    else:
        out["embed_url"] = ""
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
