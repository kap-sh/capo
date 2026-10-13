"""Generated from Smithy shape ``com.amazonaws.quicksight#SemanticType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.sensitive_string
    import capo_quicksight.types.sensitive_string_list
    import capo_quicksight.types.type_parameters


class SemanticType(TypedDict, closed=True):
    type_name: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The semantic type name.</p>"""
    sub_type_name: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The semantic type sub type name.</p>"""
    type_parameters: NotRequired["capo_quicksight.types.type_parameters.TypeParameters"]
    """<p>The semantic type parameters.</p>"""
    truthy_cell_value: NotRequired[
        "capo_quicksight.types.sensitive_string.SensitiveString"
    ]
    """<p>The semantic type truthy cell value.</p>"""
    truthy_cell_value_synonyms: NotRequired[
        "capo_quicksight.types.sensitive_string_list.SensitiveStringList"
    ]
    """<p>The other names or aliases for the true cell value.</p>"""
    falsey_cell_value: NotRequired[
        "capo_quicksight.types.sensitive_string.SensitiveString"
    ]
    """<p>The semantic type falsey cell value.</p>"""
    falsey_cell_value_synonyms: NotRequired[
        "capo_quicksight.types.sensitive_string_list.SensitiveStringList"
    ]
    """<p>The other names or aliases for the false cell value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticType) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "sub_type_name" in value:
        out["SubTypeName"] = value["sub_type_name"]
    if "type_parameters" in value:
        import capo_quicksight.types.type_parameters

        out["TypeParameters"] = capo_quicksight.types.type_parameters.serialize_json(
            value["type_parameters"]
        )
    if "truthy_cell_value" in value:
        out["TruthyCellValue"] = value["truthy_cell_value"]
    if "truthy_cell_value_synonyms" in value:
        import capo_quicksight.types.sensitive_string_list

        out["TruthyCellValueSynonyms"] = (
            capo_quicksight.types.sensitive_string_list.serialize_json(
                value["truthy_cell_value_synonyms"]
            )
        )
    if "falsey_cell_value" in value:
        out["FalseyCellValue"] = value["falsey_cell_value"]
    if "falsey_cell_value_synonyms" in value:
        import capo_quicksight.types.sensitive_string_list

        out["FalseyCellValueSynonyms"] = (
            capo_quicksight.types.sensitive_string_list.serialize_json(
                value["falsey_cell_value_synonyms"]
            )
        )
    return out


def deserialize_json(data: dict) -> SemanticType:
    out: SemanticType = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("SubTypeName") is not None:
        out["sub_type_name"] = data["SubTypeName"]
    if data.get("TypeParameters") is not None:
        import capo_quicksight.types.type_parameters

        out["type_parameters"] = capo_quicksight.types.type_parameters.deserialize_json(
            data["TypeParameters"]
        )
    if data.get("TruthyCellValue") is not None:
        out["truthy_cell_value"] = data["TruthyCellValue"]
    if data.get("TruthyCellValueSynonyms") is not None:
        import capo_quicksight.types.sensitive_string_list

        out["truthy_cell_value_synonyms"] = (
            capo_quicksight.types.sensitive_string_list.deserialize_json(
                data["TruthyCellValueSynonyms"]
            )
        )
    if data.get("FalseyCellValue") is not None:
        out["falsey_cell_value"] = data["FalseyCellValue"]
    if data.get("FalseyCellValueSynonyms") is not None:
        import capo_quicksight.types.sensitive_string_list

        out["falsey_cell_value_synonyms"] = (
            capo_quicksight.types.sensitive_string_list.deserialize_json(
                data["FalseyCellValueSynonyms"]
            )
        )
    return out


def redact_sensitive(value: SemanticType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "truthy_cell_value" in value:
        out["truthy_cell_value"] = "*** Sensitive Data Redacted ***"
    if "truthy_cell_value_synonyms" in value:
        import capo_quicksight.types.sensitive_string_list

        out["truthy_cell_value_synonyms"] = (
            capo_quicksight.types.sensitive_string_list.redact_sensitive(
                value["truthy_cell_value_synonyms"]
            )
        )
    if "falsey_cell_value" in value:
        out["falsey_cell_value"] = "*** Sensitive Data Redacted ***"
    if "falsey_cell_value_synonyms" in value:
        import capo_quicksight.types.sensitive_string_list

        out["falsey_cell_value_synonyms"] = (
            capo_quicksight.types.sensitive_string_list.redact_sensitive(
                value["falsey_cell_value_synonyms"]
            )
        )
    return out
