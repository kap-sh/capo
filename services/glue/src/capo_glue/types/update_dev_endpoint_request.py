"""Generated from Smithy shape ``com.amazonaws.glue#UpdateDevEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.boolean_value
    import capo_glue.types.dev_endpoint_custom_libraries
    import capo_glue.types.generic_string
    import capo_glue.types.map_value
    import capo_glue.types.public_keys_list
    import capo_glue.types.string_list


class UpdateDevEndpointRequest(TypedDict, closed=True):
    endpoint_name: "capo_glue.types.generic_string.GenericString"
    """<p>The name of the <code>DevEndpoint</code> to be updated.</p>"""
    public_key: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The public key for the <code>DevEndpoint</code> to use.</p>"""
    add_public_keys: NotRequired["capo_glue.types.public_keys_list.PublicKeysList"]
    """<p>The list of public keys for the <code>DevEndpoint</code> to use.</p>"""
    delete_public_keys: NotRequired["capo_glue.types.public_keys_list.PublicKeysList"]
    """<p>The list of public keys to be deleted from the <code>DevEndpoint</code>.</p>"""
    custom_libraries: NotRequired[
        "capo_glue.types.dev_endpoint_custom_libraries.DevEndpointCustomLibraries"
    ]
    """<p>Custom Python or Java libraries to be loaded in the <code>DevEndpoint</code>.</p>"""
    update_etl_libraries: "capo_glue.types.boolean_value.BooleanValue"
    """<p> <code>True</code> if the list of custom libraries to be loaded in the development endpoint needs to be updated, or <code>False</code> if otherwise.</p>"""
    delete_arguments: NotRequired["capo_glue.types.string_list.StringList"]
    """<p>The list of argument keys to be deleted from the map of arguments used to configure the <code>DevEndpoint</code>.</p>"""
    add_arguments: NotRequired["capo_glue.types.map_value.MapValue"]
    """<p>The map of arguments to add the map of arguments used to configure the <code>DevEndpoint</code>.</p> <p>Valid arguments are:</p> <ul> <li> <p> <code>"--enable-glue-datacatalog": ""</code> </p> </li> </ul> <p>You can specify a version of Python support for development endpoints by using the <code>Arguments</code> parameter in the <code>CreateDevEndpoint</code> or <code>UpdateDevEndpoint</code> APIs. If no arguments are provided, the version defaults to Python 2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDevEndpointRequest) -> dict:
    out: dict = {}
    out["EndpointName"] = value["endpoint_name"]
    if "public_key" in value:
        out["PublicKey"] = value["public_key"]
    if "add_public_keys" in value:
        import capo_glue.types.public_keys_list

        out["AddPublicKeys"] = capo_glue.types.public_keys_list.serialize_aws_json_1_1(
            value["add_public_keys"]
        )
    if "delete_public_keys" in value:
        import capo_glue.types.public_keys_list

        out["DeletePublicKeys"] = (
            capo_glue.types.public_keys_list.serialize_aws_json_1_1(
                value["delete_public_keys"]
            )
        )
    if "custom_libraries" in value:
        import capo_glue.types.dev_endpoint_custom_libraries

        out["CustomLibraries"] = (
            capo_glue.types.dev_endpoint_custom_libraries.serialize_aws_json_1_1(
                value["custom_libraries"]
            )
        )
    out["UpdateEtlLibraries"] = value.get("update_etl_libraries", False)
    if "delete_arguments" in value:
        import capo_glue.types.string_list

        out["DeleteArguments"] = capo_glue.types.string_list.serialize_aws_json_1_1(
            value["delete_arguments"]
        )
    if "add_arguments" in value:
        import capo_glue.types.map_value

        out["AddArguments"] = capo_glue.types.map_value.serialize_aws_json_1_1(
            value["add_arguments"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDevEndpointRequest:
    out: UpdateDevEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    else:
        raise DeserializationError("UpdateDevEndpointRequest.endpoint_name required")
    if data.get("PublicKey") is not None:
        out["public_key"] = data["PublicKey"]
    if data.get("AddPublicKeys") is not None:
        import capo_glue.types.public_keys_list

        out["add_public_keys"] = (
            capo_glue.types.public_keys_list.deserialize_aws_json_1_1(
                data["AddPublicKeys"]
            )
        )
    if data.get("DeletePublicKeys") is not None:
        import capo_glue.types.public_keys_list

        out["delete_public_keys"] = (
            capo_glue.types.public_keys_list.deserialize_aws_json_1_1(
                data["DeletePublicKeys"]
            )
        )
    if data.get("CustomLibraries") is not None:
        import capo_glue.types.dev_endpoint_custom_libraries

        out["custom_libraries"] = (
            capo_glue.types.dev_endpoint_custom_libraries.deserialize_aws_json_1_1(
                data["CustomLibraries"]
            )
        )
    if data.get("UpdateEtlLibraries") is not None:
        out["update_etl_libraries"] = data["UpdateEtlLibraries"]
    else:
        out["update_etl_libraries"] = False
    if data.get("DeleteArguments") is not None:
        import capo_glue.types.string_list

        out["delete_arguments"] = capo_glue.types.string_list.deserialize_aws_json_1_1(
            data["DeleteArguments"]
        )
    if data.get("AddArguments") is not None:
        import capo_glue.types.map_value

        out["add_arguments"] = capo_glue.types.map_value.deserialize_aws_json_1_1(
            data["AddArguments"]
        )
    return out
