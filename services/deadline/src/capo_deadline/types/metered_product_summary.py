"""Generated from Smithy shape ``com.amazonaws.deadline#MeteredProductSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.bounded_string
    import capo_deadline.types.metered_product_id
    import capo_deadline.types.port_number


class MeteredProductSummary(TypedDict, closed=True):
    product_id: "capo_deadline.types.metered_product_id.MeteredProductId"
    """<p>The product ID.</p>"""
    family: "capo_deadline.types.bounded_string.BoundedString"
    """<p>The family to which the metered product belongs.</p>"""
    vendor: "capo_deadline.types.bounded_string.BoundedString"
    """<p>The vendor.</p>"""
    port: "capo_deadline.types.port_number.PortNumber"
    """<p>The port on which the metered product should run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MeteredProductSummary) -> dict:
    out: dict = {}
    out["productId"] = value["product_id"]
    out["family"] = value["family"]
    out["vendor"] = value["vendor"]
    out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> MeteredProductSummary:
    out: MeteredProductSummary = {}  # type: ignore[typeddict-item]
    if data.get("productId") is not None:
        out["product_id"] = data["productId"]
    else:
        out["product_id"] = ""
    if data.get("family") is not None:
        out["family"] = data["family"]
    else:
        out["family"] = ""
    if data.get("vendor") is not None:
        out["vendor"] = data["vendor"]
    else:
        out["vendor"] = ""
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    return out
