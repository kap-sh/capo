"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IPSet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.variable_definition_list


class IPSet(TypedDict, closed=True):
    definition: (
        "capo_network_firewall.types.variable_definition_list.VariableDefinitionList"
    )
    """<p>The list of IP addresses and address ranges, in CIDR notation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IPSet) -> dict:
    out: dict = {}
    import capo_network_firewall.types.variable_definition_list

    out["Definition"] = (
        capo_network_firewall.types.variable_definition_list.serialize_aws_json_1_0(
            value["definition"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IPSet:
    out: IPSet = {}  # type: ignore[typeddict-item]
    if data.get("Definition") is not None:
        import capo_network_firewall.types.variable_definition_list

        out["definition"] = (
            capo_network_firewall.types.variable_definition_list.deserialize_aws_json_1_0(
                data["Definition"]
            )
        )
    else:
        out["definition"] = []
    return out
