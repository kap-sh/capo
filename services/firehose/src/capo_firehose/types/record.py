"""Generated from Smithy shape ``com.amazonaws.firehose#Record``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.data


class Record(TypedDict, closed=True):
    data: "capo_firehose.types.data.Data"
    """<p>The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KiB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Record) -> dict:
    out: dict = {}
    import capo_firehose.types.data

    out["Data"] = capo_firehose.types.data.serialize_aws_json_1_1(value["data"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if data.get("Data") is not None:
        import capo_firehose.types.data

        out["data"] = capo_firehose.types.data.deserialize_aws_json_1_1(data["Data"])
    else:
        out["data"] = b""
    return out
