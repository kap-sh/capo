"""Generated from Smithy shape ``com.amazonaws.ram#CreatePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.permission_name
    import capo_ram.types.policy
    import capo_ram.types.string
    import capo_ram.types.tag_list


class CreatePermissionRequest(TypedDict, closed=True):
    name: "capo_ram.types.permission_name.PermissionName"
    """<p>Specifies the name of the customer managed permission. The name must be unique within the Amazon Web Services Region.</p>"""
    resource_type: "capo_ram.types.string.String"
    """<p>Specifies the name of the resource type that this customer managed permission applies to.</p> <p>The format is <code> <i><service-code></i>:<i><resource-type></i> </code> and is case sensitive. For example, to specify an Amazon EC2 Subnet, you can use the string <code>ec2:Subnet</code>. To see the list of valid values for this parameter, query the <a>ListResourceTypes</a> operation. This value must match the display name of the resource (available in <code>ListResourceTypes</code>).</p>"""
    policy_template: "capo_ram.types.policy.Policy"
    """<p>A string in JSON format string that contains the following elements of a resource-based policy:</p> <ul> <li> <p> <b>Effect</b>: must be set to <code>ALLOW</code>.</p> </li> <li> <p> <b>Action</b>: specifies the actions that are allowed by this customer managed permission. The list must contain only actions that are supported by the specified resource type. For a list of all actions supported by each resource type, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html">Actions, resources, and condition keys for Amazon Web Services services</a> in the <i>Identity and Access Management User Guide</i>.</p> </li> <li> <p> <b>Condition</b>: (optional) specifies conditional parameters that must evaluate to true when a user attempts an action for that action to be allowed. For more information about the Condition element, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html">IAM policies: Condition element</a> in the <i>Identity and Access Management User Guide</i>.</p> </li> </ul> <p>This template can't include either the <code>Resource</code> or <code>Principal</code> elements. Those are both filled in by RAM when it instantiates the resource-based policy on each resource shared using this managed permission. The <code>Resource</code> comes from the ARN of the specific resource that you are sharing. The <code>Principal</code> comes from the list of identities added to the resource share.</p>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    tags: NotRequired["capo_ram.types.tag_list.TagList"]
    """<p>Specifies a list of one or more tag key and value pairs to attach to the permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePermissionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["resourceType"] = value["resource_type"]
    out["policyTemplate"] = value["policy_template"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_ram.types.tag_list

        out["tags"] = capo_ram.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePermissionRequest:
    out: CreatePermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePermissionRequest.name required")
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("CreatePermissionRequest.resource_type required")
    if data.get("policyTemplate") is not None:
        out["policy_template"] = data["policyTemplate"]
    else:
        raise DeserializationError("CreatePermissionRequest.policy_template required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_ram.types.tag_list

        out["tags"] = capo_ram.types.tag_list.deserialize_json(data["tags"])
    return out
