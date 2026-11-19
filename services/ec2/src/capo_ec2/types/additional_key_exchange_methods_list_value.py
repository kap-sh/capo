"""Generated from Smithy shape ``com.amazonaws.ec2#AdditionalKeyExchangeMethodsListValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer


class AdditionalKeyExchangeMethodsListValue(TypedDict, closed=True):
    value: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The key exchange method number.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AdditionalKeyExchangeMethodsListValue,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_ec2_query(el: Element) -> AdditionalKeyExchangeMethodsListValue:
    out: AdditionalKeyExchangeMethodsListValue = {}  # type: ignore[typeddict-item]
    child_value = el.find("value")
    if child_value is not None:
        out["value"] = int(child_value.text or "")
    return out
