"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateEngagementRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.engagement_contexts
    import capo_partnercentral_selling.types.engagement_description
    import capo_partnercentral_selling.types.engagement_title


class CreateEngagementRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>The <code>CreateEngagementRequest$Catalog</code> parameter specifies the catalog related to the engagement. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement is managed.</p>"""
    client_token: "capo_partnercentral_selling.types.client_token.ClientToken"
    """<p>The <code>CreateEngagementRequest$ClientToken</code> parameter specifies a unique, case-sensitive identifier to ensure that the request is handled exactly once. The value must not exceed sixty-four alphanumeric characters.</p>"""
    title: NotRequired[
        "capo_partnercentral_selling.types.engagement_title.EngagementTitle"
    ]
    """<p>Specifies the title of the <code>Engagement</code>.</p>"""
    description: NotRequired[
        "capo_partnercentral_selling.types.engagement_description.EngagementDescription"
    ]
    """<p>Provides a description of the <code>Engagement</code>.</p>"""
    contexts: NotRequired[
        "capo_partnercentral_selling.types.engagement_contexts.EngagementContexts"
    ]
    """<p>The <code>Contexts</code> field is a required array of objects, with a maximum of 5 contexts allowed, specifying detailed information about customer projects associated with the Engagement. Each context object contains a <code>Type</code> field indicating the context type, which must be <code>CustomerProject</code> in this version, and a <code>Payload</code> field containing the <code>CustomerProject</code> details. The <code>CustomerProject</code> object is composed of two main components: <code>Customer</code> and <code>Project</code>. The <code>Customer</code> object includes information such as <code>CompanyName</code>, <code>WebsiteUrl</code>, <code>Industry</code>, and <code>CountryCode</code>, providing essential details about the customer. The <code>Project</code> object contains <code>Title</code>, <code>BusinessProblem</code>, and <code>TargetCompletionDate</code>, offering insights into the specific project associated with the customer. This structure allows comprehensive context to be included within the Engagement, facilitating effective collaboration between parties by providing relevant customer and project information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEngagementRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "contexts" in value:
        import capo_partnercentral_selling.types.engagement_contexts

        out["Contexts"] = (
            capo_partnercentral_selling.types.engagement_contexts.serialize_aws_json_1_0(
                value["contexts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEngagementRequest:
    out: CreateEngagementRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Contexts") is not None:
        import capo_partnercentral_selling.types.engagement_contexts

        out["contexts"] = (
            capo_partnercentral_selling.types.engagement_contexts.deserialize_aws_json_1_0(
                data["Contexts"]
            )
        )
    return out


def redact_sensitive(value: CreateEngagementRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contexts" in value:
        import capo_partnercentral_selling.types.engagement_contexts

        out["contexts"] = (
            capo_partnercentral_selling.types.engagement_contexts.redact_sensitive(
                value["contexts"]
            )
        )
    return out
