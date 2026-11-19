"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationIndicator``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.indicator_value
    import capo_guardduty.types.investigation_indicator_type


class InvestigationIndicator(TypedDict, closed=True):
    value: NotRequired["capo_guardduty.types.indicator_value.IndicatorValue"]
    """<p>The value of the indicator.</p>"""
    type: NotRequired[
        "capo_guardduty.types.investigation_indicator_type.InvestigationIndicatorType"
    ]
    """<p>The type of the indicator. Possible values are <code>IP</code>, <code>DOMAIN</code>, and <code>FILE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationIndicator) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "type" in value:
        import capo_guardduty.types.investigation_indicator_type

        out["type"] = capo_guardduty.types.investigation_indicator_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationIndicator:
    out: InvestigationIndicator = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("type") is not None:
        import capo_guardduty.types.investigation_indicator_type

        out["type"] = (
            capo_guardduty.types.investigation_indicator_type.deserialize_json(
                data["type"]
            )
        )
    return out


def redact_sensitive(value: InvestigationIndicator) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
