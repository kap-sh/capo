"""Generated from Smithy shape ``com.amazonaws.wellarchitected#TradeOff``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.pillar
    import capo_wellarchitected.types.risk_rating


class TradeOff(TypedDict, closed=True):
    pillar: "capo_wellarchitected.types.pillar.Pillar"
    """<p>The pillar that could be negatively impacted.</p>"""
    title: "str"
    """<p>A short phrase describing what is lost or degraded.</p>"""
    description: "str"
    """<p>A description of the specific risk and the condition that triggers it.</p>"""
    risk: "capo_wellarchitected.types.risk_rating.RiskRating"
    """<p>The risk rating for the trade-off.</p>"""
    mitigation: "str"
    """<p>A specific action to mitigate the trade-off and when to take it.</p>"""
    risk_explanation: NotRequired["str"]
    """<p>An optional explanation providing additional context for the risk rating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TradeOff) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.pillar

    out["pillar"] = capo_wellarchitected.types.pillar.serialize_json(value["pillar"])
    out["title"] = value["title"]
    out["description"] = value["description"]
    import capo_wellarchitected.types.risk_rating

    out["risk"] = capo_wellarchitected.types.risk_rating.serialize_json(value["risk"])
    out["mitigation"] = value["mitigation"]
    if "risk_explanation" in value:
        out["riskExplanation"] = value["risk_explanation"]
    return out


def deserialize_json(data: dict) -> TradeOff:
    out: TradeOff = {}  # type: ignore[typeddict-item]
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
    if data.get("risk") is not None:
        import capo_wellarchitected.types.risk_rating

        out["risk"] = capo_wellarchitected.types.risk_rating.deserialize_json(
            data["risk"]
        )
    else:
        import typing

        out["risk"] = typing.cast(
            "capo_wellarchitected.types.risk_rating.RiskRating", ""
        )
    if data.get("mitigation") is not None:
        out["mitigation"] = data["mitigation"]
    else:
        out["mitigation"] = ""
    if data.get("riskExplanation") is not None:
        out["risk_explanation"] = data["riskExplanation"]
    return out
