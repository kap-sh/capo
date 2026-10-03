"""Generated from Smithy shape ``com.amazonaws.iam#UpdateOpenIDConnectProviderThumbprintRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.thumbprint_list_type


class UpdateOpenIDConnectProviderThumbprintRequest(TypedDict, closed=True):
    open_id_connect_provider_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the IAM OIDC provider resource object for which you want to update the thumbprint. You can get a list of OIDC provider ARNs by using the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOpenIDConnectProviders.html">ListOpenIDConnectProviders</a> operation.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    thumbprint_list: "capo_iam.types.thumbprint_list_type.thumbprintListType"
    """<p>A list of certificate thumbprints that are associated with the specified IAM OpenID Connect provider. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html">CreateOpenIDConnectProvider</a>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateOpenIDConnectProviderThumbprintRequest,
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
    import capo_iam.types.thumbprint_list_type

    capo_iam.types.thumbprint_list_type.serialize_query(
        value["thumbprint_list"], pairs, f"{key_prefix}ThumbprintList"
    )


def deserialize_query(el: Element) -> UpdateOpenIDConnectProviderThumbprintRequest:
    out: UpdateOpenIDConnectProviderThumbprintRequest = {}  # type: ignore[typeddict-item]
    child_open_id_connect_provider_arn = el.find("OpenIDConnectProviderArn")
    if child_open_id_connect_provider_arn is not None:
        out["open_id_connect_provider_arn"] = str(
            child_open_id_connect_provider_arn.text or ""
        )
    else:
        raise DeserializationError(
            "UpdateOpenIDConnectProviderThumbprintRequest.open_id_connect_provider_arn required"
        )
    child_thumbprint_list = el.find("ThumbprintList")
    if child_thumbprint_list is not None:
        import capo_iam.types.thumbprint_list_type

        out["thumbprint_list"] = capo_iam.types.thumbprint_list_type.deserialize_query(
            child_thumbprint_list
        )
    else:
        raise DeserializationError(
            "UpdateOpenIDConnectProviderThumbprintRequest.thumbprint_list required"
        )
    return out
