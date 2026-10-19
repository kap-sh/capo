"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateRelationshipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.account_id
    import capo_partnercentral_channel.types.association_type
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.client_token
    import capo_partnercentral_channel.types.program_management_account_identifier
    import capo_partnercentral_channel.types.relationship_display_name
    import capo_partnercentral_channel.types.resale_account_model
    import capo_partnercentral_channel.types.sector
    import capo_partnercentral_channel.types.support_plan
    import capo_partnercentral_channel.types.tag_list


class CreateRelationshipRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the relationship.</p>"""
    association_type: (
        "capo_partnercentral_channel.types.association_type.AssociationType"
    )
    """<p>The type of association for the relationship (e.g., reseller, distributor).</p>"""
    program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
    """<p>The identifier of the program management account for this relationship.</p>"""
    associated_account_id: "capo_partnercentral_channel.types.account_id.AccountId"
    """<p>The AWS account ID to associate in this relationship.</p>"""
    display_name: "capo_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName"
    """<p>A human-readable name for the relationship.</p>"""
    resale_account_model: NotRequired[
        "capo_partnercentral_channel.types.resale_account_model.ResaleAccountModel"
    ]
    """<p>The resale account model for the relationship.</p>"""
    sector: "capo_partnercentral_channel.types.sector.Sector"
    """<p>The business sector for the relationship.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_channel.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    tags: NotRequired["capo_partnercentral_channel.types.tag_list.TagList"]
    """<p>Key-value pairs to associate with the relationship.</p>"""
    requested_support_plan: NotRequired[
        "capo_partnercentral_channel.types.support_plan.SupportPlan"
    ]
    """<p>The support plan requested for this relationship.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRelationshipRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    import capo_partnercentral_channel.types.association_type

    out["associationType"] = (
        capo_partnercentral_channel.types.association_type.serialize_aws_json_1_0(
            value["association_type"]
        )
    )
    out["programManagementAccountIdentifier"] = value[
        "program_management_account_identifier"
    ]
    out["associatedAccountId"] = value["associated_account_id"]
    out["displayName"] = value["display_name"]
    if "resale_account_model" in value:
        import capo_partnercentral_channel.types.resale_account_model

        out["resaleAccountModel"] = (
            capo_partnercentral_channel.types.resale_account_model.serialize_aws_json_1_0(
                value["resale_account_model"]
            )
        )
    import capo_partnercentral_channel.types.sector

    out["sector"] = capo_partnercentral_channel.types.sector.serialize_aws_json_1_0(
        value["sector"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_partnercentral_channel.types.tag_list

        out["tags"] = capo_partnercentral_channel.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "requested_support_plan" in value:
        import capo_partnercentral_channel.types.support_plan

        out["requestedSupportPlan"] = (
            capo_partnercentral_channel.types.support_plan.serialize_aws_json_1_0(
                value["requested_support_plan"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRelationshipRequest:
    out: CreateRelationshipRequest = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    if data.get("associationType") is not None:
        import capo_partnercentral_channel.types.association_type

        out["association_type"] = (
            capo_partnercentral_channel.types.association_type.deserialize_aws_json_1_0(
                data["associationType"]
            )
        )
    else:
        import typing

        out["association_type"] = typing.cast(
            "capo_partnercentral_channel.types.association_type.AssociationType", ""
        )
    if data.get("programManagementAccountIdentifier") is not None:
        out["program_management_account_identifier"] = data[
            "programManagementAccountIdentifier"
        ]
    else:
        out["program_management_account_identifier"] = ""
    if data.get("associatedAccountId") is not None:
        out["associated_account_id"] = data["associatedAccountId"]
    else:
        out["associated_account_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("resaleAccountModel") is not None:
        import capo_partnercentral_channel.types.resale_account_model

        out["resale_account_model"] = (
            capo_partnercentral_channel.types.resale_account_model.deserialize_aws_json_1_0(
                data["resaleAccountModel"]
            )
        )
    if data.get("sector") is not None:
        import capo_partnercentral_channel.types.sector

        out["sector"] = (
            capo_partnercentral_channel.types.sector.deserialize_aws_json_1_0(
                data["sector"]
            )
        )
    else:
        import typing

        out["sector"] = typing.cast(
            "capo_partnercentral_channel.types.sector.Sector", ""
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_partnercentral_channel.types.tag_list

        out["tags"] = (
            capo_partnercentral_channel.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    if data.get("requestedSupportPlan") is not None:
        import capo_partnercentral_channel.types.support_plan

        out["requested_support_plan"] = (
            capo_partnercentral_channel.types.support_plan.deserialize_aws_json_1_0(
                data["requestedSupportPlan"]
            )
        )
    return out
