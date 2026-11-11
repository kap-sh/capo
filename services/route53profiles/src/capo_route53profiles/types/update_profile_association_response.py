"""Generated from Smithy shape ``com.amazonaws.route53profiles#UpdateProfileAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53profiles.types.profile_association


class UpdateProfileAssociationResponse(TypedDict, closed=True):
    profile_association: (
        "capo_route53profiles.types.profile_association.ProfileAssociation"
    )
    """<p> Information about the <code>UpdateProfileAssociation</code> request, including a status message. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfileAssociationResponse) -> dict:
    out: dict = {}
    import capo_route53profiles.types.profile_association

    out["ProfileAssociation"] = (
        capo_route53profiles.types.profile_association.serialize_json(
            value["profile_association"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateProfileAssociationResponse:
    out: UpdateProfileAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProfileAssociation") is not None:
        import capo_route53profiles.types.profile_association

        out["profile_association"] = (
            capo_route53profiles.types.profile_association.deserialize_json(
                data["ProfileAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProfileAssociationResponse.profile_association required"
        )
    return out
