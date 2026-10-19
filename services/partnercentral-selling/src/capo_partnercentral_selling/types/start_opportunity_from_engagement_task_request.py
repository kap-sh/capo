"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#StartOpportunityFromEngagementTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.context_identifier
    import capo_partnercentral_selling.types.engagement_arn_or_identifier
    import capo_partnercentral_selling.types.tag_list


class StartOpportunityFromEngagementTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which the opportunity creation task is executed. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>"""
    client_token: "capo_partnercentral_selling.types.client_token.ClientToken"
    """<p>A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.</p>"""
    identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier"
    """<p>The unique identifier of the engagement from which the opportunity creation task is to be initiated. This helps ensure that the task is applied to the correct engagement.</p>"""
    context_identifier: (
        "capo_partnercentral_selling.types.context_identifier.ContextIdentifier"
    )
    """<p>The unique identifier of the engagement context from which to create the opportunity. This specifies the specific contextual information within the engagement that will be used for opportunity creation.</p>"""
    tags: NotRequired["capo_partnercentral_selling.types.tag_list.TagList"]
    """<p>A map of the key-value pairs of the tag or tags to assign.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartOpportunityFromEngagementTaskRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    out["Identifier"] = value["identifier"]
    out["ContextIdentifier"] = value["context_identifier"]
    if "tags" in value:
        import capo_partnercentral_selling.types.tag_list

        out["Tags"] = capo_partnercentral_selling.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartOpportunityFromEngagementTaskRequest:
    out: StartOpportunityFromEngagementTaskRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("ContextIdentifier") is not None:
        out["context_identifier"] = data["ContextIdentifier"]
    else:
        out["context_identifier"] = ""
    if data.get("Tags") is not None:
        import capo_partnercentral_selling.types.tag_list

        out["tags"] = (
            capo_partnercentral_selling.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
