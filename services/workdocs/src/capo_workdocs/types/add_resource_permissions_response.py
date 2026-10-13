"""Generated from Smithy shape ``com.amazonaws.workdocs#AddResourcePermissionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.share_results_list


class AddResourcePermissionsResponse(TypedDict, closed=True):
    share_results: NotRequired[
        "capo_workdocs.types.share_results_list.ShareResultsList"
    ]
    """<p>The share results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddResourcePermissionsResponse) -> dict:
    out: dict = {}
    if "share_results" in value:
        import capo_workdocs.types.share_results_list

        out["ShareResults"] = capo_workdocs.types.share_results_list.serialize_json(
            value["share_results"]
        )
    return out


def deserialize_json(data: dict) -> AddResourcePermissionsResponse:
    out: AddResourcePermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ShareResults") is not None:
        import capo_workdocs.types.share_results_list

        out["share_results"] = capo_workdocs.types.share_results_list.deserialize_json(
            data["ShareResults"]
        )
    return out


def redact_sensitive(value: AddResourcePermissionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "share_results" in value:
        import capo_workdocs.types.share_results_list

        out["share_results"] = capo_workdocs.types.share_results_list.redact_sensitive(
            value["share_results"]
        )
    return out
