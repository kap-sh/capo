"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CookieSpecifications``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.cookie_specification

CookieSpecifications: TypeAlias = list[
    "capo_workspaces_web.types.cookie_specification.CookieSpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: CookieSpecifications) -> list:
    import capo_workspaces_web.types.cookie_specification

    out: list = []
    for item in value:
        out.append(capo_workspaces_web.types.cookie_specification.serialize_json(item))
    return out


def deserialize_json(data: list) -> CookieSpecifications:
    import capo_workspaces_web.types.cookie_specification

    out: CookieSpecifications = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_web.types.cookie_specification.deserialize_json(item)
        )
    return out


def redact_sensitive(value: CookieSpecifications) -> list[Any]:
    import capo_workspaces_web.types.cookie_specification

    return [
        capo_workspaces_web.types.cookie_specification.redact_sensitive(item)
        for item in value
    ]
