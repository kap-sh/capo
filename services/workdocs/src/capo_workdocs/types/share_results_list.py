"""Generated from Smithy shape ``com.amazonaws.workdocs#ShareResultsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.share_result

ShareResultsList: TypeAlias = list["capo_workdocs.types.share_result.ShareResult"]


# --- restJson1 ser/de ---
def serialize_json(value: ShareResultsList) -> list:
    import capo_workdocs.types.share_result

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.share_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> ShareResultsList:
    import capo_workdocs.types.share_result

    out: ShareResultsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workdocs.types.share_result.deserialize_json(item))
    return out


def redact_sensitive(value: ShareResultsList) -> list[Any]:
    import capo_workdocs.types.share_result

    return [capo_workdocs.types.share_result.redact_sensitive(item) for item in value]
