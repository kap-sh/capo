"""Generated from Smithy shape ``com.amazonaws.ram#ListPrincipalsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.max_results
    import capo_ram.types.principal_arn_or_id_list
    import capo_ram.types.resource_owner
    import capo_ram.types.resource_share_arn_list
    import capo_ram.types.string


class ListPrincipalsRequest(TypedDict, closed=True):
    resource_owner: "capo_ram.types.resource_owner.ResourceOwner"
    """<p>Specifies that you want to list information for only resource shares that match the following:</p> <ul> <li> <p> <b> <code>SELF</code> </b> – principals that your account is sharing resources with</p> </li> <li> <p> <b> <code>OTHER-ACCOUNTS</code> </b> – principals that are sharing resources with your account</p> </li> </ul>"""
    resource_arn: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to list principal information for the resource share with the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a>.</p>"""
    principals: NotRequired[
        "capo_ram.types.principal_arn_or_id_list.PrincipalArnOrIdList"
    ]
    """<p>Specifies that you want to list information for only the listed principals.</p> <p>You can include the following values:</p> <ul> <li> <p>An Amazon Web Services account ID, for example: <code>123456789012</code> </p> </li> <li> <p>An <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an organization in Organizations, for example: <code>organizations::123456789012:organization/o-exampleorgid</code> </p> </li> <li> <p>An ARN of an organizational unit (OU) in Organizations, for example: <code>organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123</code> </p> </li> <li> <p>An ARN of an IAM role, for example: <code>iam::123456789012:role/rolename</code> </p> </li> <li> <p>An ARN of an IAM user, for example: <code>iam::123456789012user/username</code> </p> </li> <li> <p>A service principal name, for example: <code>service-id.amazonaws.com</code> </p> </li> </ul> <note> <p>Not all resource types can be shared with IAM roles and users. For more information, see <a href="https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types">Sharing with IAM roles and users</a> in the <i>Resource Access Manager User Guide</i>.</p> </note>"""
    resource_type: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to list information for only principals associated with resource shares that include the specified resource type.</p> <p>For a list of valid values, query the <a>ListResourceTypes</a> operation.</p>"""
    resource_share_arns: NotRequired[
        "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
    ]
    """<p>Specifies that you want to list information for only principals associated with the resource shares specified by a list the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["capo_ram.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrincipalsRequest) -> dict:
    out: dict = {}
    import capo_ram.types.resource_owner

    out["resourceOwner"] = capo_ram.types.resource_owner.serialize_json(
        value["resource_owner"]
    )
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "principals" in value:
        import capo_ram.types.principal_arn_or_id_list

        out["principals"] = capo_ram.types.principal_arn_or_id_list.serialize_json(
            value["principals"]
        )
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "resource_share_arns" in value:
        import capo_ram.types.resource_share_arn_list

        out["resourceShareArns"] = (
            capo_ram.types.resource_share_arn_list.serialize_json(
                value["resource_share_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListPrincipalsRequest:
    out: ListPrincipalsRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceOwner") is not None:
        import capo_ram.types.resource_owner

        out["resource_owner"] = capo_ram.types.resource_owner.deserialize_json(
            data["resourceOwner"]
        )
    else:
        raise DeserializationError("ListPrincipalsRequest.resource_owner required")
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("principals") is not None:
        import capo_ram.types.principal_arn_or_id_list

        out["principals"] = capo_ram.types.principal_arn_or_id_list.deserialize_json(
            data["principals"]
        )
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("resourceShareArns") is not None:
        import capo_ram.types.resource_share_arn_list

        out["resource_share_arns"] = (
            capo_ram.types.resource_share_arn_list.deserialize_json(
                data["resourceShareArns"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
