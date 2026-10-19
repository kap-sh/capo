"""Generated from Smithy shape ``com.amazonaws.pricing#Service``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pricing.types.attribute_name_list
    import capo_pricing.types.string


class Service(TypedDict, closed=True):
    service_code: "capo_pricing.types.string.String"
    """<p>The code for the Amazon Web Services service.</p>"""
    attribute_names: NotRequired[
        "capo_pricing.types.attribute_name_list.AttributeNameList"
    ]
    """<p>The attributes that are available for this service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Service) -> dict:
    out: dict = {}
    out["ServiceCode"] = value["service_code"]
    if "attribute_names" in value:
        import capo_pricing.types.attribute_name_list

        out["AttributeNames"] = (
            capo_pricing.types.attribute_name_list.serialize_aws_json_1_1(
                value["attribute_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        out["service_code"] = ""
    if data.get("AttributeNames") is not None:
        import capo_pricing.types.attribute_name_list

        out["attribute_names"] = (
            capo_pricing.types.attribute_name_list.deserialize_aws_json_1_1(
                data["AttributeNames"]
            )
        )
    return out
