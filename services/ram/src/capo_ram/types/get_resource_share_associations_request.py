"""Generated from Smithy shape ``com.amazonaws.ram#GetResourceShareAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.max_results
    import capo_ram.types.resource_share_arn_list
    import capo_ram.types.resource_share_association_status
    import capo_ram.types.resource_share_association_type
    import capo_ram.types.string


class GetResourceShareAssociationsRequest(TypedDict, closed=True):
    association_type: (
        "capo_ram.types.resource_share_association_type.ResourceShareAssociationType"
    )
    """<p>Specifies whether you want to retrieve the associations that involve a specified resource or principal.</p> <ul> <li> <p> <code>PRINCIPAL</code> – list the principals whose associations you want to see.</p> </li> <li> <p> <code>RESOURCE</code> – list the resources whose associations you want to see.</p> </li> </ul>"""
    resource_share_arns: NotRequired[
        "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
    ]
    """<p>Specifies a list of <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> of the resource share whose associations you want to retrieve.</p>"""
    resource_arn: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of a resource whose resource shares you want to retrieve.</p> <p>You cannot specify this parameter if the association type is <code>PRINCIPAL</code>.</p>"""
    principal: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies the ID of the principal whose resource shares you want to retrieve. This can be an Amazon Web Services account ID, an organization ID, an organizational unit ID, or the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an individual IAM role or user.</p> <p>You cannot specify this parameter if the association type is <code>RESOURCE</code>.</p>"""
    association_status: NotRequired[
        "capo_ram.types.resource_share_association_status.ResourceShareAssociationStatus"
    ]
    """<p>Specifies that you want to retrieve only associations that have this status.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["capo_ram.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceShareAssociationsRequest) -> dict:
    out: dict = {}
    import capo_ram.types.resource_share_association_type

    out["associationType"] = (
        capo_ram.types.resource_share_association_type.serialize_json(
            value["association_type"]
        )
    )
    if "resource_share_arns" in value:
        import capo_ram.types.resource_share_arn_list

        out["resourceShareArns"] = (
            capo_ram.types.resource_share_arn_list.serialize_json(
                value["resource_share_arns"]
            )
        )
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "principal" in value:
        out["principal"] = value["principal"]
    if "association_status" in value:
        import capo_ram.types.resource_share_association_status

        out["associationStatus"] = (
            capo_ram.types.resource_share_association_status.serialize_json(
                value["association_status"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetResourceShareAssociationsRequest:
    out: GetResourceShareAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("associationType") is not None:
        import capo_ram.types.resource_share_association_type

        out["association_type"] = (
            capo_ram.types.resource_share_association_type.deserialize_json(
                data["associationType"]
            )
        )
    else:
        raise DeserializationError(
            "GetResourceShareAssociationsRequest.association_type required"
        )
    if data.get("resourceShareArns") is not None:
        import capo_ram.types.resource_share_arn_list

        out["resource_share_arns"] = (
            capo_ram.types.resource_share_arn_list.deserialize_json(
                data["resourceShareArns"]
            )
        )
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("principal") is not None:
        out["principal"] = data["principal"]
    if data.get("associationStatus") is not None:
        import capo_ram.types.resource_share_association_status

        out["association_status"] = (
            capo_ram.types.resource_share_association_status.deserialize_json(
                data["associationStatus"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
