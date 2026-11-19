"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreatePortfolioShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id


class CreatePortfolioShareOutput(TypedDict, closed=True):
    portfolio_share_token: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The portfolio shares a unique identifier that only returns if the portfolio is shared to an organization node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePortfolioShareOutput) -> dict:
    out: dict = {}
    if "portfolio_share_token" in value:
        out["PortfolioShareToken"] = value["portfolio_share_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePortfolioShareOutput:
    out: CreatePortfolioShareOutput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioShareToken") is not None:
        out["portfolio_share_token"] = data["PortfolioShareToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreatePortfolioShareOutput) -> dict:
    out: dict = {}
    if "portfolio_share_token" in value:
        out["PortfolioShareToken"] = value["portfolio_share_token"]
    return out


def deserialize_cbor(data: dict) -> CreatePortfolioShareOutput:
    out: CreatePortfolioShareOutput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioShareToken") is not None:
        out["portfolio_share_token"] = data["PortfolioShareToken"]
    return out
