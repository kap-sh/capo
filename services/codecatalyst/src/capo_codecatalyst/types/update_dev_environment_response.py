"""Generated from Smithy shape ``com.amazonaws.codecatalyst#UpdateDevEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.client_token
    import capo_codecatalyst.types.ide_configuration_list
    import capo_codecatalyst.types.inactivity_timeout_minutes
    import capo_codecatalyst.types.instance_type
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.uuid


class UpdateDevEnvironmentResponse(TypedDict, closed=True):
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment. </p>"""
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    alias: NotRequired["str"]
    """<p>The user-specified alias for the Dev Environment.</p>"""
    ides: NotRequired[
        "capo_codecatalyst.types.ide_configuration_list.IdeConfigurationList"
    ]
    """<p>Information about the integrated development environment (IDE) configured for the Dev Environment.</p>"""
    instance_type: NotRequired["capo_codecatalyst.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 instace type to use for the Dev Environment. </p>"""
    inactivity_timeout_minutes: (
        "capo_codecatalyst.types.inactivity_timeout_minutes.InactivityTimeoutMinutes"
    )
    """<p>The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. </p>"""
    client_token: NotRequired["capo_codecatalyst.types.client_token.ClientToken"]
    """<p>A user-specified idempotency token. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries return the result from the original successful request and have no additional effect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDevEnvironmentResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    if "alias" in value:
        out["alias"] = value["alias"]
    if "ides" in value:
        import capo_codecatalyst.types.ide_configuration_list

        out["ides"] = capo_codecatalyst.types.ide_configuration_list.serialize_json(
            value["ides"]
        )
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    out["inactivityTimeoutMinutes"] = value.get("inactivity_timeout_minutes", 0)
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateDevEnvironmentResponse:
    out: UpdateDevEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("spaceName") is not None:
        out["space_name"] = data["spaceName"]
    else:
        out["space_name"] = ""
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        out["project_name"] = ""
    if data.get("alias") is not None:
        out["alias"] = data["alias"]
    if data.get("ides") is not None:
        import capo_codecatalyst.types.ide_configuration_list

        out["ides"] = capo_codecatalyst.types.ide_configuration_list.deserialize_json(
            data["ides"]
        )
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("inactivityTimeoutMinutes") is not None:
        out["inactivity_timeout_minutes"] = data["inactivityTimeoutMinutes"]
    else:
        out["inactivity_timeout_minutes"] = 0
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
