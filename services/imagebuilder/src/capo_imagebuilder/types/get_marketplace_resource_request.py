"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetMarketplaceResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.marketplace_resource_location
    import capo_imagebuilder.types.marketplace_resource_type


class GetMarketplaceResourceRequest(TypedDict, closed=True):
    resource_type: (
        "capo_imagebuilder.types.marketplace_resource_type.MarketplaceResourceType"
    )
    """<p>Specifies which type of Amazon Web Services Marketplace resource Image Builder retrieves.</p>"""
    resource_arn: "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies an Amazon Web Services Marketplace resource.</p>"""
    resource_location: NotRequired[
        "capo_imagebuilder.types.marketplace_resource_location.MarketplaceResourceLocation"
    ]
    """<p>The Amazon S3 location of the component artifact to retrieve, in <code>s3://bucket/key</code> form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMarketplaceResourceRequest) -> dict:
    out: dict = {}
    import capo_imagebuilder.types.marketplace_resource_type

    out["resourceType"] = (
        capo_imagebuilder.types.marketplace_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    out["resourceArn"] = value["resource_arn"]
    if "resource_location" in value:
        out["resourceLocation"] = value["resource_location"]
    return out


def deserialize_json(data: dict) -> GetMarketplaceResourceRequest:
    out: GetMarketplaceResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_imagebuilder.types.marketplace_resource_type

        out["resource_type"] = (
            capo_imagebuilder.types.marketplace_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_imagebuilder.types.marketplace_resource_type.MarketplaceResourceType",
            "",
        )
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("resourceLocation") is not None:
        out["resource_location"] = data["resourceLocation"]
    return out
