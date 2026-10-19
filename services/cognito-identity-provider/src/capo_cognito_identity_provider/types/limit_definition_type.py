"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#LimitDefinitionType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.limit_class
    import capo_cognito_identity_provider.types.string_to_string_map_type


class LimitDefinitionType(TypedDict, closed=True):
    limit_class: "capo_cognito_identity_provider.types.limit_class.LimitClass"
    """<p>The class of the limit. For API rate limits, this is <code>API_CATEGORY</code>.</p>"""
    attributes: "capo_cognito_identity_provider.types.string_to_string_map_type.StringToStringMapType"
    """<p>The attributes that identify the specific limit. For API rate limits, specify the <code>Category</code> key with a value like <code>UserAuthentication</code> or <code>UserCreation</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LimitDefinitionType) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.limit_class

    out["LimitClass"] = (
        capo_cognito_identity_provider.types.limit_class.serialize_aws_json_1_1(
            value["limit_class"]
        )
    )
    import capo_cognito_identity_provider.types.string_to_string_map_type

    out["Attributes"] = (
        capo_cognito_identity_provider.types.string_to_string_map_type.serialize_aws_json_1_1(
            value["attributes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LimitDefinitionType:
    out: LimitDefinitionType = {}  # type: ignore[typeddict-item]
    if data.get("LimitClass") is not None:
        import capo_cognito_identity_provider.types.limit_class

        out["limit_class"] = (
            capo_cognito_identity_provider.types.limit_class.deserialize_aws_json_1_1(
                data["LimitClass"]
            )
        )
    else:
        import typing

        out["limit_class"] = typing.cast(
            "capo_cognito_identity_provider.types.limit_class.LimitClass", ""
        )
    if data.get("Attributes") is not None:
        import capo_cognito_identity_provider.types.string_to_string_map_type

        out["attributes"] = (
            capo_cognito_identity_provider.types.string_to_string_map_type.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    else:
        out["attributes"] = {}
    return out
