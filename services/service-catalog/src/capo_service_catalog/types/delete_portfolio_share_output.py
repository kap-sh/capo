"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeletePortfolioShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id


class DeletePortfolioShareOutput(TypedDict, closed=True):
    portfolio_share_token: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The portfolio share unique identifier. This will only be returned if delete is made to an organization node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePortfolioShareOutput) -> dict:
    out: dict = {}
    if "portfolio_share_token" in value:
        out["PortfolioShareToken"] = value["portfolio_share_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePortfolioShareOutput:
    out: DeletePortfolioShareOutput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioShareToken") is not None:
        out["portfolio_share_token"] = data["PortfolioShareToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeletePortfolioShareOutput) -> dict:
    out: dict = {}
    if "portfolio_share_token" in value:
        out["PortfolioShareToken"] = value["portfolio_share_token"]
    return out


def deserialize_cbor(data: dict) -> DeletePortfolioShareOutput:
    out: DeletePortfolioShareOutput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioShareToken") is not None:
        out["portfolio_share_token"] = data["PortfolioShareToken"]
    return out
