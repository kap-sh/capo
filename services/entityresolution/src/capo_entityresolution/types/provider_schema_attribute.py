"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderSchemaAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.attribute_name
    import capo_entityresolution.types.schema_attribute_type


class ProviderSchemaAttribute(TypedDict, closed=True):
    field_name: "capo_entityresolution.types.attribute_name.AttributeName"
    """<p>The field name.</p>"""
    type: "capo_entityresolution.types.schema_attribute_type.SchemaAttributeType"
    """<p>The type of the provider schema attribute.</p> <p>LiveRamp supports: <code>NAME</code> | <code>NAME_FIRST</code> | <code>NAME_MIDDLE</code> | <code>NAME_LAST</code> | <code>ADDRESS</code> | <code>ADDRESS_STREET1</code> | <code>ADDRESS_STREET2</code> | <code>ADDRESS_STREET3</code> | <code>ADDRESS_CITY</code> | <code>ADDRESS_STATE</code> | <code>ADDRESS_COUNTRY</code> | <code>ADDRESS_POSTALCODE</code> | <code>PHONE</code> | <code>PHONE_NUMBER</code> | <code>EMAIL_ADDRESS</code> | <code>UNIQUE_ID</code> | <code>PROVIDER_ID</code> </p> <p>TransUnion supports: <code>NAME</code> | <code>NAME_FIRST</code> | <code>NAME_LAST</code> | <code>ADDRESS</code> | <code>ADDRESS_CITY</code> | <code>ADDRESS_STATE</code> | <code>ADDRESS_COUNTRY</code> | <code>ADDRESS_POSTALCODE</code> | <code>PHONE_NUMBER</code> | <code>EMAIL_ADDRESS</code> | <code>UNIQUE_ID</code> | <code>DATE</code> | <code>IPV4</code> | <code>IPV6</code> | <code>MAID</code> </p> <p>Unified ID 2.0 supports: <code>PHONE_NUMBER</code> | <code>EMAIL_ADDRESS</code> | <code>UNIQUE_ID</code> </p>"""
    sub_type: NotRequired["capo_entityresolution.types.attribute_name.AttributeName"]
    """<p>The sub type of the provider schema attribute.</p>"""
    hashing: NotRequired["bool"]
    """<p>The hashing attribute of the provider schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderSchemaAttribute) -> dict:
    out: dict = {}
    out["fieldName"] = value["field_name"]
    import capo_entityresolution.types.schema_attribute_type

    out["type"] = capo_entityresolution.types.schema_attribute_type.serialize_json(
        value["type"]
    )
    if "sub_type" in value:
        out["subType"] = value["sub_type"]
    if "hashing" in value:
        out["hashing"] = value["hashing"]
    return out


def deserialize_json(data: dict) -> ProviderSchemaAttribute:
    out: ProviderSchemaAttribute = {}  # type: ignore[typeddict-item]
    if data.get("fieldName") is not None:
        out["field_name"] = data["fieldName"]
    else:
        out["field_name"] = ""
    if data.get("type") is not None:
        import capo_entityresolution.types.schema_attribute_type

        out["type"] = (
            capo_entityresolution.types.schema_attribute_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_entityresolution.types.schema_attribute_type.SchemaAttributeType", ""
        )
    if data.get("subType") is not None:
        out["sub_type"] = data["subType"]
    if data.get("hashing") is not None:
        out["hashing"] = data["hashing"]
    return out
