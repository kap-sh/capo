"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ProductCodeListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.product_code_id
    import capo_imagebuilder.types.product_code_type


class ProductCodeListItem(TypedDict, closed=True):
    product_code_id: "capo_imagebuilder.types.product_code_id.ProductCodeId"
    """<p>For Amazon Web Services Marketplace components, this contains the product code ID that can be stamped onto an EC2 AMI to ensure that components are billed correctly. If this property is empty, it might mean that the component is not published.</p>"""
    product_code_type: "capo_imagebuilder.types.product_code_type.ProductCodeType"
    """<p>The owner of the product code that's billed. If this property is empty, it might mean that the component is not published.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductCodeListItem) -> dict:
    out: dict = {}
    out["productCodeId"] = value["product_code_id"]
    import capo_imagebuilder.types.product_code_type

    out["productCodeType"] = capo_imagebuilder.types.product_code_type.serialize_json(
        value["product_code_type"]
    )
    return out


def deserialize_json(data: dict) -> ProductCodeListItem:
    out: ProductCodeListItem = {}  # type: ignore[typeddict-item]
    if data.get("productCodeId") is not None:
        out["product_code_id"] = data["productCodeId"]
    else:
        out["product_code_id"] = ""
    if data.get("productCodeType") is not None:
        import capo_imagebuilder.types.product_code_type

        out["product_code_type"] = (
            capo_imagebuilder.types.product_code_type.deserialize_json(
                data["productCodeType"]
            )
        )
    else:
        import typing

        out["product_code_type"] = typing.cast(
            "capo_imagebuilder.types.product_code_type.ProductCodeType", ""
        )
    return out
