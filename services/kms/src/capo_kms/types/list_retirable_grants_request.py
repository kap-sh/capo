"""Generated from Smithy shape ``com.amazonaws.kms#ListRetirableGrantsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.limit_type
    import capo_kms.types.marker_type
    import capo_kms.types.principal_id_type
    import capo_kms.types.service_principal_type


class ListRetirableGrantsRequest(TypedDict, closed=True):
    limit: NotRequired["capo_kms.types.limit_type.LimitType"]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, KMS does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.</p>"""
    marker: NotRequired["capo_kms.types.marker_type.MarkerType"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextMarker</code> from the truncated response you just received.</p>"""
    retiring_principal: NotRequired["capo_kms.types.principal_id_type.PrincipalIdType"]
    """<p>The retiring principal for which to list grants. Enter a principal in your Amazon Web Services account.</p> <p>To specify the retiring principal, use the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an Amazon Web Services principal. Valid principals include Amazon Web Services accounts, IAM users, IAM roles, federated users, and assumed role users. For help with the ARN syntax for a principal, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a> in the <i> <i>Identity and Access Management User Guide</i> </i>.</p> <p>You must specify either <code>RetiringPrincipal</code> or <code>RetiringServicePrincipal</code>, but not both.</p>"""
    retiring_service_principal: NotRequired[
        "capo_kms.types.service_principal_type.ServicePrincipalType"
    ]
    """<p>The retiring service principal for which to list grants. This filter is only usable by callers in a service principal.</p> <p>You must specify either <code>RetiringPrincipal</code> or <code>RetiringServicePrincipal</code>, but not both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRetirableGrantsRequest) -> dict:
    out: dict = {}
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "retiring_principal" in value:
        out["RetiringPrincipal"] = value["retiring_principal"]
    if "retiring_service_principal" in value:
        out["RetiringServicePrincipal"] = value["retiring_service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRetirableGrantsRequest:
    out: ListRetirableGrantsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("RetiringPrincipal") is not None:
        out["retiring_principal"] = data["RetiringPrincipal"]
    if data.get("RetiringServicePrincipal") is not None:
        out["retiring_service_principal"] = data["RetiringServicePrincipal"]
    return out
