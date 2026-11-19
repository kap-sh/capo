"""Generated from Smithy shape ``com.amazonaws.servicecatalog#LaunchPathSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.constraint_summaries
    import capo_service_catalog.types.id
    import capo_service_catalog.types.portfolio_name
    import capo_service_catalog.types.tags


class LaunchPathSummary(TypedDict, closed=True):
    id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the product path.</p>"""
    constraint_summaries: NotRequired[
        "capo_service_catalog.types.constraint_summaries.ConstraintSummaries"
    ]
    """<p>The constraints on the portfolio-product relationship.</p>"""
    tags: NotRequired["capo_service_catalog.types.tags.Tags"]
    """<p>The tags associated with this product path.</p>"""
    name: NotRequired["capo_service_catalog.types.portfolio_name.PortfolioName"]
    """<p>The name of the portfolio that contains the product. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LaunchPathSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "constraint_summaries" in value:
        import capo_service_catalog.types.constraint_summaries

        out["ConstraintSummaries"] = (
            capo_service_catalog.types.constraint_summaries.serialize_aws_json_1_1(
                value["constraint_summaries"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LaunchPathSummary:
    out: LaunchPathSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ConstraintSummaries") is not None:
        import capo_service_catalog.types.constraint_summaries

        out["constraint_summaries"] = (
            capo_service_catalog.types.constraint_summaries.deserialize_aws_json_1_1(
                data["ConstraintSummaries"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LaunchPathSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "constraint_summaries" in value:
        import capo_service_catalog.types.constraint_summaries

        out["ConstraintSummaries"] = (
            capo_service_catalog.types.constraint_summaries.serialize_cbor(
                value["constraint_summaries"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_cbor(value["tags"])
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> LaunchPathSummary:
    out: LaunchPathSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ConstraintSummaries") is not None:
        import capo_service_catalog.types.constraint_summaries

        out["constraint_summaries"] = (
            capo_service_catalog.types.constraint_summaries.deserialize_cbor(
                data["ConstraintSummaries"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_cbor(data["Tags"])
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
