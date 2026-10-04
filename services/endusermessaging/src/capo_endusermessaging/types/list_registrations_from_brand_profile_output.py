"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ListRegistrationsFromBrandProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.next_token
    import capo_endusermessaging.types.registration_association_summary_list


class ListRegistrationsFromBrandProfileOutput(TypedDict, closed=True):
    registration_associations: "capo_endusermessaging.types.registration_association_summary_list.RegistrationAssociationSummaryList"
    """<p>The list of registrations that are associated with the brand profile.</p>"""
    next_token: NotRequired["capo_endusermessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistrationsFromBrandProfileOutput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.registration_association_summary_list

    out["registrationAssociations"] = (
        capo_endusermessaging.types.registration_association_summary_list.serialize_json(
            value["registration_associations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRegistrationsFromBrandProfileOutput:
    out: ListRegistrationsFromBrandProfileOutput = {}  # type: ignore[typeddict-item]
    if data.get("registrationAssociations") is not None:
        import capo_endusermessaging.types.registration_association_summary_list

        out["registration_associations"] = (
            capo_endusermessaging.types.registration_association_summary_list.deserialize_json(
                data["registrationAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "ListRegistrationsFromBrandProfileOutput.registration_associations required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
