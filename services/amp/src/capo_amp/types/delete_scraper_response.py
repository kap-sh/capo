"""Generated from Smithy shape ``com.amazonaws.amp#DeleteScraperResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.scraper_id
    import capo_amp.types.scraper_status


class DeleteScraperResponse(TypedDict, closed=True):
    scraper_id: "capo_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper to delete.</p>"""
    status: "capo_amp.types.scraper_status.ScraperStatus"
    """<p>The current status of the scraper.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScraperResponse) -> dict:
    out: dict = {}
    out["scraperId"] = value["scraper_id"]
    import capo_amp.types.scraper_status

    out["status"] = capo_amp.types.scraper_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteScraperResponse:
    out: DeleteScraperResponse = {}  # type: ignore[typeddict-item]
    if data.get("scraperId") is not None:
        out["scraper_id"] = data["scraperId"]
    else:
        out["scraper_id"] = ""
    if data.get("status") is not None:
        import capo_amp.types.scraper_status

        out["status"] = capo_amp.types.scraper_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("DeleteScraperResponse.status required")
    return out
