"""Generated from Smithy shape ``com.amazonaws.vpclattice#BatchUpdateRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.listener_identifier
    import capo_vpc_lattice.types.rule_update_list
    import capo_vpc_lattice.types.service_identifier


class BatchUpdateRuleRequest(TypedDict, closed=True):
    service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier"
    """<p>The ID or ARN of the listener.</p>"""
    rules: "capo_vpc_lattice.types.rule_update_list.RuleUpdateList"
    """<p>The rules for the specified listener.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRuleRequest) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.rule_update_list

    out["rules"] = capo_vpc_lattice.types.rule_update_list.serialize_json(
        value["rules"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateRuleRequest:
    out: BatchUpdateRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("rules") is not None:
        import capo_vpc_lattice.types.rule_update_list

        out["rules"] = capo_vpc_lattice.types.rule_update_list.deserialize_json(
            data["rules"]
        )
    else:
        out["rules"] = []
    return out
