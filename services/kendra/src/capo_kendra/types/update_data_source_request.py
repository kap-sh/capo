"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.custom_document_enrichment_configuration
    import capo_kendra.types.data_source_configuration
    import capo_kendra.types.data_source_id
    import capo_kendra.types.data_source_name
    import capo_kendra.types.data_source_vpc_configuration
    import capo_kendra.types.description
    import capo_kendra.types.index_id
    import capo_kendra.types.language_code
    import capo_kendra.types.role_arn
    import capo_kendra.types.scan_schedule


class UpdateDataSourceRequest(TypedDict, closed=True):
    id: "capo_kendra.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source connector you want to update.</p>"""
    name: NotRequired["capo_kendra.types.data_source_name.DataSourceName"]
    """<p>A new name for the data source connector.</p>"""
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index used with the data source connector.</p>"""
    configuration: NotRequired[
        "capo_kendra.types.data_source_configuration.DataSourceConfiguration"
    ]
    """<p>Configuration information you want to update for the data source connector.</p>"""
    vpc_configuration: NotRequired[
        "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    """<p>Configuration information for an Amazon Virtual Private Cloud to connect to your data source. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html">Configuring a VPC</a>.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>A new description for the data source connector.</p>"""
    schedule: NotRequired["capo_kendra.types.scan_schedule.ScanSchedule"]
    """<p>The sync schedule you want to update for the data source connector.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM roles for Amazon Kendra</a>.</p>"""
    language_code: NotRequired["capo_kendra.types.language_code.LanguageCode"]
    """<p>The code for a language you want to update for the data source connector. This allows you to support a language for all documents when updating the data source. English is supported by default. For more information on supported languages, including their codes, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html">Adding documents in languages other than English</a>.</p>"""
    custom_document_enrichment_configuration: NotRequired[
        "capo_kendra.types.custom_document_enrichment_configuration.CustomDocumentEnrichmentConfiguration"
    ]
    """<p>Configuration information you want to update for altering document metadata and content during the document ingestion process.</p> <p>For more information on how to create, modify and delete document metadata, or make other content alterations when you ingest documents into Amazon Kendra, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html">Customizing document metadata during the ingestion process</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDataSourceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    out["IndexId"] = value["index_id"]
    if "configuration" in value:
        import capo_kendra.types.data_source_configuration

        out["Configuration"] = (
            capo_kendra.types.data_source_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "vpc_configuration" in value:
        import capo_kendra.types.data_source_vpc_configuration

        out["VpcConfiguration"] = (
            capo_kendra.types.data_source_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    if "custom_document_enrichment_configuration" in value:
        import capo_kendra.types.custom_document_enrichment_configuration

        out["CustomDocumentEnrichmentConfiguration"] = (
            capo_kendra.types.custom_document_enrichment_configuration.serialize_aws_json_1_1(
                value["custom_document_enrichment_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDataSourceRequest:
    out: UpdateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateDataSourceRequest.id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("UpdateDataSourceRequest.index_id required")
    if data.get("Configuration") is not None:
        import capo_kendra.types.data_source_configuration

        out["configuration"] = (
            capo_kendra.types.data_source_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if data.get("VpcConfiguration") is not None:
        import capo_kendra.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            capo_kendra.types.data_source_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Schedule") is not None:
        out["schedule"] = data["Schedule"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    if data.get("CustomDocumentEnrichmentConfiguration") is not None:
        import capo_kendra.types.custom_document_enrichment_configuration

        out["custom_document_enrichment_configuration"] = (
            capo_kendra.types.custom_document_enrichment_configuration.deserialize_aws_json_1_1(
                data["CustomDocumentEnrichmentConfiguration"]
            )
        )
    return out
