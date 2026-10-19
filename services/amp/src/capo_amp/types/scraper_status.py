"""Generated from Smithy shape ``com.amazonaws.amp#ScraperStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.scraper_status_code


class ScraperStatus(TypedDict, closed=True):
    status_code: "capo_amp.types.scraper_status_code.ScraperStatusCode"
    """<p>The current status of the scraper.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScraperStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    return out


def deserialize_json(data: dict) -> ScraperStatus:
    out: ScraperStatus = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    else:
        out["status_code"] = ""
    return out
