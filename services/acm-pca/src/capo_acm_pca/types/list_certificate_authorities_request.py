"""Generated from Smithy shape ``com.amazonaws.acmpca#ListCertificateAuthoritiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.max_results
    import capo_acm_pca.types.next_token
    import capo_acm_pca.types.resource_owner


class ListCertificateAuthoritiesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_acm_pca.types.max_results.MaxResults"]
    """<p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p> <p>Although the maximum value is 1000, the action only returns a maximum of 100 items.</p>"""
    next_token: NotRequired["capo_acm_pca.types.next_token.NextToken"]
    """<p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>"""
    resource_owner: NotRequired["capo_acm_pca.types.resource_owner.ResourceOwner"]
    """<p>Use this parameter to filter the returned set of certificate authorities based on their owner. The default is SELF.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificateAuthoritiesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resource_owner" in value:
        import capo_acm_pca.types.resource_owner

        out["ResourceOwner"] = capo_acm_pca.types.resource_owner.serialize_aws_json_1_1(
            value["resource_owner"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificateAuthoritiesRequest:
    out: ListCertificateAuthoritiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ResourceOwner") is not None:
        import capo_acm_pca.types.resource_owner

        out["resource_owner"] = (
            capo_acm_pca.types.resource_owner.deserialize_aws_json_1_1(
                data["ResourceOwner"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListCertificateAuthoritiesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resource_owner" in value:
        import capo_acm_pca.types.resource_owner

        out["ResourceOwner"] = capo_acm_pca.types.resource_owner.serialize_cbor(
            value["resource_owner"]
        )
    return out


def deserialize_cbor(data: dict) -> ListCertificateAuthoritiesRequest:
    out: ListCertificateAuthoritiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ResourceOwner") is not None:
        import capo_acm_pca.types.resource_owner

        out["resource_owner"] = capo_acm_pca.types.resource_owner.deserialize_cbor(
            data["ResourceOwner"]
        )
    return out
