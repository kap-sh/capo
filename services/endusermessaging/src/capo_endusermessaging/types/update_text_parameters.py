"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateTextParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.update_destination_country_parameters
    import capo_endusermessaging.types.update_inline_template_body


class UpdateTextParameters(TypedDict, closed=True):
    inline_template_body: NotRequired[
        "capo_endusermessaging.types.update_inline_template_body.UpdateInlineTemplateBody"
    ]
    """<p>The updated freeform SMS or RCS template body. An empty string clears the previously stored value.</p>"""
    destination_country_parameters: NotRequired[
        "capo_endusermessaging.types.update_destination_country_parameters.UpdateDestinationCountryParameters"
    ]
    """<p>The updated map of country-specific parameters that control one-time passcode delivery. An empty map clears the previously stored value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTextParameters) -> dict:
    out: dict = {}
    if "inline_template_body" in value:
        out["inlineTemplateBody"] = value["inline_template_body"]
    if "destination_country_parameters" in value:
        import capo_endusermessaging.types.update_destination_country_parameters

        out["destinationCountryParameters"] = (
            capo_endusermessaging.types.update_destination_country_parameters.serialize_json(
                value["destination_country_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTextParameters:
    out: UpdateTextParameters = {}  # type: ignore[typeddict-item]
    if data.get("inlineTemplateBody") is not None:
        out["inline_template_body"] = data["inlineTemplateBody"]
    if data.get("destinationCountryParameters") is not None:
        import capo_endusermessaging.types.update_destination_country_parameters

        out["destination_country_parameters"] = (
            capo_endusermessaging.types.update_destination_country_parameters.deserialize_json(
                data["destinationCountryParameters"]
            )
        )
    return out
