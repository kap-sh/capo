"""Generated from Smithy shape ``com.amazonaws.servicecatalog#BudgetDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.budget_name


class BudgetDetail(TypedDict, closed=True):
    budget_name: NotRequired["capo_service_catalog.types.budget_name.BudgetName"]
    """<p>Name of the associated budget.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BudgetDetail) -> dict:
    out: dict = {}
    if "budget_name" in value:
        out["BudgetName"] = value["budget_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BudgetDetail:
    out: BudgetDetail = {}  # type: ignore[typeddict-item]
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BudgetDetail) -> dict:
    out: dict = {}
    if "budget_name" in value:
        out["BudgetName"] = value["budget_name"]
    return out


def deserialize_cbor(data: dict) -> BudgetDetail:
    out: BudgetDetail = {}  # type: ignore[typeddict-item]
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    return out
