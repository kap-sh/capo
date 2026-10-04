"""Generated from Smithy shape ``com.amazonaws.endusermessaging#CreateBrandProfileAttributesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_attribute_output_list


class CreateBrandProfileAttributesOutput(TypedDict, closed=True):
    attributes: "capo_endusermessaging.types.brand_profile_attribute_output_list.BrandProfileAttributeOutputList"
    """<p>The brand profile attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrandProfileAttributesOutput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.brand_profile_attribute_output_list

    out["attributes"] = (
        capo_endusermessaging.types.brand_profile_attribute_output_list.serialize_json(
            value["attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateBrandProfileAttributesOutput:
    out: CreateBrandProfileAttributesOutput = {}  # type: ignore[typeddict-item]
    if data.get("attributes") is not None:
        import capo_endusermessaging.types.brand_profile_attribute_output_list

        out["attributes"] = (
            capo_endusermessaging.types.brand_profile_attribute_output_list.deserialize_json(
                data["attributes"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBrandProfileAttributesOutput.attributes required"
        )
    return out
