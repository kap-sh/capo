"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeviceType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.attribute_list_type
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.device_key_type


class DeviceType(TypedDict, closed=True):
    device_key: NotRequired[
        "capo_cognito_identity_provider.types.device_key_type.DeviceKeyType"
    ]
    """<p>The device key, for example <code>us-west-2_EXAMPLE-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>"""
    device_attributes: NotRequired[
        "capo_cognito_identity_provider.types.attribute_list_type.AttributeListType"
    ]
    """<p>Metadata about a user's device, like name and last-access source IP.</p>"""
    device_create_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    device_last_modified_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    device_last_authenticated_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date when the user last signed in with the device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceType) -> dict:
    out: dict = {}
    if "device_key" in value:
        out["DeviceKey"] = value["device_key"]
    if "device_attributes" in value:
        import capo_cognito_identity_provider.types.attribute_list_type

        out["DeviceAttributes"] = (
            capo_cognito_identity_provider.types.attribute_list_type.serialize_aws_json_1_1(
                value["device_attributes"]
            )
        )
    if "device_create_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["DeviceCreateDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["device_create_date"]
            )
        )
    if "device_last_modified_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["DeviceLastModifiedDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["device_last_modified_date"]
            )
        )
    if "device_last_authenticated_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["DeviceLastAuthenticatedDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["device_last_authenticated_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceType:
    out: DeviceType = {}  # type: ignore[typeddict-item]
    if data.get("DeviceKey") is not None:
        out["device_key"] = data["DeviceKey"]
    if data.get("DeviceAttributes") is not None:
        import capo_cognito_identity_provider.types.attribute_list_type

        out["device_attributes"] = (
            capo_cognito_identity_provider.types.attribute_list_type.deserialize_aws_json_1_1(
                data["DeviceAttributes"]
            )
        )
    if data.get("DeviceCreateDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["device_create_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["DeviceCreateDate"]
            )
        )
    if data.get("DeviceLastModifiedDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["device_last_modified_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["DeviceLastModifiedDate"]
            )
        )
    if data.get("DeviceLastAuthenticatedDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["device_last_authenticated_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["DeviceLastAuthenticatedDate"]
            )
        )
    return out


def redact_sensitive(value: DeviceType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "device_attributes" in value:
        import capo_cognito_identity_provider.types.attribute_list_type

        out["device_attributes"] = (
            capo_cognito_identity_provider.types.attribute_list_type.redact_sensitive(
                value["device_attributes"]
            )
        )
    return out
