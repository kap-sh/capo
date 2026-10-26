"""Generated from Smithy shape ``com.amazonaws.amp#UpdateScraperLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.scraper_components
    import capo_amp.types.scraper_id
    import capo_amp.types.scraper_logging_destination


class UpdateScraperLoggingConfigurationRequest(TypedDict, closed=True):
    scraper_id: "capo_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper whose logging configuration will be updated.</p>"""
    logging_destination: (
        "capo_amp.types.scraper_logging_destination.ScraperLoggingDestination"
    )
    """<p>The destination where scraper logs will be sent.</p>"""
    scraper_components: NotRequired[
        "capo_amp.types.scraper_components.ScraperComponents"
    ]
    """<p>The list of scraper components to configure for logging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScraperLoggingConfigurationRequest) -> dict:
    out: dict = {}
    import capo_amp.types.scraper_logging_destination

    out["loggingDestination"] = (
        capo_amp.types.scraper_logging_destination.serialize_json(
            value["logging_destination"]
        )
    )
    if "scraper_components" in value:
        import capo_amp.types.scraper_components

        out["scraperComponents"] = capo_amp.types.scraper_components.serialize_json(
            value["scraper_components"]
        )
    return out


def deserialize_json(data: dict) -> UpdateScraperLoggingConfigurationRequest:
    out: UpdateScraperLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("loggingDestination") is not None:
        import capo_amp.types.scraper_logging_destination

        out["logging_destination"] = (
            capo_amp.types.scraper_logging_destination.deserialize_json(
                data["loggingDestination"]
            )
        )
    else:
        out["logging_destination"] = {"$unknown": {"name": ""}}
    if data.get("scraperComponents") is not None:
        import capo_amp.types.scraper_components

        out["scraper_components"] = capo_amp.types.scraper_components.deserialize_json(
            data["scraperComponents"]
        )
    return out
