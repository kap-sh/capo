"""Generated from Smithy shape ``com.amazonaws.glue#ComputeEnvironmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.authentication_types
    import capo_glue.types.bool
    import capo_glue.types.compute_environment
    import capo_glue.types.compute_environment_configuration_description_string
    import capo_glue.types.compute_environment_name
    import capo_glue.types.list_of_string
    import capo_glue.types.properties_map
    import capo_glue.types.property_name_overrides


class ComputeEnvironmentConfiguration(TypedDict, closed=True):
    name: "capo_glue.types.compute_environment_name.ComputeEnvironmentName"
    """<p>A name for the compute environment configuration.</p>"""
    description: "capo_glue.types.compute_environment_configuration_description_string.ComputeEnvironmentConfigurationDescriptionString"
    """<p>A description of the compute environment.</p>"""
    compute_environment: "capo_glue.types.compute_environment.ComputeEnvironment"
    """<p>The type of compute environment.</p>"""
    supported_authentication_types: (
        "capo_glue.types.authentication_types.AuthenticationTypes"
    )
    """<p>The supported authentication types for the compute environment.</p>"""
    connection_options: "capo_glue.types.properties_map.PropertiesMap"
    """<p>The parameters used as connection options for the compute environment.</p>"""
    connection_property_name_overrides: (
        "capo_glue.types.property_name_overrides.PropertyNameOverrides"
    )
    """<p>The connection property name overrides for the compute environment.</p>"""
    connection_option_name_overrides: (
        "capo_glue.types.property_name_overrides.PropertyNameOverrides"
    )
    """<p>The connection option name overrides for the compute environment.</p>"""
    connection_properties_required_overrides: (
        "capo_glue.types.list_of_string.ListOfString"
    )
    """<p>The connection properties that are required as overrides for the compute environment.</p>"""
    physical_connection_properties_required: NotRequired["capo_glue.types.bool.Bool"]
    """<p>Indicates whether <code>PhysicalConnectionProperties</code> are required for the compute environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeEnvironmentConfiguration) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    import capo_glue.types.compute_environment

    out["ComputeEnvironment"] = (
        capo_glue.types.compute_environment.serialize_aws_json_1_1(
            value["compute_environment"]
        )
    )
    import capo_glue.types.authentication_types

    out["SupportedAuthenticationTypes"] = (
        capo_glue.types.authentication_types.serialize_aws_json_1_1(
            value["supported_authentication_types"]
        )
    )
    import capo_glue.types.properties_map

    out["ConnectionOptions"] = capo_glue.types.properties_map.serialize_aws_json_1_1(
        value["connection_options"]
    )
    import capo_glue.types.property_name_overrides

    out["ConnectionPropertyNameOverrides"] = (
        capo_glue.types.property_name_overrides.serialize_aws_json_1_1(
            value["connection_property_name_overrides"]
        )
    )
    import capo_glue.types.property_name_overrides

    out["ConnectionOptionNameOverrides"] = (
        capo_glue.types.property_name_overrides.serialize_aws_json_1_1(
            value["connection_option_name_overrides"]
        )
    )
    import capo_glue.types.list_of_string

    out["ConnectionPropertiesRequiredOverrides"] = (
        capo_glue.types.list_of_string.serialize_aws_json_1_1(
            value.get("connection_properties_required_overrides", [])
        )
    )
    if "physical_connection_properties_required" in value:
        out["PhysicalConnectionPropertiesRequired"] = value[
            "physical_connection_properties_required"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeEnvironmentConfiguration:
    out: ComputeEnvironmentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("ComputeEnvironment") is not None:
        import capo_glue.types.compute_environment

        out["compute_environment"] = (
            capo_glue.types.compute_environment.deserialize_aws_json_1_1(
                data["ComputeEnvironment"]
            )
        )
    else:
        import typing

        out["compute_environment"] = typing.cast(
            "capo_glue.types.compute_environment.ComputeEnvironment", ""
        )
    if data.get("SupportedAuthenticationTypes") is not None:
        import capo_glue.types.authentication_types

        out["supported_authentication_types"] = (
            capo_glue.types.authentication_types.deserialize_aws_json_1_1(
                data["SupportedAuthenticationTypes"]
            )
        )
    else:
        out["supported_authentication_types"] = []
    if data.get("ConnectionOptions") is not None:
        import capo_glue.types.properties_map

        out["connection_options"] = (
            capo_glue.types.properties_map.deserialize_aws_json_1_1(
                data["ConnectionOptions"]
            )
        )
    else:
        out["connection_options"] = {}
    if data.get("ConnectionPropertyNameOverrides") is not None:
        import capo_glue.types.property_name_overrides

        out["connection_property_name_overrides"] = (
            capo_glue.types.property_name_overrides.deserialize_aws_json_1_1(
                data["ConnectionPropertyNameOverrides"]
            )
        )
    else:
        out["connection_property_name_overrides"] = {}
    if data.get("ConnectionOptionNameOverrides") is not None:
        import capo_glue.types.property_name_overrides

        out["connection_option_name_overrides"] = (
            capo_glue.types.property_name_overrides.deserialize_aws_json_1_1(
                data["ConnectionOptionNameOverrides"]
            )
        )
    else:
        out["connection_option_name_overrides"] = {}
    if data.get("ConnectionPropertiesRequiredOverrides") is not None:
        import capo_glue.types.list_of_string

        out["connection_properties_required_overrides"] = (
            capo_glue.types.list_of_string.deserialize_aws_json_1_1(
                data["ConnectionPropertiesRequiredOverrides"]
            )
        )
    else:
        out["connection_properties_required_overrides"] = []
    if data.get("PhysicalConnectionPropertiesRequired") is not None:
        out["physical_connection_properties_required"] = data[
            "PhysicalConnectionPropertiesRequired"
        ]
    return out
