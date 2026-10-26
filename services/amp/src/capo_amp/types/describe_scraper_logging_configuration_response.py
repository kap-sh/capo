"""Generated from Smithy shape ``com.amazonaws.amp#DescribeScraperLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amp.types.scraper_components
    import capo_amp.types.scraper_id
    import capo_amp.types.scraper_logging_configuration_status
    import capo_amp.types.scraper_logging_destination


class DescribeScraperLoggingConfigurationResponse(TypedDict, closed=True):
    status: "capo_amp.types.scraper_logging_configuration_status.ScraperLoggingConfigurationStatus"
    """<p>The status of the scraper logging configuration.</p>"""
    scraper_id: "capo_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper.</p>"""
    logging_destination: (
        "capo_amp.types.scraper_logging_destination.ScraperLoggingDestination"
    )
    """<p>The destination where scraper logs are sent.</p>"""
    scraper_components: "capo_amp.types.scraper_components.ScraperComponents"
    """<p>The list of scraper components configured for logging.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time when the logging configuration was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeScraperLoggingConfigurationResponse) -> dict:
    out: dict = {}
    import capo_amp.types.scraper_logging_configuration_status

    out["status"] = capo_amp.types.scraper_logging_configuration_status.serialize_json(
        value["status"]
    )
    out["scraperId"] = value["scraper_id"]
    import capo_amp.types.scraper_logging_destination

    out["loggingDestination"] = (
        capo_amp.types.scraper_logging_destination.serialize_json(
            value["logging_destination"]
        )
    )
    import capo_amp.types.scraper_components

    out["scraperComponents"] = capo_amp.types.scraper_components.serialize_json(
        value["scraper_components"]
    )
    import capo_amp.types._prelude.timestamp

    out["modifiedAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    return out


def deserialize_json(data: dict) -> DescribeScraperLoggingConfigurationResponse:
    out: DescribeScraperLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_amp.types.scraper_logging_configuration_status

        out["status"] = (
            capo_amp.types.scraper_logging_configuration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeScraperLoggingConfigurationResponse.status required"
        )
    if data.get("scraperId") is not None:
        out["scraper_id"] = data["scraperId"]
    else:
        out["scraper_id"] = ""
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
    else:
        out["scraper_components"] = []
    if data.get("modifiedAt") is not None:
        import capo_amp.types._prelude.timestamp

        out["modified_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        import datetime

        out["modified_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
