"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#StartEngagementByAcceptingInvitationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier
    import capo_partnercentral_selling.types.tag_list


class StartEngagementByAcceptingInvitationTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog related to the task. Use <code>AWS</code> for production engagements and <code>Sandbox</code> for testing scenarios.</p>"""
    client_token: "capo_partnercentral_selling.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier provided by the client that helps to ensure the idempotency of the request. This can be a random or meaningful string but must be unique for each request.</p>"""
    identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier"
    """<p>Specifies the unique identifier of the <code>EngagementInvitation</code> to be accepted. Providing the correct identifier helps ensure that the correct engagement is processed.</p>"""
    tags: NotRequired["capo_partnercentral_selling.types.tag_list.TagList"]
    """<p>A map of the key-value pairs of the tag or tags to assign.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: StartEngagementByAcceptingInvitationTaskRequest,
) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    out["Identifier"] = value["identifier"]
    if "tags" in value:
        import capo_partnercentral_selling.types.tag_list

        out["Tags"] = capo_partnercentral_selling.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> StartEngagementByAcceptingInvitationTaskRequest:
    out: StartEngagementByAcceptingInvitationTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("Tags") is not None:
        import capo_partnercentral_selling.types.tag_list

        out["tags"] = (
            capo_partnercentral_selling.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
