"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TagFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.tag_filter_key
    import capo_observabilityadmin.types.tag_filter_values


class TagFilter(TypedDict, closed=True):
    key: "capo_observabilityadmin.types.tag_filter_key.TagFilterKey"
    r"""<p>The tag key. Up to 512 characters. The characters &lt; &gt; % &amp; \ ? / $ { } ' " ` and control characters aren't allowed.</p>"""
    values: "capo_observabilityadmin.types.tag_filter_values.TagFilterValues"
    """<p>The tag values to match. A resource matches if it has any of these values for the tag key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagFilter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_observabilityadmin.types.tag_filter_values

    out["Values"] = capo_observabilityadmin.types.tag_filter_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Values") is not None:
        import capo_observabilityadmin.types.tag_filter_values

        out["values"] = (
            capo_observabilityadmin.types.tag_filter_values.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
