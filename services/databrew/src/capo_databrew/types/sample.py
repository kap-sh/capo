"""Generated from Smithy shape ``com.amazonaws.databrew#Sample``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.sample_size
    import capo_databrew.types.sample_type


class Sample(TypedDict, closed=True):
    size: NotRequired["capo_databrew.types.sample_size.SampleSize"]
    """<p>The number of rows in the sample.</p>"""
    type: "capo_databrew.types.sample_type.SampleType"
    """<p>The way in which DataBrew obtains rows from a dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sample) -> dict:
    out: dict = {}
    if "size" in value:
        out["Size"] = value["size"]
    import capo_databrew.types.sample_type

    out["Type"] = capo_databrew.types.sample_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> Sample:
    out: Sample = {}  # type: ignore[typeddict-item]
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    if data.get("Type") is not None:
        import capo_databrew.types.sample_type

        out["type"] = capo_databrew.types.sample_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_databrew.types.sample_type.SampleType", "")
    return out
