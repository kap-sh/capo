"""Generated from Smithy shape ``com.amazonaws.dataexchange#RedshiftDataShareAssetSourceEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string


class RedshiftDataShareAssetSourceEntry(TypedDict, closed=True):
    data_share_arn: "capo_dataexchange.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the datashare asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftDataShareAssetSourceEntry) -> dict:
    out: dict = {}
    out["DataShareArn"] = value["data_share_arn"]
    return out


def deserialize_json(data: dict) -> RedshiftDataShareAssetSourceEntry:
    out: RedshiftDataShareAssetSourceEntry = {}  # type: ignore[typeddict-item]
    if data.get("DataShareArn") is not None:
        out["data_share_arn"] = data["DataShareArn"]
    else:
        out["data_share_arn"] = ""
    return out
