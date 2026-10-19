"""Generated from Smithy shape ``com.amazonaws.keyspaces#StaticColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.generic_string


class StaticColumn(TypedDict, closed=True):
    name: "capo_keyspaces.types.generic_string.GenericString"
    """<p>The name of the static column.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StaticColumn) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StaticColumn:
    out: StaticColumn = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
