"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterDeclaration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_parameter_declaration
    import capo_quicksight.types.decimal_parameter_declaration
    import capo_quicksight.types.integer_parameter_declaration
    import capo_quicksight.types.string_parameter_declaration


class ParameterDeclaration(TypedDict, closed=True):
    string_parameter_declaration: NotRequired[
        "capo_quicksight.types.string_parameter_declaration.StringParameterDeclaration"
    ]
    """<p>A parameter declaration for the <code>String</code> data type.</p>"""
    decimal_parameter_declaration: NotRequired[
        "capo_quicksight.types.decimal_parameter_declaration.DecimalParameterDeclaration"
    ]
    """<p>A parameter declaration for the <code>Decimal</code> data type.</p>"""
    integer_parameter_declaration: NotRequired[
        "capo_quicksight.types.integer_parameter_declaration.IntegerParameterDeclaration"
    ]
    """<p>A parameter declaration for the <code>Integer</code> data type.</p>"""
    date_time_parameter_declaration: NotRequired[
        "capo_quicksight.types.date_time_parameter_declaration.DateTimeParameterDeclaration"
    ]
    """<p>A parameter declaration for the <code>DateTime</code> data type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterDeclaration) -> dict:
    out: dict = {}
    if "string_parameter_declaration" in value:
        import capo_quicksight.types.string_parameter_declaration

        out["StringParameterDeclaration"] = (
            capo_quicksight.types.string_parameter_declaration.serialize_json(
                value["string_parameter_declaration"]
            )
        )
    if "decimal_parameter_declaration" in value:
        import capo_quicksight.types.decimal_parameter_declaration

        out["DecimalParameterDeclaration"] = (
            capo_quicksight.types.decimal_parameter_declaration.serialize_json(
                value["decimal_parameter_declaration"]
            )
        )
    if "integer_parameter_declaration" in value:
        import capo_quicksight.types.integer_parameter_declaration

        out["IntegerParameterDeclaration"] = (
            capo_quicksight.types.integer_parameter_declaration.serialize_json(
                value["integer_parameter_declaration"]
            )
        )
    if "date_time_parameter_declaration" in value:
        import capo_quicksight.types.date_time_parameter_declaration

        out["DateTimeParameterDeclaration"] = (
            capo_quicksight.types.date_time_parameter_declaration.serialize_json(
                value["date_time_parameter_declaration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParameterDeclaration:
    out: ParameterDeclaration = {}  # type: ignore[typeddict-item]
    if data.get("StringParameterDeclaration") is not None:
        import capo_quicksight.types.string_parameter_declaration

        out["string_parameter_declaration"] = (
            capo_quicksight.types.string_parameter_declaration.deserialize_json(
                data["StringParameterDeclaration"]
            )
        )
    if data.get("DecimalParameterDeclaration") is not None:
        import capo_quicksight.types.decimal_parameter_declaration

        out["decimal_parameter_declaration"] = (
            capo_quicksight.types.decimal_parameter_declaration.deserialize_json(
                data["DecimalParameterDeclaration"]
            )
        )
    if data.get("IntegerParameterDeclaration") is not None:
        import capo_quicksight.types.integer_parameter_declaration

        out["integer_parameter_declaration"] = (
            capo_quicksight.types.integer_parameter_declaration.deserialize_json(
                data["IntegerParameterDeclaration"]
            )
        )
    if data.get("DateTimeParameterDeclaration") is not None:
        import capo_quicksight.types.date_time_parameter_declaration

        out["date_time_parameter_declaration"] = (
            capo_quicksight.types.date_time_parameter_declaration.deserialize_json(
                data["DateTimeParameterDeclaration"]
            )
        )
    return out


def redact_sensitive(value: ParameterDeclaration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "string_parameter_declaration" in value:
        import capo_quicksight.types.string_parameter_declaration

        out["string_parameter_declaration"] = (
            capo_quicksight.types.string_parameter_declaration.redact_sensitive(
                value["string_parameter_declaration"]
            )
        )
    if "decimal_parameter_declaration" in value:
        import capo_quicksight.types.decimal_parameter_declaration

        out["decimal_parameter_declaration"] = (
            capo_quicksight.types.decimal_parameter_declaration.redact_sensitive(
                value["decimal_parameter_declaration"]
            )
        )
    if "integer_parameter_declaration" in value:
        import capo_quicksight.types.integer_parameter_declaration

        out["integer_parameter_declaration"] = (
            capo_quicksight.types.integer_parameter_declaration.redact_sensitive(
                value["integer_parameter_declaration"]
            )
        )
    if "date_time_parameter_declaration" in value:
        import capo_quicksight.types.date_time_parameter_declaration

        out["date_time_parameter_declaration"] = (
            capo_quicksight.types.date_time_parameter_declaration.redact_sensitive(
                value["date_time_parameter_declaration"]
            )
        )
    return out
