"""Generated from Smithy shape ``com.amazonaws.deadline#PutMeteredProductRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.license_endpoint_id
    import capo_deadline.types.metered_product_id


class PutMeteredProductRequest(TypedDict, closed=True):
    license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId"
    """The license endpoint ID to add to the metered product."""
    product_id: "capo_deadline.types.metered_product_id.MeteredProductId"
    """The product ID to add to the metered product."""


# --- restJson1 ser/de ---
def serialize_json(value: PutMeteredProductRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutMeteredProductRequest:
    out: PutMeteredProductRequest = {}  # type: ignore[typeddict-item]
    return out
