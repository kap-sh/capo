"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListOrganizationPortfolioAccessOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.organization_nodes
    import capo_service_catalog.types.page_token


class ListOrganizationPortfolioAccessOutput(TypedDict, closed=True):
    organization_nodes: NotRequired[
        "capo_service_catalog.types.organization_nodes.OrganizationNodes"
    ]
    """<p>Displays information about the organization nodes.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOrganizationPortfolioAccessOutput) -> dict:
    out: dict = {}
    if "organization_nodes" in value:
        import capo_service_catalog.types.organization_nodes

        out["OrganizationNodes"] = (
            capo_service_catalog.types.organization_nodes.serialize_aws_json_1_1(
                value["organization_nodes"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOrganizationPortfolioAccessOutput:
    out: ListOrganizationPortfolioAccessOutput = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationNodes") is not None:
        import capo_service_catalog.types.organization_nodes

        out["organization_nodes"] = (
            capo_service_catalog.types.organization_nodes.deserialize_aws_json_1_1(
                data["OrganizationNodes"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOrganizationPortfolioAccessOutput) -> dict:
    out: dict = {}
    if "organization_nodes" in value:
        import capo_service_catalog.types.organization_nodes

        out["OrganizationNodes"] = (
            capo_service_catalog.types.organization_nodes.serialize_cbor(
                value["organization_nodes"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ListOrganizationPortfolioAccessOutput:
    out: ListOrganizationPortfolioAccessOutput = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationNodes") is not None:
        import capo_service_catalog.types.organization_nodes

        out["organization_nodes"] = (
            capo_service_catalog.types.organization_nodes.deserialize_cbor(
                data["OrganizationNodes"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
