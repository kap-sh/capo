"""Generated from Smithy shape ``com.amazonaws.configservice#PutThirdPartyServiceLinkedConfigurationRecorderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.scope_configuration
    import capo_config_service.types.service_principal
    import capo_config_service.types.tags_list


class PutThirdPartyServiceLinkedConfigurationRecorderRequest(TypedDict, closed=True):
    service_principal: "capo_config_service.types.service_principal.ServicePrincipal"
    """<p>The service principal of the Amazon Web Services service for the service-linked configuration recorder that you want to create.</p>"""
    connector_arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the connector that specifies the connection between the third-party cloud service provider and Config. The specified connector must exist.</p>"""
    scope_configuration: (
        "capo_config_service.types.scope_configuration.ScopeConfiguration"
    )
    """<p>Specifies the scope of resources to record from the third-party cloud service provider.</p>"""
    tags: NotRequired["capo_config_service.types.tags_list.TagsList"]
    """<p>The tags for a service-linked configuration recorder. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: PutThirdPartyServiceLinkedConfigurationRecorderRequest,
) -> dict:
    out: dict = {}
    out["ServicePrincipal"] = value["service_principal"]
    out["ConnectorArn"] = value["connector_arn"]
    import capo_config_service.types.scope_configuration

    out["ScopeConfiguration"] = (
        capo_config_service.types.scope_configuration.serialize_aws_json_1_1(
            value["scope_configuration"]
        )
    )
    if "tags" in value:
        import capo_config_service.types.tags_list

        out["Tags"] = capo_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PutThirdPartyServiceLinkedConfigurationRecorderRequest:
    out: PutThirdPartyServiceLinkedConfigurationRecorderRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServicePrincipal") is not None:
        out["service_principal"] = data["ServicePrincipal"]
    else:
        out["service_principal"] = ""
    if data.get("ConnectorArn") is not None:
        out["connector_arn"] = data["ConnectorArn"]
    else:
        out["connector_arn"] = ""
    if data.get("ScopeConfiguration") is not None:
        import capo_config_service.types.scope_configuration

        out["scope_configuration"] = (
            capo_config_service.types.scope_configuration.deserialize_aws_json_1_1(
                data["ScopeConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutThirdPartyServiceLinkedConfigurationRecorderRequest.scope_configuration required"
        )
    if data.get("Tags") is not None:
        import capo_config_service.types.tags_list

        out["tags"] = capo_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
