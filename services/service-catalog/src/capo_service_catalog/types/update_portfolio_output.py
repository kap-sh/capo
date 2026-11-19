"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdatePortfolioOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.portfolio_detail
    import capo_service_catalog.types.tags


class UpdatePortfolioOutput(TypedDict, closed=True):
    portfolio_detail: NotRequired[
        "capo_service_catalog.types.portfolio_detail.PortfolioDetail"
    ]
    """<p>Information about the portfolio.</p>"""
    tags: NotRequired["capo_service_catalog.types.tags.Tags"]
    """<p>Information about the tags associated with the portfolio.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePortfolioOutput) -> dict:
    out: dict = {}
    if "portfolio_detail" in value:
        import capo_service_catalog.types.portfolio_detail

        out["PortfolioDetail"] = (
            capo_service_catalog.types.portfolio_detail.serialize_aws_json_1_1(
                value["portfolio_detail"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePortfolioOutput:
    out: UpdatePortfolioOutput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioDetail") is not None:
        import capo_service_catalog.types.portfolio_detail

        out["portfolio_detail"] = (
            capo_service_catalog.types.portfolio_detail.deserialize_aws_json_1_1(
                data["PortfolioDetail"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdatePortfolioOutput) -> dict:
    out: dict = {}
    if "portfolio_detail" in value:
        import capo_service_catalog.types.portfolio_detail

        out["PortfolioDetail"] = (
            capo_service_catalog.types.portfolio_detail.serialize_cbor(
                value["portfolio_detail"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> UpdatePortfolioOutput:
    out: UpdatePortfolioOutput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioDetail") is not None:
        import capo_service_catalog.types.portfolio_detail

        out["portfolio_detail"] = (
            capo_service_catalog.types.portfolio_detail.deserialize_cbor(
                data["PortfolioDetail"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_cbor(data["Tags"])
    return out
