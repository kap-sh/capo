"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribePortfolioOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.budgets
    import capo_service_catalog.types.portfolio_detail
    import capo_service_catalog.types.tag_option_details
    import capo_service_catalog.types.tags


class DescribePortfolioOutput(TypedDict, closed=True):
    portfolio_detail: NotRequired[
        "capo_service_catalog.types.portfolio_detail.PortfolioDetail"
    ]
    """<p>Information about the portfolio.</p>"""
    tags: NotRequired["capo_service_catalog.types.tags.Tags"]
    """<p>Information about the tags associated with the portfolio.</p>"""
    tag_options: NotRequired[
        "capo_service_catalog.types.tag_option_details.TagOptionDetails"
    ]
    """<p>Information about the TagOptions associated with the portfolio.</p>"""
    budgets: NotRequired["capo_service_catalog.types.budgets.Budgets"]
    """<p>Information about the associated budgets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePortfolioOutput) -> dict:
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
    if "tag_options" in value:
        import capo_service_catalog.types.tag_option_details

        out["TagOptions"] = (
            capo_service_catalog.types.tag_option_details.serialize_aws_json_1_1(
                value["tag_options"]
            )
        )
    if "budgets" in value:
        import capo_service_catalog.types.budgets

        out["Budgets"] = capo_service_catalog.types.budgets.serialize_aws_json_1_1(
            value["budgets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePortfolioOutput:
    out: DescribePortfolioOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("TagOptions") is not None:
        import capo_service_catalog.types.tag_option_details

        out["tag_options"] = (
            capo_service_catalog.types.tag_option_details.deserialize_aws_json_1_1(
                data["TagOptions"]
            )
        )
    if data.get("Budgets") is not None:
        import capo_service_catalog.types.budgets

        out["budgets"] = capo_service_catalog.types.budgets.deserialize_aws_json_1_1(
            data["Budgets"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribePortfolioOutput) -> dict:
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
    if "tag_options" in value:
        import capo_service_catalog.types.tag_option_details

        out["TagOptions"] = (
            capo_service_catalog.types.tag_option_details.serialize_cbor(
                value["tag_options"]
            )
        )
    if "budgets" in value:
        import capo_service_catalog.types.budgets

        out["Budgets"] = capo_service_catalog.types.budgets.serialize_cbor(
            value["budgets"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribePortfolioOutput:
    out: DescribePortfolioOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("TagOptions") is not None:
        import capo_service_catalog.types.tag_option_details

        out["tag_options"] = (
            capo_service_catalog.types.tag_option_details.deserialize_cbor(
                data["TagOptions"]
            )
        )
    if data.get("Budgets") is not None:
        import capo_service_catalog.types.budgets

        out["budgets"] = capo_service_catalog.types.budgets.deserialize_cbor(
            data["Budgets"]
        )
    return out
