"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#CreateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.client_token
    import capo_pca_connector_ad.types.connector_arn
    import capo_pca_connector_ad.types.tags
    import capo_pca_connector_ad.types.template_definition
    import capo_pca_connector_ad.types.template_name


class CreateTemplateRequest(TypedDict, closed=True):
    connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>"""
    name: "capo_pca_connector_ad.types.template_name.TemplateName"
    """<p>Name of the template. The template name must be unique.</p>"""
    definition: "capo_pca_connector_ad.types.template_definition.TemplateDefinition"
    """<p>Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.</p>"""
    client_token: NotRequired["capo_pca_connector_ad.types.client_token.ClientToken"]
    """<p>Idempotency token.</p>"""
    tags: NotRequired["capo_pca_connector_ad.types.tags.Tags"]
    """<p>Metadata assigned to a template consisting of a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateRequest) -> dict:
    out: dict = {}
    out["ConnectorArn"] = value["connector_arn"]
    out["Name"] = value["name"]
    import capo_pca_connector_ad.types.template_definition

    out["Definition"] = capo_pca_connector_ad.types.template_definition.serialize_json(
        value["definition"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_pca_connector_ad.types.tags

        out["Tags"] = capo_pca_connector_ad.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTemplateRequest:
    out: CreateTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorArn") is not None:
        out["connector_arn"] = data["ConnectorArn"]
    else:
        raise DeserializationError("CreateTemplateRequest.connector_arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateTemplateRequest.name required")
    if data.get("Definition") is not None:
        import capo_pca_connector_ad.types.template_definition

        out["definition"] = (
            capo_pca_connector_ad.types.template_definition.deserialize_json(
                data["Definition"]
            )
        )
    else:
        raise DeserializationError("CreateTemplateRequest.definition required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_pca_connector_ad.types.tags

        out["tags"] = capo_pca_connector_ad.types.tags.deserialize_json(data["Tags"])
    return out
