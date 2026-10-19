"""Generated from Smithy shape ``com.amazonaws.appintegrations#ExternalUrlConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.application_approved_origins
    import capo_appintegrations.types.url


class ExternalUrlConfig(TypedDict, closed=True):
    access_url: "capo_appintegrations.types.url.URL"
    """<p>The URL to access the application.</p>"""
    approved_origins: NotRequired[
        "capo_appintegrations.types.application_approved_origins.ApplicationApprovedOrigins"
    ]
    """<p>Additional URLs to allow list if different than the access URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalUrlConfig) -> dict:
    out: dict = {}
    out["AccessUrl"] = value["access_url"]
    if "approved_origins" in value:
        import capo_appintegrations.types.application_approved_origins

        out["ApprovedOrigins"] = (
            capo_appintegrations.types.application_approved_origins.serialize_json(
                value["approved_origins"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExternalUrlConfig:
    out: ExternalUrlConfig = {}  # type: ignore[typeddict-item]
    if data.get("AccessUrl") is not None:
        out["access_url"] = data["AccessUrl"]
    else:
        out["access_url"] = ""
    if data.get("ApprovedOrigins") is not None:
        import capo_appintegrations.types.application_approved_origins

        out["approved_origins"] = (
            capo_appintegrations.types.application_approved_origins.deserialize_json(
                data["ApprovedOrigins"]
            )
        )
    return out
