"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CrossPillarBenefit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.impact_category
    import capo_wellarchitected.types.pillar


class CrossPillarBenefit(TypedDict, closed=True):
    pillar: "capo_wellarchitected.types.pillar.Pillar"
    """<p>The pillar that would be positively impacted.</p>"""
    title: "str"
    """<p>A short phrase describing the outcome.</p>"""
    description: "str"
    """<p>A description of what changes and why it matters.</p>"""
    impact: "capo_wellarchitected.types.impact_category.ImpactCategory"
    """<p>The severity of the benefit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossPillarBenefit) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.pillar

    out["pillar"] = capo_wellarchitected.types.pillar.serialize_json(value["pillar"])
    out["title"] = value["title"]
    out["description"] = value["description"]
    import capo_wellarchitected.types.impact_category

    out["impact"] = capo_wellarchitected.types.impact_category.serialize_json(
        value["impact"]
    )
    return out


def deserialize_json(data: dict) -> CrossPillarBenefit:
    out: CrossPillarBenefit = {}  # type: ignore[typeddict-item]
    if data.get("pillar") is not None:
        import capo_wellarchitected.types.pillar

        out["pillar"] = capo_wellarchitected.types.pillar.deserialize_json(
            data["pillar"]
        )
    else:
        import typing

        out["pillar"] = typing.cast("capo_wellarchitected.types.pillar.Pillar", "")
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("impact") is not None:
        import capo_wellarchitected.types.impact_category

        out["impact"] = capo_wellarchitected.types.impact_category.deserialize_json(
            data["impact"]
        )
    else:
        import typing

        out["impact"] = typing.cast(
            "capo_wellarchitected.types.impact_category.ImpactCategory", ""
        )
    return out
