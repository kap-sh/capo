"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ConstraintDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.account_id
    import capo_service_catalog.types.constraint_description
    import capo_service_catalog.types.constraint_type
    import capo_service_catalog.types.id


class ConstraintDetail(TypedDict, closed=True):
    constraint_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the constraint.</p>"""
    type: NotRequired["capo_service_catalog.types.constraint_type.ConstraintType"]
    """<p>The type of constraint.</p> <ul> <li> <p> <code>LAUNCH</code> </p> </li> <li> <p> <code>NOTIFICATION</code> </p> </li> <li> <p>STACKSET</p> </li> <li> <p> <code>TEMPLATE</code> </p> </li> </ul>"""
    description: NotRequired[
        "capo_service_catalog.types.constraint_description.ConstraintDescription"
    ]
    """<p>The description of the constraint.</p>"""
    owner: NotRequired["capo_service_catalog.types.account_id.AccountId"]
    """<p>The owner of the constraint.</p>"""
    product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the product the constraint applies to. Note that a constraint applies to a specific instance of a product within a certain portfolio.</p>"""
    portfolio_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the portfolio the product resides in. The constraint applies only to the instance of the product that lives within this portfolio.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConstraintDetail) -> dict:
    out: dict = {}
    if "constraint_id" in value:
        out["ConstraintId"] = value["constraint_id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "description" in value:
        out["Description"] = value["description"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "portfolio_id" in value:
        out["PortfolioId"] = value["portfolio_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConstraintDetail:
    out: ConstraintDetail = {}  # type: ignore[typeddict-item]
    if data.get("ConstraintId") is not None:
        out["constraint_id"] = data["ConstraintId"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("PortfolioId") is not None:
        out["portfolio_id"] = data["PortfolioId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConstraintDetail) -> dict:
    out: dict = {}
    if "constraint_id" in value:
        out["ConstraintId"] = value["constraint_id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "description" in value:
        out["Description"] = value["description"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "portfolio_id" in value:
        out["PortfolioId"] = value["portfolio_id"]
    return out


def deserialize_cbor(data: dict) -> ConstraintDetail:
    out: ConstraintDetail = {}  # type: ignore[typeddict-item]
    if data.get("ConstraintId") is not None:
        out["constraint_id"] = data["ConstraintId"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("PortfolioId") is not None:
        out["portfolio_id"] = data["PortfolioId"]
    return out
