"""Generated from Smithy shape ``com.amazonaws.workspaces#CertificateBasedAuthProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.certificate_authority_arn
    import capo_workspaces.types.certificate_based_auth_status_enum


class CertificateBasedAuthProperties(TypedDict, closed=True):
    status: NotRequired[
        "capo_workspaces.types.certificate_based_auth_status_enum.CertificateBasedAuthStatusEnum"
    ]
    """<p>The status of the certificate-based authentication properties.</p>"""
    certificate_authority_arn: NotRequired[
        "capo_workspaces.types.certificate_authority_arn.CertificateAuthorityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Certificate Manager Private CA resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateBasedAuthProperties) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_workspaces.types.certificate_based_auth_status_enum

        out["Status"] = (
            capo_workspaces.types.certificate_based_auth_status_enum.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateBasedAuthProperties:
    out: CertificateBasedAuthProperties = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_workspaces.types.certificate_based_auth_status_enum

        out["status"] = (
            capo_workspaces.types.certificate_based_auth_status_enum.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificateBasedAuthProperties) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_workspaces.types.certificate_based_auth_status_enum

        out["Status"] = (
            capo_workspaces.types.certificate_based_auth_status_enum.serialize_cbor(
                value["status"]
            )
        )
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    return out


def deserialize_cbor(data: dict) -> CertificateBasedAuthProperties:
    out: CertificateBasedAuthProperties = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_workspaces.types.certificate_based_auth_status_enum

        out["status"] = (
            capo_workspaces.types.certificate_based_auth_status_enum.deserialize_cbor(
                data["Status"]
            )
        )
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    return out
