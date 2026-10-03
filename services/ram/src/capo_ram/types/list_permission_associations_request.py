"""Generated from Smithy shape ``com.amazonaws.ram#ListPermissionAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.boolean
    import capo_ram.types.integer
    import capo_ram.types.max_results
    import capo_ram.types.permission_feature_set
    import capo_ram.types.resource_share_association_status
    import capo_ram.types.string


class ListPermissionAssociationsRequest(TypedDict, closed=True):
    permission_arn: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the managed permission.</p>"""
    permission_version: NotRequired["capo_ram.types.integer.Integer"]
    """<p>Specifies that you want to list only those associations with resource shares that use this version of the managed permission. If you don't provide a value for this parameter, then the operation returns information about associations with resource shares that use any version of the managed permission.</p>"""
    association_status: NotRequired[
        "capo_ram.types.resource_share_association_status.ResourceShareAssociationStatus"
    ]
    """<p>Specifies that you want to list only those associations with resource shares that match this status.</p>"""
    resource_type: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to list only those associations with resource shares that include at least one resource of this resource type.</p>"""
    feature_set: NotRequired[
        "capo_ram.types.permission_feature_set.PermissionFeatureSet"
    ]
    """<p>Specifies that you want to list only those associations with resource shares that have a <code>featureSet</code> with this value.</p>"""
    default_version: NotRequired["capo_ram.types.boolean.Boolean"]
    """<p>When <code>true</code>, specifies that you want to list only those associations with resource shares that use the default version of the specified managed permission.</p> <p>When <code>false</code> (the default value), lists associations with resource shares that use any version of the specified managed permission.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["capo_ram.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionAssociationsRequest) -> dict:
    out: dict = {}
    if "permission_arn" in value:
        out["permissionArn"] = value["permission_arn"]
    if "permission_version" in value:
        out["permissionVersion"] = value["permission_version"]
    if "association_status" in value:
        import capo_ram.types.resource_share_association_status

        out["associationStatus"] = (
            capo_ram.types.resource_share_association_status.serialize_json(
                value["association_status"]
            )
        )
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "feature_set" in value:
        import capo_ram.types.permission_feature_set

        out["featureSet"] = capo_ram.types.permission_feature_set.serialize_json(
            value["feature_set"]
        )
    if "default_version" in value:
        out["defaultVersion"] = value["default_version"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListPermissionAssociationsRequest:
    out: ListPermissionAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("permissionArn") is not None:
        out["permission_arn"] = data["permissionArn"]
    if data.get("permissionVersion") is not None:
        out["permission_version"] = data["permissionVersion"]
    if data.get("associationStatus") is not None:
        import capo_ram.types.resource_share_association_status

        out["association_status"] = (
            capo_ram.types.resource_share_association_status.deserialize_json(
                data["associationStatus"]
            )
        )
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("featureSet") is not None:
        import capo_ram.types.permission_feature_set

        out["feature_set"] = capo_ram.types.permission_feature_set.deserialize_json(
            data["featureSet"]
        )
    if data.get("defaultVersion") is not None:
        out["default_version"] = data["defaultVersion"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
