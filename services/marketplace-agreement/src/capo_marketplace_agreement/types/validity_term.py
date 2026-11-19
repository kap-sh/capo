"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ValidityTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.timestamp
    import capo_marketplace_agreement.types.unversioned_term_type


class ValidityTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Category of the term being updated. </p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    agreement_duration: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Defines the duration that the agreement remains active. If <code>AgreementStartDate</code> isn't provided, the agreement duration is relative to the agreement signature time. The duration is represented in the ISO_8601 format.</p>"""
    agreement_start_date: NotRequired[
        "capo_marketplace_agreement.types.timestamp.Timestamp"
    ]
    """<p>Defines the date when agreement starts. The agreement starts at 00:00:00.000 UTC on the date provided. If <code>AgreementStartDate</code> isn't provided, the agreement start date is determined based on agreement signature time.</p>"""
    agreement_end_date: NotRequired[
        "capo_marketplace_agreement.types.timestamp.Timestamp"
    ]
    """<p>Defines the date when the agreement ends. The agreement ends at 23:59:59.999 UTC on the date provided. If <code>AgreementEndDate</code> isn't provided, the agreement end date is determined by the validity of individual terms.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidityTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "agreement_duration" in value:
        out["agreementDuration"] = value["agreement_duration"]
    if "agreement_start_date" in value:
        import capo_marketplace_agreement.types.timestamp

        out["agreementStartDate"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["agreement_start_date"]
            )
        )
    if "agreement_end_date" in value:
        import capo_marketplace_agreement.types.timestamp

        out["agreementEndDate"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["agreement_end_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidityTerm:
    out: ValidityTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("agreementDuration") is not None:
        out["agreement_duration"] = data["agreementDuration"]
    if data.get("agreementStartDate") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["agreement_start_date"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["agreementStartDate"]
            )
        )
    if data.get("agreementEndDate") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["agreement_end_date"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["agreementEndDate"]
            )
        )
    return out
