"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#InstanceIdFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.instance_id
    import capo_connectcampaigns.types.instance_id_filter_operator


class InstanceIdFilter(TypedDict, closed=True):
    value: "capo_connectcampaigns.types.instance_id.InstanceId"
    operator: "capo_connectcampaigns.types.instance_id_filter_operator.InstanceIdFilterOperator"


# --- restJson1 ser/de ---
def serialize_json(value: InstanceIdFilter) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    out["operator"] = value["operator"]
    return out


def deserialize_json(data: dict) -> InstanceIdFilter:
    out: InstanceIdFilter = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("operator") is not None:
        out["operator"] = data["operator"]
    else:
        out["operator"] = ""
    return out
