"""Generated from Smithy shape ``com.amazonaws.endusermessaging#TextParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.destination_country_parameters
    import capo_endusermessaging.types.inline_template_body


class TextParameters(TypedDict, closed=True):
    inline_template_body: NotRequired[
        "capo_endusermessaging.types.inline_template_body.InlineTemplateBody"
    ]
    """<p>The freeform message template used to render the one-time passcode for the SMS or RCS channels. The template must contain the code placeholder.</p>"""
    destination_country_parameters: NotRequired[
        "capo_endusermessaging.types.destination_country_parameters.DestinationCountryParameters"
    ]
    """<p>A map of country-specific parameters that control one-time passcode delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextParameters) -> dict:
    out: dict = {}
    if "inline_template_body" in value:
        out["inlineTemplateBody"] = value["inline_template_body"]
    if "destination_country_parameters" in value:
        import capo_endusermessaging.types.destination_country_parameters

        out["destinationCountryParameters"] = (
            capo_endusermessaging.types.destination_country_parameters.serialize_json(
                value["destination_country_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextParameters:
    out: TextParameters = {}  # type: ignore[typeddict-item]
    if data.get("inlineTemplateBody") is not None:
        out["inline_template_body"] = data["inlineTemplateBody"]
    if data.get("destinationCountryParameters") is not None:
        import capo_endusermessaging.types.destination_country_parameters

        out["destination_country_parameters"] = (
            capo_endusermessaging.types.destination_country_parameters.deserialize_json(
                data["destinationCountryParameters"]
            )
        )
    return out
