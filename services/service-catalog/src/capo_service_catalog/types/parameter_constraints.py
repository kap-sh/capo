"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ParameterConstraints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.allowed_values
    import capo_service_catalog.types.string


class ParameterConstraints(TypedDict, closed=True):
    allowed_values: NotRequired[
        "capo_service_catalog.types.allowed_values.AllowedValues"
    ]
    """<p>The values that the administrator has allowed for the parameter.</p>"""
    allowed_pattern: NotRequired["capo_service_catalog.types.string.String"]
    """<p>A regular expression that represents the patterns that allow for <code>String</code> types. The pattern must match the entire parameter value provided.</p>"""
    constraint_description: NotRequired["capo_service_catalog.types.string.String"]
    """<p>A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of <code>[A-Za-z0-9]+</code> displays the following error message when the user specifies an invalid value:</p> <p> <code>Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+</code> </p> <p>By adding a constraint description, such as must only contain letters (uppercase and lowercase) and numbers, you can display the following customized error message:</p> <p> <code>Malformed input-Parameter MyParameter must only contain uppercase and lowercase letters and numbers.</code> </p>"""
    max_length: NotRequired["capo_service_catalog.types.string.String"]
    """<p>An integer value that determines the largest number of characters you want to allow for <code>String</code> types. </p>"""
    min_length: NotRequired["capo_service_catalog.types.string.String"]
    """<p>An integer value that determines the smallest number of characters you want to allow for <code>String</code> types.</p>"""
    max_value: NotRequired["capo_service_catalog.types.string.String"]
    """<p>A numeric value that determines the largest numeric value you want to allow for <code>Number</code> types.</p>"""
    min_value: NotRequired["capo_service_catalog.types.string.String"]
    """<p>A numeric value that determines the smallest numeric value you want to allow for <code>Number</code> types. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterConstraints) -> dict:
    out: dict = {}
    if "allowed_values" in value:
        import capo_service_catalog.types.allowed_values

        out["AllowedValues"] = (
            capo_service_catalog.types.allowed_values.serialize_aws_json_1_1(
                value["allowed_values"]
            )
        )
    if "allowed_pattern" in value:
        out["AllowedPattern"] = value["allowed_pattern"]
    if "constraint_description" in value:
        out["ConstraintDescription"] = value["constraint_description"]
    if "max_length" in value:
        out["MaxLength"] = value["max_length"]
    if "min_length" in value:
        out["MinLength"] = value["min_length"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterConstraints:
    out: ParameterConstraints = {}  # type: ignore[typeddict-item]
    if data.get("AllowedValues") is not None:
        import capo_service_catalog.types.allowed_values

        out["allowed_values"] = (
            capo_service_catalog.types.allowed_values.deserialize_aws_json_1_1(
                data["AllowedValues"]
            )
        )
    if data.get("AllowedPattern") is not None:
        out["allowed_pattern"] = data["AllowedPattern"]
    if data.get("ConstraintDescription") is not None:
        out["constraint_description"] = data["ConstraintDescription"]
    if data.get("MaxLength") is not None:
        out["max_length"] = data["MaxLength"]
    if data.get("MinLength") is not None:
        out["min_length"] = data["MinLength"]
    if data.get("MaxValue") is not None:
        out["max_value"] = data["MaxValue"]
    if data.get("MinValue") is not None:
        out["min_value"] = data["MinValue"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ParameterConstraints) -> dict:
    out: dict = {}
    if "allowed_values" in value:
        import capo_service_catalog.types.allowed_values

        out["AllowedValues"] = capo_service_catalog.types.allowed_values.serialize_cbor(
            value["allowed_values"]
        )
    if "allowed_pattern" in value:
        out["AllowedPattern"] = value["allowed_pattern"]
    if "constraint_description" in value:
        out["ConstraintDescription"] = value["constraint_description"]
    if "max_length" in value:
        out["MaxLength"] = value["max_length"]
    if "min_length" in value:
        out["MinLength"] = value["min_length"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    return out


def deserialize_cbor(data: dict) -> ParameterConstraints:
    out: ParameterConstraints = {}  # type: ignore[typeddict-item]
    if data.get("AllowedValues") is not None:
        import capo_service_catalog.types.allowed_values

        out["allowed_values"] = (
            capo_service_catalog.types.allowed_values.deserialize_cbor(
                data["AllowedValues"]
            )
        )
    if data.get("AllowedPattern") is not None:
        out["allowed_pattern"] = data["AllowedPattern"]
    if data.get("ConstraintDescription") is not None:
        out["constraint_description"] = data["ConstraintDescription"]
    if data.get("MaxLength") is not None:
        out["max_length"] = data["MaxLength"]
    if data.get("MinLength") is not None:
        out["min_length"] = data["MinLength"]
    if data.get("MaxValue") is not None:
        out["max_value"] = data["MaxValue"]
    if data.get("MinValue") is not None:
        out["min_value"] = data["MinValue"]
    return out
