"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#Template``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pca_connector_ad.types.connector_arn
    import capo_pca_connector_ad.types.custom_object_identifier
    import capo_pca_connector_ad.types.template_arn
    import capo_pca_connector_ad.types.template_definition
    import capo_pca_connector_ad.types.template_name
    import capo_pca_connector_ad.types.template_revision
    import capo_pca_connector_ad.types.template_status


class Template(TypedDict, closed=True):
    arn: NotRequired["capo_pca_connector_ad.types.template_arn.TemplateArn"]
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>"""
    connector_arn: NotRequired["capo_pca_connector_ad.types.connector_arn.ConnectorArn"]
    """<p> The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>"""
    definition: NotRequired[
        "capo_pca_connector_ad.types.template_definition.TemplateDefinition"
    ]
    """<p>Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.</p>"""
    name: NotRequired["capo_pca_connector_ad.types.template_name.TemplateName"]
    """<p>Name of the templates. Template names must be unique.</p>"""
    object_identifier: NotRequired[
        "capo_pca_connector_ad.types.custom_object_identifier.CustomObjectIdentifier"
    ]
    """<p>Object identifier of a template.</p>"""
    policy_schema: NotRequired["int"]
    """<p>The template schema version. Template schema versions can be v2, v3, or v4. The template configuration options change based on the template schema version.</p>"""
    status: NotRequired["capo_pca_connector_ad.types.template_status.TemplateStatus"]
    """<p>Status of the template. Status can be creating, active, deleting, or failed.</p>"""
    revision: NotRequired[
        "capo_pca_connector_ad.types.template_revision.TemplateRevision"
    ]
    """<p>The version of the template. Template updates will increment the minor revision. Re-enrolling all certificate holders will increment the major revision.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the template was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the template was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Template) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "definition" in value:
        import capo_pca_connector_ad.types.template_definition

        out["Definition"] = (
            capo_pca_connector_ad.types.template_definition.serialize_json(
                value["definition"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "object_identifier" in value:
        out["ObjectIdentifier"] = value["object_identifier"]
    if "policy_schema" in value:
        out["PolicySchema"] = value["policy_schema"]
    if "status" in value:
        import capo_pca_connector_ad.types.template_status

        out["Status"] = capo_pca_connector_ad.types.template_status.serialize_json(
            value["status"]
        )
    if "revision" in value:
        import capo_pca_connector_ad.types.template_revision

        out["Revision"] = capo_pca_connector_ad.types.template_revision.serialize_json(
            value["revision"]
        )
    if "created_at" in value:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["CreatedAt"] = (
            capo_pca_connector_ad.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["UpdatedAt"] = (
            capo_pca_connector_ad.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> Template:
    out: Template = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ConnectorArn") is not None:
        out["connector_arn"] = data["ConnectorArn"]
    if data.get("Definition") is not None:
        import capo_pca_connector_ad.types.template_definition

        out["definition"] = (
            capo_pca_connector_ad.types.template_definition.deserialize_json(
                data["Definition"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ObjectIdentifier") is not None:
        out["object_identifier"] = data["ObjectIdentifier"]
    if data.get("PolicySchema") is not None:
        out["policy_schema"] = data["PolicySchema"]
    if data.get("Status") is not None:
        import capo_pca_connector_ad.types.template_status

        out["status"] = capo_pca_connector_ad.types.template_status.deserialize_json(
            data["Status"]
        )
    if data.get("Revision") is not None:
        import capo_pca_connector_ad.types.template_revision

        out["revision"] = (
            capo_pca_connector_ad.types.template_revision.deserialize_json(
                data["Revision"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["created_at"] = (
            capo_pca_connector_ad.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["updated_at"] = (
            capo_pca_connector_ad.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    return out
