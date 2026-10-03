"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentAccountConnectionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.arn
    import capo_proton.types.aws_account_id
    import capo_proton.types.environment_account_connection_arn
    import capo_proton.types.environment_account_connection_id
    import capo_proton.types.environment_account_connection_status
    import capo_proton.types.resource_name


class EnvironmentAccountConnectionSummary(TypedDict, closed=True):
    id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
    """<p>The ID of the environment account connection.</p>"""
    arn: "capo_proton.types.environment_account_connection_arn.EnvironmentAccountConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the environment account connection.</p>"""
    management_account_id: "capo_proton.types.aws_account_id.AwsAccountId"
    """<p>The ID of the management account that's connected to the environment account connection.</p>"""
    environment_account_id: "capo_proton.types.aws_account_id.AwsAccountId"
    """<p>The ID of the environment account that's connected to the environment account connection.</p>"""
    role_arn: "capo_proton.types.arn.Arn"
    """<p>The IAM service role that's associated with the environment account connection.</p>"""
    environment_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment that's associated with the environment account connection.</p>"""
    requested_at: "datetime.datetime"
    """<p>The time when the environment account connection request was made.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The time when the environment account connection was last modified.</p>"""
    status: "capo_proton.types.environment_account_connection_status.EnvironmentAccountConnectionStatus"
    """<p>The status of the environment account connection.</p>"""
    component_role_arn: NotRequired["capo_proton.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>The environment account connection must have a <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in the account.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentAccountConnectionSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["managementAccountId"] = value["management_account_id"]
    out["environmentAccountId"] = value["environment_account_id"]
    out["roleArn"] = value["role_arn"]
    out["environmentName"] = value["environment_name"]
    import capo_proton.types._prelude.timestamp

    out["requestedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["requested_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastModifiedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["last_modified_at"]
    )
    out["status"] = value["status"]
    if "component_role_arn" in value:
        out["componentRoleArn"] = value["component_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EnvironmentAccountConnectionSummary:
    out: EnvironmentAccountConnectionSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("EnvironmentAccountConnectionSummary.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EnvironmentAccountConnectionSummary.arn required")
    if data.get("managementAccountId") is not None:
        out["management_account_id"] = data["managementAccountId"]
    else:
        raise DeserializationError(
            "EnvironmentAccountConnectionSummary.management_account_id required"
        )
    if data.get("environmentAccountId") is not None:
        out["environment_account_id"] = data["environmentAccountId"]
    else:
        raise DeserializationError(
            "EnvironmentAccountConnectionSummary.environment_account_id required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "EnvironmentAccountConnectionSummary.role_arn required"
        )
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError(
            "EnvironmentAccountConnectionSummary.environment_name required"
        )
    if data.get("requestedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["requested_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["requestedAt"]
            )
        )
    else:
        raise DeserializationError(
            "EnvironmentAccountConnectionSummary.requested_at required"
        )
    if data.get("lastModifiedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError(
            "EnvironmentAccountConnectionSummary.last_modified_at required"
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError(
            "EnvironmentAccountConnectionSummary.status required"
        )
    if data.get("componentRoleArn") is not None:
        out["component_role_arn"] = data["componentRoleArn"]
    return out
