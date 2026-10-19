"""Generated from Smithy shape ``com.amazonaws.quicksight#Logo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.alt_text
    import capo_quicksight.types.logo_set


class Logo(TypedDict, closed=True):
    alt_text: "capo_quicksight.types.alt_text.AltText"
    """<p>The alt text for the logo.</p>"""
    logo_set: "capo_quicksight.types.logo_set.LogoSet"
    """<p>A set of configured logos.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Logo) -> dict:
    out: dict = {}
    out["AltText"] = value["alt_text"]
    import capo_quicksight.types.logo_set

    out["LogoSet"] = capo_quicksight.types.logo_set.serialize_json(value["logo_set"])
    return out


def deserialize_json(data: dict) -> Logo:
    out: Logo = {}  # type: ignore[typeddict-item]
    if data.get("AltText") is not None:
        out["alt_text"] = data["AltText"]
    else:
        out["alt_text"] = ""
    if data.get("LogoSet") is not None:
        import capo_quicksight.types.logo_set

        out["logo_set"] = capo_quicksight.types.logo_set.deserialize_json(
            data["LogoSet"]
        )
    else:
        raise DeserializationError("Logo.logo_set required")
    return out
