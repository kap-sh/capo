"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListPortfolioAccessOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.account_ids
    import capo_service_catalog.types.page_token


class ListPortfolioAccessOutput(TypedDict, closed=True):
    account_ids: NotRequired["capo_service_catalog.types.account_ids.AccountIds"]
    """<p>Information about the Amazon Web Services accounts with access to the portfolio.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPortfolioAccessOutput) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_service_catalog.types.account_ids

        out["AccountIds"] = (
            capo_service_catalog.types.account_ids.serialize_aws_json_1_1(
                value["account_ids"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPortfolioAccessOutput:
    out: ListPortfolioAccessOutput = {}  # type: ignore[typeddict-item]
    if data.get("AccountIds") is not None:
        import capo_service_catalog.types.account_ids

        out["account_ids"] = (
            capo_service_catalog.types.account_ids.deserialize_aws_json_1_1(
                data["AccountIds"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListPortfolioAccessOutput) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_service_catalog.types.account_ids

        out["AccountIds"] = capo_service_catalog.types.account_ids.serialize_cbor(
            value["account_ids"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ListPortfolioAccessOutput:
    out: ListPortfolioAccessOutput = {}  # type: ignore[typeddict-item]
    if data.get("AccountIds") is not None:
        import capo_service_catalog.types.account_ids

        out["account_ids"] = capo_service_catalog.types.account_ids.deserialize_cbor(
            data["AccountIds"]
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
