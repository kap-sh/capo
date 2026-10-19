"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CertificateAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rtbfabric.types.acm_certificate_arn
    import capo_rtbfabric.types.certificate_association_status


class CertificateAssociationSummary(TypedDict, closed=True):
    acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn"
    """<p>The Amazon Resource Name (ARN) of the ACM certificate.</p>"""
    status: "capo_rtbfabric.types.certificate_association_status.CertificateAssociationStatus"
    """<p>The status of the certificate association.</p>"""
    associated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the certificate was associated.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the certificate association was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAssociationSummary) -> dict:
    out: dict = {}
    out["acmCertificateArn"] = value["acm_certificate_arn"]
    import capo_rtbfabric.types.certificate_association_status

    out["status"] = capo_rtbfabric.types.certificate_association_status.serialize_json(
        value["status"]
    )
    if "associated_at" in value:
        import capo_rtbfabric.types._prelude.timestamp

        out["associatedAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
            value["associated_at"]
        )
    if "updated_at" in value:
        import capo_rtbfabric.types._prelude.timestamp

        out["updatedAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> CertificateAssociationSummary:
    out: CertificateAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("acmCertificateArn") is not None:
        out["acm_certificate_arn"] = data["acmCertificateArn"]
    else:
        out["acm_certificate_arn"] = ""
    if data.get("status") is not None:
        import capo_rtbfabric.types.certificate_association_status

        out["status"] = (
            capo_rtbfabric.types.certificate_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_rtbfabric.types.certificate_association_status.CertificateAssociationStatus",
            "",
        )
    if data.get("associatedAt") is not None:
        import capo_rtbfabric.types._prelude.timestamp

        out["associated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["associatedAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_rtbfabric.types._prelude.timestamp

        out["updated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
