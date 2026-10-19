"""Generated from Smithy shape ``com.amazonaws.ssmincidents#DeleteRegionAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.region_name


class DeleteRegionAction(TypedDict, closed=True):
    region_name: "capo_ssm_incidents.types.region_name.RegionName"
    """<p>The name of the Amazon Web Services Region you're deleting from the replication set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRegionAction) -> dict:
    out: dict = {}
    out["regionName"] = value["region_name"]
    return out


def deserialize_json(data: dict) -> DeleteRegionAction:
    out: DeleteRegionAction = {}  # type: ignore[typeddict-item]
    if data.get("regionName") is not None:
        out["region_name"] = data["regionName"]
    else:
        out["region_name"] = ""
    return out
