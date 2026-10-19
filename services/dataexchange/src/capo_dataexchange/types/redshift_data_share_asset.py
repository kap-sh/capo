"""Generated from Smithy shape ``com.amazonaws.dataexchange#RedshiftDataShareAsset``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string


class RedshiftDataShareAsset(TypedDict, closed=True):
    arn: "capo_dataexchange.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the datashare asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftDataShareAsset) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> RedshiftDataShareAsset:
    out: RedshiftDataShareAsset = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
