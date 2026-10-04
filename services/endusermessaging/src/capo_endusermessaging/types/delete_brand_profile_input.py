"""Generated from Smithy shape ``com.amazonaws.endusermessaging#DeleteBrandProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_id_or_arn


class DeleteBrandProfileInput(TypedDict, closed=True):
    brand_profile_id: (
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    )
    """<p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrandProfileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBrandProfileInput:
    out: DeleteBrandProfileInput = {}  # type: ignore[typeddict-item]
    return out
