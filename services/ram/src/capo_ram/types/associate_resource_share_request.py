"""Generated from Smithy shape ``com.amazonaws.ram#AssociateResourceShareRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.principal_arn_or_id_list
    import capo_ram.types.resource_arn_list
    import capo_ram.types.source_arn_or_account_list
    import capo_ram.types.string


class AssociateResourceShareRequest(TypedDict, closed=True):
    resource_share_arn: "capo_ram.types.string.String"
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share that you want to add principals or resources to.</p>"""
    resource_arns: NotRequired["capo_ram.types.resource_arn_list.ResourceArnList"]
    """<p>Specifies a list of <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> of the resources that you want to share. This can be <code>null</code> if you want to add only principals.</p>"""
    principals: NotRequired[
        "capo_ram.types.principal_arn_or_id_list.PrincipalArnOrIdList"
    ]
    """<p>Specifies a list of principals to whom you want to the resource share. This can be <code>null</code> if you want to add only resources.</p> <p>What the principals can do with the resources in the share is determined by the RAM permissions that you associate with the resource share. See <a>AssociateResourceSharePermission</a>.</p> <p>You can include the following values:</p> <ul> <li> <p>An Amazon Web Services account ID, for example: <code>123456789012</code> </p> </li> <li> <p>An <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an organization in Organizations, for example: <code>organizations::123456789012:organization/o-exampleorgid</code> </p> </li> <li> <p>An ARN of an organizational unit (OU) in Organizations, for example: <code>organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123</code> </p> </li> <li> <p>An ARN of an IAM role, for example: <code>iam::123456789012:role/rolename</code> </p> </li> <li> <p>An ARN of an IAM user, for example: <code>iam::123456789012user/username</code> </p> </li> <li> <p>A service principal name, for example: <code>service-id.amazonaws.com</code> </p> </li> </ul> <note> <p>Not all resource types can be shared with IAM roles and users. For more information, see <a href="https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types">Sharing with IAM roles and users</a> in the <i>Resource Access Manager User Guide</i>.</p> </note>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    sources: NotRequired[
        "capo_ram.types.source_arn_or_account_list.SourceArnOrAccountList"
    ]
    """<p>Specifies source constraints (accounts, ARNs, organization IDs, or organization paths) that limit when service principals can access resources in this resource share. When a service principal attempts to access a shared resource, validation is performed to ensure the request originates from one of the specified sources. This helps prevent confused deputy attacks by applying constraints on where service principals can access resources from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateResourceShareRequest) -> dict:
    out: dict = {}
    out["resourceShareArn"] = value["resource_share_arn"]
    if "resource_arns" in value:
        import capo_ram.types.resource_arn_list

        out["resourceArns"] = capo_ram.types.resource_arn_list.serialize_json(
            value["resource_arns"]
        )
    if "principals" in value:
        import capo_ram.types.principal_arn_or_id_list

        out["principals"] = capo_ram.types.principal_arn_or_id_list.serialize_json(
            value["principals"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "sources" in value:
        import capo_ram.types.source_arn_or_account_list

        out["sources"] = capo_ram.types.source_arn_or_account_list.serialize_json(
            value["sources"]
        )
    return out


def deserialize_json(data: dict) -> AssociateResourceShareRequest:
    out: AssociateResourceShareRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceShareArn") is not None:
        out["resource_share_arn"] = data["resourceShareArn"]
    else:
        raise DeserializationError(
            "AssociateResourceShareRequest.resource_share_arn required"
        )
    if data.get("resourceArns") is not None:
        import capo_ram.types.resource_arn_list

        out["resource_arns"] = capo_ram.types.resource_arn_list.deserialize_json(
            data["resourceArns"]
        )
    if data.get("principals") is not None:
        import capo_ram.types.principal_arn_or_id_list

        out["principals"] = capo_ram.types.principal_arn_or_id_list.deserialize_json(
            data["principals"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("sources") is not None:
        import capo_ram.types.source_arn_or_account_list

        out["sources"] = capo_ram.types.source_arn_or_account_list.deserialize_json(
            data["sources"]
        )
    return out
