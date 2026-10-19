"""Generated from Smithy shape ``com.amazonaws.licensemanager#ProductCodeListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.product_code_id
    import capo_license_manager.types.product_code_type


class ProductCodeListItem(TypedDict, closed=True):
    product_code_id: "capo_license_manager.types.product_code_id.ProductCodeId"
    """<p>The product code ID</p>"""
    product_code_type: "capo_license_manager.types.product_code_type.ProductCodeType"
    """<p>The product code type</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductCodeListItem) -> dict:
    out: dict = {}
    out["ProductCodeId"] = value["product_code_id"]
    import capo_license_manager.types.product_code_type

    out["ProductCodeType"] = (
        capo_license_manager.types.product_code_type.serialize_aws_json_1_1(
            value["product_code_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductCodeListItem:
    out: ProductCodeListItem = {}  # type: ignore[typeddict-item]
    if data.get("ProductCodeId") is not None:
        out["product_code_id"] = data["ProductCodeId"]
    else:
        out["product_code_id"] = ""
    if data.get("ProductCodeType") is not None:
        import capo_license_manager.types.product_code_type

        out["product_code_type"] = (
            capo_license_manager.types.product_code_type.deserialize_aws_json_1_1(
                data["ProductCodeType"]
            )
        )
    else:
        import typing

        out["product_code_type"] = typing.cast(
            "capo_license_manager.types.product_code_type.ProductCodeType", ""
        )
    return out
