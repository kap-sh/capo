"""Generated from Smithy shape ``com.amazonaws.athena#UpdateWorkGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.work_group_configuration_updates
    import capo_athena.types.work_group_description_string
    import capo_athena.types.work_group_name
    import capo_athena.types.work_group_state


class UpdateWorkGroupInput(TypedDict, closed=True):
    work_group: "capo_athena.types.work_group_name.WorkGroupName"
    """<p>The specified workgroup that will be updated.</p>"""
    description: NotRequired[
        "capo_athena.types.work_group_description_string.WorkGroupDescriptionString"
    ]
    """<p>The workgroup description.</p>"""
    configuration_updates: NotRequired[
        "capo_athena.types.work_group_configuration_updates.WorkGroupConfigurationUpdates"
    ]
    """<p>Contains configuration updates for an Athena SQL workgroup.</p>"""
    state: NotRequired["capo_athena.types.work_group_state.WorkGroupState"]
    """<p>The workgroup state that will be updated for the given workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkGroupInput) -> dict:
    out: dict = {}
    out["WorkGroup"] = value["work_group"]
    if "description" in value:
        out["Description"] = value["description"]
    if "configuration_updates" in value:
        import capo_athena.types.work_group_configuration_updates

        out["ConfigurationUpdates"] = (
            capo_athena.types.work_group_configuration_updates.serialize_aws_json_1_1(
                value["configuration_updates"]
            )
        )
    if "state" in value:
        import capo_athena.types.work_group_state

        out["State"] = capo_athena.types.work_group_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkGroupInput:
    out: UpdateWorkGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    else:
        out["work_group"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ConfigurationUpdates") is not None:
        import capo_athena.types.work_group_configuration_updates

        out["configuration_updates"] = (
            capo_athena.types.work_group_configuration_updates.deserialize_aws_json_1_1(
                data["ConfigurationUpdates"]
            )
        )
    if data.get("State") is not None:
        import capo_athena.types.work_group_state

        out["state"] = capo_athena.types.work_group_state.deserialize_aws_json_1_1(
            data["State"]
        )
    return out
