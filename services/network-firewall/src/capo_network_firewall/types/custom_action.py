"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CustomAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.action_definition
    import capo_network_firewall.types.action_name


class CustomAction(TypedDict, closed=True):
    action_name: "capo_network_firewall.types.action_name.ActionName"
    """<p>The descriptive name of the custom action. You can't change the name of a custom action after you create it.</p>"""
    action_definition: "capo_network_firewall.types.action_definition.ActionDefinition"
    """<p>The custom action associated with the action name.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomAction) -> dict:
    out: dict = {}
    out["ActionName"] = value["action_name"]
    import capo_network_firewall.types.action_definition

    out["ActionDefinition"] = (
        capo_network_firewall.types.action_definition.serialize_aws_json_1_0(
            value["action_definition"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomAction:
    out: CustomAction = {}  # type: ignore[typeddict-item]
    if data.get("ActionName") is not None:
        out["action_name"] = data["ActionName"]
    else:
        out["action_name"] = ""
    if data.get("ActionDefinition") is not None:
        import capo_network_firewall.types.action_definition

        out["action_definition"] = (
            capo_network_firewall.types.action_definition.deserialize_aws_json_1_0(
                data["ActionDefinition"]
            )
        )
    else:
        raise DeserializationError("CustomAction.action_definition required")
    return out
