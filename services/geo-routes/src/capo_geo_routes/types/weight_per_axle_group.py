"""Generated from Smithy shape ``com.amazonaws.georoutes#WeightPerAxleGroup``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.weight_kilograms


class WeightPerAxleGroup(TypedDict, closed=True):
    single: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Total weight in kilograms for single axle configurations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    tandem: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Total weight in kilograms for tandem (two adjacent) axle configurations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    triple: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Total weight in kilograms for triple (three adjacent) axle configurations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    quad: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Total weight in kilograms for quad (four adjacent) axle configurations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    quint: "capo_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Total weight in kilograms for quint (five adjacent) axle configurations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeightPerAxleGroup) -> dict:
    out: dict = {}
    out["Single"] = value.get("single", 0)
    out["Tandem"] = value.get("tandem", 0)
    out["Triple"] = value.get("triple", 0)
    out["Quad"] = value.get("quad", 0)
    out["Quint"] = value.get("quint", 0)
    return out


def deserialize_json(data: dict) -> WeightPerAxleGroup:
    out: WeightPerAxleGroup = {}  # type: ignore[typeddict-item]
    if data.get("Single") is not None:
        out["single"] = data["Single"]
    else:
        out["single"] = 0
    if data.get("Tandem") is not None:
        out["tandem"] = data["Tandem"]
    else:
        out["tandem"] = 0
    if data.get("Triple") is not None:
        out["triple"] = data["Triple"]
    else:
        out["triple"] = 0
    if data.get("Quad") is not None:
        out["quad"] = data["Quad"]
    else:
        out["quad"] = 0
    if data.get("Quint") is not None:
        out["quint"] = data["Quint"]
    else:
        out["quint"] = 0
    return out


def redact_sensitive(value: WeightPerAxleGroup) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "single" in value:
        out["single"] = "*** Sensitive Data Redacted ***"
    if "tandem" in value:
        out["tandem"] = "*** Sensitive Data Redacted ***"
    if "triple" in value:
        out["triple"] = "*** Sensitive Data Redacted ***"
    if "quad" in value:
        out["quad"] = "*** Sensitive Data Redacted ***"
    if "quint" in value:
        out["quint"] = "*** Sensitive Data Redacted ***"
    return out
