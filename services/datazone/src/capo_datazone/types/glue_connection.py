"""Generated from Smithy shape ``com.amazonaws.datazone#GlueConnection``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.authentication_configuration
    import capo_datazone.types.compute_environments_list
    import capo_datazone.types.connection_properties
    import capo_datazone.types.connection_status
    import capo_datazone.types.connection_type
    import capo_datazone.types.match_criteria
    import capo_datazone.types.physical_connection_requirements
    import capo_datazone.types.property_map


class GlueConnection(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the Amazon Web Services Glue connection.</p>"""
    description: NotRequired["str"]
    """<p>The description of the Amazon Web Services Glue connection.</p>"""
    connection_type: NotRequired["capo_datazone.types.connection_type.ConnectionType"]
    """<p>The type of the Amazon Web Services Glue connection.</p>"""
    match_criteria: NotRequired["capo_datazone.types.match_criteria.MatchCriteria"]
    """<p>The match criteria of the Amazon Web Services Glue connection.</p>"""
    connection_properties: NotRequired[
        "capo_datazone.types.connection_properties.ConnectionProperties"
    ]
    """<p>The properties of the Amazon Web Services Glue connection.</p>"""
    spark_properties: NotRequired["capo_datazone.types.property_map.PropertyMap"]
    """<p>The Spark properties of the Amazon Web Services Glue connection.</p>"""
    athena_properties: NotRequired["capo_datazone.types.property_map.PropertyMap"]
    """<p>The Amazon Athena properties of the Amazon Web Services Glue connection.</p>"""
    python_properties: NotRequired["capo_datazone.types.property_map.PropertyMap"]
    """<p>The Python properties of the Amazon Web Services Glue connection.</p>"""
    physical_connection_requirements: NotRequired[
        "capo_datazone.types.physical_connection_requirements.PhysicalConnectionRequirements"
    ]
    """<p>The physical connection requirements of the Amazon Web Services Glue connection.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The creation time of the Amazon Web Services Glue connection.</p>"""
    last_updated_time: NotRequired["datetime.datetime"]
    """<p>The timestamp at which the Amazon Web Services Glue connection was last updated.</p>"""
    last_updated_by: NotRequired["str"]
    """<p>The user who last updated the Amazon Web Services Glue connection.</p>"""
    status: NotRequired["capo_datazone.types.connection_status.ConnectionStatus"]
    """<p>The status of the Amazon Web Services Glue connection.</p>"""
    status_reason: NotRequired["str"]
    """<p>The status reason of the Amazon Web Services Glue connection.</p>"""
    last_connection_validation_time: NotRequired["datetime.datetime"]
    """<p>The last validation time of the Amazon Web Services Glue connection.</p>"""
    authentication_configuration: NotRequired[
        "capo_datazone.types.authentication_configuration.AuthenticationConfiguration"
    ]
    """<p>The authentication configuration of the Amazon Web Services Glue connection.</p>"""
    connection_schema_version: NotRequired["int"]
    """<p>The connection schema version of the Amazon Web Services Glue connection.</p>"""
    compatible_compute_environments: NotRequired[
        "capo_datazone.types.compute_environments_list.ComputeEnvironmentsList"
    ]
    """<p>The compatible compute environments of the Amazon Web Services Glue connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueConnection) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "connection_type" in value:
        import capo_datazone.types.connection_type

        out["connectionType"] = capo_datazone.types.connection_type.serialize_json(
            value["connection_type"]
        )
    if "match_criteria" in value:
        import capo_datazone.types.match_criteria

        out["matchCriteria"] = capo_datazone.types.match_criteria.serialize_json(
            value["match_criteria"]
        )
    if "connection_properties" in value:
        import capo_datazone.types.connection_properties

        out["connectionProperties"] = (
            capo_datazone.types.connection_properties.serialize_json(
                value["connection_properties"]
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
    if "physical_connection_requirements" in value:
        import capo_datazone.types.physical_connection_requirements

        out["physicalConnectionRequirements"] = (
            capo_datazone.types.physical_connection_requirements.serialize_json(
                value["physical_connection_requirements"]
            )
        )
    if "creation_time" in value:
        import capo_datazone.types._prelude.timestamp

        out["creationTime"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_datazone.types._prelude.timestamp

        out["lastUpdatedTime"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "status" in value:
        import capo_datazone.types.connection_status

        out["status"] = capo_datazone.types.connection_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "last_connection_validation_time" in value:
        import capo_datazone.types._prelude.timestamp

        out["lastConnectionValidationTime"] = (
            capo_datazone.types._prelude.timestamp.serialize_json(
                value["last_connection_validation_time"]
            )
        )
    if "authentication_configuration" in value:
        import capo_datazone.types.authentication_configuration

        out["authenticationConfiguration"] = (
            capo_datazone.types.authentication_configuration.serialize_json(
                value["authentication_configuration"]
            )
        )
    if "connection_schema_version" in value:
        out["connectionSchemaVersion"] = value["connection_schema_version"]
    if "compatible_compute_environments" in value:
        import capo_datazone.types.compute_environments_list

        out["compatibleComputeEnvironments"] = (
            capo_datazone.types.compute_environments_list.serialize_json(
                value["compatible_compute_environments"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlueConnection:
    out: GlueConnection = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("connectionType") is not None:
        import capo_datazone.types.connection_type

        out["connection_type"] = capo_datazone.types.connection_type.deserialize_json(
            data["connectionType"]
        )
    if data.get("matchCriteria") is not None:
        import capo_datazone.types.match_criteria

        out["match_criteria"] = capo_datazone.types.match_criteria.deserialize_json(
            data["matchCriteria"]
        )
    if data.get("connectionProperties") is not None:
        import capo_datazone.types.connection_properties

        out["connection_properties"] = (
            capo_datazone.types.connection_properties.deserialize_json(
                data["connectionProperties"]
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
    if data.get("physicalConnectionRequirements") is not None:
        import capo_datazone.types.physical_connection_requirements

        out["physical_connection_requirements"] = (
            capo_datazone.types.physical_connection_requirements.deserialize_json(
                data["physicalConnectionRequirements"]
            )
        )
    if data.get("creationTime") is not None:
        import capo_datazone.types._prelude.timestamp

        out["creation_time"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("lastUpdatedTime") is not None:
        import capo_datazone.types._prelude.timestamp

        out["last_updated_time"] = (
            capo_datazone.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    if data.get("lastUpdatedBy") is not None:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if data.get("status") is not None:
        import capo_datazone.types.connection_status

        out["status"] = capo_datazone.types.connection_status.deserialize_json(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("lastConnectionValidationTime") is not None:
        import capo_datazone.types._prelude.timestamp

        out["last_connection_validation_time"] = (
            capo_datazone.types._prelude.timestamp.deserialize_json(
                data["lastConnectionValidationTime"]
            )
        )
    if data.get("authenticationConfiguration") is not None:
        import capo_datazone.types.authentication_configuration

        out["authentication_configuration"] = (
            capo_datazone.types.authentication_configuration.deserialize_json(
                data["authenticationConfiguration"]
            )
        )
    if data.get("connectionSchemaVersion") is not None:
        out["connection_schema_version"] = data["connectionSchemaVersion"]
    if data.get("compatibleComputeEnvironments") is not None:
        import capo_datazone.types.compute_environments_list

        out["compatible_compute_environments"] = (
            capo_datazone.types.compute_environments_list.deserialize_json(
                data["compatibleComputeEnvironments"]
            )
        )
    return out


def redact_sensitive(value: GlueConnection) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_configuration" in value:
        import capo_datazone.types.authentication_configuration

        out["authentication_configuration"] = (
            capo_datazone.types.authentication_configuration.redact_sensitive(
                value["authentication_configuration"]
            )
        )
    return out
