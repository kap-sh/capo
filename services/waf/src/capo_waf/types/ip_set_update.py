"""Generated from Smithy shape ``com.amazonaws.waf#IPSetUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.change_action
    import capo_waf.types.ip_set_descriptor


class IPSetUpdate(TypedDict, closed=True):
    action: "capo_waf.types.change_action.ChangeAction"
    """<p>Specifies whether to insert or delete an IP address with <a>UpdateIPSet</a>.</p>"""
    ip_set_descriptor: "capo_waf.types.ip_set_descriptor.IPSetDescriptor"
    """<p>The IP address type (<code>IPV4</code> or <code>IPV6</code>) and the IP address range (in CIDR notation) that web requests originate from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSetUpdate) -> dict:
    out: dict = {}
    import capo_waf.types.change_action

    out["Action"] = capo_waf.types.change_action.serialize_aws_json_1_1(value["action"])
    import capo_waf.types.ip_set_descriptor

    out["IPSetDescriptor"] = capo_waf.types.ip_set_descriptor.serialize_aws_json_1_1(
        value["ip_set_descriptor"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IPSetUpdate:
    out: IPSetUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_waf.types.change_action

        out["action"] = capo_waf.types.change_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast("capo_waf.types.change_action.ChangeAction", "")
    if data.get("IPSetDescriptor") is not None:
        import capo_waf.types.ip_set_descriptor

        out["ip_set_descriptor"] = (
            capo_waf.types.ip_set_descriptor.deserialize_aws_json_1_1(
                data["IPSetDescriptor"]
            )
        )
    else:
        raise DeserializationError("IPSetUpdate.ip_set_descriptor required")
    return out
