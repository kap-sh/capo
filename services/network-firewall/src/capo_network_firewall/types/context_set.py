"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContextSet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.context_definition_list


class ContextSet(TypedDict, closed=True):
    definition: (
        "capo_network_firewall.types.context_definition_list.ContextDefinitionList"
    )
    """<p>The list of resource identifiers. Each entry is the ID of a resource that the context store records, for example <code>vpc-1234567890abcdef0</code>, <code>subnet-1234567890abcdef0</code>, <code>sg-1234567890abcdef0</code>, or <code>tgw-attach-1234567890abcdef0</code>. You can specify 1-1,000 entries.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContextSet) -> dict:
    out: dict = {}
    import capo_network_firewall.types.context_definition_list

    out["Definition"] = (
        capo_network_firewall.types.context_definition_list.serialize_aws_json_1_0(
            value["definition"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ContextSet:
    out: ContextSet = {}  # type: ignore[typeddict-item]
    if data.get("Definition") is not None:
        import capo_network_firewall.types.context_definition_list

        out["definition"] = (
            capo_network_firewall.types.context_definition_list.deserialize_aws_json_1_0(
                data["Definition"]
            )
        )
    else:
        out["definition"] = []
    return out
