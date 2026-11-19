"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdatePortfolioShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id
    import capo_service_catalog.types.share_status


class UpdatePortfolioShareOutput(TypedDict, closed=True):
    portfolio_share_token: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The token that tracks the status of the <code>UpdatePortfolioShare</code> operation for external account to account or organizational type sharing.</p>"""
    status: NotRequired["capo_service_catalog.types.share_status.ShareStatus"]
    """<p>The status of <code>UpdatePortfolioShare</code> operation. You can also obtain the operation status using <code>DescribePortfolioShareStatus</code> API. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePortfolioShareOutput) -> dict:
    out: dict = {}
    if "portfolio_share_token" in value:
        out["PortfolioShareToken"] = value["portfolio_share_token"]
    if "status" in value:
        import capo_service_catalog.types.share_status

        out["Status"] = capo_service_catalog.types.share_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePortfolioShareOutput:
    out: UpdatePortfolioShareOutput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioShareToken") is not None:
        out["portfolio_share_token"] = data["PortfolioShareToken"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.share_status

        out["status"] = (
            capo_service_catalog.types.share_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdatePortfolioShareOutput) -> dict:
    out: dict = {}
    if "portfolio_share_token" in value:
        out["PortfolioShareToken"] = value["portfolio_share_token"]
    if "status" in value:
        import capo_service_catalog.types.share_status

        out["Status"] = capo_service_catalog.types.share_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> UpdatePortfolioShareOutput:
    out: UpdatePortfolioShareOutput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioShareToken") is not None:
        out["portfolio_share_token"] = data["PortfolioShareToken"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.share_status

        out["status"] = capo_service_catalog.types.share_status.deserialize_cbor(
            data["Status"]
        )
    return out
