"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#UpdateRelationshipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.program_management_account_identifier
    import capo_partnercentral_channel.types.relationship_display_name
    import capo_partnercentral_channel.types.relationship_identifier
    import capo_partnercentral_channel.types.revision
    import capo_partnercentral_channel.types.support_plan


class UpdateRelationshipRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the relationship.</p>"""
    identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier"
    """<p>The unique identifier of the relationship to update.</p>"""
    program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
    """<p>The identifier of the program management account associated with the relationship.</p>"""
    revision: NotRequired["capo_partnercentral_channel.types.revision.Revision"]
    """<p>The current revision number of the relationship.</p>"""
    display_name: NotRequired[
        "capo_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName"
    ]
    """<p>The new display name for the relationship.</p>"""
    requested_support_plan: NotRequired[
        "capo_partnercentral_channel.types.support_plan.SupportPlan"
    ]
    """<p>The updated support plan for the relationship.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRelationshipRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    out["identifier"] = value["identifier"]
    out["programManagementAccountIdentifier"] = value[
        "program_management_account_identifier"
    ]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "requested_support_plan" in value:
        import capo_partnercentral_channel.types.support_plan

        out["requestedSupportPlan"] = (
            capo_partnercentral_channel.types.support_plan.serialize_aws_json_1_0(
                value["requested_support_plan"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRelationshipRequest:
    out: UpdateRelationshipRequest = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("programManagementAccountIdentifier") is not None:
        out["program_management_account_identifier"] = data[
            "programManagementAccountIdentifier"
        ]
    else:
        out["program_management_account_identifier"] = ""
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("requestedSupportPlan") is not None:
        import capo_partnercentral_channel.types.support_plan

        out["requested_support_plan"] = (
            capo_partnercentral_channel.types.support_plan.deserialize_aws_json_1_0(
                data["requestedSupportPlan"]
            )
        )
    return out
