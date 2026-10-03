"""Generated from Smithy shape ``com.amazonaws.iam#RemoveClientIDFromOpenIDConnectProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.client_id_type


class RemoveClientIDFromOpenIDConnectProviderRequest(TypedDict, closed=True):
    open_id_connect_provider_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the IAM OIDC provider resource to remove the client ID from. You can get a list of OIDC provider ARNs by using the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOpenIDConnectProviders.html">ListOpenIDConnectProviders</a> operation.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    client_id: "capo_iam.types.client_id_type.clientIDType"
    """<p>The client ID (also known as audience) to remove from the IAM OIDC provider resource. For more information about client IDs, see <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html">CreateOpenIDConnectProvider</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveClientIDFromOpenIDConnectProviderRequest,
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
    pairs.append((f"{key_prefix}ClientID", str(value["client_id"])))


def deserialize_query(el: Element) -> RemoveClientIDFromOpenIDConnectProviderRequest:
    out: RemoveClientIDFromOpenIDConnectProviderRequest = {}  # type: ignore[typeddict-item]
    child_open_id_connect_provider_arn = el.find("OpenIDConnectProviderArn")
    if child_open_id_connect_provider_arn is not None:
        out["open_id_connect_provider_arn"] = str(
            child_open_id_connect_provider_arn.text or ""
        )
    else:
        raise DeserializationError(
            "RemoveClientIDFromOpenIDConnectProviderRequest.open_id_connect_provider_arn required"
        )
    child_client_id = el.find("ClientID")
    if child_client_id is not None:
        out["client_id"] = str(child_client_id.text or "")
    else:
        raise DeserializationError(
            "RemoveClientIDFromOpenIDConnectProviderRequest.client_id required"
        )
    return out
