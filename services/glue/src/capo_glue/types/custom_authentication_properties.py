"""Generated from Smithy shape ``com.amazonaws.glue#CustomAuthenticationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connector_property_list


class CustomAuthenticationProperties(TypedDict, closed=True):
    authentication_parameters: (
        "capo_glue.types.connector_property_list.ConnectorPropertyList"
    )
    """<p>A map of custom authentication parameters that define the specific authentication mechanism and required properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomAuthenticationProperties) -> dict:
    out: dict = {}
    import capo_glue.types.connector_property_list

    out["AuthenticationParameters"] = (
        capo_glue.types.connector_property_list.serialize_aws_json_1_1(
            value["authentication_parameters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomAuthenticationProperties:
    out: CustomAuthenticationProperties = {}  # type: ignore[typeddict-item]
    if data.get("AuthenticationParameters") is not None:
        import capo_glue.types.connector_property_list

        out["authentication_parameters"] = (
            capo_glue.types.connector_property_list.deserialize_aws_json_1_1(
                data["AuthenticationParameters"]
            )
        )
    else:
        out["authentication_parameters"] = []
    return out
