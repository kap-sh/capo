"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.certificate_ids
    import capo_transfer.types.profile_id


class UpdateProfileRequest(TypedDict, closed=True):
    profile_id: "capo_transfer.types.profile_id.ProfileId"
    """<p>The identifier of the profile object that you are updating.</p>"""
    certificate_ids: NotRequired["capo_transfer.types.certificate_ids.CertificateIds"]
    """<p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProfileRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    if "certificate_ids" in value:
        import capo_transfer.types.certificate_ids

        out["CertificateIds"] = (
            capo_transfer.types.certificate_ids.serialize_aws_json_1_1(
                value["certificate_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProfileRequest:
    out: UpdateProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("CertificateIds") is not None:
        import capo_transfer.types.certificate_ids

        out["certificate_ids"] = (
            capo_transfer.types.certificate_ids.deserialize_aws_json_1_1(
                data["CertificateIds"]
            )
        )
    return out
