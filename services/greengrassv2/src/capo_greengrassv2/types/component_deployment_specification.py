"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentDeploymentSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_configuration_update
    import capo_greengrassv2.types.component_run_with
    import capo_greengrassv2.types.component_version_string


class ComponentDeploymentSpecification(TypedDict, closed=True):
    component_version: (
        "capo_greengrassv2.types.component_version_string.ComponentVersionString"
    )
    """<p>The version of the component.</p>"""
    configuration_update: NotRequired[
        "capo_greengrassv2.types.component_configuration_update.ComponentConfigurationUpdate"
    ]
    """<p>The configuration updates to deploy for the component. You can define <i>reset</i> updates and <i>merge</i> updates. A reset updates the keys that you specify to the default configuration for the component. A merge updates the core device's component configuration with the keys and values that you specify. The IoT Greengrass Core software applies reset updates before it applies merge updates. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html">Update component configurations</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""
    run_with: NotRequired["capo_greengrassv2.types.component_run_with.ComponentRunWith"]
    """<p>The system user and group that the IoT Greengrass Core software uses to run component processes on the core device. If you omit this parameter, the IoT Greengrass Core software uses the system user and group that you configure for the core device. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user">Configure the user and group that run components</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentDeploymentSpecification) -> dict:
    out: dict = {}
    out["componentVersion"] = value["component_version"]
    if "configuration_update" in value:
        import capo_greengrassv2.types.component_configuration_update

        out["configurationUpdate"] = (
            capo_greengrassv2.types.component_configuration_update.serialize_json(
                value["configuration_update"]
            )
        )
    if "run_with" in value:
        import capo_greengrassv2.types.component_run_with

        out["runWith"] = capo_greengrassv2.types.component_run_with.serialize_json(
            value["run_with"]
        )
    return out


def deserialize_json(data: dict) -> ComponentDeploymentSpecification:
    out: ComponentDeploymentSpecification = {}  # type: ignore[typeddict-item]
    if data.get("componentVersion") is not None:
        out["component_version"] = data["componentVersion"]
    else:
        raise DeserializationError(
            "ComponentDeploymentSpecification.component_version required"
        )
    if data.get("configurationUpdate") is not None:
        import capo_greengrassv2.types.component_configuration_update

        out["configuration_update"] = (
            capo_greengrassv2.types.component_configuration_update.deserialize_json(
                data["configurationUpdate"]
            )
        )
    if data.get("runWith") is not None:
        import capo_greengrassv2.types.component_run_with

        out["run_with"] = capo_greengrassv2.types.component_run_with.deserialize_json(
            data["runWith"]
        )
    return out
