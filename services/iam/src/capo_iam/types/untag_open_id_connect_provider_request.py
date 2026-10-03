"""Generated from Smithy shape ``com.amazonaws.iam#UntagOpenIDConnectProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.tag_key_list_type


class UntagOpenIDConnectProviderRequest(TypedDict, closed=True):
    open_id_connect_provider_arn: "capo_iam.types.arn_type.arnType"
    """<p>The ARN of the OIDC provider in IAM from which you want to remove tags.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tag_keys: "capo_iam.types.tag_key_list_type.tagKeyListType"
    """<p>A list of key names as a simple array of strings. The tags with matching keys are removed from the specified OIDC provider.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagOpenIDConnectProviderRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (
            f"{key_prefix}OpenIDConnectProviderArn",
            str(value["open_id_connect_provider_arn"]),
        )
    )
    import capo_iam.types.tag_key_list_type

    capo_iam.types.tag_key_list_type.serialize_query(
        value["tag_keys"], pairs, f"{key_prefix}TagKeys"
    )


def deserialize_query(el: Element) -> UntagOpenIDConnectProviderRequest:
    out: UntagOpenIDConnectProviderRequest = {}  # type: ignore[typeddict-item]
    child_open_id_connect_provider_arn = el.find("OpenIDConnectProviderArn")
    if child_open_id_connect_provider_arn is not None:
        out["open_id_connect_provider_arn"] = str(
            child_open_id_connect_provider_arn.text or ""
        )
    else:
        raise DeserializationError(
            "UntagOpenIDConnectProviderRequest.open_id_connect_provider_arn required"
        )
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import capo_iam.types.tag_key_list_type

        out["tag_keys"] = capo_iam.types.tag_key_list_type.deserialize_query(
            child_tag_keys
        )
    else:
        raise DeserializationError(
            "UntagOpenIDConnectProviderRequest.tag_keys required"
        )
    return out
