"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetElementRenderingRule``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.expression
    import capo_quicksight.types.sheet_element_configuration_overrides


class SheetElementRenderingRule(TypedDict, closed=True):
    expression: "capo_quicksight.types.expression.Expression"
    """<p>The expression of the rendering rules of a sheet.</p>"""
    configuration_overrides: "capo_quicksight.types.sheet_element_configuration_overrides.SheetElementConfigurationOverrides"
    """<p>The override configuration of the rendering rules of a sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetElementRenderingRule) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    import capo_quicksight.types.sheet_element_configuration_overrides

    out["ConfigurationOverrides"] = (
        capo_quicksight.types.sheet_element_configuration_overrides.serialize_json(
            value["configuration_overrides"]
        )
    )
    return out


def deserialize_json(data: dict) -> SheetElementRenderingRule:
    out: SheetElementRenderingRule = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        out["expression"] = ""
    if data.get("ConfigurationOverrides") is not None:
        import capo_quicksight.types.sheet_element_configuration_overrides

        out["configuration_overrides"] = (
            capo_quicksight.types.sheet_element_configuration_overrides.deserialize_json(
                data["ConfigurationOverrides"]
            )
        )
    else:
        raise DeserializationError(
            "SheetElementRenderingRule.configuration_overrides required"
        )
    return out


def redact_sensitive(value: SheetElementRenderingRule) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
