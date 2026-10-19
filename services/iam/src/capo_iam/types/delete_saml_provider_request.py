"""Generated from Smithy shape ``com.amazonaws.iam#DeleteSAMLProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type


class DeleteSAMLProviderRequest(TypedDict, closed=True):
    saml_provider_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the SAML provider to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSAMLProviderRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}SAMLProviderArn", str(value["saml_provider_arn"])))


def deserialize_query(el: Element) -> DeleteSAMLProviderRequest:
    out: DeleteSAMLProviderRequest = {}  # type: ignore[typeddict-item]
    child_saml_provider_arn = el.find("SAMLProviderArn")
    if child_saml_provider_arn is not None:
        out["saml_provider_arn"] = str(child_saml_provider_arn.text or "")
    else:
        out["saml_provider_arn"] = ""
    return out
