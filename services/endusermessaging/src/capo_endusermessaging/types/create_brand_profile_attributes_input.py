"""Generated from Smithy shape ``com.amazonaws.endusermessaging#CreateBrandProfileAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_attribute_input_list
    import capo_endusermessaging.types.brand_profile_id_or_arn
    import capo_endusermessaging.types.client_token


class CreateBrandProfileAttributesInput(TypedDict, closed=True):
    brand_profile_id: (
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    )
    """<p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>"""
    attributes: "capo_endusermessaging.types.brand_profile_attribute_input_list.BrandProfileAttributeInputList"
    """<p>The brand profile attributes.</p>"""
    client_token: NotRequired["capo_endusermessaging.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrandProfileAttributesInput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.brand_profile_attribute_input_list

    out["attributes"] = (
        capo_endusermessaging.types.brand_profile_attribute_input_list.serialize_json(
            value["attributes"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateBrandProfileAttributesInput:
    out: CreateBrandProfileAttributesInput = {}  # type: ignore[typeddict-item]
    if data.get("attributes") is not None:
        import capo_endusermessaging.types.brand_profile_attribute_input_list

        out["attributes"] = (
            capo_endusermessaging.types.brand_profile_attribute_input_list.deserialize_json(
                data["attributes"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBrandProfileAttributesInput.attributes required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
