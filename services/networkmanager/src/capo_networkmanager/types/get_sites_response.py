"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetSitesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.site_list


class GetSitesResponse(TypedDict, closed=True):
    sites: NotRequired["capo_networkmanager.types.site_list.SiteList"]
    """<p>The sites.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSitesResponse) -> dict:
    out: dict = {}
    if "sites" in value:
        import capo_networkmanager.types.site_list

        out["Sites"] = capo_networkmanager.types.site_list.serialize_json(
            value["sites"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSitesResponse:
    out: GetSitesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Sites") is not None:
        import capo_networkmanager.types.site_list

        out["sites"] = capo_networkmanager.types.site_list.deserialize_json(
            data["Sites"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: GetSitesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sites" in value:
        import capo_networkmanager.types.site_list

        out["sites"] = capo_networkmanager.types.site_list.redact_sensitive(
            value["sites"]
        )
    return out
