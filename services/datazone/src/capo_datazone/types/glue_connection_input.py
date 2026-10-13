"""Generated from Smithy shape ``com.amazonaws.datazone#GlueConnectionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.authentication_configuration_input
    import capo_datazone.types.compute_environments_list
    import capo_datazone.types.connection_properties
    import capo_datazone.types.glue_connection_type
    import capo_datazone.types.physical_connection_requirements
    import capo_datazone.types.property_map


class GlueConnectionInput(TypedDict, closed=True):
    connection_properties: NotRequired[
        "capo_datazone.types.connection_properties.ConnectionProperties"
    ]
    """<p>The connection properties of the Amazon Web Services Glue connection.</p>"""
    physical_connection_requirements: NotRequired[
        "capo_datazone.types.physical_connection_requirements.PhysicalConnectionRequirements"
    ]
    """<p>The physical connection requirements for the Amazon Web Services Glue connection.</p>"""
    name: NotRequired["str"]
    """<p>The name of the Amazon Web Services Glue connection.</p>"""
    description: NotRequired["str"]
    """<p>The description of the Amazon Web Services Glue connection.</p>"""
    connection_type: NotRequired[
        "capo_datazone.types.glue_connection_type.GlueConnectionType"
    ]
    """<p>The connection type of the Amazon Web Services Glue connection.</p>"""
    match_criteria: NotRequired["str"]
    """<p>The match criteria of the Amazon Web Services Glue connection.</p>"""
    validate_credentials: NotRequired["bool"]
    """<p>Speciefies whether to validate credentials of the Amazon Web Services Glue connection.</p>"""
    validate_for_compute_environments: NotRequired[
        "capo_datazone.types.compute_environments_list.ComputeEnvironmentsList"
    ]
    """<p>Speciefies whether to validate for compute environments of the Amazon Web Services Glue connection.</p>"""
    spark_properties: NotRequired["capo_datazone.types.property_map.PropertyMap"]
    """<p>The Spark properties of the Amazon Web Services Glue connection.</p>"""
    athena_properties: NotRequired["capo_datazone.types.property_map.PropertyMap"]
    """<p>The Amazon Athena properties of the Amazon Web Services Glue connection.</p>"""
    python_properties: NotRequired["capo_datazone.types.property_map.PropertyMap"]
    """<p>The Python properties of the Amazon Web Services Glue connection.</p>"""
    authentication_configuration: NotRequired[
        "capo_datazone.types.authentication_configuration_input.AuthenticationConfigurationInput"
    ]
    """<p>The authentication configuration of the Amazon Web Services Glue connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueConnectionInput) -> dict:
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
    if "connection_type" in value:
        import capo_datazone.types.glue_connection_type

        out["connectionType"] = capo_datazone.types.glue_connection_type.serialize_json(
            value["connection_type"]
        )
    if "match_criteria" in value:
        out["matchCriteria"] = value["match_criteria"]
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


def deserialize_json(data: dict) -> GlueConnectionInput:
    out: GlueConnectionInput = {}  # type: ignore[typeddict-item]
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
    if data.get("connectionType") is not None:
        import capo_datazone.types.glue_connection_type

        out["connection_type"] = (
            capo_datazone.types.glue_connection_type.deserialize_json(
                data["connectionType"]
            )
        )
    if data.get("matchCriteria") is not None:
        out["match_criteria"] = data["matchCriteria"]
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


def redact_sensitive(value: GlueConnectionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_configuration" in value:
        import capo_datazone.types.authentication_configuration_input

        out["authentication_configuration"] = (
            capo_datazone.types.authentication_configuration_input.redact_sensitive(
                value["authentication_configuration"]
            )
        )
    return out
