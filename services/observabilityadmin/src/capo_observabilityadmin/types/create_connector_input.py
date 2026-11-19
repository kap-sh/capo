"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateConnectorInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.client_token
    import capo_observabilityadmin.types.connector_configuration
    import capo_observabilityadmin.types.connector_name
    import capo_observabilityadmin.types.role_arn
    import capo_observabilityadmin.types.tag_map_input


class CreateConnectorInput(TypedDict, closed=True):
    connector_configuration: (
        "capo_observabilityadmin.types.connector_configuration.ConnectorConfiguration"
    )
    """<p>The configuration for connecting to the third-party cloud provider.</p>"""
    role_arn: "capo_observabilityadmin.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role that CloudWatch assumes to get credentials for the third-party cloud provider. The role must trust the Amazon CloudWatch Observability Admin service principal, <code>observabilityadmin.amazonaws.com</code>. The role must also allow <code>sts:GetWebIdentityToken</code> for the provider's token exchange audience.</p>"""
    name: "capo_observabilityadmin.types.connector_name.ConnectorName"
    """<p>The name of the connector. The name must be unique in the account and Region (case-sensitive). If another connector already uses the name, the request fails with a <code>ConflictException</code>.</p> <p>The name can contain letters, digits, hyphens (-), underscores (_) and periods (.), and must start with a letter.</p>"""
    tags: NotRequired["capo_observabilityadmin.types.tag_map_input.TagMapInput"]
    """<p>The tags that you want to apply to the connector.</p>"""
    client_token: NotRequired["capo_observabilityadmin.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the operation completes no more than one time. If you use an Amazon Web Services SDK, the SDK generates this value and reuses it on retries. If this token matches a previous request with the same parameters, the service returns the connector from the first request without an error. If you use the same token with different parameters, including different tags, the service returns a <code>ValidationException</code>. This operation is idempotent when you use the same token and parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorInput) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.connector_configuration

    out["ConnectorConfiguration"] = (
        capo_observabilityadmin.types.connector_configuration.serialize_json(
            value["connector_configuration"]
        )
    )
    out["RoleArn"] = value["role_arn"]
    out["Name"] = value["name"]
    if "tags" in value:
        import capo_observabilityadmin.types.tag_map_input

        out["Tags"] = capo_observabilityadmin.types.tag_map_input.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateConnectorInput:
    out: CreateConnectorInput = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorConfiguration") is not None:
        import capo_observabilityadmin.types.connector_configuration

        out["connector_configuration"] = (
            capo_observabilityadmin.types.connector_configuration.deserialize_json(
                data["ConnectorConfiguration"]
            )
        )
    else:
        out["connector_configuration"] = {"$unknown": {"name": ""}}
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Tags") is not None:
        import capo_observabilityadmin.types.tag_map_input

        out["tags"] = capo_observabilityadmin.types.tag_map_input.deserialize_json(
            data["Tags"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: CreateConnectorInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_token" in value:
        out["client_token"] = "*** Sensitive Data Redacted ***"
    return out
