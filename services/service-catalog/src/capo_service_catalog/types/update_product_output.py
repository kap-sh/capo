"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.product_view_detail
    import capo_service_catalog.types.tags


class UpdateProductOutput(TypedDict, closed=True):
    product_view_detail: NotRequired[
        "capo_service_catalog.types.product_view_detail.ProductViewDetail"
    ]
    """<p>Information about the product view.</p>"""
    tags: NotRequired["capo_service_catalog.types.tags.Tags"]
    """<p>Information about the tags associated with the product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProductOutput) -> dict:
    out: dict = {}
    if "product_view_detail" in value:
        import capo_service_catalog.types.product_view_detail

        out["ProductViewDetail"] = (
            capo_service_catalog.types.product_view_detail.serialize_aws_json_1_1(
                value["product_view_detail"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProductOutput:
    out: UpdateProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewDetail") is not None:
        import capo_service_catalog.types.product_view_detail

        out["product_view_detail"] = (
            capo_service_catalog.types.product_view_detail.deserialize_aws_json_1_1(
                data["ProductViewDetail"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateProductOutput) -> dict:
    out: dict = {}
    if "product_view_detail" in value:
        import capo_service_catalog.types.product_view_detail

        out["ProductViewDetail"] = (
            capo_service_catalog.types.product_view_detail.serialize_cbor(
                value["product_view_detail"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> UpdateProductOutput:
    out: UpdateProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewDetail") is not None:
        import capo_service_catalog.types.product_view_detail

        out["product_view_detail"] = (
            capo_service_catalog.types.product_view_detail.deserialize_cbor(
                data["ProductViewDetail"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_cbor(data["Tags"])
    return out
