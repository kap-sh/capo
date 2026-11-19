"""Generated from Smithy shape ``com.amazonaws.cloudformation#RemoveAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.alias_name


class RemoveAliasInput(TypedDict, closed=True):
    alias_name: NotRequired["capo_cloudformation.types.alias_name.AliasName"]
    """<p>The alias name to remove.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveAliasInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alias_name" in value:
        pairs.append((f"{key_prefix}AliasName", str(value["alias_name"])))


def deserialize_query(el: Element) -> RemoveAliasInput:
    out: RemoveAliasInput = {}  # type: ignore[typeddict-item]
    child_alias_name = el.find("AliasName")
    if child_alias_name is not None:
        out["alias_name"] = str(child_alias_name.text or "")
    return out
