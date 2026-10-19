"""Generated from Smithy shape ``com.amazonaws.iam#ParameterDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.parameter_default_value_type
    import capo_iam.types.parameter_description_type
    import capo_iam.types.parameter_name_type
    import capo_iam.types.parameter_sub_type_type
    import capo_iam.types.parameter_type_type


class ParameterDefinition(TypedDict, closed=True):
    name: "capo_iam.types.parameter_name_type.parameterNameType"
    """<p>The name of the parameter.</p>"""
    type: "capo_iam.types.parameter_type_type.parameterTypeType"
    """<p>The data type of the parameter. Valid values are <code>String</code>, <code>StringList</code>, <code>Number</code>, <code>NumberList</code>, <code>Arn</code>, and <code>ArnList</code>.</p>"""
    sub_type: NotRequired["capo_iam.types.parameter_sub_type_type.parameterSubTypeType"]
    """<p>An optional subtype that further constrains the values that are allowed for the parameter.</p>"""
    description: NotRequired[
        "capo_iam.types.parameter_description_type.parameterDescriptionType"
    ]
    """<p>A description of the parameter.</p>"""
    is_required: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether you must supply a value for the parameter when you create a role from the template.</p>"""
    default_value: NotRequired[
        "capo_iam.types.parameter_default_value_type.parameterDefaultValueType"
    ]
    """<p>The value that the service uses for the parameter when you do not supply one.</p>"""
    immutable: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether you can change the parameter value after you create the role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ParameterDefinition, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Name", str(value["name"])))
    import capo_iam.types.parameter_type_type

    capo_iam.types.parameter_type_type.serialize_query(
        value["type"], pairs, f"{key_prefix}Type"
    )
    if "sub_type" in value:
        pairs.append((f"{key_prefix}SubType", str(value["sub_type"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    pairs.append(
        (
            f"{key_prefix}IsRequired",
            "true" if value.get("is_required", False) else "false",
        )
    )
    if "default_value" in value:
        pairs.append((f"{key_prefix}DefaultValue", str(value["default_value"])))
    pairs.append(
        (f"{key_prefix}Immutable", "true" if value.get("immutable", False) else "false")
    )


def deserialize_query(el: Element) -> ParameterDefinition:
    out: ParameterDefinition = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_type = el.find("Type")
    if child_type is not None:
        import capo_iam.types.parameter_type_type

        out["type"] = capo_iam.types.parameter_type_type.deserialize_query(child_type)
    else:
        import typing

        out["type"] = typing.cast(
            "capo_iam.types.parameter_type_type.parameterTypeType", ""
        )
    child_sub_type = el.find("SubType")
    if child_sub_type is not None:
        out["sub_type"] = str(child_sub_type.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_is_required = el.find("IsRequired")
    if child_is_required is not None:
        out["is_required"] = (child_is_required.text or "").lower() == "true"
    else:
        out["is_required"] = False
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_immutable = el.find("Immutable")
    if child_immutable is not None:
        out["immutable"] = (child_immutable.text or "").lower() == "true"
    else:
        out["immutable"] = False
    return out
