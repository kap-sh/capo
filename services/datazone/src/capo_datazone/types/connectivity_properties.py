"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectivityProperties``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.authentication_configuration_input
    import capo_datazone.types.compute_environments_list
    import capo_datazone.types.connection_properties
    import capo_datazone.types.physical_connection_requirements
    import capo_datazone.types.property_map


class ConnectivityProperties(TypedDict, closed=True):
    connection_properties: NotRequired[
        "capo_datazone.types.connection_properties.ConnectionProperties"
    ]
    """<p>The connection properties for this configuration.</p>"""
    physical_connection_requirements: NotRequired[
        "capo_datazone.types.physical_connection_requirements.PhysicalConnectionRequirements"
    ]
    """<p>The physical network requirements for the connection, such as the subnet, security group, and VPC settings needed to reach the data source.</p>"""
    name: NotRequired["str"]
    """<p>The name of the connectivity configuration.</p>"""
    description: NotRequired["str"]
    """<p>The description of the connectivity configuration.</p>"""
    validate_credentials: NotRequired["bool"]
    """<p>Specifies whether to validate credentials for the connectivity configuration. Defaults to true if not specified.</p>"""
    validate_for_compute_environments: NotRequired[
        "capo_datazone.types.compute_environments_list.ComputeEnvironmentsList"
    ]
    """<p>The compute environments to use when validating connectivity. The service validates that the connection is reachable from each specified environment.</p>"""
    spark_properties: NotRequired["capo_datazone.types.property_map.PropertyMap"]
    """<p>The Spark properties for this configuration.</p>"""
    athena_properties: NotRequired["capo_datazone.types.property_map.PropertyMap"]
    """<p>The Athena properties for this configuration.</p>"""
    python_properties: NotRequired["capo_datazone.types.property_map.PropertyMap"]
    """<p>The Python properties for this configuration.</p>"""
    authentication_configuration: NotRequired[
        "capo_datazone.types.authentication_configuration_input.AuthenticationConfigurationInput"
    ]
    """<p>The authentication settings for this configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectivityProperties) -> dict:
    out: dict = {}
    if "connection_properties" in value:
        import capo_datazone.types.connection_properties

        out["connectionProperties"] = (
            capo_datazone.types.connection_properties.serialize_json(
                value["connection_properties"]
            )
        )
    if "physical_connection_requirements" in value:
        import capo_datazone.types.physical_connection_requirements

        out["physicalConnectionRequirements"] = (
            capo_datazone.types.physical_connection_requirements.serialize_json(
                value["physical_connection_requirements"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "validate_credentials" in value:
        out["validateCredentials"] = value["validate_credentials"]
    if "validate_for_compute_environments" in value:
        import capo_datazone.types.compute_environments_list

        out["validateForComputeEnvironments"] = (
            capo_datazone.types.compute_environments_list.serialize_json(
                value["validate_for_compute_environments"]
            )
        )
    if "spark_properties" in value:
        import capo_datazone.types.property_map

        out["sparkProperties"] = capo_datazone.types.property_map.serialize_json(
            value["spark_properties"]
        )
    if "athena_properties" in value:
        import capo_datazone.types.property_map

        out["athenaProperties"] = capo_datazone.types.property_map.serialize_json(
            value["athena_properties"]
        )
    if "python_properties" in value:
        import capo_datazone.types.property_map

        out["pythonProperties"] = capo_datazone.types.property_map.serialize_json(
            value["python_properties"]
        )
    if "authentication_configuration" in value:
        import capo_datazone.types.authentication_configuration_input

        out["authenticationConfiguration"] = (
            capo_datazone.types.authentication_configuration_input.serialize_json(
                value["authentication_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectivityProperties:
    out: ConnectivityProperties = {}  # type: ignore[typeddict-item]
    if data.get("connectionProperties") is not None:
        import capo_datazone.types.connection_properties

        out["connection_properties"] = (
            capo_datazone.types.connection_properties.deserialize_json(
                data["connectionProperties"]
            )
        )
    if data.get("physicalConnectionRequirements") is not None:
        import capo_datazone.types.physical_connection_requirements

        out["physical_connection_requirements"] = (
            capo_datazone.types.physical_connection_requirements.deserialize_json(
                data["physicalConnectionRequirements"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("validateCredentials") is not None:
        out["validate_credentials"] = data["validateCredentials"]
    if data.get("validateForComputeEnvironments") is not None:
        import capo_datazone.types.compute_environments_list

        out["validate_for_compute_environments"] = (
            capo_datazone.types.compute_environments_list.deserialize_json(
                data["validateForComputeEnvironments"]
            )
        )
    if data.get("sparkProperties") is not None:
        import capo_datazone.types.property_map

        out["spark_properties"] = capo_datazone.types.property_map.deserialize_json(
            data["sparkProperties"]
        )
    if data.get("athenaProperties") is not None:
        import capo_datazone.types.property_map

        out["athena_properties"] = capo_datazone.types.property_map.deserialize_json(
            data["athenaProperties"]
        )
    if data.get("pythonProperties") is not None:
        import capo_datazone.types.property_map

        out["python_properties"] = capo_datazone.types.property_map.deserialize_json(
            data["pythonProperties"]
        )
    if data.get("authenticationConfiguration") is not None:
        import capo_datazone.types.authentication_configuration_input

        out["authentication_configuration"] = (
            capo_datazone.types.authentication_configuration_input.deserialize_json(
                data["authenticationConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ConnectivityProperties) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_configuration" in value:
        import capo_datazone.types.authentication_configuration_input

        out["authentication_configuration"] = (
            capo_datazone.types.authentication_configuration_input.redact_sensitive(
                value["authentication_configuration"]
            )
        )
    return out
