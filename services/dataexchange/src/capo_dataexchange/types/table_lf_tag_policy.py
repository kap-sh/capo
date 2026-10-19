"""Generated from Smithy shape ``com.amazonaws.dataexchange#TableLFTagPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.list_of_lf_tags


class TableLFTagPolicy(TypedDict, closed=True):
    expression: "capo_dataexchange.types.list_of_lf_tags.ListOfLFTags"
    """<p>A list of LF-tag conditions that apply to table resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableLFTagPolicy) -> dict:
    out: dict = {}
    import capo_dataexchange.types.list_of_lf_tags

    out["Expression"] = capo_dataexchange.types.list_of_lf_tags.serialize_json(
        value["expression"]
    )
    return out


def deserialize_json(data: dict) -> TableLFTagPolicy:
    out: TableLFTagPolicy = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        import capo_dataexchange.types.list_of_lf_tags

        out["expression"] = capo_dataexchange.types.list_of_lf_tags.deserialize_json(
            data["Expression"]
        )
    else:
        out["expression"] = []
    return out
