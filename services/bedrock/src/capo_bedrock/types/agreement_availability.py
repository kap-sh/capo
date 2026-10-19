"""Generated from Smithy shape ``com.amazonaws.bedrock#AgreementAvailability``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.agreement_status


class AgreementAvailability(TypedDict, closed=True):
    status: "capo_bedrock.types.agreement_status.AgreementStatus"
    """<p>Status of the agreement.</p>"""
    error_message: NotRequired["str"]
    """<p>Error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgreementAvailability) -> dict:
    out: dict = {}
    import capo_bedrock.types.agreement_status

    out["status"] = capo_bedrock.types.agreement_status.serialize_json(value["status"])
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> AgreementAvailability:
    out: AgreementAvailability = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_bedrock.types.agreement_status

        out["status"] = capo_bedrock.types.agreement_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock.types.agreement_status.AgreementStatus", ""
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
