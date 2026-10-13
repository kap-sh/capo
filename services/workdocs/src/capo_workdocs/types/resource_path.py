"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourcePath``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.resource_path_component_list


class ResourcePath(TypedDict, closed=True):
    components: NotRequired[
        "capo_workdocs.types.resource_path_component_list.ResourcePathComponentList"
    ]
    """<p>The components of the resource path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePath) -> dict:
    out: dict = {}
    if "components" in value:
        import capo_workdocs.types.resource_path_component_list

        out["Components"] = (
            capo_workdocs.types.resource_path_component_list.serialize_json(
                value["components"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourcePath:
    out: ResourcePath = {}  # type: ignore[typeddict-item]
    if data.get("Components") is not None:
        import capo_workdocs.types.resource_path_component_list

        out["components"] = (
            capo_workdocs.types.resource_path_component_list.deserialize_json(
                data["Components"]
            )
        )
    return out


def redact_sensitive(value: ResourcePath) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "components" in value:
        import capo_workdocs.types.resource_path_component_list

        out["components"] = (
            capo_workdocs.types.resource_path_component_list.redact_sensitive(
                value["components"]
            )
        )
    return out
