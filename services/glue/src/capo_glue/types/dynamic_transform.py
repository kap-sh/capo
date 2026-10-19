"""Generated from Smithy shape ``com.amazonaws.glue#DynamicTransform``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_schemas
    import capo_glue.types.one_input
    import capo_glue.types.transform_config_parameter_list


class DynamicTransform(TypedDict, closed=True):
    name: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>Specifies the name of the dynamic transform.</p>"""
    transform_name: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>Specifies the name of the dynamic transform as it appears in the Glue Studio visual editor.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>Specifies the inputs for the dynamic transform that are required.</p>"""
    parameters: NotRequired[
        "capo_glue.types.transform_config_parameter_list.TransformConfigParameterList"
    ]
    """<p>Specifies the parameters of the dynamic transform.</p>"""
    function_name: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>Specifies the name of the function of the dynamic transform.</p>"""
    path: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>Specifies the path of the dynamic transform source and config files.</p>"""
    version: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>This field is not used and will be deprecated in future release.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the dynamic transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamicTransform) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["TransformName"] = value["transform_name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "parameters" in value:
        import capo_glue.types.transform_config_parameter_list

        out["Parameters"] = (
            capo_glue.types.transform_config_parameter_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    out["FunctionName"] = value["function_name"]
    out["Path"] = value["path"]
    if "version" in value:
        out["Version"] = value["version"]
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DynamicTransform:
    out: DynamicTransform = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("TransformName") is not None:
        out["transform_name"] = data["TransformName"]
    else:
        out["transform_name"] = ""
    if data.get("Inputs") is not None:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("Parameters") is not None:
        import capo_glue.types.transform_config_parameter_list

        out["parameters"] = (
            capo_glue.types.transform_config_parameter_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("FunctionName") is not None:
        out["function_name"] = data["FunctionName"]
    else:
        out["function_name"] = ""
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    else:
        out["path"] = ""
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
