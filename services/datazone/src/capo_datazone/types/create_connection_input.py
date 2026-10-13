"""Generated from Smithy shape ``com.amazonaws.datazone#CreateConnectionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.aws_location
    import capo_datazone.types.configurations
    import capo_datazone.types.connection_name
    import capo_datazone.types.connection_properties_input
    import capo_datazone.types.connection_scope
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_id


class CreateConnectionInput(TypedDict, closed=True):
    aws_location: NotRequired["capo_datazone.types.aws_location.AwsLocation"]
    """<p>The location where the connection is created.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""
    configurations: NotRequired["capo_datazone.types.configurations.Configurations"]
    """<p>The configurations of the connection.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>A connection description.</p>"""
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the connection is created.</p>"""
    environment_identifier: NotRequired[
        "capo_datazone.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the environment where the connection is created.</p>"""
    name: "capo_datazone.types.connection_name.ConnectionName"
    """<p>The connection name.</p>"""
    props: NotRequired[
        "capo_datazone.types.connection_properties_input.ConnectionPropertiesInput"
    ]
    """<p>The connection props.</p>"""
    enable_trusted_identity_propagation: NotRequired["bool"]
    """<p>Specifies whether the trusted identity propagation is enabled.</p>"""
    scope: NotRequired["capo_datazone.types.connection_scope.ConnectionScope"]
    """<p>The scope of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectionInput) -> dict:
    out: dict = {}
    if "aws_location" in value:
        import capo_datazone.types.aws_location

        out["awsLocation"] = capo_datazone.types.aws_location.serialize_json(
            value["aws_location"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "configurations" in value:
        import capo_datazone.types.configurations

        out["configurations"] = capo_datazone.types.configurations.serialize_json(
            value["configurations"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "environment_identifier" in value:
        out["environmentIdentifier"] = value["environment_identifier"]
    out["name"] = value["name"]
    if "props" in value:
        import capo_datazone.types.connection_properties_input

        out["props"] = capo_datazone.types.connection_properties_input.serialize_json(
            value["props"]
        )
    if "enable_trusted_identity_propagation" in value:
        out["enableTrustedIdentityPropagation"] = value[
            "enable_trusted_identity_propagation"
        ]
    if "scope" in value:
        import capo_datazone.types.connection_scope

        out["scope"] = capo_datazone.types.connection_scope.serialize_json(
            value["scope"]
        )
    return out


def deserialize_json(data: dict) -> CreateConnectionInput:
    out: CreateConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("awsLocation") is not None:
        import capo_datazone.types.aws_location

        out["aws_location"] = capo_datazone.types.aws_location.deserialize_json(
            data["awsLocation"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("configurations") is not None:
        import capo_datazone.types.configurations

        out["configurations"] = capo_datazone.types.configurations.deserialize_json(
            data["configurations"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("environmentIdentifier") is not None:
        out["environment_identifier"] = data["environmentIdentifier"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateConnectionInput.name required")
    if data.get("props") is not None:
        import capo_datazone.types.connection_properties_input

        out["props"] = capo_datazone.types.connection_properties_input.deserialize_json(
            data["props"]
        )
    if data.get("enableTrustedIdentityPropagation") is not None:
        out["enable_trusted_identity_propagation"] = data[
            "enableTrustedIdentityPropagation"
        ]
    if data.get("scope") is not None:
        import capo_datazone.types.connection_scope

        out["scope"] = capo_datazone.types.connection_scope.deserialize_json(
            data["scope"]
        )
    return out


def redact_sensitive(value: CreateConnectionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "props" in value:
        import capo_datazone.types.connection_properties_input

        out["props"] = capo_datazone.types.connection_properties_input.redact_sensitive(
            value["props"]
        )
    return out
