"""Generated from Smithy shape ``com.amazonaws.cloud9#UpdateEnvironmentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.environment_description
    import capo_cloud9.types.environment_id
    import capo_cloud9.types.environment_name
    import capo_cloud9.types.managed_credentials_action


class UpdateEnvironmentRequest(TypedDict, closed=True):
    environment_id: "capo_cloud9.types.environment_id.EnvironmentId"
    """<p>The ID of the environment to change settings.</p>"""
    name: NotRequired["capo_cloud9.types.environment_name.EnvironmentName"]
    """<p>A replacement name for the environment.</p>"""
    description: NotRequired[
        "capo_cloud9.types.environment_description.EnvironmentDescription"
    ]
    """<p>Any new or replacement description for the environment.</p>"""
    managed_credentials_action: NotRequired[
        "capo_cloud9.types.managed_credentials_action.ManagedCredentialsAction"
    ]
    """<p>Allows the environment owner to turn on or turn off the Amazon Web Services managed temporary credentials for an Cloud9 environment by using one of the following values:</p> <ul> <li> <p> <code>ENABLE</code> </p> </li> <li> <p> <code>DISABLE</code> </p> </li> </ul> <note> <p>Only the environment owner can change the status of managed temporary credentials. An <code>AccessDeniedException</code> is thrown if an attempt to turn on or turn off managed temporary credentials is made by an account that's not the environment owner.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEnvironmentRequest) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "managed_credentials_action" in value:
        import capo_cloud9.types.managed_credentials_action

        out["managedCredentialsAction"] = (
            capo_cloud9.types.managed_credentials_action.serialize_aws_json_1_1(
                value["managed_credentials_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEnvironmentRequest:
    out: UpdateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("managedCredentialsAction") is not None:
        import capo_cloud9.types.managed_credentials_action

        out["managed_credentials_action"] = (
            capo_cloud9.types.managed_credentials_action.deserialize_aws_json_1_1(
                data["managedCredentialsAction"]
            )
        )
    return out


def redact_sensitive(value: UpdateEnvironmentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
