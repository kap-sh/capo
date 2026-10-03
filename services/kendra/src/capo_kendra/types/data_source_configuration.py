"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.alfresco_configuration
    import capo_kendra.types.box_configuration
    import capo_kendra.types.confluence_configuration
    import capo_kendra.types.database_configuration
    import capo_kendra.types.fsx_configuration
    import capo_kendra.types.git_hub_configuration
    import capo_kendra.types.google_drive_configuration
    import capo_kendra.types.jira_configuration
    import capo_kendra.types.one_drive_configuration
    import capo_kendra.types.quip_configuration
    import capo_kendra.types.s3_data_source_configuration
    import capo_kendra.types.salesforce_configuration
    import capo_kendra.types.service_now_configuration
    import capo_kendra.types.share_point_configuration
    import capo_kendra.types.slack_configuration
    import capo_kendra.types.template_configuration
    import capo_kendra.types.web_crawler_configuration
    import capo_kendra.types.work_docs_configuration


class DataSourceConfiguration(TypedDict, closed=True):
    s3_configuration: NotRequired[
        "capo_kendra.types.s3_data_source_configuration.S3DataSourceConfiguration"
    ]
    """<p>Provides the configuration information to connect to an Amazon S3 bucket as your data source.</p> <note> <p>Amazon Kendra now supports an upgraded Amazon S3 connector.</p> <p>You must now use the <a href="https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html">TemplateConfiguration</a> object instead of the <code>S3DataSourceConfiguration</code> object to configure your connector.</p> <p>Connectors configured using the older console and API architecture will continue to function as configured. However, you won't be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.</p> <p>We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.</p> </note>"""
    share_point_configuration: NotRequired[
        "capo_kendra.types.share_point_configuration.SharePointConfiguration"
    ]
    """<p>Provides the configuration information to connect to Microsoft SharePoint as your data source.</p>"""
    database_configuration: NotRequired[
        "capo_kendra.types.database_configuration.DatabaseConfiguration"
    ]
    """<p>Provides the configuration information to connect to a database as your data source.</p>"""
    salesforce_configuration: NotRequired[
        "capo_kendra.types.salesforce_configuration.SalesforceConfiguration"
    ]
    """<p>Provides the configuration information to connect to Salesforce as your data source.</p>"""
    one_drive_configuration: NotRequired[
        "capo_kendra.types.one_drive_configuration.OneDriveConfiguration"
    ]
    """<p>Provides the configuration information to connect to Microsoft OneDrive as your data source.</p>"""
    service_now_configuration: NotRequired[
        "capo_kendra.types.service_now_configuration.ServiceNowConfiguration"
    ]
    """<p>Provides the configuration information to connect to ServiceNow as your data source.</p>"""
    confluence_configuration: NotRequired[
        "capo_kendra.types.confluence_configuration.ConfluenceConfiguration"
    ]
    """<p>Provides the configuration information to connect to Confluence as your data source.</p>"""
    google_drive_configuration: NotRequired[
        "capo_kendra.types.google_drive_configuration.GoogleDriveConfiguration"
    ]
    """<p>Provides the configuration information to connect to Google Drive as your data source.</p>"""
    web_crawler_configuration: NotRequired[
        "capo_kendra.types.web_crawler_configuration.WebCrawlerConfiguration"
    ]
    work_docs_configuration: NotRequired[
        "capo_kendra.types.work_docs_configuration.WorkDocsConfiguration"
    ]
    """<p>Provides the configuration information to connect to WorkDocs as your data source.</p>"""
    fsx_configuration: NotRequired[
        "capo_kendra.types.fsx_configuration.FsxConfiguration"
    ]
    """<p>Provides the configuration information to connect to Amazon FSx as your data source.</p> <note> <p>Amazon Kendra now supports an upgraded Amazon FSx Windows connector.</p> <p>You must now use the <a href="https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html">TemplateConfiguration</a> object instead of the <code>FsxConfiguration</code> object to configure your connector.</p> <p>Connectors configured using the older console and API architecture will continue to function as configured. However, you won't be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.</p> <p>We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.</p> </note>"""
    slack_configuration: NotRequired[
        "capo_kendra.types.slack_configuration.SlackConfiguration"
    ]
    """<p>Provides the configuration information to connect to Slack as your data source.</p> <note> <p>Amazon Kendra now supports an upgraded Slack connector.</p> <p>You must now use the <a href="https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html">TemplateConfiguration</a> object instead of the <code>SlackConfiguration</code> object to configure your connector.</p> <p>Connectors configured using the older console and API architecture will continue to function as configured. However, you won't be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.</p> <p>We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.</p> </note>"""
    box_configuration: NotRequired[
        "capo_kendra.types.box_configuration.BoxConfiguration"
    ]
    """<p>Provides the configuration information to connect to Box as your data source.</p>"""
    quip_configuration: NotRequired[
        "capo_kendra.types.quip_configuration.QuipConfiguration"
    ]
    """<p>Provides the configuration information to connect to Quip as your data source.</p>"""
    jira_configuration: NotRequired[
        "capo_kendra.types.jira_configuration.JiraConfiguration"
    ]
    """<p>Provides the configuration information to connect to Jira as your data source.</p>"""
    git_hub_configuration: NotRequired[
        "capo_kendra.types.git_hub_configuration.GitHubConfiguration"
    ]
    """<p>Provides the configuration information to connect to GitHub as your data source.</p> <note> <p>Amazon Kendra now supports an upgraded GitHub connector.</p> <p>You must now use the <a href="https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html">TemplateConfiguration</a> object instead of the <code>GitHubConfiguration</code> object to configure your connector.</p> <p>Connectors configured using the older console and API architecture will continue to function as configured. However, you won’t be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.</p> <p>We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.</p> </note>"""
    alfresco_configuration: NotRequired[
        "capo_kendra.types.alfresco_configuration.AlfrescoConfiguration"
    ]
    """<p>Provides the configuration information to connect to Alfresco as your data source.</p> <note> <p>Support for <code>AlfrescoConfiguration</code> ended May 2023. We recommend migrating to or using the Alfresco data source template schema / <a href="https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html">TemplateConfiguration</a> API.</p> </note>"""
    template_configuration: NotRequired[
        "capo_kendra.types.template_configuration.TemplateConfiguration"
    ]
    """<p>Provides a template for the configuration information to connect to your data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceConfiguration) -> dict:
    out: dict = {}
    if "s3_configuration" in value:
        import capo_kendra.types.s3_data_source_configuration

        out["S3Configuration"] = (
            capo_kendra.types.s3_data_source_configuration.serialize_aws_json_1_1(
                value["s3_configuration"]
            )
        )
    if "share_point_configuration" in value:
        import capo_kendra.types.share_point_configuration

        out["SharePointConfiguration"] = (
            capo_kendra.types.share_point_configuration.serialize_aws_json_1_1(
                value["share_point_configuration"]
            )
        )
    if "database_configuration" in value:
        import capo_kendra.types.database_configuration

        out["DatabaseConfiguration"] = (
            capo_kendra.types.database_configuration.serialize_aws_json_1_1(
                value["database_configuration"]
            )
        )
    if "salesforce_configuration" in value:
        import capo_kendra.types.salesforce_configuration

        out["SalesforceConfiguration"] = (
            capo_kendra.types.salesforce_configuration.serialize_aws_json_1_1(
                value["salesforce_configuration"]
            )
        )
    if "one_drive_configuration" in value:
        import capo_kendra.types.one_drive_configuration

        out["OneDriveConfiguration"] = (
            capo_kendra.types.one_drive_configuration.serialize_aws_json_1_1(
                value["one_drive_configuration"]
            )
        )
    if "service_now_configuration" in value:
        import capo_kendra.types.service_now_configuration

        out["ServiceNowConfiguration"] = (
            capo_kendra.types.service_now_configuration.serialize_aws_json_1_1(
                value["service_now_configuration"]
            )
        )
    if "confluence_configuration" in value:
        import capo_kendra.types.confluence_configuration

        out["ConfluenceConfiguration"] = (
            capo_kendra.types.confluence_configuration.serialize_aws_json_1_1(
                value["confluence_configuration"]
            )
        )
    if "google_drive_configuration" in value:
        import capo_kendra.types.google_drive_configuration

        out["GoogleDriveConfiguration"] = (
            capo_kendra.types.google_drive_configuration.serialize_aws_json_1_1(
                value["google_drive_configuration"]
            )
        )
    if "web_crawler_configuration" in value:
        import capo_kendra.types.web_crawler_configuration

        out["WebCrawlerConfiguration"] = (
            capo_kendra.types.web_crawler_configuration.serialize_aws_json_1_1(
                value["web_crawler_configuration"]
            )
        )
    if "work_docs_configuration" in value:
        import capo_kendra.types.work_docs_configuration

        out["WorkDocsConfiguration"] = (
            capo_kendra.types.work_docs_configuration.serialize_aws_json_1_1(
                value["work_docs_configuration"]
            )
        )
    if "fsx_configuration" in value:
        import capo_kendra.types.fsx_configuration

        out["FsxConfiguration"] = (
            capo_kendra.types.fsx_configuration.serialize_aws_json_1_1(
                value["fsx_configuration"]
            )
        )
    if "slack_configuration" in value:
        import capo_kendra.types.slack_configuration

        out["SlackConfiguration"] = (
            capo_kendra.types.slack_configuration.serialize_aws_json_1_1(
                value["slack_configuration"]
            )
        )
    if "box_configuration" in value:
        import capo_kendra.types.box_configuration

        out["BoxConfiguration"] = (
            capo_kendra.types.box_configuration.serialize_aws_json_1_1(
                value["box_configuration"]
            )
        )
    if "quip_configuration" in value:
        import capo_kendra.types.quip_configuration

        out["QuipConfiguration"] = (
            capo_kendra.types.quip_configuration.serialize_aws_json_1_1(
                value["quip_configuration"]
            )
        )
    if "jira_configuration" in value:
        import capo_kendra.types.jira_configuration

        out["JiraConfiguration"] = (
            capo_kendra.types.jira_configuration.serialize_aws_json_1_1(
                value["jira_configuration"]
            )
        )
    if "git_hub_configuration" in value:
        import capo_kendra.types.git_hub_configuration

        out["GitHubConfiguration"] = (
            capo_kendra.types.git_hub_configuration.serialize_aws_json_1_1(
                value["git_hub_configuration"]
            )
        )
    if "alfresco_configuration" in value:
        import capo_kendra.types.alfresco_configuration

        out["AlfrescoConfiguration"] = (
            capo_kendra.types.alfresco_configuration.serialize_aws_json_1_1(
                value["alfresco_configuration"]
            )
        )
    if "template_configuration" in value:
        import capo_kendra.types.template_configuration

        out["TemplateConfiguration"] = (
            capo_kendra.types.template_configuration.serialize_aws_json_1_1(
                value["template_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSourceConfiguration:
    out: DataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("S3Configuration") is not None:
        import capo_kendra.types.s3_data_source_configuration

        out["s3_configuration"] = (
            capo_kendra.types.s3_data_source_configuration.deserialize_aws_json_1_1(
                data["S3Configuration"]
            )
        )
    if data.get("SharePointConfiguration") is not None:
        import capo_kendra.types.share_point_configuration

        out["share_point_configuration"] = (
            capo_kendra.types.share_point_configuration.deserialize_aws_json_1_1(
                data["SharePointConfiguration"]
            )
        )
    if data.get("DatabaseConfiguration") is not None:
        import capo_kendra.types.database_configuration

        out["database_configuration"] = (
            capo_kendra.types.database_configuration.deserialize_aws_json_1_1(
                data["DatabaseConfiguration"]
            )
        )
    if data.get("SalesforceConfiguration") is not None:
        import capo_kendra.types.salesforce_configuration

        out["salesforce_configuration"] = (
            capo_kendra.types.salesforce_configuration.deserialize_aws_json_1_1(
                data["SalesforceConfiguration"]
            )
        )
    if data.get("OneDriveConfiguration") is not None:
        import capo_kendra.types.one_drive_configuration

        out["one_drive_configuration"] = (
            capo_kendra.types.one_drive_configuration.deserialize_aws_json_1_1(
                data["OneDriveConfiguration"]
            )
        )
    if data.get("ServiceNowConfiguration") is not None:
        import capo_kendra.types.service_now_configuration

        out["service_now_configuration"] = (
            capo_kendra.types.service_now_configuration.deserialize_aws_json_1_1(
                data["ServiceNowConfiguration"]
            )
        )
    if data.get("ConfluenceConfiguration") is not None:
        import capo_kendra.types.confluence_configuration

        out["confluence_configuration"] = (
            capo_kendra.types.confluence_configuration.deserialize_aws_json_1_1(
                data["ConfluenceConfiguration"]
            )
        )
    if data.get("GoogleDriveConfiguration") is not None:
        import capo_kendra.types.google_drive_configuration

        out["google_drive_configuration"] = (
            capo_kendra.types.google_drive_configuration.deserialize_aws_json_1_1(
                data["GoogleDriveConfiguration"]
            )
        )
    if data.get("WebCrawlerConfiguration") is not None:
        import capo_kendra.types.web_crawler_configuration

        out["web_crawler_configuration"] = (
            capo_kendra.types.web_crawler_configuration.deserialize_aws_json_1_1(
                data["WebCrawlerConfiguration"]
            )
        )
    if data.get("WorkDocsConfiguration") is not None:
        import capo_kendra.types.work_docs_configuration

        out["work_docs_configuration"] = (
            capo_kendra.types.work_docs_configuration.deserialize_aws_json_1_1(
                data["WorkDocsConfiguration"]
            )
        )
    if data.get("FsxConfiguration") is not None:
        import capo_kendra.types.fsx_configuration

        out["fsx_configuration"] = (
            capo_kendra.types.fsx_configuration.deserialize_aws_json_1_1(
                data["FsxConfiguration"]
            )
        )
    if data.get("SlackConfiguration") is not None:
        import capo_kendra.types.slack_configuration

        out["slack_configuration"] = (
            capo_kendra.types.slack_configuration.deserialize_aws_json_1_1(
                data["SlackConfiguration"]
            )
        )
    if data.get("BoxConfiguration") is not None:
        import capo_kendra.types.box_configuration

        out["box_configuration"] = (
            capo_kendra.types.box_configuration.deserialize_aws_json_1_1(
                data["BoxConfiguration"]
            )
        )
    if data.get("QuipConfiguration") is not None:
        import capo_kendra.types.quip_configuration

        out["quip_configuration"] = (
            capo_kendra.types.quip_configuration.deserialize_aws_json_1_1(
                data["QuipConfiguration"]
            )
        )
    if data.get("JiraConfiguration") is not None:
        import capo_kendra.types.jira_configuration

        out["jira_configuration"] = (
            capo_kendra.types.jira_configuration.deserialize_aws_json_1_1(
                data["JiraConfiguration"]
            )
        )
    if data.get("GitHubConfiguration") is not None:
        import capo_kendra.types.git_hub_configuration

        out["git_hub_configuration"] = (
            capo_kendra.types.git_hub_configuration.deserialize_aws_json_1_1(
                data["GitHubConfiguration"]
            )
        )
    if data.get("AlfrescoConfiguration") is not None:
        import capo_kendra.types.alfresco_configuration

        out["alfresco_configuration"] = (
            capo_kendra.types.alfresco_configuration.deserialize_aws_json_1_1(
                data["AlfrescoConfiguration"]
            )
        )
    if data.get("TemplateConfiguration") is not None:
        import capo_kendra.types.template_configuration

        out["template_configuration"] = (
            capo_kendra.types.template_configuration.deserialize_aws_json_1_1(
                data["TemplateConfiguration"]
            )
        )
    return out
