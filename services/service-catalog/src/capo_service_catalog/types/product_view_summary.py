"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.has_default_path
    import capo_service_catalog.types.id
    import capo_service_catalog.types.product_type
    import capo_service_catalog.types.product_view_distributor
    import capo_service_catalog.types.product_view_name
    import capo_service_catalog.types.product_view_owner
    import capo_service_catalog.types.product_view_short_description
    import capo_service_catalog.types.support_description
    import capo_service_catalog.types.support_email
    import capo_service_catalog.types.support_url


class ProductViewSummary(TypedDict, closed=True):
    id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The product view identifier.</p>"""
    product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    name: NotRequired["capo_service_catalog.types.product_view_name.ProductViewName"]
    """<p>The name of the product.</p>"""
    owner: NotRequired["capo_service_catalog.types.product_view_owner.ProductViewOwner"]
    """<p>The owner of the product. Contact the product administrator for the significance of this value.</p>"""
    short_description: NotRequired[
        "capo_service_catalog.types.product_view_short_description.ProductViewShortDescription"
    ]
    """<p>Short description of the product.</p>"""
    type: NotRequired["capo_service_catalog.types.product_type.ProductType"]
    """<p>The product type. Contact the product administrator for the significance of this value. If this value is <code>MARKETPLACE</code>, the product was created by Amazon Web Services Marketplace.</p>"""
    distributor: NotRequired[
        "capo_service_catalog.types.product_view_distributor.ProductViewDistributor"
    ]
    """<p>The distributor of the product. Contact the product administrator for the significance of this value.</p>"""
    has_default_path: "capo_service_catalog.types.has_default_path.HasDefaultPath"
    """<p>Indicates whether the product has a default path. If the product does not have a default path, call <a>ListLaunchPaths</a> to disambiguate between paths. Otherwise, <a>ListLaunchPaths</a> is not required, and the output of <a>ProductViewSummary</a> can be used directly with <a>DescribeProvisioningParameters</a>.</p>"""
    support_email: NotRequired["capo_service_catalog.types.support_email.SupportEmail"]
    """<p>The email contact information to obtain support for this Product.</p>"""
    support_description: NotRequired[
        "capo_service_catalog.types.support_description.SupportDescription"
    ]
    """<p>The description of the support for this Product.</p>"""
    support_url: NotRequired["capo_service_catalog.types.support_url.SupportUrl"]
    """<p>The URL information to obtain support for this Product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductViewSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "short_description" in value:
        out["ShortDescription"] = value["short_description"]
    if "type" in value:
        import capo_service_catalog.types.product_type

        out["Type"] = capo_service_catalog.types.product_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "distributor" in value:
        out["Distributor"] = value["distributor"]
    out["HasDefaultPath"] = value.get("has_default_path", False)
    if "support_email" in value:
        out["SupportEmail"] = value["support_email"]
    if "support_description" in value:
        out["SupportDescription"] = value["support_description"]
    if "support_url" in value:
        out["SupportUrl"] = value["support_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductViewSummary:
    out: ProductViewSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("ShortDescription") is not None:
        out["short_description"] = data["ShortDescription"]
    if data.get("Type") is not None:
        import capo_service_catalog.types.product_type

        out["type"] = capo_service_catalog.types.product_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Distributor") is not None:
        out["distributor"] = data["Distributor"]
    if data.get("HasDefaultPath") is not None:
        out["has_default_path"] = data["HasDefaultPath"]
    else:
        out["has_default_path"] = False
    if data.get("SupportEmail") is not None:
        out["support_email"] = data["SupportEmail"]
    if data.get("SupportDescription") is not None:
        out["support_description"] = data["SupportDescription"]
    if data.get("SupportUrl") is not None:
        out["support_url"] = data["SupportUrl"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProductViewSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "short_description" in value:
        out["ShortDescription"] = value["short_description"]
    if "type" in value:
        import capo_service_catalog.types.product_type

        out["Type"] = capo_service_catalog.types.product_type.serialize_cbor(
            value["type"]
        )
    if "distributor" in value:
        out["Distributor"] = value["distributor"]
    out["HasDefaultPath"] = value.get("has_default_path", False)
    if "support_email" in value:
        out["SupportEmail"] = value["support_email"]
    if "support_description" in value:
        out["SupportDescription"] = value["support_description"]
    if "support_url" in value:
        out["SupportUrl"] = value["support_url"]
    return out


def deserialize_cbor(data: dict) -> ProductViewSummary:
    out: ProductViewSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("ShortDescription") is not None:
        out["short_description"] = data["ShortDescription"]
    if data.get("Type") is not None:
        import capo_service_catalog.types.product_type

        out["type"] = capo_service_catalog.types.product_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("Distributor") is not None:
        out["distributor"] = data["Distributor"]
    if data.get("HasDefaultPath") is not None:
        out["has_default_path"] = data["HasDefaultPath"]
    else:
        out["has_default_path"] = False
    if data.get("SupportEmail") is not None:
        out["support_email"] = data["SupportEmail"]
    if data.get("SupportDescription") is not None:
        out["support_description"] = data["SupportDescription"]
    if data.get("SupportUrl") is not None:
        out["support_url"] = data["SupportUrl"]
    return out
