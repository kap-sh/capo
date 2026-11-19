"""Generated from Smithy shape ``com.amazonaws.cloudformation#SetAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.alias_name
    import capo_cloudformation.types.stack_name


class SetAliasInput(TypedDict, closed=True):
    stack_name: NotRequired["capo_cloudformation.types.stack_name.StackName"]
    """<p>The name or unique stack ID of the stack to assign an alias to.</p>"""
    alias_name: NotRequired["capo_cloudformation.types.alias_name.AliasName"]
    """<p>The alias to assign to the stack. The alias can then be used in place of the stack name in any API call that accepts <code>StackName</code>.</p> <p>The name must be unique within the same account and Region. It cannot match an existing stack name or another active alias.</p> <note> <p>An alias name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 128 characters.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetAliasInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
    if "alias_name" in value:
        pairs.append((f"{key_prefix}AliasName", str(value["alias_name"])))


def deserialize_query(el: Element) -> SetAliasInput:
    out: SetAliasInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_alias_name = el.find("AliasName")
    if child_alias_name is not None:
        out["alias_name"] = str(child_alias_name.text or "")
    return out
