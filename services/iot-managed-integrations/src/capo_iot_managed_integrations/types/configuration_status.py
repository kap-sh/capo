"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConfigurationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.configuration_error
    import capo_iot_managed_integrations.types.configuration_state


class ConfigurationStatus(TypedDict, closed=True):
    error: NotRequired[
        "capo_iot_managed_integrations.types.configuration_error.ConfigurationError"
    ]
    """<p>The error details describing a failed default encryption configuration update.</p>"""
    state: "capo_iot_managed_integrations.types.configuration_state.ConfigurationState"
    """<p>The status state describing the default encryption configuration update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationStatus) -> dict:
    out: dict = {}
    if "error" in value:
        import capo_iot_managed_integrations.types.configuration_error

        out["error"] = (
            capo_iot_managed_integrations.types.configuration_error.serialize_json(
                value["error"]
            )
        )
    import capo_iot_managed_integrations.types.configuration_state

    out["state"] = (
        capo_iot_managed_integrations.types.configuration_state.serialize_json(
            value["state"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConfigurationStatus:
    out: ConfigurationStatus = {}  # type: ignore[typeddict-item]
    if data.get("error") is not None:
        import capo_iot_managed_integrations.types.configuration_error

        out["error"] = (
            capo_iot_managed_integrations.types.configuration_error.deserialize_json(
                data["error"]
            )
        )
    if data.get("state") is not None:
        import capo_iot_managed_integrations.types.configuration_state

        out["state"] = (
            capo_iot_managed_integrations.types.configuration_state.deserialize_json(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_iot_managed_integrations.types.configuration_state.ConfigurationState",
            "",
        )
    return out
