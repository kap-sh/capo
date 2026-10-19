"""Generated from Smithy shape ``com.amazonaws.applicationsignals#SelectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.selection_pattern
    import capo_application_signals.types.selection_type


class SelectionConfig(TypedDict, closed=True):
    type: "capo_application_signals.types.selection_type.SelectionType"
    pattern: NotRequired[
        "capo_application_signals.types.selection_pattern.SelectionPattern"
    ]
    """<p>A prefix string or regular expression that specifies which operations to include in a service-level SLO. When <code>SelectionType</code> is <code>PREFIX</code>, this value is a prefix string that matches the beginning of operation names. When <code>SelectionType</code> is <code>REGEX</code>, this value is a regular expression that matches operation names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectionConfig) -> dict:
    out: dict = {}
    import capo_application_signals.types.selection_type

    out["Type"] = capo_application_signals.types.selection_type.serialize_json(
        value["type"]
    )
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    return out


def deserialize_json(data: dict) -> SelectionConfig:
    out: SelectionConfig = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_application_signals.types.selection_type

        out["type"] = capo_application_signals.types.selection_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_application_signals.types.selection_type.SelectionType", ""
        )
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    return out
