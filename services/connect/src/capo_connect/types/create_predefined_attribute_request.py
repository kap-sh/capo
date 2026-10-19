"""Generated from Smithy shape ``com.amazonaws.connect#CreatePredefinedAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.input_predefined_attribute_configuration
    import capo_connect.types.instance_id
    import capo_connect.types.predefined_attribute_name
    import capo_connect.types.predefined_attribute_purpose_name_list
    import capo_connect.types.predefined_attribute_values


class CreatePredefinedAttributeRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.predefined_attribute_name.PredefinedAttributeName"
    """<p> The name of the predefined attribute. </p>"""
    values: NotRequired[
        "capo_connect.types.predefined_attribute_values.PredefinedAttributeValues"
    ]
    """<p> The values of the predefined attribute. </p>"""
    purposes: NotRequired[
        "capo_connect.types.predefined_attribute_purpose_name_list.PredefinedAttributePurposeNameList"
    ]
    """<p>Values that enable you to categorize your predefined attributes. You can use them in custom UI elements across the Connect Customer admin website.</p>"""
    attribute_configuration: NotRequired[
        "capo_connect.types.input_predefined_attribute_configuration.InputPredefinedAttributeConfiguration"
    ]
    """<p>Custom metadata that is associated to predefined attributes to control behavior in upstream services, such as controlling how a predefined attribute should be displayed in the Connect Customer admin website.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePredefinedAttributeRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "values" in value:
        import capo_connect.types.predefined_attribute_values

        out["Values"] = capo_connect.types.predefined_attribute_values.serialize_json(
            value["values"]
        )
    if "purposes" in value:
        import capo_connect.types.predefined_attribute_purpose_name_list

        out["Purposes"] = (
            capo_connect.types.predefined_attribute_purpose_name_list.serialize_json(
                value["purposes"]
            )
        )
    if "attribute_configuration" in value:
        import capo_connect.types.input_predefined_attribute_configuration

        out["AttributeConfiguration"] = (
            capo_connect.types.input_predefined_attribute_configuration.serialize_json(
                value["attribute_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreatePredefinedAttributeRequest:
    out: CreatePredefinedAttributeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Values") is not None:
        import capo_connect.types.predefined_attribute_values

        out["values"] = capo_connect.types.predefined_attribute_values.deserialize_json(
            data["Values"]
        )
    if data.get("Purposes") is not None:
        import capo_connect.types.predefined_attribute_purpose_name_list

        out["purposes"] = (
            capo_connect.types.predefined_attribute_purpose_name_list.deserialize_json(
                data["Purposes"]
            )
        )
    if data.get("AttributeConfiguration") is not None:
        import capo_connect.types.input_predefined_attribute_configuration

        out["attribute_configuration"] = (
            capo_connect.types.input_predefined_attribute_configuration.deserialize_json(
                data["AttributeConfiguration"]
            )
        )
    return out
