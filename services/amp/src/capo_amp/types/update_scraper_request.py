"""Generated from Smithy shape ``com.amazonaws.amp#UpdateScraperRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.destination
    import capo_amp.types.exporter_list
    import capo_amp.types.idempotency_token
    import capo_amp.types.role_configuration
    import capo_amp.types.scrape_configuration
    import capo_amp.types.scraper_alias
    import capo_amp.types.scraper_id


class UpdateScraperRequest(TypedDict, closed=True):
    scraper_id: "capo_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper to update.</p>"""
    alias: NotRequired["capo_amp.types.scraper_alias.ScraperAlias"]
    """<p>The new alias of the scraper.</p>"""
    scrape_configuration: NotRequired[
        "capo_amp.types.scrape_configuration.ScrapeConfiguration"
    ]
    """<p>Contains the base-64 encoded YAML configuration for the scraper.</p> <note> <p>For more information about configuring a scraper, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html">Using an Amazon Web Services managed collector</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p> </note>"""
    destination: NotRequired["capo_amp.types.destination.Destination"]
    """<p>The new destination where the scraper sends metrics. Valid destinations are Amazon Managed Service for Prometheus workspaces and CloudWatch datasets.</p>"""
    role_configuration: NotRequired[
        "capo_amp.types.role_configuration.RoleConfiguration"
    ]
    """<p>Use this structure to enable cross-account access, so that you can use a target account to access Prometheus metrics from source accounts.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""
    exporters: NotRequired["capo_amp.types.exporter_list.ExporterList"]
    """<p>The exporter configurations for the scraper. You can configure at most one Amazon OpenSearch Service domain. If you don't specify a value, the existing exporter configuration remains unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScraperRequest) -> dict:
    out: dict = {}
    if "alias" in value:
        out["alias"] = value["alias"]
    if "scrape_configuration" in value:
        import capo_amp.types.scrape_configuration

        out["scrapeConfiguration"] = capo_amp.types.scrape_configuration.serialize_json(
            value["scrape_configuration"]
        )
    if "destination" in value:
        import capo_amp.types.destination

        out["destination"] = capo_amp.types.destination.serialize_json(
            value["destination"]
        )
    if "role_configuration" in value:
        import capo_amp.types.role_configuration

        out["roleConfiguration"] = capo_amp.types.role_configuration.serialize_json(
            value["role_configuration"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "exporters" in value:
        import capo_amp.types.exporter_list

        out["exporters"] = capo_amp.types.exporter_list.serialize_json(
            value["exporters"]
        )
    return out


def deserialize_json(data: dict) -> UpdateScraperRequest:
    out: UpdateScraperRequest = {}  # type: ignore[typeddict-item]
    if data.get("alias") is not None:
        out["alias"] = data["alias"]
    if data.get("scrapeConfiguration") is not None:
        import capo_amp.types.scrape_configuration

        out["scrape_configuration"] = (
            capo_amp.types.scrape_configuration.deserialize_json(
                data["scrapeConfiguration"]
            )
        )
    if data.get("destination") is not None:
        import capo_amp.types.destination

        out["destination"] = capo_amp.types.destination.deserialize_json(
            data["destination"]
        )
    if data.get("roleConfiguration") is not None:
        import capo_amp.types.role_configuration

        out["role_configuration"] = capo_amp.types.role_configuration.deserialize_json(
            data["roleConfiguration"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("exporters") is not None:
        import capo_amp.types.exporter_list

        out["exporters"] = capo_amp.types.exporter_list.deserialize_json(
            data["exporters"]
        )
    return out
