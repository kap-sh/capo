"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_source_format
    import capo_iotsitewise.types.dataset_source_type
    import capo_iotsitewise.types.source_detail


class DatasetSource(TypedDict, closed=True):
    source_type: "capo_iotsitewise.types.dataset_source_type.DatasetSourceType"
    """<p>The type of data source for the dataset.</p>"""
    source_format: "capo_iotsitewise.types.dataset_source_format.DatasetSourceFormat"
    """<p>The format of the dataset source associated with the dataset.</p>"""
    source_detail: NotRequired["capo_iotsitewise.types.source_detail.SourceDetail"]
    """<p>The details of the dataset source associated with the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSource) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.dataset_source_type

    out["sourceType"] = capo_iotsitewise.types.dataset_source_type.serialize_json(
        value["source_type"]
    )
    import capo_iotsitewise.types.dataset_source_format

    out["sourceFormat"] = capo_iotsitewise.types.dataset_source_format.serialize_json(
        value["source_format"]
    )
    if "source_detail" in value:
        import capo_iotsitewise.types.source_detail

        out["sourceDetail"] = capo_iotsitewise.types.source_detail.serialize_json(
            value["source_detail"]
        )
    return out


def deserialize_json(data: dict) -> DatasetSource:
    out: DatasetSource = {}  # type: ignore[typeddict-item]
    if data.get("sourceType") is not None:
        import capo_iotsitewise.types.dataset_source_type

        out["source_type"] = (
            capo_iotsitewise.types.dataset_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_iotsitewise.types.dataset_source_type.DatasetSourceType", ""
        )
    if data.get("sourceFormat") is not None:
        import capo_iotsitewise.types.dataset_source_format

        out["source_format"] = (
            capo_iotsitewise.types.dataset_source_format.deserialize_json(
                data["sourceFormat"]
            )
        )
    else:
        import typing

        out["source_format"] = typing.cast(
            "capo_iotsitewise.types.dataset_source_format.DatasetSourceFormat", ""
        )
    if data.get("sourceDetail") is not None:
        import capo_iotsitewise.types.source_detail

        out["source_detail"] = capo_iotsitewise.types.source_detail.deserialize_json(
            data["sourceDetail"]
        )
    return out
