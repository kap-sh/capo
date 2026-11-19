"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PortSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.variable_definition_list


class PortSet(TypedDict, closed=True):
    definition: NotRequired[
        "capo_network_firewall.types.variable_definition_list.VariableDefinitionList"
    ]
    """<p>The set of port ranges. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PortSet) -> dict:
    out: dict = {}
    if "definition" in value:
        import capo_network_firewall.types.variable_definition_list

        out["Definition"] = (
            capo_network_firewall.types.variable_definition_list.serialize_aws_json_1_0(
                value["definition"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PortSet:
    out: PortSet = {}  # type: ignore[typeddict-item]
    if data.get("Definition") is not None:
        import capo_network_firewall.types.variable_definition_list

        out["definition"] = (
            capo_network_firewall.types.variable_definition_list.deserialize_aws_json_1_0(
                data["Definition"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PortSet) -> dict:
    out: dict = {}
    if "definition" in value:
        import capo_network_firewall.types.variable_definition_list

        out["Definition"] = (
            capo_network_firewall.types.variable_definition_list.serialize_cbor(
                value["definition"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PortSet:
    out: PortSet = {}  # type: ignore[typeddict-item]
    if data.get("Definition") is not None:
        import capo_network_firewall.types.variable_definition_list

        out["definition"] = (
            capo_network_firewall.types.variable_definition_list.deserialize_cbor(
                data["Definition"]
            )
        )
    return out
