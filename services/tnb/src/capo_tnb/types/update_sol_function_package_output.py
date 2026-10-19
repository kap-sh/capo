"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolFunctionPackageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.operational_state


class UpdateSolFunctionPackageOutput(TypedDict, closed=True):
    operational_state: "capo_tnb.types.operational_state.OperationalState"
    """<p>Operational state of the function package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolFunctionPackageOutput) -> dict:
    out: dict = {}
    import capo_tnb.types.operational_state

    out["operationalState"] = capo_tnb.types.operational_state.serialize_json(
        value["operational_state"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSolFunctionPackageOutput:
    out: UpdateSolFunctionPackageOutput = {}  # type: ignore[typeddict-item]
    if data.get("operationalState") is not None:
        import capo_tnb.types.operational_state

        out["operational_state"] = capo_tnb.types.operational_state.deserialize_json(
            data["operationalState"]
        )
    else:
        import typing

        out["operational_state"] = typing.cast(
            "capo_tnb.types.operational_state.OperationalState", ""
        )
    return out
