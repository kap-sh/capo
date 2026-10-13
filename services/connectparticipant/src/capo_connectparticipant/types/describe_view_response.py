"""Generated from Smithy shape ``com.amazonaws.connectparticipant#DescribeViewResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.view


class DescribeViewResponse(TypedDict, closed=True):
    view: NotRequired["capo_connectparticipant.types.view.View"]
    """<p>A view resource object. Contains metadata and content necessary to render the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeViewResponse) -> dict:
    out: dict = {}
    if "view" in value:
        import capo_connectparticipant.types.view

        out["View"] = capo_connectparticipant.types.view.serialize_json(value["view"])
    return out


def deserialize_json(data: dict) -> DescribeViewResponse:
    out: DescribeViewResponse = {}  # type: ignore[typeddict-item]
    if data.get("View") is not None:
        import capo_connectparticipant.types.view

        out["view"] = capo_connectparticipant.types.view.deserialize_json(data["View"])
    return out


def redact_sensitive(value: DescribeViewResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "view" in value:
        import capo_connectparticipant.types.view

        out["view"] = capo_connectparticipant.types.view.redact_sensitive(value["view"])
    return out
