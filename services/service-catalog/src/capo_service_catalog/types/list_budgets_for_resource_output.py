"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListBudgetsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.budgets
    import capo_service_catalog.types.page_token


class ListBudgetsForResourceOutput(TypedDict, closed=True):
    budgets: NotRequired["capo_service_catalog.types.budgets.Budgets"]
    """<p>Information about the associated budgets.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBudgetsForResourceOutput) -> dict:
    out: dict = {}
    if "budgets" in value:
        import capo_service_catalog.types.budgets

        out["Budgets"] = capo_service_catalog.types.budgets.serialize_aws_json_1_1(
            value["budgets"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBudgetsForResourceOutput:
    out: ListBudgetsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("Budgets") is not None:
        import capo_service_catalog.types.budgets

        out["budgets"] = capo_service_catalog.types.budgets.deserialize_aws_json_1_1(
            data["Budgets"]
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListBudgetsForResourceOutput) -> dict:
    out: dict = {}
    if "budgets" in value:
        import capo_service_catalog.types.budgets

        out["Budgets"] = capo_service_catalog.types.budgets.serialize_cbor(
            value["budgets"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ListBudgetsForResourceOutput:
    out: ListBudgetsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("Budgets") is not None:
        import capo_service_catalog.types.budgets

        out["budgets"] = capo_service_catalog.types.budgets.deserialize_cbor(
            data["Budgets"]
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
