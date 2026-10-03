"""Generated from Smithy shape ``com.amazonaws.cloudformation#ModuleInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.logical_id_hierarchy
    import capo_cloudformation.types.type_hierarchy


class ModuleInfo(TypedDict, closed=True):
    type_hierarchy: NotRequired[
        "capo_cloudformation.types.type_hierarchy.TypeHierarchy"
    ]
    """<p>A concatenated list of the module type or types that contains the resource. Module types are listed starting with the inner-most nested module, and separated by <code>/</code>.</p> <p>In the following example, the resource was created from a module of type <code>AWS::First::Example::MODULE</code>, that's nested inside a parent module of type <code>AWS::Second::Example::MODULE</code>.</p> <p> <code>AWS::First::Example::MODULE/AWS::Second::Example::MODULE</code> </p>"""
    logical_id_hierarchy: NotRequired[
        "capo_cloudformation.types.logical_id_hierarchy.LogicalIdHierarchy"
    ]
    """<p>A concatenated list of the logical IDs of the module or modules that contains the resource. Modules are listed starting with the inner-most nested module, and separated by <code>/</code>.</p> <p>In the following example, the resource was created from a module, <code>moduleA</code>, that's nested inside a parent module, <code>moduleB</code>.</p> <p> <code>moduleA/moduleB</code> </p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/module-ref-resources.html">Reference module resources in CloudFormation templates</a> in the <i>CloudFormation User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModuleInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type_hierarchy" in value:
        pairs.append((f"{key_prefix}TypeHierarchy", str(value["type_hierarchy"])))
    if "logical_id_hierarchy" in value:
        pairs.append(
            (f"{key_prefix}LogicalIdHierarchy", str(value["logical_id_hierarchy"]))
        )


def deserialize_query(el: Element) -> ModuleInfo:
    out: ModuleInfo = {}  # type: ignore[typeddict-item]
    child_type_hierarchy = el.find("TypeHierarchy")
    if child_type_hierarchy is not None:
        out["type_hierarchy"] = str(child_type_hierarchy.text or "")
    child_logical_id_hierarchy = el.find("LogicalIdHierarchy")
    if child_logical_id_hierarchy is not None:
        out["logical_id_hierarchy"] = str(child_logical_id_hierarchy.text or "")
    return out
