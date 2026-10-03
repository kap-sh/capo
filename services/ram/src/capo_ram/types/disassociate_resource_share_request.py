"""Generated from Smithy shape ``com.amazonaws.ram#DisassociateResourceShareRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.principal_arn_or_id_list
    import capo_ram.types.resource_arn_list
    import capo_ram.types.source_arn_or_account_list
    import capo_ram.types.string


class DisassociateResourceShareRequest(TypedDict, closed=True):
    resource_share_arn: "capo_ram.types.string.String"
    """<p>Specifies <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share that you want to remove resources or principals from.</p>"""
    resource_arns: NotRequired["capo_ram.types.resource_arn_list.ResourceArnList"]
    """<p>Specifies a list of <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> for one or more resources that you want to remove from the resource share. After the operation runs, these resources are no longer shared with principals associated with the resource share.</p>"""
    principals: NotRequired[
        "capo_ram.types.principal_arn_or_id_list.PrincipalArnOrIdList"
    ]
    """<p>Specifies a list of one or more principals that no longer are to have access to the resources in this resource share.</p> <p>You can include the following values:</p> <ul> <li> <p>An Amazon Web Services account ID, for example: <code>123456789012</code> </p> </li> <li> <p>An <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an organization in Organizations, for example: <code>organizations::123456789012:organization/o-exampleorgid</code> </p> </li> <li> <p>An ARN of an organizational unit (OU) in Organizations, for example: <code>organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123</code> </p> </li> <li> <p>An ARN of an IAM role, for example: <code>iam::123456789012:role/rolename</code> </p> </li> <li> <p>An ARN of an IAM user, for example: <code>iam::123456789012user/username</code> </p> </li> <li> <p>A service principal name, for example: <code>service-id.amazonaws.com</code> </p> </li> </ul> <note> <p>Not all resource types can be shared with IAM roles and users. For more information, see <a href="https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types">Sharing with IAM roles and users</a> in the <i>Resource Access Manager User Guide</i>.</p> </note>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    sources: NotRequired[
        "capo_ram.types.source_arn_or_account_list.SourceArnOrAccountList"
    ]
    """<p>Specifies source constraints (accounts, ARNs, organization IDs, or organization paths) to remove from the resource share. This enables granular management of source constraints while maintaining service principal associations. At least one source must remain when service principals are present.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourceShareRequest) -> dict:
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


def deserialize_json(data: dict) -> DisassociateResourceShareRequest:
    out: DisassociateResourceShareRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceShareArn") is not None:
        out["resource_share_arn"] = data["resourceShareArn"]
    else:
        raise DeserializationError(
            "DisassociateResourceShareRequest.resource_share_arn required"
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
