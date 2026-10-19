"""Generated from Smithy shape ``com.amazonaws.servicediscovery#SOAChange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.record_ttl


class SOAChange(TypedDict, closed=True):
    ttl: "capo_servicediscovery.types.record_ttl.RecordTTL"
    """<p>The updated time to live (TTL) for purposes of negative caching.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SOAChange) -> dict:
    out: dict = {}
    out["TTL"] = value["ttl"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SOAChange:
    out: SOAChange = {}  # type: ignore[typeddict-item]
    if data.get("TTL") is not None:
        out["ttl"] = data["TTL"]
    else:
        out["ttl"] = 0
    return out
