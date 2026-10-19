"""Generated from Smithy shape ``com.amazonaws.appmesh#TlsValidationContextAcmTrust``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.certificate_authority_arns


class TlsValidationContextAcmTrust(TypedDict, closed=True):
    certificate_authority_arns: (
        "capo_app_mesh.types.certificate_authority_arns.CertificateAuthorityArns"
    )
    """<p>One or more ACM Amazon Resource Name (ARN)s.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TlsValidationContextAcmTrust) -> dict:
    out: dict = {}
    import capo_app_mesh.types.certificate_authority_arns

    out["certificateAuthorityArns"] = (
        capo_app_mesh.types.certificate_authority_arns.serialize_json(
            value["certificate_authority_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> TlsValidationContextAcmTrust:
    out: TlsValidationContextAcmTrust = {}  # type: ignore[typeddict-item]
    if data.get("certificateAuthorityArns") is not None:
        import capo_app_mesh.types.certificate_authority_arns

        out["certificate_authority_arns"] = (
            capo_app_mesh.types.certificate_authority_arns.deserialize_json(
                data["certificateAuthorityArns"]
            )
        )
    else:
        out["certificate_authority_arns"] = []
    return out
