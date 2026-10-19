"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolNetworkPackageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.nsd_operational_state


class UpdateSolNetworkPackageInput(TypedDict, closed=True):
    nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network service descriptor in the network package.</p>"""
    nsd_operational_state: "capo_tnb.types.nsd_operational_state.NsdOperationalState"
    """<p>Operational state of the network service descriptor in the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolNetworkPackageInput) -> dict:
    out: dict = {}
    import capo_tnb.types.nsd_operational_state

    out["nsdOperationalState"] = capo_tnb.types.nsd_operational_state.serialize_json(
        value["nsd_operational_state"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSolNetworkPackageInput:
    out: UpdateSolNetworkPackageInput = {}  # type: ignore[typeddict-item]
    if data.get("nsdOperationalState") is not None:
        import capo_tnb.types.nsd_operational_state

        out["nsd_operational_state"] = (
            capo_tnb.types.nsd_operational_state.deserialize_json(
                data["nsdOperationalState"]
            )
        )
    else:
        import typing

        out["nsd_operational_state"] = typing.cast(
            "capo_tnb.types.nsd_operational_state.NsdOperationalState", ""
        )
    return out
