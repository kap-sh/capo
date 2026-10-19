"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.path_element_list
    import capo_accessanalyzer.types.span


class Location(TypedDict, closed=True):
    path: "capo_accessanalyzer.types.path_element_list.PathElementList"
    """<p>A path in a policy, represented as a sequence of path elements.</p>"""
    span: "capo_accessanalyzer.types.span.Span"
    """<p>A span in a policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Location) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.path_element_list

    out["path"] = capo_accessanalyzer.types.path_element_list.serialize_json(
        value["path"]
    )
    import capo_accessanalyzer.types.span

    out["span"] = capo_accessanalyzer.types.span.serialize_json(value["span"])
    return out


def deserialize_json(data: dict) -> Location:
    out: Location = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        import capo_accessanalyzer.types.path_element_list

        out["path"] = capo_accessanalyzer.types.path_element_list.deserialize_json(
            data["path"]
        )
    else:
        out["path"] = []
    if data.get("span") is not None:
        import capo_accessanalyzer.types.span

        out["span"] = capo_accessanalyzer.types.span.deserialize_json(data["span"])
    else:
        raise DeserializationError("Location.span required")
    return out
