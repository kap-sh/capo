"""Generated from Smithy shape ``com.amazonaws.repostspace#ListSpacesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_repostspace.types.spaces_list


class ListSpacesOutput(TypedDict, closed=True):
    spaces: "capo_repostspace.types.spaces_list.SpacesList"
    """<p>An array of structures that contain some information about the private re:Posts in the account.</p>"""
    next_token: NotRequired["str"]
    """<p>The token that you use when you request the next set of private re:Posts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpacesOutput) -> dict:
    out: dict = {}
    import capo_repostspace.types.spaces_list

    out["spaces"] = capo_repostspace.types.spaces_list.serialize_json(value["spaces"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSpacesOutput:
    out: ListSpacesOutput = {}  # type: ignore[typeddict-item]
    if data.get("spaces") is not None:
        import capo_repostspace.types.spaces_list

        out["spaces"] = capo_repostspace.types.spaces_list.deserialize_json(
            data["spaces"]
        )
    else:
        raise DeserializationError("ListSpacesOutput.spaces required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListSpacesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "spaces" in value:
        import capo_repostspace.types.spaces_list

        out["spaces"] = capo_repostspace.types.spaces_list.redact_sensitive(
            value["spaces"]
        )
    return out
