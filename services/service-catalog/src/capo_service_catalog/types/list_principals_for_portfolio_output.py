"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListPrincipalsForPortfolioOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.principals


class ListPrincipalsForPortfolioOutput(TypedDict, closed=True):
    principals: NotRequired["capo_service_catalog.types.principals.Principals"]
    """<p>The <code>PrincipalARN</code>s and corresponding <code>PrincipalType</code>s associated with the portfolio.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPrincipalsForPortfolioOutput) -> dict:
    out: dict = {}
    if "principals" in value:
        import capo_service_catalog.types.principals

        out["Principals"] = (
            capo_service_catalog.types.principals.serialize_aws_json_1_1(
                value["principals"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPrincipalsForPortfolioOutput:
    out: ListPrincipalsForPortfolioOutput = {}  # type: ignore[typeddict-item]
    if data.get("Principals") is not None:
        import capo_service_catalog.types.principals

        out["principals"] = (
            capo_service_catalog.types.principals.deserialize_aws_json_1_1(
                data["Principals"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListPrincipalsForPortfolioOutput) -> dict:
    out: dict = {}
    if "principals" in value:
        import capo_service_catalog.types.principals

        out["Principals"] = capo_service_catalog.types.principals.serialize_cbor(
            value["principals"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ListPrincipalsForPortfolioOutput:
    out: ListPrincipalsForPortfolioOutput = {}  # type: ignore[typeddict-item]
    if data.get("Principals") is not None:
        import capo_service_catalog.types.principals

        out["principals"] = capo_service_catalog.types.principals.deserialize_cbor(
            data["Principals"]
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
