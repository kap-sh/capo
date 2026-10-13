"""Generated from Smithy shape ``com.amazonaws.invoicing#BatchGetInvoiceProfileResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.profile_list


class BatchGetInvoiceProfileResponse(TypedDict, closed=True):
    profiles: NotRequired["capo_invoicing.types.profile_list.ProfileList"]
    """<p> A list of invoice profiles corresponding to the requested accounts. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetInvoiceProfileResponse) -> dict:
    out: dict = {}
    if "profiles" in value:
        import capo_invoicing.types.profile_list

        out["Profiles"] = capo_invoicing.types.profile_list.serialize_aws_json_1_0(
            value["profiles"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetInvoiceProfileResponse:
    out: BatchGetInvoiceProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("Profiles") is not None:
        import capo_invoicing.types.profile_list

        out["profiles"] = capo_invoicing.types.profile_list.deserialize_aws_json_1_0(
            data["Profiles"]
        )
    return out


def redact_sensitive(value: BatchGetInvoiceProfileResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "profiles" in value:
        import capo_invoicing.types.profile_list

        out["profiles"] = capo_invoicing.types.profile_list.redact_sensitive(
            value["profiles"]
        )
    return out
