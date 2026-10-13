"""Generated from Smithy shape ``com.amazonaws.location#RouteMatrix``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.route_matrix_row

RouteMatrix: TypeAlias = list["capo_location.types.route_matrix_row.RouteMatrixRow"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrix) -> list:
    import capo_location.types.route_matrix_row

    out: list = []
    for item in value:
        out.append(capo_location.types.route_matrix_row.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteMatrix:
    import capo_location.types.route_matrix_row

    out: RouteMatrix = []
    for item in data:
        if item is None:
            continue
        out.append(capo_location.types.route_matrix_row.deserialize_json(item))
    return out


def redact_sensitive(value: RouteMatrix) -> list[Any]:
    import capo_location.types.route_matrix_row

    return [
        capo_location.types.route_matrix_row.redact_sensitive(item) for item in value
    ]
