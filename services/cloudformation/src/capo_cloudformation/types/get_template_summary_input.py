"""Generated from Smithy shape ``com.amazonaws.cloudformation#GetTemplateSummaryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.call_as
    import capo_cloudformation.types.stack_name_or_id
    import capo_cloudformation.types.stack_set_name_or_id
    import capo_cloudformation.types.template_body
    import capo_cloudformation.types.template_summary_config
    import capo_cloudformation.types.template_url


class GetTemplateSummaryInput(TypedDict, closed=True):
    template_body: NotRequired["capo_cloudformation.types.template_body.TemplateBody"]
    """<p>Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>"""
    template_url: NotRequired["capo_cloudformation.types.template_url.TemplateURL"]
    """<p>The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>"""
    stack_name: NotRequired["capo_cloudformation.types.stack_name_or_id.StackNameOrId"]
    """<p>The name or the stack ID that's associated with the stack, which aren't always interchangeable. For running stacks, you can specify either the stack's name or its unique stack ID. For deleted stack, you must specify the unique stack ID.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>"""
    stack_set_name: NotRequired[
        "capo_cloudformation.types.stack_set_name_or_id.StackSetNameOrId"
    ]
    """<p>The name or unique ID of the StackSet from which the stack was created.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>"""
    call_as: NotRequired["capo_cloudformation.types.call_as.CallAs"]
    """<p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>"""
    template_summary_config: NotRequired[
        "capo_cloudformation.types.template_summary_config.TemplateSummaryConfig"
    ]
    """<p>Specifies options for the <code>GetTemplateSummary</code> API action.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetTemplateSummaryInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "template_body" in value:
        pairs.append((f"{key_prefix}TemplateBody", str(value["template_body"])))
    if "template_url" in value:
        pairs.append((f"{key_prefix}TemplateURL", str(value["template_url"])))
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
    if "stack_set_name" in value:
        pairs.append((f"{key_prefix}StackSetName", str(value["stack_set_name"])))
    if "call_as" in value:
        import capo_cloudformation.types.call_as

        capo_cloudformation.types.call_as.serialize_query(
            value["call_as"], pairs, f"{key_prefix}CallAs"
        )
    if "template_summary_config" in value:
        import capo_cloudformation.types.template_summary_config

        capo_cloudformation.types.template_summary_config.serialize_query(
            value["template_summary_config"],
            pairs,
            f"{key_prefix}TemplateSummaryConfig",
        )


def deserialize_query(el: Element) -> GetTemplateSummaryInput:
    out: GetTemplateSummaryInput = {}  # type: ignore[typeddict-item]
    child_template_body = el.find("TemplateBody")
    if child_template_body is not None:
        out["template_body"] = str(child_template_body.text or "")
    child_template_url = el.find("TemplateURL")
    if child_template_url is not None:
        out["template_url"] = str(child_template_url.text or "")
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_stack_set_name = el.find("StackSetName")
    if child_stack_set_name is not None:
        out["stack_set_name"] = str(child_stack_set_name.text or "")
    child_call_as = el.find("CallAs")
    if child_call_as is not None:
        import capo_cloudformation.types.call_as

        out["call_as"] = capo_cloudformation.types.call_as.deserialize_query(
            child_call_as
        )
    child_template_summary_config = el.find("TemplateSummaryConfig")
    if child_template_summary_config is not None:
        import capo_cloudformation.types.template_summary_config

        out["template_summary_config"] = (
            capo_cloudformation.types.template_summary_config.deserialize_query(
                child_template_summary_config
            )
        )
    return out
