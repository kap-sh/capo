"""Generated from Smithy shape ``com.amazonaws.iam#CreateServiceSpecificCredentialResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.service_specific_credential


class CreateServiceSpecificCredentialResponse(TypedDict, closed=True):
    service_specific_credential: NotRequired[
        "capo_iam.types.service_specific_credential.ServiceSpecificCredential"
    ]
    """<p>A structure that contains information about the newly created service-specific credential.</p> <important> <p>This is the only time that the password for this credential set is available. It cannot be recovered later. Instead, you must reset the password with <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_ResetServiceSpecificCredential.html">ResetServiceSpecificCredential</a>.</p> </important>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateServiceSpecificCredentialResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "service_specific_credential" in value:
        import capo_iam.types.service_specific_credential

        capo_iam.types.service_specific_credential.serialize_query(
            value["service_specific_credential"],
            pairs,
            f"{key_prefix}ServiceSpecificCredential",
        )


def deserialize_query(el: Element) -> CreateServiceSpecificCredentialResponse:
    out: CreateServiceSpecificCredentialResponse = {}  # type: ignore[typeddict-item]
    child_service_specific_credential = el.find("ServiceSpecificCredential")
    if child_service_specific_credential is not None:
        import capo_iam.types.service_specific_credential

        out["service_specific_credential"] = (
            capo_iam.types.service_specific_credential.deserialize_query(
                child_service_specific_credential
            )
        )
    return out
