"""Generated from Smithy shape ``com.amazonaws.grafana#UpdatePermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.update_error_list


class UpdatePermissionsResponse(TypedDict, closed=True):
    errors: "capo_grafana.types.update_error_list.UpdateErrorList"
    """<p>An array of structures that contain the errors from the operation, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePermissionsResponse) -> dict:
    out: dict = {}
    import capo_grafana.types.update_error_list

    out["errors"] = capo_grafana.types.update_error_list.serialize_json(value["errors"])
    return out


def deserialize_json(data: dict) -> UpdatePermissionsResponse:
    out: UpdatePermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("errors") is not None:
        import capo_grafana.types.update_error_list

        out["errors"] = capo_grafana.types.update_error_list.deserialize_json(
            data["errors"]
        )
    else:
        out["errors"] = []
    return out
