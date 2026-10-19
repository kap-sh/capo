"""Generated from Smithy shape ``com.amazonaws.quicksight#LogoConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.logo_set_configuration
    import capo_quicksight.types.string


class LogoConfiguration(TypedDict, closed=True):
    alt_text: "capo_quicksight.types.string.String"
    """<p>The alt text for the logo.</p>"""
    logo_set: "capo_quicksight.types.logo_set_configuration.LogoSetConfiguration"
    """<p>A set of configured logos.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogoConfiguration) -> dict:
    out: dict = {}
    out["AltText"] = value["alt_text"]
    import capo_quicksight.types.logo_set_configuration

    out["LogoSet"] = capo_quicksight.types.logo_set_configuration.serialize_json(
        value["logo_set"]
    )
    return out


def deserialize_json(data: dict) -> LogoConfiguration:
    out: LogoConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AltText") is not None:
        out["alt_text"] = data["AltText"]
    else:
        out["alt_text"] = ""
    if data.get("LogoSet") is not None:
        import capo_quicksight.types.logo_set_configuration

        out["logo_set"] = capo_quicksight.types.logo_set_configuration.deserialize_json(
            data["LogoSet"]
        )
    else:
        raise DeserializationError("LogoConfiguration.logo_set required")
    return out
