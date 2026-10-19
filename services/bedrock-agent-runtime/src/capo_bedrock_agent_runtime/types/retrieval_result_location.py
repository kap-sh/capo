"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retrieval_result_confluence_location
    import capo_bedrock_agent_runtime.types.retrieval_result_custom_document_location
    import capo_bedrock_agent_runtime.types.retrieval_result_google_drive_location
    import capo_bedrock_agent_runtime.types.retrieval_result_kendra_document_location
    import capo_bedrock_agent_runtime.types.retrieval_result_location_type
    import capo_bedrock_agent_runtime.types.retrieval_result_one_drive_location
    import capo_bedrock_agent_runtime.types.retrieval_result_s3_location
    import capo_bedrock_agent_runtime.types.retrieval_result_salesforce_location
    import capo_bedrock_agent_runtime.types.retrieval_result_share_point_location
    import capo_bedrock_agent_runtime.types.retrieval_result_sql_location
    import capo_bedrock_agent_runtime.types.retrieval_result_web_location


class RetrievalResultLocation(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.retrieval_result_location_type.RetrievalResultLocationType"
    """<p>The type of data source location.</p>"""
    s3_location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_s3_location.RetrievalResultS3Location"
    ]
    """<p>The S3 data source location.</p>"""
    web_location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_web_location.RetrievalResultWebLocation"
    ]
    """<p>The web URL/URLs data source location.</p>"""
    confluence_location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_confluence_location.RetrievalResultConfluenceLocation"
    ]
    """<p>The Confluence data source location.</p>"""
    salesforce_location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_salesforce_location.RetrievalResultSalesforceLocation"
    ]
    """<p>The Salesforce data source location.</p>"""
    share_point_location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_share_point_location.RetrievalResultSharePointLocation"
    ]
    """<p>The SharePoint data source location.</p>"""
    custom_document_location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_custom_document_location.RetrievalResultCustomDocumentLocation"
    ]
    """<p>Specifies the location of a document in a custom data source.</p>"""
    kendra_document_location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_kendra_document_location.RetrievalResultKendraDocumentLocation"
    ]
    """<p>The location of a document in Amazon Kendra.</p>"""
    sql_location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_sql_location.RetrievalResultSqlLocation"
    ]
    """<p>Specifies information about the SQL query used to retrieve the result.</p>"""
    one_drive_location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_one_drive_location.RetrievalResultOneDriveLocation"
    ]
    """<p>The Microsoft OneDrive data source location.</p>"""
    google_drive_location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_google_drive_location.RetrievalResultGoogleDriveLocation"
    ]
    """<p>The Google Drive data source location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultLocation) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.retrieval_result_location_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.retrieval_result_location_type.serialize_json(
            value["type"]
        )
    )
    if "s3_location" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_s3_location

        out["s3Location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_s3_location.serialize_json(
                value["s3_location"]
            )
        )
    if "web_location" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_web_location

        out["webLocation"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_web_location.serialize_json(
                value["web_location"]
            )
        )
    if "confluence_location" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_confluence_location

        out["confluenceLocation"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_confluence_location.serialize_json(
                value["confluence_location"]
            )
        )
    if "salesforce_location" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_salesforce_location

        out["salesforceLocation"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_salesforce_location.serialize_json(
                value["salesforce_location"]
            )
        )
    if "share_point_location" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_share_point_location

        out["sharePointLocation"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_share_point_location.serialize_json(
                value["share_point_location"]
            )
        )
    if "custom_document_location" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_custom_document_location

        out["customDocumentLocation"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_custom_document_location.serialize_json(
                value["custom_document_location"]
            )
        )
    if "kendra_document_location" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_kendra_document_location

        out["kendraDocumentLocation"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_kendra_document_location.serialize_json(
                value["kendra_document_location"]
            )
        )
    if "sql_location" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_sql_location

        out["sqlLocation"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_sql_location.serialize_json(
                value["sql_location"]
            )
        )
    if "one_drive_location" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_one_drive_location

        out["oneDriveLocation"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_one_drive_location.serialize_json(
                value["one_drive_location"]
            )
        )
    if "google_drive_location" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_google_drive_location

        out["googleDriveLocation"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_google_drive_location.serialize_json(
                value["google_drive_location"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrievalResultLocation:
    out: RetrievalResultLocation = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_location_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_location_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.retrieval_result_location_type.RetrievalResultLocationType",
            "",
        )
    if data.get("s3Location") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_s3_location

        out["s3_location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_s3_location.deserialize_json(
                data["s3Location"]
            )
        )
    if data.get("webLocation") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_web_location

        out["web_location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_web_location.deserialize_json(
                data["webLocation"]
            )
        )
    if data.get("confluenceLocation") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_confluence_location

        out["confluence_location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_confluence_location.deserialize_json(
                data["confluenceLocation"]
            )
        )
    if data.get("salesforceLocation") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_salesforce_location

        out["salesforce_location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_salesforce_location.deserialize_json(
                data["salesforceLocation"]
            )
        )
    if data.get("sharePointLocation") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_share_point_location

        out["share_point_location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_share_point_location.deserialize_json(
                data["sharePointLocation"]
            )
        )
    if data.get("customDocumentLocation") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_custom_document_location

        out["custom_document_location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_custom_document_location.deserialize_json(
                data["customDocumentLocation"]
            )
        )
    if data.get("kendraDocumentLocation") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_kendra_document_location

        out["kendra_document_location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_kendra_document_location.deserialize_json(
                data["kendraDocumentLocation"]
            )
        )
    if data.get("sqlLocation") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_sql_location

        out["sql_location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_sql_location.deserialize_json(
                data["sqlLocation"]
            )
        )
    if data.get("oneDriveLocation") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_one_drive_location

        out["one_drive_location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_one_drive_location.deserialize_json(
                data["oneDriveLocation"]
            )
        )
    if data.get("googleDriveLocation") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_google_drive_location

        out["google_drive_location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_google_drive_location.deserialize_json(
                data["googleDriveLocation"]
            )
        )
    return out
