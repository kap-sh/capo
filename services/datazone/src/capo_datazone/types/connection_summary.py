"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.configurations
    import capo_datazone.types.connection_id
    import capo_datazone.types.connection_name
    import capo_datazone.types.connection_properties_output
    import capo_datazone.types.connection_scope
    import capo_datazone.types.connection_type
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.environment_id
    import capo_datazone.types.physical_endpoints
    import capo_datazone.types.project_id


class ConnectionSummary(TypedDict, closed=True):
    configurations: NotRequired["capo_datazone.types.configurations.Configurations"]
    """<p>The configurations of a connection summary.</p>"""
    connection_id: "capo_datazone.types.connection_id.ConnectionId"
    """<p>The ID of a connection.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The domain ID of a connection.</p>"""
    domain_unit_id: "capo_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The domain unit ID of a connection.</p>"""
    environment_id: NotRequired["capo_datazone.types.environment_id.EnvironmentId"]
    """<p>The environment ID of a connection.</p>"""
    name: "capo_datazone.types.connection_name.ConnectionName"
    """<p>The connection name.</p>"""
    physical_endpoints: "capo_datazone.types.physical_endpoints.PhysicalEndpoints"
    """<p>The connection physical endpoints.</p>"""
    project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The connection project ID.</p>"""
    props: NotRequired[
        "capo_datazone.types.connection_properties_output.ConnectionPropertiesOutput"
    ]
    """<p>The connection props.</p>"""
    type: "capo_datazone.types.connection_type.ConnectionType"
    """<p>The connection type.</p>"""
    scope: NotRequired["capo_datazone.types.connection_scope.ConnectionScope"]
    """<p>The scope of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionSummary) -> dict:
    out: dict = {}
    if "configurations" in value:
        import capo_datazone.types.configurations

        out["configurations"] = capo_datazone.types.configurations.serialize_json(
            value["configurations"]
        )
    out["connectionId"] = value["connection_id"]
    out["domainId"] = value["domain_id"]
    out["domainUnitId"] = value["domain_unit_id"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
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


def deserialize_json(data: dict) -> ConnectionSummary:
    out: ConnectionSummary = {}  # type: ignore[typeddict-item]
    if data.get("configurations") is not None:
        import capo_datazone.types.configurations

        out["configurations"] = capo_datazone.types.configurations.deserialize_json(
            data["configurations"]
        )
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError("ConnectionSummary.connection_id required")
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("ConnectionSummary.domain_id required")
    if data.get("domainUnitId") is not None:
        out["domain_unit_id"] = data["domainUnitId"]
    else:
        raise DeserializationError("ConnectionSummary.domain_unit_id required")
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConnectionSummary.name required")
    if data.get("physicalEndpoints") is not None:
        import capo_datazone.types.physical_endpoints

        out["physical_endpoints"] = (
            capo_datazone.types.physical_endpoints.deserialize_json(
                data["physicalEndpoints"]
            )
        )
    else:
        raise DeserializationError("ConnectionSummary.physical_endpoints required")
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
        raise DeserializationError("ConnectionSummary.type required")
    if data.get("scope") is not None:
        import capo_datazone.types.connection_scope

        out["scope"] = capo_datazone.types.connection_scope.deserialize_json(
            data["scope"]
        )
    return out


def redact_sensitive(value: ConnectionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
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
