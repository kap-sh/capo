"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SchemaAttributeType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.attribute_data_type
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.custom_attribute_name_type
    import capo_cognito_identity_provider.types.number_attribute_constraints_type
    import capo_cognito_identity_provider.types.string_attribute_constraints_type


class SchemaAttributeType(TypedDict, closed=True):
    name: NotRequired[
        "capo_cognito_identity_provider.types.custom_attribute_name_type.CustomAttributeNameType"
    ]
    """<p>The name of your user pool attribute. When you create or update a user pool, adding a schema attribute creates a custom or developer-only attribute. When you add an attribute with a <code>Name</code> value of <code>MyAttribute</code>, Amazon Cognito creates the custom attribute <code>custom:MyAttribute</code>. When <code>DeveloperOnlyAttribute</code> is <code>true</code>, Amazon Cognito creates your attribute as <code>dev:MyAttribute</code>. In an operation that describes a user pool, Amazon Cognito returns this value as <code>value</code> for standard attributes, <code>custom:value</code> for custom attributes, and <code>dev:value</code> for developer-only attributes..</p>"""
    attribute_data_type: NotRequired[
        "capo_cognito_identity_provider.types.attribute_data_type.AttributeDataType"
    ]
    """<p>The data format of the values for your attribute. When you choose an <code>AttributeDataType</code>, Amazon Cognito validates the input against the data type. A custom attribute value in your user's ID token is always a string, for example <code>"custom:isMember" : "true"</code> or <code>"custom:YearsAsMember" : "12"</code>. </p>"""
    developer_only_attribute: NotRequired[
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    ]
    """<note> <p>You should use <a href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserPoolClientType.html#CognitoUserPools-Type-UserPoolClientType-WriteAttributes">WriteAttributes</a> in the user pool client to control how attributes can be mutated for new use cases instead of using <code>DeveloperOnlyAttribute</code>.</p> </note> <p>Specifies whether the attribute type is developer only. This attribute can only be modified by an administrator. Users won't be able to modify this attribute using their access token. For example, <code>DeveloperOnlyAttribute</code> can be modified using AdminUpdateUserAttributes but can't be updated using UpdateUserAttributes.</p>"""
    mutable: NotRequired[
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    ]
    """<p>Specifies whether the value of the attribute can be changed.</p> <p>Any user pool attribute whose value you map from an IdP attribute must be mutable, with a parameter value of <code>true</code>. Amazon Cognito updates mapped attributes when users sign in to your application through an IdP. If an attribute is immutable, Amazon Cognito throws an error when it attempts to update the attribute. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html">Specifying Identity Provider Attribute Mappings for Your User Pool</a>.</p>"""
    required: NotRequired[
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    ]
    """<p>Specifies whether a user pool attribute is required. If the attribute is required and the user doesn't provide a value, registration or sign-in will fail.</p>"""
    number_attribute_constraints: NotRequired[
        "capo_cognito_identity_provider.types.number_attribute_constraints_type.NumberAttributeConstraintsType"
    ]
    """<p>Specifies the constraints for an attribute of the number type.</p>"""
    string_attribute_constraints: NotRequired[
        "capo_cognito_identity_provider.types.string_attribute_constraints_type.StringAttributeConstraintsType"
    ]
    """<p>Specifies the constraints for an attribute of the string type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaAttributeType) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "attribute_data_type" in value:
        import capo_cognito_identity_provider.types.attribute_data_type

        out["AttributeDataType"] = (
            capo_cognito_identity_provider.types.attribute_data_type.serialize_aws_json_1_1(
                value["attribute_data_type"]
            )
        )
    if "developer_only_attribute" in value:
        out["DeveloperOnlyAttribute"] = value["developer_only_attribute"]
    if "mutable" in value:
        out["Mutable"] = value["mutable"]
    if "required" in value:
        out["Required"] = value["required"]
    if "number_attribute_constraints" in value:
        import capo_cognito_identity_provider.types.number_attribute_constraints_type

        out["NumberAttributeConstraints"] = (
            capo_cognito_identity_provider.types.number_attribute_constraints_type.serialize_aws_json_1_1(
                value["number_attribute_constraints"]
            )
        )
    if "string_attribute_constraints" in value:
        import capo_cognito_identity_provider.types.string_attribute_constraints_type

        out["StringAttributeConstraints"] = (
            capo_cognito_identity_provider.types.string_attribute_constraints_type.serialize_aws_json_1_1(
                value["string_attribute_constraints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaAttributeType:
    out: SchemaAttributeType = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AttributeDataType") is not None:
        import capo_cognito_identity_provider.types.attribute_data_type

        out["attribute_data_type"] = (
            capo_cognito_identity_provider.types.attribute_data_type.deserialize_aws_json_1_1(
                data["AttributeDataType"]
            )
        )
    if data.get("DeveloperOnlyAttribute") is not None:
        out["developer_only_attribute"] = data["DeveloperOnlyAttribute"]
    if data.get("Mutable") is not None:
        out["mutable"] = data["Mutable"]
    if data.get("Required") is not None:
        out["required"] = data["Required"]
    if data.get("NumberAttributeConstraints") is not None:
        import capo_cognito_identity_provider.types.number_attribute_constraints_type

        out["number_attribute_constraints"] = (
            capo_cognito_identity_provider.types.number_attribute_constraints_type.deserialize_aws_json_1_1(
                data["NumberAttributeConstraints"]
            )
        )
    if data.get("StringAttributeConstraints") is not None:
        import capo_cognito_identity_provider.types.string_attribute_constraints_type

        out["string_attribute_constraints"] = (
            capo_cognito_identity_provider.types.string_attribute_constraints_type.deserialize_aws_json_1_1(
                data["StringAttributeConstraints"]
            )
        )
    return out
