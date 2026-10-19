"""Generated from Smithy shape ``com.amazonaws.iam#ReplacementValueEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.replacement_value_list_type


class ReplacementValueEntry(TypedDict, closed=True):
    values: "capo_iam.types.replacement_value_list_type.replacementValueListType"
    """<p>The list of replacement values for the template parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReplacementValueEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.replacement_value_list_type

    capo_iam.types.replacement_value_list_type.serialize_query(
        value["values"], pairs, f"{key_prefix}Values"
    )


def deserialize_query(el: Element) -> ReplacementValueEntry:
    out: ReplacementValueEntry = {}  # type: ignore[typeddict-item]
    child_values = el.find("Values")
    if child_values is not None:
        import capo_iam.types.replacement_value_list_type

        out["values"] = capo_iam.types.replacement_value_list_type.deserialize_query(
            child_values
        )
    else:
        out["values"] = []
    return out
