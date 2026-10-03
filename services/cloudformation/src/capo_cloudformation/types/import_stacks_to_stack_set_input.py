"""Generated from Smithy shape ``com.amazonaws.cloudformation#ImportStacksToStackSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.call_as
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.organizational_unit_id_list
    import capo_cloudformation.types.stack_id_list
    import capo_cloudformation.types.stack_ids_url
    import capo_cloudformation.types.stack_set_name_or_id
    import capo_cloudformation.types.stack_set_operation_preferences


class ImportStacksToStackSetInput(TypedDict, closed=True):
    stack_set_name: NotRequired[
        "capo_cloudformation.types.stack_set_name_or_id.StackSetNameOrId"
    ]
    """<p>The name of the StackSet. The name must be unique in the Region where you create your StackSet.</p>"""
    stack_ids: NotRequired["capo_cloudformation.types.stack_id_list.StackIdList"]
    """<p>The IDs of the stacks you are importing into a StackSet. You import up to 10 stacks per StackSet at a time.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>"""
    stack_ids_url: NotRequired["capo_cloudformation.types.stack_ids_url.StackIdsUrl"]
    """<p>The Amazon S3 URL which contains list of stack ids to be inputted.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>"""
    organizational_unit_ids: NotRequired[
        "capo_cloudformation.types.organizational_unit_id_list.OrganizationalUnitIdList"
    ]
    """<p>The list of OU ID's to which the imported stacks must be mapped as deployment targets.</p>"""
    operation_preferences: NotRequired[
        "capo_cloudformation.types.stack_set_operation_preferences.StackSetOperationPreferences"
    ]
    """<p>The user-specified preferences for how CloudFormation performs a StackSet operation.</p> <p>For more information about maximum concurrent accounts and failure tolerance, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">StackSet operation options</a>.</p>"""
    operation_id: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, user defined, identifier for the StackSet operation.</p>"""
    call_as: NotRequired["capo_cloudformation.types.call_as.CallAs"]
    """<p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>For service managed StackSets, specify <code>DELEGATED_ADMIN</code>.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ImportStacksToStackSetInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_set_name" in value:
        pairs.append((f"{key_prefix}StackSetName", str(value["stack_set_name"])))
    if "stack_ids" in value:
        import capo_cloudformation.types.stack_id_list

        capo_cloudformation.types.stack_id_list.serialize_query(
            value["stack_ids"], pairs, f"{key_prefix}StackIds"
        )
    if "stack_ids_url" in value:
        pairs.append((f"{key_prefix}StackIdsUrl", str(value["stack_ids_url"])))
    if "organizational_unit_ids" in value:
        import capo_cloudformation.types.organizational_unit_id_list

        capo_cloudformation.types.organizational_unit_id_list.serialize_query(
            value["organizational_unit_ids"],
            pairs,
            f"{key_prefix}OrganizationalUnitIds",
        )
    if "operation_preferences" in value:
        import capo_cloudformation.types.stack_set_operation_preferences

        capo_cloudformation.types.stack_set_operation_preferences.serialize_query(
            value["operation_preferences"], pairs, f"{key_prefix}OperationPreferences"
        )
    if "operation_id" in value:
        pairs.append((f"{key_prefix}OperationId", str(value["operation_id"])))
    if "call_as" in value:
        import capo_cloudformation.types.call_as

        capo_cloudformation.types.call_as.serialize_query(
            value["call_as"], pairs, f"{key_prefix}CallAs"
        )


def deserialize_query(el: Element) -> ImportStacksToStackSetInput:
    out: ImportStacksToStackSetInput = {}  # type: ignore[typeddict-item]
    child_stack_set_name = el.find("StackSetName")
    if child_stack_set_name is not None:
        out["stack_set_name"] = str(child_stack_set_name.text or "")
    child_stack_ids = el.find("StackIds")
    if child_stack_ids is not None:
        import capo_cloudformation.types.stack_id_list

        out["stack_ids"] = capo_cloudformation.types.stack_id_list.deserialize_query(
            child_stack_ids
        )
    child_stack_ids_url = el.find("StackIdsUrl")
    if child_stack_ids_url is not None:
        out["stack_ids_url"] = str(child_stack_ids_url.text or "")
    child_organizational_unit_ids = el.find("OrganizationalUnitIds")
    if child_organizational_unit_ids is not None:
        import capo_cloudformation.types.organizational_unit_id_list

        out["organizational_unit_ids"] = (
            capo_cloudformation.types.organizational_unit_id_list.deserialize_query(
                child_organizational_unit_ids
            )
        )
    child_operation_preferences = el.find("OperationPreferences")
    if child_operation_preferences is not None:
        import capo_cloudformation.types.stack_set_operation_preferences

        out["operation_preferences"] = (
            capo_cloudformation.types.stack_set_operation_preferences.deserialize_query(
                child_operation_preferences
            )
        )
    child_operation_id = el.find("OperationId")
    if child_operation_id is not None:
        out["operation_id"] = str(child_operation_id.text or "")
    child_call_as = el.find("CallAs")
    if child_call_as is not None:
        import capo_cloudformation.types.call_as

        out["call_as"] = capo_cloudformation.types.call_as.deserialize_query(
            child_call_as
        )
    return out
