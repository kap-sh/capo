"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateKmsKeyIdResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean

DisassociateKmsKeyIdResult = TypedDict(
    "DisassociateKmsKeyIdResult",
    {
        "return": NotRequired["capo_ec2.types.boolean.Boolean"],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateKmsKeyIdResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "return" in value:
        pairs.append((f"{key_prefix}Return", "true" if value["return"] else "false"))


def deserialize_ec2_query(el: Element) -> DisassociateKmsKeyIdResult:
    out: DisassociateKmsKeyIdResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("return")
    if child_return is not None:
        out["return"] = (child_return.text or "").lower() == "true"
    return out
