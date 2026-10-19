"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetTrustStoreCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.certificate


class GetTrustStoreCertificateResponse(TypedDict, closed=True):
    trust_store_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store certificate.</p>"""
    certificate: NotRequired["capo_workspaces_web.types.certificate.Certificate"]
    """<p>The certificate of the trust store certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrustStoreCertificateResponse) -> dict:
    out: dict = {}
    out["trustStoreArn"] = value["trust_store_arn"]
    if "certificate" in value:
        import capo_workspaces_web.types.certificate

        out["certificate"] = capo_workspaces_web.types.certificate.serialize_json(
            value["certificate"]
        )
    return out


def deserialize_json(data: dict) -> GetTrustStoreCertificateResponse:
    out: GetTrustStoreCertificateResponse = {}  # type: ignore[typeddict-item]
    if data.get("trustStoreArn") is not None:
        out["trust_store_arn"] = data["trustStoreArn"]
    else:
        out["trust_store_arn"] = ""
    if data.get("certificate") is not None:
        import capo_workspaces_web.types.certificate

        out["certificate"] = capo_workspaces_web.types.certificate.deserialize_json(
            data["certificate"]
        )
    return out
