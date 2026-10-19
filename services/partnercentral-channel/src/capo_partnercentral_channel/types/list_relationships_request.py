"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListRelationshipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.account_id_list
    import capo_partnercentral_channel.types.association_type_list
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.list_relationships_sort_base
    import capo_partnercentral_channel.types.next_token
    import capo_partnercentral_channel.types.program_management_account_identifier_list
    import capo_partnercentral_channel.types.relationship_display_name_list


class ListRelationshipsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier to filter relationships.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call.</p>"""
    associated_account_ids: NotRequired[
        "capo_partnercentral_channel.types.account_id_list.AccountIdList"
    ]
    """<p>Filter by associated AWS account IDs.</p>"""
    association_types: NotRequired[
        "capo_partnercentral_channel.types.association_type_list.AssociationTypeList"
    ]
    """<p>Filter by association types.</p>"""
    display_names: NotRequired[
        "capo_partnercentral_channel.types.relationship_display_name_list.RelationshipDisplayNameList"
    ]
    """<p>Filter by display names.</p>"""
    program_management_account_identifiers: NotRequired[
        "capo_partnercentral_channel.types.program_management_account_identifier_list.ProgramManagementAccountIdentifierList"
    ]
    """<p>Filter by program management account identifiers.</p>"""
    sort: NotRequired[
        "capo_partnercentral_channel.types.list_relationships_sort_base.ListRelationshipsSortBase"
    ]
    """<p>Sorting options for the results.</p>"""
    next_token: NotRequired["capo_partnercentral_channel.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRelationshipsRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "associated_account_ids" in value:
        import capo_partnercentral_channel.types.account_id_list

        out["associatedAccountIds"] = (
            capo_partnercentral_channel.types.account_id_list.serialize_aws_json_1_0(
                value["associated_account_ids"]
            )
        )
    if "association_types" in value:
        import capo_partnercentral_channel.types.association_type_list

        out["associationTypes"] = (
            capo_partnercentral_channel.types.association_type_list.serialize_aws_json_1_0(
                value["association_types"]
            )
        )
    if "display_names" in value:
        import capo_partnercentral_channel.types.relationship_display_name_list

        out["displayNames"] = (
            capo_partnercentral_channel.types.relationship_display_name_list.serialize_aws_json_1_0(
                value["display_names"]
            )
        )
    if "program_management_account_identifiers" in value:
        import capo_partnercentral_channel.types.program_management_account_identifier_list

        out["programManagementAccountIdentifiers"] = (
            capo_partnercentral_channel.types.program_management_account_identifier_list.serialize_aws_json_1_0(
                value["program_management_account_identifiers"]
            )
        )
    if "sort" in value:
        import capo_partnercentral_channel.types.list_relationships_sort_base

        out["sort"] = (
            capo_partnercentral_channel.types.list_relationships_sort_base.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRelationshipsRequest:
    out: ListRelationshipsRequest = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("ListRelationshipsRequest.catalog required")
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("associatedAccountIds") is not None:
        import capo_partnercentral_channel.types.account_id_list

        out["associated_account_ids"] = (
            capo_partnercentral_channel.types.account_id_list.deserialize_aws_json_1_0(
                data["associatedAccountIds"]
            )
        )
    if data.get("associationTypes") is not None:
        import capo_partnercentral_channel.types.association_type_list

        out["association_types"] = (
            capo_partnercentral_channel.types.association_type_list.deserialize_aws_json_1_0(
                data["associationTypes"]
            )
        )
    if data.get("displayNames") is not None:
        import capo_partnercentral_channel.types.relationship_display_name_list

        out["display_names"] = (
            capo_partnercentral_channel.types.relationship_display_name_list.deserialize_aws_json_1_0(
                data["displayNames"]
            )
        )
    if data.get("programManagementAccountIdentifiers") is not None:
        import capo_partnercentral_channel.types.program_management_account_identifier_list

        out["program_management_account_identifiers"] = (
            capo_partnercentral_channel.types.program_management_account_identifier_list.deserialize_aws_json_1_0(
                data["programManagementAccountIdentifiers"]
            )
        )
    if data.get("sort") is not None:
        import capo_partnercentral_channel.types.list_relationships_sort_base

        out["sort"] = (
            capo_partnercentral_channel.types.list_relationships_sort_base.deserialize_aws_json_1_0(
                data["sort"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
