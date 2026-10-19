"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#UnsupportedTimestamps``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.integer


class UnsupportedTimestamps(TypedDict, closed=True):
    total_number_of_unsupported_timestamps: (
        "capo_lookoutequipment.types.integer.Integer"
    )
    """<p> Indicates the total number of unsupported timestamps across the ingested data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UnsupportedTimestamps) -> dict:
    out: dict = {}
    out["TotalNumberOfUnsupportedTimestamps"] = value[
        "total_number_of_unsupported_timestamps"
    ]
    return out


def deserialize_aws_json_1_0(data: dict) -> UnsupportedTimestamps:
    out: UnsupportedTimestamps = {}  # type: ignore[typeddict-item]
    if data.get("TotalNumberOfUnsupportedTimestamps") is not None:
        out["total_number_of_unsupported_timestamps"] = data[
            "TotalNumberOfUnsupportedTimestamps"
        ]
    else:
        out["total_number_of_unsupported_timestamps"] = 0
    return out
