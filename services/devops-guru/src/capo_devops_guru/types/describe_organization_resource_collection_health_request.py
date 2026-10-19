"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeOrganizationResourceCollectionHealthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.account_id_list
    import capo_devops_guru.types.organization_resource_collection_max_results
    import capo_devops_guru.types.organization_resource_collection_type
    import capo_devops_guru.types.organizational_unit_id_list
    import capo_devops_guru.types.uuid_next_token


class DescribeOrganizationResourceCollectionHealthRequest(TypedDict, closed=True):
    organization_resource_collection_type: "capo_devops_guru.types.organization_resource_collection_type.OrganizationResourceCollectionType"
    """<p> An Amazon Web Services resource collection type. This type specifies how analyzed Amazon Web Services resources are defined. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag <i>key</i>. You can specify up to 500 Amazon Web Services CloudFormation stacks. </p>"""
    account_ids: NotRequired["capo_devops_guru.types.account_id_list.AccountIdList"]
    """<p>The ID of the Amazon Web Services account.</p>"""
    organizational_unit_ids: NotRequired[
        "capo_devops_guru.types.organizational_unit_id_list.OrganizationalUnitIdList"
    ]
    """<p>The ID of the organizational unit.</p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""
    max_results: NotRequired[
        "capo_devops_guru.types.organization_resource_collection_max_results.OrganizationResourceCollectionMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationResourceCollectionHealthRequest) -> dict:
    out: dict = {}
    import capo_devops_guru.types.organization_resource_collection_type

    out["OrganizationResourceCollectionType"] = (
        capo_devops_guru.types.organization_resource_collection_type.serialize_json(
            value["organization_resource_collection_type"]
        )
    )
    if "account_ids" in value:
        import capo_devops_guru.types.account_id_list

        out["AccountIds"] = capo_devops_guru.types.account_id_list.serialize_json(
            value["account_ids"]
        )
    if "organizational_unit_ids" in value:
        import capo_devops_guru.types.organizational_unit_id_list

        out["OrganizationalUnitIds"] = (
            capo_devops_guru.types.organizational_unit_id_list.serialize_json(
                value["organizational_unit_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> DescribeOrganizationResourceCollectionHealthRequest:
    out: DescribeOrganizationResourceCollectionHealthRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationResourceCollectionType") is not None:
        import capo_devops_guru.types.organization_resource_collection_type

        out["organization_resource_collection_type"] = (
            capo_devops_guru.types.organization_resource_collection_type.deserialize_json(
                data["OrganizationResourceCollectionType"]
            )
        )
    else:
        import typing

        out["organization_resource_collection_type"] = typing.cast(
            "capo_devops_guru.types.organization_resource_collection_type.OrganizationResourceCollectionType",
            "",
        )
    if data.get("AccountIds") is not None:
        import capo_devops_guru.types.account_id_list

        out["account_ids"] = capo_devops_guru.types.account_id_list.deserialize_json(
            data["AccountIds"]
        )
    if data.get("OrganizationalUnitIds") is not None:
        import capo_devops_guru.types.organizational_unit_id_list

        out["organizational_unit_ids"] = (
            capo_devops_guru.types.organizational_unit_id_list.deserialize_json(
                data["OrganizationalUnitIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
