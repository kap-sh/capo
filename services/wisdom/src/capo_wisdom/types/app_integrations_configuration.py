"""Generated from Smithy shape ``com.amazonaws.wisdom#AppIntegrationsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.generic_arn
    import capo_wisdom.types.object_fields_list


class AppIntegrationsConfiguration(TypedDict, closed=True):
    app_integration_arn: "capo_wisdom.types.generic_arn.GenericArn"
    """<p>The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content.</p> <ul> <li> <p> For <a href="https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm"> Salesforce</a>, your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least <code>Id</code>, <code>ArticleNumber</code>, <code>VersionNumber</code>, <code>Title</code>, <code>PublishStatus</code>, and <code>IsDeleted</code> as source fields. </p> </li> <li> <p> For <a href="https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api"> ServiceNow</a>, your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least <code>number</code>, <code>short_description</code>, <code>sys_mod_count</code>, <code>workflow_state</code>, and <code>active</code> as source fields. </p> </li> <li> <p> For <a href="https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/"> Zendesk</a>, your AppIntegrations DataIntegration must have an ObjectConfiguration if <code>objectFields</code> is not provided, including at least <code>id</code>, <code>title</code>, <code>updated_at</code>, and <code>draft</code> as source fields. </p> </li> <li> <p> For <a href="https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index">SharePoint</a>, your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among <code>docx</code>, <code>pdf</code>, <code>html</code>, <code>htm</code>, and <code>txt</code>. </p> </li> <li> <p> For <a href="https://aws.amazon.com/s3/">Amazon S3</a>, the ObjectConfiguration and FileConfiguration of your AppIntegrations DataIntegration must be null. The <code>SourceURI</code> of your DataIntegration must use the following format: <code>s3://your_s3_bucket_name</code>.</p> <important> <p>The bucket policy of the corresponding S3 bucket must allow the Amazon Web Services principal <code>app-integrations.amazonaws.com</code> to perform <code>s3:ListBucket</code>, <code>s3:GetObject</code>, and <code>s3:GetBucketLocation</code> against the bucket.</p> </important> </li> </ul>"""
    object_fields: NotRequired["capo_wisdom.types.object_fields_list.ObjectFieldsList"]
    """<p>The fields from the source that are made available to your agents in Wisdom. Optional if ObjectConfiguration is included in the provided DataIntegration. </p> <ul> <li> <p> For <a href="https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm"> Salesforce</a>, you must include at least <code>Id</code>, <code>ArticleNumber</code>, <code>VersionNumber</code>, <code>Title</code>, <code>PublishStatus</code>, and <code>IsDeleted</code>. </p> </li> <li> <p>For <a href="https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api"> ServiceNow</a>, you must include at least <code>number</code>, <code>short_description</code>, <code>sys_mod_count</code>, <code>workflow_state</code>, and <code>active</code>. </p> </li> <li> <p>For <a href="https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/"> Zendesk</a>, you must include at least <code>id</code>, <code>title</code>, <code>updated_at</code>, and <code>draft</code>. </p> </li> </ul> <p>Make sure to include additional fields. These fields are indexed and used to source recommendations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppIntegrationsConfiguration) -> dict:
    out: dict = {}
    out["appIntegrationArn"] = value["app_integration_arn"]
    if "object_fields" in value:
        import capo_wisdom.types.object_fields_list

        out["objectFields"] = capo_wisdom.types.object_fields_list.serialize_json(
            value["object_fields"]
        )
    return out


def deserialize_json(data: dict) -> AppIntegrationsConfiguration:
    out: AppIntegrationsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("appIntegrationArn") is not None:
        out["app_integration_arn"] = data["appIntegrationArn"]
    else:
        raise DeserializationError(
            "AppIntegrationsConfiguration.app_integration_arn required"
        )
    if data.get("objectFields") is not None:
        import capo_wisdom.types.object_fields_list

        out["object_fields"] = capo_wisdom.types.object_fields_list.deserialize_json(
            data["objectFields"]
        )
    return out
