"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentComponentUpdatePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.deployment_component_update_policy_action
    import capo_greengrassv2.types.optional_integer


class DeploymentComponentUpdatePolicy(TypedDict, closed=True):
    timeout_in_seconds: NotRequired[
        "capo_greengrassv2.types.optional_integer.OptionalInteger"
    ]
    """<p>The amount of time in seconds that each component on a device has to report that it's safe to update. If the component waits for longer than this timeout, then the deployment proceeds on the device.</p> <p>Default: <code>60</code> </p>"""
    action: NotRequired[
        "capo_greengrassv2.types.deployment_component_update_policy_action.DeploymentComponentUpdatePolicyAction"
    ]
    """<p>Whether or not to notify components and wait for components to become safe to update. Choose from the following options:</p> <ul> <li> <p> <code>NOTIFY_COMPONENTS</code> – The deployment notifies each component before it stops and updates that component. Components can use the <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-subscribetocomponentupdates">SubscribeToComponentUpdates</a> IPC operation to receive these notifications. Then, components can respond with the <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-defercomponentupdate">DeferComponentUpdate</a> IPC operation. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html">Create deployments</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p> </li> <li> <p> <code>SKIP_NOTIFY_COMPONENTS</code> – The deployment doesn't notify components or wait for them to be safe to update.</p> </li> </ul> <p>Default: <code>NOTIFY_COMPONENTS</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentComponentUpdatePolicy) -> dict:
    out: dict = {}
    if "timeout_in_seconds" in value:
        out["timeoutInSeconds"] = value["timeout_in_seconds"]
    if "action" in value:
        import capo_greengrassv2.types.deployment_component_update_policy_action

        out["action"] = (
            capo_greengrassv2.types.deployment_component_update_policy_action.serialize_json(
                value["action"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeploymentComponentUpdatePolicy:
    out: DeploymentComponentUpdatePolicy = {}  # type: ignore[typeddict-item]
    if data.get("timeoutInSeconds") is not None:
        out["timeout_in_seconds"] = data["timeoutInSeconds"]
    if data.get("action") is not None:
        import capo_greengrassv2.types.deployment_component_update_policy_action

        out["action"] = (
            capo_greengrassv2.types.deployment_component_update_policy_action.deserialize_json(
                data["action"]
            )
        )
    return out
