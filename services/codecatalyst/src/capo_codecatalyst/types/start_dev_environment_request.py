"""Generated from Smithy shape ``com.amazonaws.codecatalyst#StartDevEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.ide_configuration_list
    import capo_codecatalyst.types.inactivity_timeout_minutes
    import capo_codecatalyst.types.instance_type
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.uuid


class StartDevEnvironmentRequest(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment. </p>"""
    ides: NotRequired[
        "capo_codecatalyst.types.ide_configuration_list.IdeConfigurationList"
    ]
    """<p>Information about the integrated development environment (IDE) configured for a Dev Environment. </p>"""
    instance_type: NotRequired["capo_codecatalyst.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 instace type to use for the Dev Environment. </p>"""
    inactivity_timeout_minutes: NotRequired[
        "capo_codecatalyst.types.inactivity_timeout_minutes.InactivityTimeoutMinutes"
    ]
    """<p>The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. Only whole integers are allowed. Dev Environments consume compute minutes when running.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDevEnvironmentRequest) -> dict:
    out: dict = {}
    if "ides" in value:
        import capo_codecatalyst.types.ide_configuration_list

        out["ides"] = capo_codecatalyst.types.ide_configuration_list.serialize_json(
            value["ides"]
        )
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "inactivity_timeout_minutes" in value:
        out["inactivityTimeoutMinutes"] = value["inactivity_timeout_minutes"]
    return out


def deserialize_json(data: dict) -> StartDevEnvironmentRequest:
    out: StartDevEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("ides") is not None:
        import capo_codecatalyst.types.ide_configuration_list

        out["ides"] = capo_codecatalyst.types.ide_configuration_list.deserialize_json(
            data["ides"]
        )
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("inactivityTimeoutMinutes") is not None:
        out["inactivity_timeout_minutes"] = data["inactivityTimeoutMinutes"]
    return out
