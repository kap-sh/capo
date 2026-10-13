"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#BatchGetViewOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.batch_get_view_errors
    import capo_resource_explorer_2.types.view_list


class BatchGetViewOutput(TypedDict, closed=True):
    views: NotRequired["capo_resource_explorer_2.types.view_list.ViewList"]
    """<p>A structure with a list of objects with details for each of the specified views.</p>"""
    errors: NotRequired[
        "capo_resource_explorer_2.types.batch_get_view_errors.BatchGetViewErrors"
    ]
    """<p>If any of the specified ARNs result in an error, then this structure describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetViewOutput) -> dict:
    out: dict = {}
    if "views" in value:
        import capo_resource_explorer_2.types.view_list

        out["Views"] = capo_resource_explorer_2.types.view_list.serialize_json(
            value["views"]
        )
    if "errors" in value:
        import capo_resource_explorer_2.types.batch_get_view_errors

        out["Errors"] = (
            capo_resource_explorer_2.types.batch_get_view_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetViewOutput:
    out: BatchGetViewOutput = {}  # type: ignore[typeddict-item]
    if data.get("Views") is not None:
        import capo_resource_explorer_2.types.view_list

        out["views"] = capo_resource_explorer_2.types.view_list.deserialize_json(
            data["Views"]
        )
    if data.get("Errors") is not None:
        import capo_resource_explorer_2.types.batch_get_view_errors

        out["errors"] = (
            capo_resource_explorer_2.types.batch_get_view_errors.deserialize_json(
                data["Errors"]
            )
        )
    return out


def redact_sensitive(value: BatchGetViewOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "views" in value:
        import capo_resource_explorer_2.types.view_list

        out["views"] = capo_resource_explorer_2.types.view_list.redact_sensitive(
            value["views"]
        )
    return out
