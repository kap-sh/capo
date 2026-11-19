"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.filter_name
    import capo_imagebuilder.types.filter_values


class Filter(TypedDict, closed=True):
    name: NotRequired["capo_imagebuilder.types.filter_name.FilterName"]
    """<p>The name of the filter. Filter names are case-sensitive.</p> <p>The <code>name</code> filter matches the name that you gave the resource when you created it, exactly as you entered it. It doesn't match the name segment of the resource ARN, which Image Builder converts to lowercase with hyphens in place of spaces and underscores. For example, a resource named <code>My Image</code> has an ARN that contains <code>my-image</code> – filter on <code>My Image</code> to find it.</p>"""
    values: NotRequired["capo_imagebuilder.types.filter_values.FilterValues"]
    """<p>The filter values. Filter values are case-sensitive.</p> <p>The <code>name</code> filter can use a wildcard: <code>web*</code> matches names that begin with <code>web</code>, and <code>*web*</code> matches names that contain <code>web</code>. The wildcard isn't supported in other positions or in other filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "values" in value:
        import capo_imagebuilder.types.filter_values

        out["values"] = capo_imagebuilder.types.filter_values.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("values") is not None:
        import capo_imagebuilder.types.filter_values

        out["values"] = capo_imagebuilder.types.filter_values.deserialize_json(
            data["values"]
        )
    return out
