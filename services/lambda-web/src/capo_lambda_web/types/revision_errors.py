"""Generated from Smithy shape ``com.amazonaws.lambdaweb#RevisionErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_web.types.revision_error

RevisionErrors: TypeAlias = list["capo_lambda_web.types.revision_error.RevisionError"]


# --- restJson1 ser/de ---
def serialize_json(value: RevisionErrors) -> list:
    import capo_lambda_web.types.revision_error

    out: list = []
    for item in value:
        out.append(capo_lambda_web.types.revision_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> RevisionErrors:
    import capo_lambda_web.types.revision_error

    out: RevisionErrors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_web.types.revision_error.deserialize_json(item))
    return out
