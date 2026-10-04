"""Generated from Smithy shape ``com.amazonaws.deadline#FleetSoftwareAddOn``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.fleet_software_add_on_name


class FleetSoftwareAddOn(TypedDict, closed=True):
    name: "capo_deadline.types.fleet_software_add_on_name.FleetSoftwareAddOnName"
    """<p>The name of the software add-on. The supported value is <code>docker</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FleetSoftwareAddOn) -> dict:
    out: dict = {}
    import capo_deadline.types.fleet_software_add_on_name

    out["name"] = capo_deadline.types.fleet_software_add_on_name.serialize_json(
        value["name"]
    )
    return out


def deserialize_json(data: dict) -> FleetSoftwareAddOn:
    out: FleetSoftwareAddOn = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_deadline.types.fleet_software_add_on_name

        out["name"] = capo_deadline.types.fleet_software_add_on_name.deserialize_json(
            data["name"]
        )
    else:
        raise DeserializationError("FleetSoftwareAddOn.name required")
    return out
