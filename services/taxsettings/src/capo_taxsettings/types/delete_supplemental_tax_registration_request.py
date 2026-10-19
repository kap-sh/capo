"""Generated from Smithy shape ``com.amazonaws.taxsettings#DeleteSupplementalTaxRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.generic_string


class DeleteSupplementalTaxRegistrationRequest(TypedDict, closed=True):
    authority_id: "capo_taxsettings.types.generic_string.GenericString"
    """<p> The unique authority Id for the supplemental TRN information that needs to be deleted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSupplementalTaxRegistrationRequest) -> dict:
    out: dict = {}
    out["authorityId"] = value["authority_id"]
    return out


def deserialize_json(data: dict) -> DeleteSupplementalTaxRegistrationRequest:
    out: DeleteSupplementalTaxRegistrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("authorityId") is not None:
        out["authority_id"] = data["authorityId"]
    else:
        out["authority_id"] = ""
    return out
