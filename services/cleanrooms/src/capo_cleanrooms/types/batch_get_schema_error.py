"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.table_alias


class BatchGetSchemaError(TypedDict, closed=True):
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>An error name for the error.</p>"""
    code: "str"
    """<p>An error code for the error. </p>"""
    message: "str"
    """<p>An error message for the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaError) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetSchemaError:
    out: BatchGetSchemaError = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
