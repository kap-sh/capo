"""Generated from Smithy shape ``com.amazonaws.cloudformation#TemplateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.generated_template_deletion_policy
    import capo_cloudformation.types.generated_template_update_replace_policy


class TemplateConfiguration(TypedDict, closed=True):
    deletion_policy: NotRequired[
        "capo_cloudformation.types.generated_template_deletion_policy.GeneratedTemplateDeletionPolicy"
    ]
    """<p>The <code>DeletionPolicy</code> assigned to resources in the generated template. Supported values are:</p> <ul> <li> <p> <code>DELETE</code> - delete all resources when the stack is deleted.</p> </li> <li> <p> <code>RETAIN</code> - retain all resources when the stack is deleted.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html">DeletionPolicy attribute</a> in the <i>CloudFormation User Guide</i>.</p>"""
    update_replace_policy: NotRequired[
        "capo_cloudformation.types.generated_template_update_replace_policy.GeneratedTemplateUpdateReplacePolicy"
    ]
    """<p>The <code>UpdateReplacePolicy</code> assigned to resources in the generated template. Supported values are:</p> <ul> <li> <p> <code>DELETE</code> - delete all resources when the resource is replaced during an update operation.</p> </li> <li> <p> <code>RETAIN</code> - retain all resources when the resource is replaced during an update operation.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html">UpdateReplacePolicy attribute</a> in the <i>CloudFormation User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TemplateConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "deletion_policy" in value:
        import capo_cloudformation.types.generated_template_deletion_policy

        capo_cloudformation.types.generated_template_deletion_policy.serialize_query(
            value["deletion_policy"], pairs, f"{key_prefix}DeletionPolicy"
        )
    if "update_replace_policy" in value:
        import capo_cloudformation.types.generated_template_update_replace_policy

        capo_cloudformation.types.generated_template_update_replace_policy.serialize_query(
            value["update_replace_policy"], pairs, f"{key_prefix}UpdateReplacePolicy"
        )


def deserialize_query(el: Element) -> TemplateConfiguration:
    out: TemplateConfiguration = {}  # type: ignore[typeddict-item]
    child_deletion_policy = el.find("DeletionPolicy")
    if child_deletion_policy is not None:
        import capo_cloudformation.types.generated_template_deletion_policy

        out["deletion_policy"] = (
            capo_cloudformation.types.generated_template_deletion_policy.deserialize_query(
                child_deletion_policy
            )
        )
    child_update_replace_policy = el.find("UpdateReplacePolicy")
    if child_update_replace_policy is not None:
        import capo_cloudformation.types.generated_template_update_replace_policy

        out["update_replace_policy"] = (
            capo_cloudformation.types.generated_template_update_replace_policy.deserialize_query(
                child_update_replace_policy
            )
        )
    return out
