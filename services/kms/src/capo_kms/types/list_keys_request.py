"""Generated from Smithy shape ``com.amazonaws.kms#ListKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.limit_type
    import capo_kms.types.marker_type
    import capo_kms.types.resource_owners_list


class ListKeysRequest(TypedDict, closed=True):
    limit: NotRequired["capo_kms.types.limit_type.LimitType"]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, KMS does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.</p>"""
    marker: NotRequired["capo_kms.types.marker_type.MarkerType"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextMarker</code> from the truncated response you just received.</p>"""
    resource_owners: NotRequired[
        "capo_kms.types.resource_owners_list.ResourceOwnersList"
    ]
    """<p>Specifies whose KMS keys to list. Use this parameter to list KMS keys that other Amazon Web Services accounts shared with your Amazon Web Services account through Resource Access Manager (RAM).</p> <p>Specify one or two values. Valid values are:</p> <dl> <dt>SELF</dt> <dd> <p>Lists the KMS keys in your Amazon Web Services account and Region.</p> </dd> <dt>OTHER_ACCOUNTS_VIA_RAM</dt> <dd> <p>Lists the KMS keys in the Region that other Amazon Web Services accounts currently share with your Amazon Web Services account through RAM. This list doesn't include KMS keys that your Amazon Web Services account owns. For each of these KMS keys, the key ARN in the response contains the account ID of the Amazon Web Services account that owns the KMS key.</p> </dd> </dl> <p>If you omit this parameter, <code>ListKeys</code> lists only the KMS keys in your Amazon Web Services account. If you specify both values, in either order, <code>ListKeys</code> returns the KMS keys in your Amazon Web Services account first, and then the KMS keys that other Amazon Web Services accounts shared with you. A single response doesn't contain both kinds of KMS keys.</p> <p>When <code>ResourceOwners</code> includes <code>OTHER_ACCOUNTS_VIA_RAM</code>, a response can contain fewer KMS keys than the <code>Limit</code> value, or none, even when <code>Truncated</code> is true. To get all of the KMS keys, continue calling <code>ListKeys</code> with the <code>NextMarker</code> value from each response until <code>Truncated</code> is false. Use a <code>NextMarker</code> value only in a request that has the same <code>ResourceOwners</code> value as the request that returned it. Otherwise, the request can fail with an <code>InvalidMarkerException</code>.</p> <p>KMS keys that other Amazon Web Services accounts share with you can take some time to appear in or disappear from the results after changes to resource shares.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListKeysRequest) -> dict:
    out: dict = {}
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "resource_owners" in value:
        import capo_kms.types.resource_owners_list

        out["ResourceOwners"] = (
            capo_kms.types.resource_owners_list.serialize_aws_json_1_1(
                value["resource_owners"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListKeysRequest:
    out: ListKeysRequest = {}  # type: ignore[typeddict-item]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("ResourceOwners") is not None:
        import capo_kms.types.resource_owners_list

        out["resource_owners"] = (
            capo_kms.types.resource_owners_list.deserialize_aws_json_1_1(
                data["ResourceOwners"]
            )
        )
    return out
