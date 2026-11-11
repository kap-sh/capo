"""Generated from Smithy shape ``com.amazonaws.route53profiles#AssociateProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53profiles.types.profile_association


class AssociateProfileResponse(TypedDict, closed=True):
    profile_association: NotRequired[
        "capo_route53profiles.types.profile_association.ProfileAssociation"
    ]
    """<p> The association that you just created. The association has an ID that you can use to identify it in other requests, such as update and delete. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateProfileResponse) -> dict:
    out: dict = {}
    if "profile_association" in value:
        import capo_route53profiles.types.profile_association

        out["ProfileAssociation"] = (
            capo_route53profiles.types.profile_association.serialize_json(
                value["profile_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateProfileResponse:
    out: AssociateProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProfileAssociation") is not None:
        import capo_route53profiles.types.profile_association

        out["profile_association"] = (
            capo_route53profiles.types.profile_association.deserialize_json(
                data["ProfileAssociation"]
            )
        )
    return out
