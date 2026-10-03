"""Generated from Smithy shape ``com.amazonaws.iam#ListOpenIDConnectProviderTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.marker_type
    import capo_iam.types.max_items_type


class ListOpenIDConnectProviderTagsRequest(TypedDict, closed=True):
    open_id_connect_provider_arn: "capo_iam.types.arn_type.arnType"
    """<p>The ARN of the OpenID Connect (OIDC) identity provider whose tags you want to see.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    marker: NotRequired["capo_iam.types.marker_type.markerType"]
    """<p>Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the <code>Marker</code> element in the response that you received to indicate where the next call should start.</p>"""
    max_items: NotRequired["capo_iam.types.max_items_type.maxItemsType"]
    """<p>Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the <code>IsTruncated</code> response element is <code>true</code>.</p> <p>If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the <code>IsTruncated</code> response element returns <code>true</code>, and <code>Marker</code> contains a value to include in the subsequent call that tells the service where to continue from.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListOpenIDConnectProviderTagsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (
            f"{key_prefix}OpenIDConnectProviderArn",
            str(value["open_id_connect_provider_arn"]),
        )
    )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "max_items" in value:
        pairs.append((f"{key_prefix}MaxItems", str(value["max_items"])))


def deserialize_query(el: Element) -> ListOpenIDConnectProviderTagsRequest:
    out: ListOpenIDConnectProviderTagsRequest = {}  # type: ignore[typeddict-item]
    child_open_id_connect_provider_arn = el.find("OpenIDConnectProviderArn")
    if child_open_id_connect_provider_arn is not None:
        out["open_id_connect_provider_arn"] = str(
            child_open_id_connect_provider_arn.text or ""
        )
    else:
        raise DeserializationError(
            "ListOpenIDConnectProviderTagsRequest.open_id_connect_provider_arn required"
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
