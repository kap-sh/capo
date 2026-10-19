"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#DeleteRelationshipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.client_token
    import capo_partnercentral_channel.types.program_management_account_identifier
    import capo_partnercentral_channel.types.relationship_identifier


class DeleteRelationshipRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the relationship.</p>"""
    identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier"
    """<p>The unique identifier of the relationship to delete.</p>"""
    program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
    """<p>The identifier of the program management account associated with the relationship.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_channel.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRelationshipRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    out["identifier"] = value["identifier"]
    out["programManagementAccountIdentifier"] = value[
        "program_management_account_identifier"
    ]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRelationshipRequest:
    out: DeleteRelationshipRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
