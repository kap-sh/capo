"""Generated from Smithy shape ``com.amazonaws.kendra#ServiceNowConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.secret_arn
    import capo_kendra.types.service_now_authentication_type
    import capo_kendra.types.service_now_build_version_type
    import capo_kendra.types.service_now_host_url
    import capo_kendra.types.service_now_knowledge_article_configuration
    import capo_kendra.types.service_now_service_catalog_configuration


class ServiceNowConfiguration(TypedDict, closed=True):
    host_url: "capo_kendra.types.service_now_host_url.ServiceNowHostUrl"
    """<p>The ServiceNow instance that the data source connects to. The host endpoint should look like the following: <i>{instance}.service-now.com.</i> </p>"""
    secret_arn: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret that contains the user name and password required to connect to the ServiceNow instance. You can also provide OAuth authentication credentials of user name, password, client ID, and client secret. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/data-source-servicenow.html">Using a ServiceNow data source</a>.</p>"""
    service_now_build_version: (
        "capo_kendra.types.service_now_build_version_type.ServiceNowBuildVersionType"
    )
    """<p>The identifier of the release that the ServiceNow host is running. If the host is not running the <code>LONDON</code> release, use <code>OTHERS</code>.</p>"""
    knowledge_article_configuration: NotRequired[
        "capo_kendra.types.service_now_knowledge_article_configuration.ServiceNowKnowledgeArticleConfiguration"
    ]
    """<p>Configuration information for crawling knowledge articles in the ServiceNow site.</p>"""
    service_catalog_configuration: NotRequired[
        "capo_kendra.types.service_now_service_catalog_configuration.ServiceNowServiceCatalogConfiguration"
    ]
    """<p>Configuration information for crawling service catalogs in the ServiceNow site.</p>"""
    authentication_type: NotRequired[
        "capo_kendra.types.service_now_authentication_type.ServiceNowAuthenticationType"
    ]
    """<p>The type of authentication used to connect to the ServiceNow instance. If you choose <code>HTTP_BASIC</code>, Amazon Kendra is authenticated using the user name and password provided in the Secrets Manager secret in the <code>SecretArn</code> field. If you choose <code>OAUTH2</code>, Amazon Kendra is authenticated using the credentials of client ID, client secret, user name and password.</p> <p>When you use <code>OAUTH2</code> authentication, you must generate a token and a client secret using the ServiceNow console. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/data-source-servicenow.html">Using a ServiceNow data source</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceNowConfiguration) -> dict:
    out: dict = {}
    out["HostUrl"] = value["host_url"]
    out["SecretArn"] = value["secret_arn"]
    import capo_kendra.types.service_now_build_version_type

    out["ServiceNowBuildVersion"] = (
        capo_kendra.types.service_now_build_version_type.serialize_aws_json_1_1(
            value["service_now_build_version"]
        )
    )
    if "knowledge_article_configuration" in value:
        import capo_kendra.types.service_now_knowledge_article_configuration

        out["KnowledgeArticleConfiguration"] = (
            capo_kendra.types.service_now_knowledge_article_configuration.serialize_aws_json_1_1(
                value["knowledge_article_configuration"]
            )
        )
    if "service_catalog_configuration" in value:
        import capo_kendra.types.service_now_service_catalog_configuration

        out["ServiceCatalogConfiguration"] = (
            capo_kendra.types.service_now_service_catalog_configuration.serialize_aws_json_1_1(
                value["service_catalog_configuration"]
            )
        )
    if "authentication_type" in value:
        import capo_kendra.types.service_now_authentication_type

        out["AuthenticationType"] = (
            capo_kendra.types.service_now_authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceNowConfiguration:
    out: ServiceNowConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("HostUrl") is not None:
        out["host_url"] = data["HostUrl"]
    else:
        raise DeserializationError("ServiceNowConfiguration.host_url required")
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("ServiceNowConfiguration.secret_arn required")
    if data.get("ServiceNowBuildVersion") is not None:
        import capo_kendra.types.service_now_build_version_type

        out["service_now_build_version"] = (
            capo_kendra.types.service_now_build_version_type.deserialize_aws_json_1_1(
                data["ServiceNowBuildVersion"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceNowConfiguration.service_now_build_version required"
        )
    if data.get("KnowledgeArticleConfiguration") is not None:
        import capo_kendra.types.service_now_knowledge_article_configuration

        out["knowledge_article_configuration"] = (
            capo_kendra.types.service_now_knowledge_article_configuration.deserialize_aws_json_1_1(
                data["KnowledgeArticleConfiguration"]
            )
        )
    if data.get("ServiceCatalogConfiguration") is not None:
        import capo_kendra.types.service_now_service_catalog_configuration

        out["service_catalog_configuration"] = (
            capo_kendra.types.service_now_service_catalog_configuration.deserialize_aws_json_1_1(
                data["ServiceCatalogConfiguration"]
            )
        )
    if data.get("AuthenticationType") is not None:
        import capo_kendra.types.service_now_authentication_type

        out["authentication_type"] = (
            capo_kendra.types.service_now_authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    return out
