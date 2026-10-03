"""Generated from Smithy shape ``com.amazonaws.kendra#CustomDocumentEnrichmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.hook_configuration
    import capo_kendra.types.inline_custom_document_enrichment_configuration_list
    import capo_kendra.types.role_arn


class CustomDocumentEnrichmentConfiguration(TypedDict, closed=True):
    inline_configurations: NotRequired[
        "capo_kendra.types.inline_custom_document_enrichment_configuration_list.InlineCustomDocumentEnrichmentConfigurationList"
    ]
    """<p>Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Kendra.</p>"""
    pre_extraction_hook_configuration: NotRequired[
        "capo_kendra.types.hook_configuration.HookConfiguration"
    ]
    """<p>Configuration information for invoking a Lambda function in Lambda on the original or raw documents before extracting their metadata and text. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation">Advanced data manipulation</a>.</p>"""
    post_extraction_hook_configuration: NotRequired[
        "capo_kendra.types.hook_configuration.HookConfiguration"
    ]
    """<p>Configuration information for invoking a Lambda function in Lambda on the structured documents with their metadata and text extracted. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation">Advanced data manipulation</a>.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to run <code>PreExtractionHookConfiguration</code> and <code>PostExtractionHookConfiguration</code> for altering document metadata and content during the document ingestion process. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">an IAM roles for Amazon Kendra</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomDocumentEnrichmentConfiguration) -> dict:
    out: dict = {}
    if "inline_configurations" in value:
        import capo_kendra.types.inline_custom_document_enrichment_configuration_list

        out["InlineConfigurations"] = (
            capo_kendra.types.inline_custom_document_enrichment_configuration_list.serialize_aws_json_1_1(
                value["inline_configurations"]
            )
        )
    if "pre_extraction_hook_configuration" in value:
        import capo_kendra.types.hook_configuration

        out["PreExtractionHookConfiguration"] = (
            capo_kendra.types.hook_configuration.serialize_aws_json_1_1(
                value["pre_extraction_hook_configuration"]
            )
        )
    if "post_extraction_hook_configuration" in value:
        import capo_kendra.types.hook_configuration

        out["PostExtractionHookConfiguration"] = (
            capo_kendra.types.hook_configuration.serialize_aws_json_1_1(
                value["post_extraction_hook_configuration"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomDocumentEnrichmentConfiguration:
    out: CustomDocumentEnrichmentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InlineConfigurations") is not None:
        import capo_kendra.types.inline_custom_document_enrichment_configuration_list

        out["inline_configurations"] = (
            capo_kendra.types.inline_custom_document_enrichment_configuration_list.deserialize_aws_json_1_1(
                data["InlineConfigurations"]
            )
        )
    if data.get("PreExtractionHookConfiguration") is not None:
        import capo_kendra.types.hook_configuration

        out["pre_extraction_hook_configuration"] = (
            capo_kendra.types.hook_configuration.deserialize_aws_json_1_1(
                data["PreExtractionHookConfiguration"]
            )
        )
    if data.get("PostExtractionHookConfiguration") is not None:
        import capo_kendra.types.hook_configuration

        out["post_extraction_hook_configuration"] = (
            capo_kendra.types.hook_configuration.deserialize_aws_json_1_1(
                data["PostExtractionHookConfiguration"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
