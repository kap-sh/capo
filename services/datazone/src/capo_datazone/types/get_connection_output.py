"""Generated from Smithy shape ``com.amazonaws.datazone#GetConnectionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.configurations
    import capo_datazone.types.connection_credentials
    import capo_datazone.types.connection_id
    import capo_datazone.types.connection_name
    import capo_datazone.types.connection_properties_output
    import capo_datazone.types.connection_scope
    import capo_datazone.types.connection_type
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.environment_id
    import capo_datazone.types.physical_endpoints
    import capo_datazone.types.project_id


class GetConnectionOutput(TypedDict, closed=True):
    connection_credentials: NotRequired[
        "capo_datazone.types.connection_credentials.ConnectionCredentials"
    ]
    """<p>Connection credentials.</p>"""
    configurations: NotRequired["capo_datazone.types.configurations.Configurations"]
    """<p>The configurations of the connection.</p>"""
    connection_id: "capo_datazone.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>Connection description.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The domain ID of the connection.</p>"""
    domain_unit_id: "capo_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The domain unit ID of the connection.</p>"""
    environment_id: NotRequired["capo_datazone.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment.</p>"""
    environment_user_role: NotRequired["str"]
    """<p>The environment user role.</p>"""
    name: "capo_datazone.types.connection_name.ConnectionName"
    """<p>The name of the connection.</p>"""
    physical_endpoints: "capo_datazone.types.physical_endpoints.PhysicalEndpoints"
    """<p>The physical endpoints of the connection.</p>"""
    project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The ID of the project.</p>"""
    props: NotRequired[
        "capo_datazone.types.connection_properties_output.ConnectionPropertiesOutput"
    ]
    """<p>Connection props.</p>"""
    type: "capo_datazone.types.connection_type.ConnectionType"
    """<p>The type of the connection.</p>"""
    scope: NotRequired["capo_datazone.types.connection_scope.ConnectionScope"]
    """<p>The scope of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionOutput) -> dict:
    out: dict = {}
    if "connection_credentials" in value:
        import capo_datazone.types.connection_credentials

        out["connectionCredentials"] = (
            capo_datazone.types.connection_credentials.serialize_json(
                value["connection_credentials"]
            )
        )
    if "configurations" in value:
        import capo_datazone.types.configurations

        out["configurations"] = capo_datazone.types.configurations.serialize_json(
            value["configurations"]
        )
    out["connectionId"] = value["connection_id"]
    if "description" in value:
        out["description"] = value["description"]
    out["domainId"] = value["domain_id"]
    out["domainUnitId"] = value["domain_unit_id"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "environment_user_role" in value:
        out["environmentUserRole"] = value["environment_user_role"]
    out["name"] = value["name"]
    import capo_datazone.types.physical_endpoints

    out["physicalEndpoints"] = capo_datazone.types.physical_endpoints.serialize_json(
        value["physical_endpoints"]
    )
    if "project_id" in value:
        out["projectId"] = value["project_id"]
    if "props" in value:
        import capo_datazone.types.connection_properties_output

        out["props"] = capo_datazone.types.connection_properties_output.serialize_json(
            value["props"]
        )
    import capo_datazone.types.connection_type

    out["type"] = capo_datazone.types.connection_type.serialize_json(value["type"])
    if "scope" in value:
        import capo_datazone.types.connection_scope

        out["scope"] = capo_datazone.types.connection_scope.serialize_json(
            value["scope"]
        )
    return out


def deserialize_json(data: dict) -> GetConnectionOutput:
    out: GetConnectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("connectionCredentials") is not None:
        import capo_datazone.types.connection_credentials

        out["connection_credentials"] = (
            capo_datazone.types.connection_credentials.deserialize_json(
                data["connectionCredentials"]
            )
        )
    if data.get("configurations") is not None:
        import capo_datazone.types.configurations

        out["configurations"] = capo_datazone.types.configurations.deserialize_json(
            data["configurations"]
        )
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError("GetConnectionOutput.connection_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetConnectionOutput.domain_id required")
    if data.get("domainUnitId") is not None:
        out["domain_unit_id"] = data["domainUnitId"]
    else:
        raise DeserializationError("GetConnectionOutput.domain_unit_id required")
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("environmentUserRole") is not None:
        out["environment_user_role"] = data["environmentUserRole"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetConnectionOutput.name required")
    if data.get("physicalEndpoints") is not None:
        import capo_datazone.types.physical_endpoints

        out["physical_endpoints"] = (
            capo_datazone.types.physical_endpoints.deserialize_json(
                data["physicalEndpoints"]
            )
        )
    else:
        raise DeserializationError("GetConnectionOutput.physical_endpoints required")
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    if data.get("props") is not None:
        import capo_datazone.types.connection_properties_output

        out["props"] = (
            capo_datazone.types.connection_properties_output.deserialize_json(
                data["props"]
            )
        )
    if data.get("type") is not None:
        import capo_datazone.types.connection_type

        out["type"] = capo_datazone.types.connection_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("GetConnectionOutput.type required")
    if data.get("scope") is not None:
        import capo_datazone.types.connection_scope

        out["scope"] = capo_datazone.types.connection_scope.deserialize_json(
            data["scope"]
        )
    return out


def redact_sensitive(value: GetConnectionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection_credentials" in value:
        out["connection_credentials"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "physical_endpoints" in value:
        import capo_datazone.types.physical_endpoints

        out["physical_endpoints"] = (
            capo_datazone.types.physical_endpoints.redact_sensitive(
                value["physical_endpoints"]
            )
        )
    if "props" in value:
        import capo_datazone.types.connection_properties_output

        out["props"] = (
            capo_datazone.types.connection_properties_output.redact_sensitive(
                value["props"]
            )
        )
    return out
