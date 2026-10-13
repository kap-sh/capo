"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateSiteResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.site


class UpdateSiteResponse(TypedDict, closed=True):
    site: NotRequired["capo_networkmanager.types.site.Site"]
    """<p>Information about the site.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSiteResponse) -> dict:
    out: dict = {}
    if "site" in value:
        import capo_networkmanager.types.site

        out["Site"] = capo_networkmanager.types.site.serialize_json(value["site"])
    return out


def deserialize_json(data: dict) -> UpdateSiteResponse:
    out: UpdateSiteResponse = {}  # type: ignore[typeddict-item]
    if data.get("Site") is not None:
        import capo_networkmanager.types.site

        out["site"] = capo_networkmanager.types.site.deserialize_json(data["Site"])
    return out


def redact_sensitive(value: UpdateSiteResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "site" in value:
        import capo_networkmanager.types.site

        out["site"] = capo_networkmanager.types.site.redact_sensitive(value["site"])
    return out
