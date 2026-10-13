"""Generated from Smithy shape ``com.amazonaws.cloud9#Environment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloud9.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloud9.types.connection_type
    import capo_cloud9.types.environment_description
    import capo_cloud9.types.environment_id
    import capo_cloud9.types.environment_lifecycle
    import capo_cloud9.types.environment_name
    import capo_cloud9.types.environment_type
    import capo_cloud9.types.managed_credentials_status
    import capo_cloud9.types.string


class Environment(TypedDict, closed=True):
    id: NotRequired["capo_cloud9.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment.</p>"""
    name: NotRequired["capo_cloud9.types.environment_name.EnvironmentName"]
    """<p>The name of the environment.</p>"""
    description: NotRequired[
        "capo_cloud9.types.environment_description.EnvironmentDescription"
    ]
    """<p>The description for the environment.</p>"""
    type: "capo_cloud9.types.environment_type.EnvironmentType"
    """<p>The type of environment. Valid values include the following:</p> <ul> <li> <p> <code>ec2</code>: An Amazon Elastic Compute Cloud (Amazon EC2) instance connects to the environment.</p> </li> <li> <p> <code>ssh</code>: Your own server connects to the environment.</p> </li> </ul>"""
    connection_type: NotRequired["capo_cloud9.types.connection_type.ConnectionType"]
    """<p>The connection type used for connecting to an Amazon EC2 environment. <code>CONNECT_SSH</code> is selected by default.</p>"""
    arn: "capo_cloud9.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the environment.</p>"""
    owner_arn: "capo_cloud9.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the environment owner.</p>"""
    lifecycle: NotRequired[
        "capo_cloud9.types.environment_lifecycle.EnvironmentLifecycle"
    ]
    """<p>The state of the environment in its creation or deletion lifecycle.</p>"""
    managed_credentials_status: NotRequired[
        "capo_cloud9.types.managed_credentials_status.ManagedCredentialsStatus"
    ]
    """<p>Describes the status of Amazon Web Services managed temporary credentials for the Cloud9 environment. Available values are:</p> <ul> <li> <p> <code>ENABLED_ON_CREATE</code> </p> </li> <li> <p> <code>ENABLED_BY_OWNER</code> </p> </li> <li> <p> <code>DISABLED_BY_DEFAULT</code> </p> </li> <li> <p> <code>DISABLED_BY_OWNER</code> </p> </li> <li> <p> <code>DISABLED_BY_COLLABORATOR</code> </p> </li> <li> <p> <code>PENDING_REMOVAL_BY_COLLABORATOR</code> </p> </li> <li> <p> <code>PENDING_REMOVAL_BY_OWNER</code> </p> </li> <li> <p> <code>FAILED_REMOVAL_BY_COLLABORATOR</code> </p> </li> <li> <p> <code>ENABLED_BY_OWNER</code> </p> </li> <li> <p> <code>DISABLED_BY_DEFAULT</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Environment) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cloud9.types.environment_type

    out["type"] = capo_cloud9.types.environment_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "connection_type" in value:
        import capo_cloud9.types.connection_type

        out["connectionType"] = (
            capo_cloud9.types.connection_type.serialize_aws_json_1_1(
                value["connection_type"]
            )
        )
    out["arn"] = value["arn"]
    out["ownerArn"] = value["owner_arn"]
    if "lifecycle" in value:
        import capo_cloud9.types.environment_lifecycle

        out["lifecycle"] = (
            capo_cloud9.types.environment_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "managed_credentials_status" in value:
        import capo_cloud9.types.managed_credentials_status

        out["managedCredentialsStatus"] = (
            capo_cloud9.types.managed_credentials_status.serialize_aws_json_1_1(
                value["managed_credentials_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_cloud9.types.environment_type

        out["type"] = capo_cloud9.types.environment_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("Environment.type required")
    if data.get("connectionType") is not None:
        import capo_cloud9.types.connection_type

        out["connection_type"] = (
            capo_cloud9.types.connection_type.deserialize_aws_json_1_1(
                data["connectionType"]
            )
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Environment.arn required")
    if data.get("ownerArn") is not None:
        out["owner_arn"] = data["ownerArn"]
    else:
        raise DeserializationError("Environment.owner_arn required")
    if data.get("lifecycle") is not None:
        import capo_cloud9.types.environment_lifecycle

        out["lifecycle"] = (
            capo_cloud9.types.environment_lifecycle.deserialize_aws_json_1_1(
                data["lifecycle"]
            )
        )
    if data.get("managedCredentialsStatus") is not None:
        import capo_cloud9.types.managed_credentials_status

        out["managed_credentials_status"] = (
            capo_cloud9.types.managed_credentials_status.deserialize_aws_json_1_1(
                data["managedCredentialsStatus"]
            )
        )
    return out


def redact_sensitive(value: Environment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
