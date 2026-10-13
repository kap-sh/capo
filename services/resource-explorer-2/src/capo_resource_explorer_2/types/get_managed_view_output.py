"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetManagedViewOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.managed_view


class GetManagedViewOutput(TypedDict, closed=True):
    managed_view: NotRequired["capo_resource_explorer_2.types.managed_view.ManagedView"]
    """<p>Details about the specified managed view. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedViewOutput) -> dict:
    out: dict = {}
    if "managed_view" in value:
        import capo_resource_explorer_2.types.managed_view

        out["ManagedView"] = capo_resource_explorer_2.types.managed_view.serialize_json(
            value["managed_view"]
        )
    return out


def deserialize_json(data: dict) -> GetManagedViewOutput:
    out: GetManagedViewOutput = {}  # type: ignore[typeddict-item]
    if data.get("ManagedView") is not None:
        import capo_resource_explorer_2.types.managed_view

        out["managed_view"] = (
            capo_resource_explorer_2.types.managed_view.deserialize_json(
                data["ManagedView"]
            )
        )
    return out


def redact_sensitive(value: GetManagedViewOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "managed_view" in value:
        import capo_resource_explorer_2.types.managed_view

        out["managed_view"] = (
            capo_resource_explorer_2.types.managed_view.redact_sensitive(
                value["managed_view"]
            )
        )
    return out
