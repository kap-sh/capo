"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ConfigurationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.configuration_error_details
    import capo_iotsitewise.types.configuration_state


class ConfigurationStatus(TypedDict, closed=True):
    state: "capo_iotsitewise.types.configuration_state.ConfigurationState"
    """<p>The current state of the configuration.</p>"""
    error: NotRequired[
        "capo_iotsitewise.types.configuration_error_details.ConfigurationErrorDetails"
    ]
    """<p>Contains associated error information, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationStatus) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.configuration_state

    out["state"] = capo_iotsitewise.types.configuration_state.serialize_json(
        value["state"]
    )
    if "error" in value:
        import capo_iotsitewise.types.configuration_error_details

        out["error"] = (
            capo_iotsitewise.types.configuration_error_details.serialize_json(
                value["error"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationStatus:
    out: ConfigurationStatus = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_iotsitewise.types.configuration_state

        out["state"] = capo_iotsitewise.types.configuration_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_iotsitewise.types.configuration_state.ConfigurationState", ""
        )
    if data.get("error") is not None:
        import capo_iotsitewise.types.configuration_error_details

        out["error"] = (
            capo_iotsitewise.types.configuration_error_details.deserialize_json(
                data["error"]
            )
        )
    return out
