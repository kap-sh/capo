"""Generated from Smithy shape ``com.amazonaws.sesv2#ImportDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.data_format
    import capo_sesv2.types.s3_url


class ImportDataSource(TypedDict, closed=True):
    s3_url: "capo_sesv2.types.s3_url.S3Url"
    """<p>An Amazon S3 URL in the format s3://<i><bucket_name></i>/<i><object></i>.</p>"""
    data_format: "capo_sesv2.types.data_format.DataFormat"
    """<p>The data format of the import job's data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportDataSource) -> dict:
    out: dict = {}
    out["S3Url"] = value["s3_url"]
    import capo_sesv2.types.data_format

    out["DataFormat"] = capo_sesv2.types.data_format.serialize_json(
        value["data_format"]
    )
    return out


def deserialize_json(data: dict) -> ImportDataSource:
    out: ImportDataSource = {}  # type: ignore[typeddict-item]
    if data.get("S3Url") is not None:
        out["s3_url"] = data["S3Url"]
    else:
        out["s3_url"] = ""
    if data.get("DataFormat") is not None:
        import capo_sesv2.types.data_format

        out["data_format"] = capo_sesv2.types.data_format.deserialize_json(
            data["DataFormat"]
        )
    else:
        import typing

        out["data_format"] = typing.cast("capo_sesv2.types.data_format.DataFormat", "")
    return out
