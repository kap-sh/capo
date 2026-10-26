"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetProviderServiceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.provider_component_schema
    import capo_entityresolution.types.provider_endpoint_configuration
    import capo_entityresolution.types.provider_id_name_space_configuration
    import capo_entityresolution.types.provider_intermediate_data_access_configuration
    import capo_entityresolution.types.provider_service_arn
    import capo_entityresolution.types.provider_service_display_name
    import capo_entityresolution.types.service_type


class GetProviderServiceOutput(TypedDict, closed=True):
    provider_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the provider. This name is typically the company name.</p>"""
    provider_service_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the product that the provider service provides. </p>"""
    provider_service_display_name: "capo_entityresolution.types.provider_service_display_name.ProviderServiceDisplayName"
    """<p>The display name of the provider service.</p>"""
    provider_service_type: "capo_entityresolution.types.service_type.ServiceType"
    """<p>The type of provider service.</p>"""
    provider_service_arn: (
        "capo_entityresolution.types.provider_service_arn.ProviderServiceArn"
    )
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the provider service.</p>"""
    provider_configuration_definition: NotRequired["object"]
    """<p>The definition of the provider configuration.</p>"""
    provider_id_name_space_configuration: NotRequired[
        "capo_entityresolution.types.provider_id_name_space_configuration.ProviderIdNameSpaceConfiguration"
    ]
    """<p>The provider configuration required for different ID namespace types.</p>"""
    provider_job_configuration: NotRequired["object"]
    """<p>Provider service job configurations.</p>"""
    provider_endpoint_configuration: "capo_entityresolution.types.provider_endpoint_configuration.ProviderEndpointConfiguration"
    """<p>The required configuration fields to use with the provider service.</p>"""
    anonymized_output: "bool"
    """<p>Specifies whether output data from the provider is anonymized. A value of <code>TRUE</code> means the output will be anonymized and you can't relate the data that comes back from the provider to the identifying input. A value of <code>FALSE</code> means the output won't be anonymized and you can relate the data that comes back from the provider to your source data. </p>"""
    provider_entity_output_definition: "object"
    """<p>The definition of the provider entity output.</p>"""
    provider_intermediate_data_access_configuration: NotRequired[
        "capo_entityresolution.types.provider_intermediate_data_access_configuration.ProviderIntermediateDataAccessConfiguration"
    ]
    """<p>The Amazon Web Services accounts and the S3 permissions that are required by some providers to create an S3 bucket for intermediate data storage.</p>"""
    provider_component_schema: NotRequired[
        "capo_entityresolution.types.provider_component_schema.ProviderComponentSchema"
    ]
    """<p>Input schema for the provider service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProviderServiceOutput) -> dict:
    out: dict = {}
    out["providerName"] = value["provider_name"]
    out["providerServiceName"] = value["provider_service_name"]
    out["providerServiceDisplayName"] = value["provider_service_display_name"]
    import capo_entityresolution.types.service_type

    out["providerServiceType"] = (
        capo_entityresolution.types.service_type.serialize_json(
            value["provider_service_type"]
        )
    )
    out["providerServiceArn"] = value["provider_service_arn"]
    if "provider_configuration_definition" in value:
        out["providerConfigurationDefinition"] = value[
            "provider_configuration_definition"
        ]
    if "provider_id_name_space_configuration" in value:
        import capo_entityresolution.types.provider_id_name_space_configuration

        out["providerIdNameSpaceConfiguration"] = (
            capo_entityresolution.types.provider_id_name_space_configuration.serialize_json(
                value["provider_id_name_space_configuration"]
            )
        )
    if "provider_job_configuration" in value:
        out["providerJobConfiguration"] = value["provider_job_configuration"]
    import capo_entityresolution.types.provider_endpoint_configuration

    out["providerEndpointConfiguration"] = (
        capo_entityresolution.types.provider_endpoint_configuration.serialize_json(
            value["provider_endpoint_configuration"]
        )
    )
    out["anonymizedOutput"] = value["anonymized_output"]
    out["providerEntityOutputDefinition"] = value["provider_entity_output_definition"]
    if "provider_intermediate_data_access_configuration" in value:
        import capo_entityresolution.types.provider_intermediate_data_access_configuration

        out["providerIntermediateDataAccessConfiguration"] = (
            capo_entityresolution.types.provider_intermediate_data_access_configuration.serialize_json(
                value["provider_intermediate_data_access_configuration"]
            )
        )
    if "provider_component_schema" in value:
        import capo_entityresolution.types.provider_component_schema

        out["providerComponentSchema"] = (
            capo_entityresolution.types.provider_component_schema.serialize_json(
                value["provider_component_schema"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetProviderServiceOutput:
    out: GetProviderServiceOutput = {}  # type: ignore[typeddict-item]
    if data.get("providerName") is not None:
        out["provider_name"] = data["providerName"]
    else:
        out["provider_name"] = ""
    if data.get("providerServiceName") is not None:
        out["provider_service_name"] = data["providerServiceName"]
    else:
        out["provider_service_name"] = ""
    if data.get("providerServiceDisplayName") is not None:
        out["provider_service_display_name"] = data["providerServiceDisplayName"]
    else:
        out["provider_service_display_name"] = ""
    if data.get("providerServiceType") is not None:
        import capo_entityresolution.types.service_type

        out["provider_service_type"] = (
            capo_entityresolution.types.service_type.deserialize_json(
                data["providerServiceType"]
            )
        )
    else:
        import typing

        out["provider_service_type"] = typing.cast(
            "capo_entityresolution.types.service_type.ServiceType", ""
        )
    if data.get("providerServiceArn") is not None:
        out["provider_service_arn"] = data["providerServiceArn"]
    else:
        out["provider_service_arn"] = ""
    if data.get("providerConfigurationDefinition") is not None:
        out["provider_configuration_definition"] = data[
            "providerConfigurationDefinition"
        ]
    if data.get("providerIdNameSpaceConfiguration") is not None:
        import capo_entityresolution.types.provider_id_name_space_configuration

        out["provider_id_name_space_configuration"] = (
            capo_entityresolution.types.provider_id_name_space_configuration.deserialize_json(
                data["providerIdNameSpaceConfiguration"]
            )
        )
    if data.get("providerJobConfiguration") is not None:
        out["provider_job_configuration"] = data["providerJobConfiguration"]
    if data.get("providerEndpointConfiguration") is not None:
        import capo_entityresolution.types.provider_endpoint_configuration

        out["provider_endpoint_configuration"] = (
            capo_entityresolution.types.provider_endpoint_configuration.deserialize_json(
                data["providerEndpointConfiguration"]
            )
        )
    else:
        out["provider_endpoint_configuration"] = {"$unknown": {"name": ""}}
    if data.get("anonymizedOutput") is not None:
        out["anonymized_output"] = data["anonymizedOutput"]
    else:
        out["anonymized_output"] = False
    if data.get("providerEntityOutputDefinition") is not None:
        out["provider_entity_output_definition"] = data[
            "providerEntityOutputDefinition"
        ]
    else:
        out["provider_entity_output_definition"] = None
    if data.get("providerIntermediateDataAccessConfiguration") is not None:
        import capo_entityresolution.types.provider_intermediate_data_access_configuration

        out["provider_intermediate_data_access_configuration"] = (
            capo_entityresolution.types.provider_intermediate_data_access_configuration.deserialize_json(
                data["providerIntermediateDataAccessConfiguration"]
            )
        )
    if data.get("providerComponentSchema") is not None:
        import capo_entityresolution.types.provider_component_schema

        out["provider_component_schema"] = (
            capo_entityresolution.types.provider_component_schema.deserialize_json(
                data["providerComponentSchema"]
            )
        )
    return out
