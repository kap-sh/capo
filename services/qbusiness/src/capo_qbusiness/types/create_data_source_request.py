"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.data_source_configuration
    import capo_qbusiness.types.data_source_name
    import capo_qbusiness.types.data_source_vpc_configuration
    import capo_qbusiness.types.description
    import capo_qbusiness.types.document_enrichment_configuration
    import capo_qbusiness.types.index_id
    import capo_qbusiness.types.media_extraction_configuration
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.sync_schedule
    import capo_qbusiness.types.tags


class CreateDataSourceRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p> The identifier of the Amazon Q Business application the data source will be attached to.</p>"""
    index_id: "capo_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index that you want to use with the data source connector.</p>"""
    display_name: "capo_qbusiness.types.data_source_name.DataSourceName"
    """<p>A name for the data source connector.</p>"""
    configuration: (
        "capo_qbusiness.types.data_source_configuration.DataSourceConfiguration"
    )
    """<p>Configuration information to connect your data source repository to Amazon Q Business. Use this parameter to provide a JSON schema with configuration information specific to your data source connector.</p> <p>Each data source has a JSON schema provided by Amazon Q Business that you must use. For example, the Amazon S3 and Web Crawler connectors require the following JSON schemas:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-api.html">Amazon S3 JSON schema</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-api.html">Web Crawler JSON schema</a> </p> </li> </ul> <p>You can find configuration templates for your specific data source using the following steps:</p> <ol> <li> <p>Navigate to the <a href="https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connectors-list.html">Supported connectors</a> page in the Amazon Q Business User Guide, and select the data source of your choice.</p> </li> <li> <p>Then, from your specific data source connector page, select <b>Using the API</b>. You will find the JSON schema for your data source, including parameter descriptions, in this section.</p> </li> </ol>"""
    vpc_configuration: NotRequired[
        "capo_qbusiness.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    """<p>Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connector-vpc.html">Using Amazon VPC with Amazon Q Business connectors</a>.</p>"""
    description: NotRequired["capo_qbusiness.types.description.Description"]
    """<p>A description for the data source connector.</p>"""
    tags: NotRequired["capo_qbusiness.types.tags.Tags"]
    """<p>A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    sync_schedule: NotRequired["capo_qbusiness.types.sync_schedule.SyncSchedule"]
    """<p>Sets the frequency for Amazon Q Business to check the documents in your data source repository and update your index. If you don't set a schedule, Amazon Q Business won't periodically update the index.</p> <p>Specify a <code>cron-</code> format schedule string or an empty string to indicate that the index is updated on demand. You can't specify the <code>Schedule</code> parameter when the <code>Type</code> parameter is set to <code>CUSTOM</code>. If you do, you receive a <code>ValidationException</code> exception. </p>"""
    role_arn: NotRequired["capo_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources. This field is required for all connector types except custom connectors, where it is optional.</p>"""
    client_token: NotRequired["capo_qbusiness.types.client_token.ClientToken"]
    """<p>A token you provide to identify a request to create a data source connector. Multiple calls to the <code>CreateDataSource</code> API with the same client token will create only one data source connector. </p>"""
    document_enrichment_configuration: NotRequired[
        "capo_qbusiness.types.document_enrichment_configuration.DocumentEnrichmentConfiguration"
    ]
    media_extraction_configuration: NotRequired[
        "capo_qbusiness.types.media_extraction_configuration.MediaExtractionConfiguration"
    ]
    """<p>The configuration for extracting information from media in documents during ingestion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    out["configuration"] = value["configuration"]
    if "vpc_configuration" in value:
        import capo_qbusiness.types.data_source_vpc_configuration

        out["vpcConfiguration"] = (
            capo_qbusiness.types.data_source_vpc_configuration.serialize_json(
                value["vpc_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.serialize_json(value["tags"])
    if "sync_schedule" in value:
        out["syncSchedule"] = value["sync_schedule"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "document_enrichment_configuration" in value:
        import capo_qbusiness.types.document_enrichment_configuration

        out["documentEnrichmentConfiguration"] = (
            capo_qbusiness.types.document_enrichment_configuration.serialize_json(
                value["document_enrichment_configuration"]
            )
        )
    if "media_extraction_configuration" in value:
        import capo_qbusiness.types.media_extraction_configuration

        out["mediaExtractionConfiguration"] = (
            capo_qbusiness.types.media_extraction_configuration.serialize_json(
                value["media_extraction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDataSourceRequest:
    out: CreateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateDataSourceRequest.display_name required")
    if data.get("configuration") is not None:
        out["configuration"] = data["configuration"]
    else:
        raise DeserializationError("CreateDataSourceRequest.configuration required")
    if data.get("vpcConfiguration") is not None:
        import capo_qbusiness.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            capo_qbusiness.types.data_source_vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.deserialize_json(data["tags"])
    if data.get("syncSchedule") is not None:
        out["sync_schedule"] = data["syncSchedule"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("documentEnrichmentConfiguration") is not None:
        import capo_qbusiness.types.document_enrichment_configuration

        out["document_enrichment_configuration"] = (
            capo_qbusiness.types.document_enrichment_configuration.deserialize_json(
                data["documentEnrichmentConfiguration"]
            )
        )
    if data.get("mediaExtractionConfiguration") is not None:
        import capo_qbusiness.types.media_extraction_configuration

        out["media_extraction_configuration"] = (
            capo_qbusiness.types.media_extraction_configuration.deserialize_json(
                data["mediaExtractionConfiguration"]
            )
        )
    return out
