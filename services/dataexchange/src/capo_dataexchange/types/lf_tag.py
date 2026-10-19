"""Generated from Smithy shape ``com.amazonaws.dataexchange#LFTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.list_of_lf_tag_values


class LFTag(TypedDict, closed=True):
    tag_key: "str"
    """<p>The key name for the LF-tag.</p>"""
    tag_values: "capo_dataexchange.types.list_of_lf_tag_values.ListOfLFTagValues"
    """<p>A list of LF-tag values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFTag) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    import capo_dataexchange.types.list_of_lf_tag_values

    out["TagValues"] = capo_dataexchange.types.list_of_lf_tag_values.serialize_json(
        value["tag_values"]
    )
    return out


def deserialize_json(data: dict) -> LFTag:
    out: LFTag = {}  # type: ignore[typeddict-item]
    if data.get("TagKey") is not None:
        out["tag_key"] = data["TagKey"]
    else:
        out["tag_key"] = ""
    if data.get("TagValues") is not None:
        import capo_dataexchange.types.list_of_lf_tag_values

        out["tag_values"] = (
            capo_dataexchange.types.list_of_lf_tag_values.deserialize_json(
                data["TagValues"]
            )
        )
    else:
        out["tag_values"] = []
    return out
