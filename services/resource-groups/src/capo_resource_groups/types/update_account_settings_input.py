"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UpdateAccountSettingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_lifecycle_events_desired_status


class UpdateAccountSettingsInput(TypedDict, closed=True):
    group_lifecycle_events_desired_status: NotRequired[
        "capo_resource_groups.types.group_lifecycle_events_desired_status.GroupLifecycleEventsDesiredStatus"
    ]
    """<p>Specifies whether you want to turn <a href="https://docs.aws.amazon.com/ARG/latest/userguide/monitor-groups.html">group lifecycle events</a> on or off.</p> <p>You can't turn on group lifecycle events if your resource groups quota is greater than 2,000. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountSettingsInput) -> dict:
    out: dict = {}
    if "group_lifecycle_events_desired_status" in value:
        import capo_resource_groups.types.group_lifecycle_events_desired_status

        out["GroupLifecycleEventsDesiredStatus"] = (
            capo_resource_groups.types.group_lifecycle_events_desired_status.serialize_json(
                value["group_lifecycle_events_desired_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountSettingsInput:
    out: UpdateAccountSettingsInput = {}  # type: ignore[typeddict-item]
    if data.get("GroupLifecycleEventsDesiredStatus") is not None:
        import capo_resource_groups.types.group_lifecycle_events_desired_status

        out["group_lifecycle_events_desired_status"] = (
            capo_resource_groups.types.group_lifecycle_events_desired_status.deserialize_json(
                data["GroupLifecycleEventsDesiredStatus"]
            )
        )
    return out
