"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ParameterDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__boolean
    import capo_serverlessapplicationrepository.types.__integer
    import capo_serverlessapplicationrepository.types.__list_of__string
    import capo_serverlessapplicationrepository.types.__string


class ParameterDefinition(TypedDict, closed=True):
    allowed_pattern: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A regular expression that represents the patterns to allow for String types.</p>"""
    allowed_values: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
    ]
    """<p>An array containing the list of values allowed for the parameter.</p>"""
    constraint_description: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value:</p><p> Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+ </p><p>By adding a constraint description, such as "must contain only uppercase and lowercase letters and numbers," you can display the following customized error message:</p><p> Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers. </p>"""
    default_value: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.</p>"""
    description: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A string of up to 4,000 characters that describes the parameter.</p>"""
    max_length: NotRequired[
        "capo_serverlessapplicationrepository.types.__integer.__integer"
    ]
    """<p>An integer value that determines the largest number of characters that you want to allow for String types.</p>"""
    max_value: NotRequired[
        "capo_serverlessapplicationrepository.types.__integer.__integer"
    ]
    """<p>A numeric value that determines the largest numeric value that you want to allow for Number types.</p>"""
    min_length: NotRequired[
        "capo_serverlessapplicationrepository.types.__integer.__integer"
    ]
    """<p>An integer value that determines the smallest number of characters that you want to allow for String types.</p>"""
    min_value: NotRequired[
        "capo_serverlessapplicationrepository.types.__integer.__integer"
    ]
    """<p>A numeric value that determines the smallest numeric value that you want to allow for Number types.</p>"""
    name: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    """<p>The name of the parameter.</p>"""
    no_echo: NotRequired[
        "capo_serverlessapplicationrepository.types.__boolean.__boolean"
    ]
    """<p>Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the value to true, the parameter value is masked with asterisks (*****).</p>"""
    referenced_by_resources: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
    ]
    """<p>A list of AWS SAM resources that use this parameter.</p>"""
    type: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    """<p>The type of the parameter.</p><p>Valid values: String | Number | List&lt;Number> | CommaDelimitedList </p><p> String: A literal string.</p><p>For example, users can specify "MyUserName".</p><p> Number: An integer or float. AWS CloudFormation validates the parameter value as a number. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.</p><p>For example, users might specify "8888".</p><p> List&lt;Number>: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.</p><p>For example, users might specify "80,20", and then Ref results in ["80","20"].</p><p> CommaDelimitedList: An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas. Also, each member string is space-trimmed.</p><p>For example, users might specify "test,dev,prod", and then Ref results in ["test","dev","prod"].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterDefinition) -> dict:
    out: dict = {}
    if "allowed_pattern" in value:
        out["allowedPattern"] = value["allowed_pattern"]
    if "allowed_values" in value:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["allowedValues"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.serialize_json(
                value["allowed_values"]
            )
        )
    if "constraint_description" in value:
        out["constraintDescription"] = value["constraint_description"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "description" in value:
        out["description"] = value["description"]
    if "max_length" in value:
        out["maxLength"] = value["max_length"]
    if "max_value" in value:
        out["maxValue"] = value["max_value"]
    if "min_length" in value:
        out["minLength"] = value["min_length"]
    if "min_value" in value:
        out["minValue"] = value["min_value"]
    if "name" in value:
        out["name"] = value["name"]
    if "no_echo" in value:
        out["noEcho"] = value["no_echo"]
    if "referenced_by_resources" in value:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["referencedByResources"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.serialize_json(
                value["referenced_by_resources"]
            )
        )
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ParameterDefinition:
    out: ParameterDefinition = {}  # type: ignore[typeddict-item]
    if data.get("allowedPattern") is not None:
        out["allowed_pattern"] = data["allowedPattern"]
    if data.get("allowedValues") is not None:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["allowed_values"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.deserialize_json(
                data["allowedValues"]
            )
        )
    if data.get("constraintDescription") is not None:
        out["constraint_description"] = data["constraintDescription"]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("maxLength") is not None:
        out["max_length"] = data["maxLength"]
    if data.get("maxValue") is not None:
        out["max_value"] = data["maxValue"]
    if data.get("minLength") is not None:
        out["min_length"] = data["minLength"]
    if data.get("minValue") is not None:
        out["min_value"] = data["minValue"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("noEcho") is not None:
        out["no_echo"] = data["noEcho"]
    if data.get("referencedByResources") is not None:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["referenced_by_resources"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.deserialize_json(
                data["referencedByResources"]
            )
        )
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out
