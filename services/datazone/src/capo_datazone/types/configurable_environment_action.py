"""Generated from Smithy shape ``com.amazonaws.datazone#ConfigurableEnvironmentAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.configurable_action_parameter_list
    import capo_datazone.types.configurable_action_type_authorization


class ConfigurableEnvironmentAction(TypedDict, closed=True):
    type: "str"
    """<p>The type of a configurable action in a Amazon DataZone environment.</p>"""
    auth: NotRequired[
        "capo_datazone.types.configurable_action_type_authorization.ConfigurableActionTypeAuthorization"
    ]
    """<p>The authentication type of a configurable action of a Amazon DataZone environment. </p>"""
    parameters: "capo_datazone.types.configurable_action_parameter_list.ConfigurableActionParameterList"
    """<p>The parameters of a configurable action in a Amazon DataZone environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurableEnvironmentAction) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "auth" in value:
        import capo_datazone.types.configurable_action_type_authorization

        out["auth"] = (
            capo_datazone.types.configurable_action_type_authorization.serialize_json(
                value["auth"]
            )
        )
    import capo_datazone.types.configurable_action_parameter_list

    out["parameters"] = (
        capo_datazone.types.configurable_action_parameter_list.serialize_json(
            value["parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConfigurableEnvironmentAction:
    out: ConfigurableEnvironmentAction = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("auth") is not None:
        import capo_datazone.types.configurable_action_type_authorization

        out["auth"] = (
            capo_datazone.types.configurable_action_type_authorization.deserialize_json(
                data["auth"]
            )
        )
    if data.get("parameters") is not None:
        import capo_datazone.types.configurable_action_parameter_list

        out["parameters"] = (
            capo_datazone.types.configurable_action_parameter_list.deserialize_json(
                data["parameters"]
            )
        )
    else:
        out["parameters"] = []
    return out
