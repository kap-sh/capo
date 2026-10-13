"""Generated from Smithy shape ``com.amazonaws.drs#UpdateLaunchConfigurationTemplateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.launch_configuration_template


class UpdateLaunchConfigurationTemplateResponse(TypedDict, closed=True):
    launch_configuration_template: NotRequired[
        "capo_drs.types.launch_configuration_template.LaunchConfigurationTemplate"
    ]
    """<p>Updated Launch Configuration Template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLaunchConfigurationTemplateResponse) -> dict:
    out: dict = {}
    if "launch_configuration_template" in value:
        import capo_drs.types.launch_configuration_template

        out["launchConfigurationTemplate"] = (
            capo_drs.types.launch_configuration_template.serialize_json(
                value["launch_configuration_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateLaunchConfigurationTemplateResponse:
    out: UpdateLaunchConfigurationTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("launchConfigurationTemplate") is not None:
        import capo_drs.types.launch_configuration_template

        out["launch_configuration_template"] = (
            capo_drs.types.launch_configuration_template.deserialize_json(
                data["launchConfigurationTemplate"]
            )
        )
    return out


def redact_sensitive(
    value: UpdateLaunchConfigurationTemplateResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "launch_configuration_template" in value:
        import capo_drs.types.launch_configuration_template

        out["launch_configuration_template"] = (
            capo_drs.types.launch_configuration_template.redact_sensitive(
                value["launch_configuration_template"]
            )
        )
    return out
